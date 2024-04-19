"""Scheduler classes."""

import asyncio
import traceback
from dataclasses import dataclass, field
from enum import Enum
from types import MappingProxyType
from typing import Any, Awaitable, Callable, ClassVar, Dict, List, Mapping, NoReturn, Optional, TypedDict, cast, final
from weakref import proxy

from kaiju_scheduler.interfaces import Logger
from kaiju_scheduler.utils import SortedStack, retry, timeout

__all__ = ["ExecPolicy", "ScheduledTask"]

_AsyncCallable = Callable[..., Awaitable[Any]]
_Sentinel = ...


class _TaskInfo(TypedDict):
    name: str
    enabled: bool
    interval: float
    policy: str
    retries: int
    retry_interval: float
    max_timeout: float
    started: bool
    called_at: float


def wrap_sync(f: Callable, /) -> Callable[..., Awaitable[Any]]:
    """Wrap a synchronous function in async."""

    async def _wrap_sync(*args, **kws):
        return f(*args, **kws)

    return _wrap_sync


@final
class ExecPolicy(Enum):
    """Method execution  policy for a scheduled task."""

    WAIT = "WAIT"  #: Wait until the previous run of this task finishes
    CANCEL = "CANCEL"  #: Cancel the previous call immediately and restart the task


@final
class ScheduledTask:
    """Scheduled task."""

    class _TaskDisableCtx:
        __slots__ = ("__weakref__", "_task")

        def __init__(self, task: "ScheduledTask", /):
            self._task = proxy(task)

        async def __aenter__(self):
            await self._task.idle.wait()
            self._task.disable()

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            self._task.enable()

    __slots__ = (
        "_scheduler",
        "name",
        "method",
        "args",
        "kws",
        "interval",
        "policy",
        "called_at",
        "enabled",
        "idle",
        "executed_task",
        "retries",
        "retry_interval",
        "max_timeout",
        "result",
        "__weakref__",
    )

    def __init__(
        self,
        scheduler: "Scheduler",
        name: str,
        method: _AsyncCallable,
        args: tuple,
        kws: Mapping,
        interval: float,
        policy: ExecPolicy,
        max_timeout: float,
        retries: int,
        retry_interval: float,
    ):
        """Initialize."""
        self._scheduler = proxy(scheduler)
        self.name = name
        self.method = method
        self.args = args
        self.kws = kws
        self.interval = interval
        self.max_timeout = max_timeout
        self.policy = policy
        self.called_at = 0.0
        self.retries = retries
        self.retry_interval = retry_interval
        self.result = None
        self.enabled = True
        self.idle = asyncio.Event()
        self.idle.set()
        self.executed_task: Optional[asyncio.Task] = None

    def enable(self) -> None:
        self._scheduler.enable_task(self)

    def disable(self) -> None:
        self._scheduler.disable_task(self)

    def suspend(self) -> _TaskDisableCtx:
        """Temporarily suspend execution of a task within a context block."""
        return self._TaskDisableCtx(self)

    def json_repr(self) -> Dict[str, Any]:
        return {
            "cls": "Task",
            "data": _TaskInfo(
                name=self.name,
                policy=self.policy.value,
                enabled=self.enabled,
                started=not self.idle.is_set(),
                interval=self.interval,
                max_timeout=self.max_timeout,
                retries=self.retries,
                retry_interval=self.retry_interval,
                called_at=self.called_at,
            ),
        }


