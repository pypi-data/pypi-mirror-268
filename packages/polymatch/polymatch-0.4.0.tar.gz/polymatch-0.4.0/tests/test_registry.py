import pytest

from polymatch import pattern_registry
from polymatch.base import CaseAction
from polymatch.error import (
    DuplicateMatcherRegistrationError,
    NoMatchersAvailableError,
    NoSuchMatcherError,
)
from polymatch.matchers.glob import GlobMatcher
from polymatch.matchers.standard import ExactMatcher
from polymatch.registry import PatternMatcherRegistry


def test_register_duplicate() -> None:
    registry = PatternMatcherRegistry()
    registry.register(GlobMatcher)
    with pytest.raises(DuplicateMatcherRegistrationError):
        registry.register(GlobMatcher)


def test_register_non_pattern() -> None:
    registry = PatternMatcherRegistry()
    with pytest.raises(TypeError):
        registry.register(object)


def test_parse() -> None:
    matcher = pattern_registry.pattern_from_string("foo")
    matcher.compile()
    assert matcher.match("foo")
    assert not matcher.match("Foo")
    assert isinstance(matcher, ExactMatcher)
    assert not matcher.inverted
    assert matcher.case_action == CaseAction.NONE


def test_parse_error_bad_type() -> None:
    with pytest.raises(
        TypeError, match="Unable to parse pattern string of type 'int'"
    ):
        pattern_registry.pattern_from_string(27)  # type: ignore[type-var]


def test_parse_error_no_matcher() -> None:
    with pytest.raises(LookupError, match="av"):
        pattern_registry.pattern_from_string("av:cs:foo")


def test_parse_error_no_case_action() -> None:
    with pytest.raises(LookupError, match="av"):
        pattern_registry.pattern_from_string("regex:av:foo")


def test_parse_error_no_default_matcher() -> None:
    registry = PatternMatcherRegistry()
    with pytest.raises(NoMatchersAvailableError):
        registry.pattern_from_string("foo")


@pytest.mark.parametrize(
    ("pattern", "success"), [("regex:foo\\\\a[-{", False), ("foo", True)]
)
def test_parse_error_bad_regex(pattern: str, success: bool) -> None:
    matcher = pattern_registry.pattern_from_string(pattern)
    assert matcher.try_compile() is success


def test_remove() -> None:
    registry = PatternMatcherRegistry()
    registry.register(GlobMatcher)
    assert registry["glob"] is GlobMatcher
    registry.remove("glob")
    with pytest.raises(NoSuchMatcherError):
        registry["glob"]
