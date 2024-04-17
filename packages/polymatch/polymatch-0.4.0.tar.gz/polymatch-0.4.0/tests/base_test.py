import pytest

from polymatch import pattern_registry
from polymatch.base import CaseAction
from polymatch.error import (
    PatternNotCompiledError,
    PatternTextTypeMismatchError,
)
from polymatch.matchers.standard import ExactMatcher


def test_case_action_validate() -> None:
    with pytest.raises(
        TypeError, match="Case-folding is not supported with bytes patterns"
    ):
        _ = ExactMatcher(b"foo", CaseAction.CASEFOLD)


def test_type_mismatch() -> None:
    matcher = ExactMatcher(b"foo", CaseAction.CASEINSENSITIVE)
    with pytest.raises(PatternTextTypeMismatchError):
        matcher.match("foo")  # type: ignore[arg-type]


def test_compare() -> None:
    matcher = pattern_registry.pattern_from_string("exact:ci:foo")
    matcher.compile()
    res = matcher == 123
    assert not res
    res = matcher != "aaaaa"
    assert res
    res = matcher != "foo"
    assert not res
    res = matcher != 123
    assert res


def test_compare_invert() -> None:
    matcher = pattern_registry.pattern_from_string("~exact:ci:foo")
    matcher.compile()
    assert matcher == "lekndlwkn"
    assert matcher != "FOO"


def test_compare_no_compile() -> None:
    matcher = pattern_registry.pattern_from_string("~exact:ci:foo")
    with pytest.raises(PatternNotCompiledError):
        matcher.match("foo")