@dataclass
class Scheduler:
    """Schedule and execute local functions.

    It can be used to set up periodic execution of local service methods at specific intervals. The best way to do it
    is to discover the scheduler in your service `init()` and create a task using
    :py:meth:`~kaiju_tools.app.Scheduler.schedule_task` method.

    .. code-block:: python

        from kaiju_tools import Scheduler, ContextableService

        class CacheService(ContextableService):

            async def reload_cache(self):
                ...

            async def init(self):
                scheduler = self.discover_service(None, cls=Scheduler)
                self._task_reload = scheduler.schedule_task(self.reload_cache, 60, name='CacheService.reload')

    It's a good idea to disable the task on service exit by setting `enabled=False`.
    A disabled task will not be re-scheduled until enabled.

    .. code-block:: python

            async def close(self):
                self._task_reload.enabled = False

    You can also temporarily suspend your task using the task disable context. The task will be automatically enabled
    on context exit.

    .. code-block:: python

        async def rebuild_database(self):
            async with self._task_reload.suspend():
                ...

    You can manage how the task is handled if the previous execution hasn't finished on time.
    By default, a not finished task will be cancelled and rescheduled.
    Change it to :py:attr:`~kaiju_tools.app.ExecPolicy.WAIT` to wait for a previous call to finish instead.

    .. code-block:: python

        self._task_reload = scheduler.schedule_task(self.reload_cache, 60, policy=ExecPolicy.WAIT)

    You can set a retry policy to handle timeouts or connection errors by setting the maximum number of retries.
    The scheduler uses :py:func:`~kaiju_tools.func.retry` function to handle retries.

    .. code-block:: python

        self._task_reload = scheduler.schedule_task(self.reload_cache, 60, retries=5)

    """

    ExecPolicy: ClassVar = ExecPolicy
    """Alias to scheduled task exec policy enum."""

    min_refresh_rate: ClassVar[float] = 0.1
    """Minimum allowed refresh rate between cycles in seconds, limits `refresh_rate` value."""

    wait_task_timeout_safe_mod: ClassVar[float] = 4.0
    """Timeout modifier for WAIT tasks (to prevent them waiting forever)."""

    refresh_rate: float = min_refresh_rate
    """Refresh rate for the next cycle."""

    logger: Optional[Logger] = None
    """Optional logger instance."""

    loop: asyncio.AbstractEventLoop = None  # type: ignore

    _stack: SortedStack[ScheduledTask] = field(init=False, default_factory=SortedStack)
    _tasks: List[ScheduledTask] = field(init=False, default_factory=list)
    _daemon: Optional[asyncio.Task] = field(init=False, default=None)

    def schedule_task(
        self,
        func: Callable,
        interval: float,
        args: tuple = tuple(),
        kws: Mapping = MappingProxyType({}),
        *,
        policy: ExecPolicy = ExecPolicy.CANCEL,
        max_timeout: Optional[float] = None,
        retries: int = 0,
        retry_interval: Optional[float] = None,
        name: Optional[str] = None,
        run_immediately: bool = False,
    ) -> ScheduledTask:
        """Schedule a periodic task.

        :param func: asynchronous function
        :param args: input positional arguments
        :param kws: input kw arguments
        :param interval: schedule interval in seconds
        :param policy: task execution policy
        :param max_timeout: optional max timeout in seconds, for :py:obj:`~kaiju_scheduler.scheduler.ExecPolicy.CANCEL`
            the lowest between `max_timeout` and `interval` will be used, by default `interval` is used for
            cancelled tasks and `interval * 4` for waited tasks
        :param retries: number of retries if any, see :py:func:`~kaiju_scheduler.utils.retry` for more info
        :param retry_interval: interval between retries, see :py:func:`~kaiju_scheduler.utils.retry` for more info
        :param name: optional custom task name, which will be shown in the app's server list of task
        :param run_immediately: run the task immediately not waiting for the first interval
        :returns: an instance of scheduled task
        """
        if name is None:
            name = f"scheduled:{func.__name__}"
        if kws is None:
            kws = {}
        if retries:
            if retry_interval is None:
                retry_interval = interval / (retries + 1)
        else:
            retry_interval = 0
        if policy == self.ExecPolicy.CANCEL:
            max_timeout = min(interval, max_timeout) if max_timeout else interval
        elif not max_timeout:
            max_timeout = self.wait_task_timeout_safe_mod * interval
        if self.logger is not None:
            self.logger.debug(f"Schedule task {name}")
        if not asyncio.iscoroutinefunction(func):
            func = wrap_sync(func)
        task = ScheduledTask(self, name, func, args, kws, interval, policy, max_timeout, retries, retry_interval)
        self._tasks.append(task)
        self.refresh_rate = max(min(self.refresh_rate, interval), self.min_refresh_rate)
        if run_immediately:
            interval = 0
        self._stack.add((task, self.loop.time() + interval))
        return task

    def enable_task(self, task: ScheduledTask, /) -> None:
        if not task.enabled:
            task.enabled = True
            t_ex = task.called_at + task.interval
            self._stack.add((task, t_ex))

    def disable_task(self, task: ScheduledTask, /) -> None:
        task.enabled = False

    def cancel_task(self, task: ScheduledTask, /) -> None:
        if task.executed_task and not task.executed_task.done() and not task.executed_task.cancelled():
            task.executed_task.cancel("cancelled by the scheduler")
        task.executed_task = None
        task.idle.set()

    async def start(self):
        """Initialize."""
        if not self.loop:
            self.loop = asyncio.get_running_loop()
        self._daemon = asyncio.create_task(self._start_daemon())  # noqa: pycharm can't handle typing here

    async def stop(self):
        """Close."""
        self._daemon.cancel()
        self._daemon = None
        self._stack.clear()
        await asyncio.gather(
            *(
                task.executed_task
                for task in self._tasks
                if task.executed_task
                and not all((task.idle.is_set(), task.executed_task.done(), task.executed_task.cancelled()))
            ),
            return_exceptions=True,
        )

    def json_repr(self) -> Dict[str, Any]:
        return {
            "cls": "Scheduler",
            "data": {
                "started": self._daemon is not None,
                "time": self.loop.time(),
                "refresh_rate": self.refresh_rate,
                "tasks": [task.json_repr() for task in self._tasks],
            },
        }

    async def __aenter__(self) -> "Scheduler":
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.stop()

    async def _start_daemon(self) -> NoReturn:
        while 1:
            await self._run_tasks()
            await asyncio.sleep(self._get_sleep_interval())

    def _get_sleep_interval(self) -> float:
        lowest_score = self._stack.lowest_score
        if lowest_score is None:
            lowest_score = 0
        t0 = self.loop.time()
        interval = min(max(lowest_score - t0, t0), self.refresh_rate)
        return cast(float, interval)

    async def _run_tasks(self) -> None:
        t0 = self.loop.time()
        to_execute = self._stack.pop_many(t0)
        for task in to_execute:
            if not task.enabled:
                continue
            if not task.idle.is_set():
                if task.policy is self.ExecPolicy.WAIT:
                    continue
                elif task.policy is self.ExecPolicy.CANCEL:
                    self.cancel_task(task)
                else:
                    raise RuntimeError(f'unsupported exec policy "{task.policy}"')

            task.idle.clear()
            task.executed_task = self.loop.create_task(self._run_task(task))
            task.called_at = t0

    async def _run_task(self, task: ScheduledTask, /) -> None:
        try:
            if task.retries:
                task.result = await retry(
                    task.method,
                    args=task.args,
                    kws=task.kws,
                    retries=task.retries,
                    interval_s=task.retry_interval,
                    timeout_s=task.max_timeout,
                )
            else:
                async with timeout(task.max_timeout):
                    task.result = await task.method(*task.args, **task.kws)
        except Exception as exc:
            if self.logger is not None:
                self.logger.error(f'Task error in task "{task.name}"', exc_info=exc)
            else:
                print(traceback.format_exc())
        else:
            ...
        finally:
            task.idle.set()
            self._stack.add((task, task.called_at + task.interval))
