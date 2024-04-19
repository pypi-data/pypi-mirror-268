from collections.abc import Callable
from typing import Generic
from typing import TypeVar

TLazyObject = TypeVar('TLazyObject')
TLazyInstanceObject = TypeVar('TLazyInstanceObject')


class NoValue: ...


class LazyObject(Generic[TLazyObject]):
    """Helper class to lazily load an attribute."""

    def __init__(self, resolver: Callable[[], TLazyObject]) -> None:
        self._value: TLazyObject | NoValue = NoValue()
        self._resolver: Callable[[], TLazyObject] = resolver

    @property
    def value(self) -> TLazyObject:
        if isinstance(self._value, NoValue):
            self._value = self._resolver()

        return self._value


class LazyInstanceObject(Generic[TLazyInstanceObject, TLazyObject]):
    """Helper class to lazily load an attribute of an instance."""

    def __init__(self, resolver: Callable[[TLazyInstanceObject], TLazyObject]) -> None:
        self._value: TLazyObject | NoValue = NoValue()
        self._resolver: Callable[[TLazyInstanceObject], TLazyObject] = resolver

    def value(self, instance: TLazyInstanceObject) -> TLazyObject:
        if isinstance(self._value, NoValue):
            self._value = self._resolver(instance)

        return self._value
