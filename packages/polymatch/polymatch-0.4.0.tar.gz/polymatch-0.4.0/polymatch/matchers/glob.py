from fnmatch import translate
from typing import TYPE_CHECKING, AnyStr

from polymatch.matchers.regex import RegexMatcher

if TYPE_CHECKING:
    import regex


class GlobMatcher(RegexMatcher[AnyStr]):
    def compile_pattern(
        self, raw_pattern: AnyStr, *, flags: int = 0
    ) -> "regex.Pattern[AnyStr]":
        if isinstance(raw_pattern, str):
            res = translate(raw_pattern)
        else:
            # Mimic how fnmatch handles bytes patterns
            pat_str = str(raw_pattern, "ISO-8859-1")
            res_str = translate(pat_str)
            res = bytes(res_str, "ISO-8859-1")

        return RegexMatcher.compile_pattern(self, res, flags=flags)

    @classmethod
    def get_type(cls) -> str:
        return "glob"
