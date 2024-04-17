from typing import AnyStr

from polymatch import PolymorphicMatcher


class ExactMatcher(PolymorphicMatcher[AnyStr, AnyStr]):
    def compile_pattern(self, raw_pattern: AnyStr) -> AnyStr:
        return raw_pattern

    def compile_pattern_cs(self, raw_pattern: AnyStr) -> AnyStr:
        return raw_pattern

    def compile_pattern_ci(self, raw_pattern: AnyStr) -> AnyStr:
        return raw_pattern.lower()

    def compile_pattern_cf(self, raw_pattern: AnyStr) -> AnyStr:
        if isinstance(raw_pattern, str):
            return raw_pattern.casefold()

        msg = "Casefold is not supported on bytes patterns"
        raise TypeError(msg)

    def match_text(self, pattern: AnyStr, text: AnyStr) -> bool:
        return text == pattern

    @classmethod
    def get_type(cls) -> str:
        return "exact"


class ContainsMatcher(PolymorphicMatcher[AnyStr, AnyStr]):
    def compile_pattern(self, raw_pattern: AnyStr) -> AnyStr:
        return raw_pattern

    def compile_pattern_cs(self, raw_pattern: AnyStr) -> AnyStr:
        return raw_pattern

    def compile_pattern_ci(self, raw_pattern: AnyStr) -> AnyStr:
        return raw_pattern.lower()

    def compile_pattern_cf(self, raw_pattern: AnyStr) -> AnyStr:
        if isinstance(raw_pattern, bytes):
            msg = "Casefold is not supported on bytes patterns"
            raise TypeError(msg)

        return raw_pattern.casefold()

    def match_text(self, pattern: AnyStr, text: AnyStr) -> bool:
        return pattern in text

    @classmethod
    def get_type(cls) -> str:
        return "contains"
