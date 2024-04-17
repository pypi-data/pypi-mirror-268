from collections import OrderedDict
from typing import Any, AnyStr, Dict, Optional, Tuple, Type

from polymatch.base import CaseAction, PolymorphicMatcher
from polymatch.error import (
    DuplicateMatcherRegistrationError,
    NoMatchersAvailableError,
    NoSuchMatcherError,
)
from polymatch.matchers.glob import GlobMatcher
from polymatch.matchers.regex import RegexMatcher
from polymatch.matchers.standard import ContainsMatcher, ExactMatcher


def _opt_split(
    text: AnyStr, delim: AnyStr, empty: AnyStr, invchar: AnyStr
) -> Tuple[bool, AnyStr, AnyStr, AnyStr]:
    if text.startswith(invchar):
        invert = True
        text = text[len(invchar) :]
    else:
        invert = False

    if delim in text:
        name, _, text = text.partition(delim)

        if delim in text:
            opts, _, text = text.partition(delim)
        else:
            opts = empty
    else:
        name = empty
        opts = empty

    return invert, name, opts, text


def _parse_pattern_string(text: AnyStr) -> Tuple[bool, str, str, AnyStr]:
    if isinstance(text, str):
        invert, name, opts, pattern = _opt_split(text, ":", "", "~")
        return invert, name, opts, pattern

    if isinstance(text, bytes):
        invert, name, opts, pattern = _opt_split(text, b":", b"", b"~")
        return invert, name.decode(), opts.decode(), pattern

    msg = f"Unable to parse pattern string of type {type(text).__name__!r}"
    raise TypeError(msg)


_Matcher = PolymorphicMatcher[Any, Any]
_MatcherCls = Type[_Matcher]


class PatternMatcherRegistry:
    def __init__(self) -> None:
        self._matchers: Dict[str, _MatcherCls] = OrderedDict()

    def register(self, cls: Type[Any]) -> None:
        if not issubclass(cls, PolymorphicMatcher):
            msg = "Pattern matcher must be of type {!r} not {!r}".format(
                PolymorphicMatcher.__name__, cls.__name__
            )
            raise TypeError(msg)

        name = cls.get_type()
        if name in self._matchers:
            raise DuplicateMatcherRegistrationError(name)

        self._matchers[name] = cls

    def remove(self, name: str) -> None:
        del self._matchers[name]

    def __getitem__(self, item: str) -> _MatcherCls:
        return self.get_matcher(item)

    def get_matcher(self, name: str) -> _MatcherCls:
        try:
            return self._matchers[name]
        except LookupError as e:
            raise NoSuchMatcherError(name) from e

    def get_default_matcher(self) -> _MatcherCls:
        if self._matchers:
            return next(iter(self._matchers.values()))

        raise NoMatchersAvailableError

    def pattern_from_string(self, text: AnyStr) -> _Matcher:
        invert, name, opts, pattern = _parse_pattern_string(text)
        match_cls = (
            self.get_default_matcher() if not name else self.get_matcher(name)
        )

        case_action: Optional[CaseAction] = None
        for action in CaseAction:
            if action.value[1] == opts:
                case_action = action
                break

        if case_action is None:
            msg = f"Unable to find CaseAction for options: {opts!r}"
            raise LookupError(msg)

        return match_cls(pattern, case_action, invert=invert)


pattern_registry = PatternMatcherRegistry()

pattern_registry.register(ExactMatcher)
pattern_registry.register(ContainsMatcher)
pattern_registry.register(GlobMatcher)
pattern_registry.register(RegexMatcher)
