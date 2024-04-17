from typing import AnyStr

import regex

from polymatch import PolymorphicMatcher


class RegexMatcher(PolymorphicMatcher[AnyStr, "regex.Pattern[AnyStr]"]):
    def compile_pattern(
        self, raw_pattern: AnyStr, *, flags: int = 0
    ) -> "regex.Pattern[AnyStr]":
        return regex.compile(raw_pattern, flags)

    def compile_pattern_cs(
        self, raw_pattern: AnyStr
    ) -> "regex.Pattern[AnyStr]":
        return self.compile_pattern(raw_pattern)

    def compile_pattern_ci(
        self, raw_pattern: AnyStr
    ) -> "regex.Pattern[AnyStr]":
        return self.compile_pattern(raw_pattern, flags=regex.IGNORECASE)

    def compile_pattern_cf(
        self, raw_pattern: AnyStr
    ) -> "regex.Pattern[AnyStr]":
        return self.compile_pattern(
            raw_pattern, flags=regex.FULLCASE | regex.IGNORECASE
        )

    def match_text(
        self, pattern: "regex.Pattern[AnyStr]", text: AnyStr
    ) -> bool:
        return pattern.match(text) is not None

    def match_text_cf(
        self, pattern: "regex.Pattern[AnyStr]", text: AnyStr
    ) -> bool:
        return self.match_text(pattern, text)

    def match_text_ci(
        self, pattern: "regex.Pattern[AnyStr]", text: AnyStr
    ) -> bool:
        return self.match_text(pattern, text)

    def match_text_cs(
        self, pattern: "regex.Pattern[AnyStr]", text: AnyStr
    ) -> bool:
        return self.match_text(pattern, text)

    @classmethod
    def get_type(cls) -> str:
        return "regex"
