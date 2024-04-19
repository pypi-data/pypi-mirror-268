"""Utility classes and functions."""

import asyncio
from bisect import bisect
from collections.abc import Mapping, Sized
from types import MappingProxyType
from typing import Any, Awaitable, Callable, Dict, Generic, Iterable, List, Optional, Tuple, Type, TypeVar, Union

from kaiju_scheduler.interfaces import Logger

__all__ = ["SortedStack", "timeout", "retry", "RetryError"]


_Item = TypeVar("_Item")


class RetryError(Exception):
    """Error recognized by :py:func:`~kaiju_scheduler.utils.retry` as suitable for retry."""


class SortedStack(Sized, Iterable, Generic[_Item]):
    """Sorted stack of elements.

    >>> stack = SortedStack({'sobaki': 5})
    >>> stack = SortedStack(stack)
    >>> stack.add(*SortedStack({'cats': 5}))

    Select elements without removing them from stack:

    >>> stack.select(8)
    ['sobaki', 'cats']

    >>> stack.rselect(8)
    []

    Add elements:

    >>> stack.add(('koty', 1), ('dogs', 12))

    Pop elements from stack according to certain compare value:

    >>> stack.pop_many(3)
    ['koty']

    >>> stack.pop()
    'sobaki'

    >>> stack.rpop()
    'dogs'

    >>> stack.rpop_many(3)
    ['cats']

    >>> stack.clear()
    >>> bool(stack)
    False

    Empty stack raises `StopIteration` on pop:

    >>> stack.pop()  # +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    StopIteration: Empty stack.

    """

    __slots__ = ("_scores", "_values")

    def __init__(self, items: Union[Iterable[Tuple[_Item, Any]], Dict[_Item, Any], None] = None, /):
        """Initialize."""
        self._scores: List[Any] = []
        self._values: List[_Item] = []
        if items:
            if isinstance(items, dict):
                items = items.items()
            self.add(*items)

    @property
    def lowest_score(self) -> Optional[Any]:
        """Get the lowest score in the stack."""
        return next(iter(self._scores), None)

    def add(self, *items: Tuple[_Item, Any]):
        """Extend the stack by adding more than one element."""
        for item, score in items:
            idx = bisect(self._scores, score)
            self._scores.insert(idx, score)
            self._values.insert(idx, item)

    def select(self, score_threshold, /) -> List[_Item]:
        """Select and return items without removing them from the lowest score to `score_threshold`.

        The values are guaranteed to be in order.
        """
        return self._select(score_threshold, reverse=False)

    def rselect(self, score_threshold: Any, /) -> List[_Item]:
        """Select and return items without removing them from the highest score to `score_threshold`.

        The values are guaranteed to be in order.
        """
        return self._select(score_threshold, reverse=True)

    def pop(self) -> _Item:
        """Pop a single element which has the lowest score.

        :raises StopIteration: if there are no values to return.
        """
        return self._pop(reverse=False)

    def rpop(self) -> _Item:
        """Pop a single element which has the highest score.

        :raises StopIteration: if there are no values to return.
        """
        return self._pop(reverse=True)

    def pop_many(self, score_threshold: Any, /) -> List[_Item]:
        """Pop and return values with scores less than `score_threshold`.

        The returned values are guaranteed to be in order.
        Returns an empty list if no values.
        """
        return self._pop_many(score_threshold, reverse=False)

    def rpop_many(self, score_threshold: Any, /) -> List[_Item]:
        """Pop and return values with scores greater than `score_threshold`.

        Returned values are guaranteed to be in order.
        """
        return self._pop_many(score_threshold, reverse=True)

    def clear(self) -> None:
        """Clear all values."""
        self._scores.clear()
        self._values.clear()

    def __iter__(self):
        return iter(zip(self._values, self._scores))

    def __len__(self):
        return len(self._values)

    def _pop_many(self, score_threshold: Any, reverse: bool = False) -> List[_Item]:
        """Pop values with scores less than `score`.

        The returned values are guaranteed to be in order.
        Returns an empty list if no values.
        """
        idx = bisect(self._scores, score_threshold)
        if reverse:
            self._scores = self._scores[:idx]
            values, self._values = self._values[idx:], self._values[:idx]
        else:
            self._scores = self._scores[idx:]
            values, self._values = self._values[:idx], self._values[idx:]
        return values

    def _pop(self, reverse: bool = False) -> _Item:
        if not self._values:
            raise StopIteration("Empty stack.")
        if reverse:
            del self._scores[-1]
            return self._values.pop(-1)
        else:
            del self._scores[0]
            return self._values.pop(0)

    def _select(self, score_threshold: Any, reverse: bool = False) -> List[_Item]:
        """Select and return items without removing them from the stack.

        The values are guaranteed to be in order.
        """
        idx = bisect(self._scores, score_threshold)
        if reverse:
            values = self._values[idx:]
            values.reverse()
            return values
        else:
            return self._values[:idx]


def timeout(time_sec: float, /):
    """Execute async callables within a timeout.

    .. code-block:: python

        async with timeout(5):
            await do_something_asynchronous()

    """
    return _Timeout(time_sec)


class _Timeout:
    __slots__ = ("_timeout", "_loop", "_task", "_handler")

    _handler: asyncio.Handle

    def __init__(self, time_sec: float, loop=None):
        self._timeout = max(0.0, time_sec)
        self._loop = loop
        # self._handler: asyncio.Task = None

    async def __aenter__(self):
        if self._loop is None:
            loop = asyncio.get_running_loop()
        else:
            loop = self._loop
        task = asyncio.current_task()
        self._handler = loop.call_at(loop.time() + self._timeout, self._cancel_task, task)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is asyncio.CancelledError:
            raise asyncio.TimeoutError
        if self._handler:
            self._handler.cancel()

    @staticmethod
    def _cancel_task(task: asyncio.Task):
        task.cancel()


async def retry(
    func: Callable[..., Awaitable[Any]],
    retries: int,
    args: tuple = tuple(),
    kws: Mapping = MappingProxyType({}),
    *,
    interval_s: float = 1.0,
    timeout_s: float = 120.0,
    catch_exceptions: Tuple[Type[BaseException], ...] = (TimeoutError, IOError, ConnectionError, RetryError),
    logger: Optional[Logger] = None,
):
    async with timeout(timeout_s):
        while retries + 1 > 0:
            try:
                return await func(*args, **kws)
            except catch_exceptions as exc:
                retries -= 1
                if logger is not None:
                    logger.info("retrying on error", exc_info=exc)
                await asyncio.sleep(interval_s)
