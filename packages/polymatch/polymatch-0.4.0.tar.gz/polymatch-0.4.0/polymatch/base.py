from abc import ABCMeta, abstractmethod
from enum import Enum
from typing import (
    AnyStr,
    Callable,
    Generic,
    Optional,
    Tuple,
    Type,
    TypeVar,
    cast,
)

import polymatch
from polymatch.error import (
    PatternCompileError,
    PatternNotCompiledError,
    PatternTextTypeMismatchError,
)


class CaseAction(Enum):
    NONE = "none", ""  # Use whatever the pattern's default is
    CASESENSITIVE = "case-sensitive", "cs"  # Fore case sensitivity
    CASEINSENSITIVE = "case-insensitive", "ci"  # Force case insensitivity
    CASEFOLD = "casefold", "cf"  # Force case-folded comparison


AnyPattern = TypeVar("AnyPattern")

TUPLE_V1 = Tuple[AnyStr, CaseAction, bool, AnyPattern, Type[AnyStr], object]
TUPLE_V2 = Tuple[
    str, AnyStr, CaseAction, bool, Optional[AnyPattern], Type[AnyStr], object
]

CompileFunc = Callable[[AnyStr], AnyPattern]
MatchFunc = Callable[[AnyPattern, AnyStr], bool]

FuncTuple = Tuple[
    CompileFunc[AnyStr, AnyPattern], MatchFunc[AnyPattern, AnyStr]
]


class PolymorphicMatcher(Generic[AnyStr, AnyPattern], metaclass=ABCMeta):
    _empty = object()

    def __init__(
        self,
        pattern: AnyStr,
        /,
        case_action: CaseAction = CaseAction.NONE,
        *,
        invert: bool = False,
    ) -> None:
        self._raw_pattern: AnyStr = pattern
        self._str_type: Type[AnyStr] = type(pattern)
        self._compiled_pattern: Optional[AnyPattern] = None
        self._case_action = case_action
        self._invert = invert

        funcs: FuncTuple[AnyStr, AnyPattern] = self._get_case_functions()
        self._compile_func: CompileFunc[AnyStr, AnyPattern] = funcs[0]
        self._match_func: MatchFunc[AnyPattern, AnyStr] = funcs[1]

        if self._case_action is CaseAction.CASEFOLD and self._str_type is bytes:
            msg = "Case-folding is not supported with bytes patterns"
            raise TypeError(msg)

    def try_compile(self) -> bool:
        try:
            self.compile()
        except PatternCompileError:
            return False

        return True

    def compile(self) -> None:  # noqa: A003
        try:
            self._compiled_pattern = self._compile_func(self.pattern)
        except Exception as e:  # noqa: BLE001
            msg = f"Failed to compile pattern {self.pattern!r}"
            raise PatternCompileError(msg) from e

    def __eq__(self, other: object) -> bool:
        if isinstance(other, self._str_type):
            return self.match(other)

        return NotImplemented

    def __ne__(self, other: object) -> bool:
        if isinstance(other, self._str_type):
            return not self.match(other)

        return NotImplemented

    def match(self, text: AnyStr) -> bool:
        if not isinstance(text, self._str_type):
            raise PatternTextTypeMismatchError(self._str_type, type(text))

        if self._compiled_pattern is None:
            # If it wasn't compiled
            msg = "Pattern must be compiled."
            raise PatternNotCompiledError(msg)

        out = self._match_func(self._compiled_pattern, text)

        if self.inverted:
            return not out

        return out

    def is_compiled(self) -> bool:
        return self._compiled_pattern is not None

    @abstractmethod
    def compile_pattern(self, raw_pattern: AnyStr) -> AnyPattern:
        raise NotImplementedError

    @abstractmethod
    def compile_pattern_cs(self, raw_pattern: AnyStr) -> AnyPattern:
        """Matchers should override this to compile their pattern with case-sensitive options"""
        raise NotImplementedError

    @abstractmethod
    def compile_pattern_ci(self, raw_pattern: AnyStr) -> AnyPattern:
        """Matchers should override this to compile their pattern with case-insensitive options"""
        raise NotImplementedError

    @abstractmethod
    def compile_pattern_cf(self, raw_pattern: AnyStr) -> AnyPattern:
        """Matchers should override this to compile their pattern with case-folding options"""
        raise NotImplementedError

    @abstractmethod
    def match_text(self, pattern: AnyPattern, text: AnyStr) -> bool:
        raise NotImplementedError

    def match_text_cs(self, pattern: AnyPattern, text: AnyStr) -> bool:
        return self.match_text(pattern, text)

    def match_text_ci(self, pattern: AnyPattern, text: AnyStr) -> bool:
        return self.match_text(pattern, text.lower())

    def match_text_cf(self, pattern: AnyPattern, text: AnyStr) -> bool:
        if isinstance(text, bytes):
            msg = "Casefold is not supported on bytes patterns"
            raise TypeError(msg)

        return self.match_text(pattern, text.casefold())

    def _get_case_functions(
        self,
    ) -> Tuple[CompileFunc[AnyStr, AnyPattern], MatchFunc[AnyPattern, AnyStr]]:
        suffix = self.case_action.value[1]

        if suffix:
            suffix = f"_{suffix}"

        comp_func = cast(
            CompileFunc[AnyStr, AnyPattern],
            getattr(self, f"compile_pattern{suffix}"),
        )
        match_func = cast(
            MatchFunc[AnyPattern, AnyStr], getattr(self, f"match_text{suffix}")
        )
        return comp_func, match_func

    @classmethod
    @abstractmethod
    def get_type(cls) -> str:
        raise NotImplementedError

    @property
    def pattern(self) -> AnyStr:
        return self._raw_pattern

    @property
    def case_action(self) -> CaseAction:
        return self._case_action

    @property
    def inverted(self) -> bool:
        return self._invert

    def to_string(self) -> AnyStr:
        if isinstance(self.pattern, str):
            return "{}{}:{}:{}".format(
                "~" if self.inverted else "",
                self.get_type(),
                self.case_action.value[1],
                self.pattern,
            )

        return (
            "{}{}:{}:".format(
                "~" if self.inverted else "",
                self.get_type(),
                self.case_action.value[1],
            )
        ).encode() + self.pattern

    def __str__(self) -> str:
        res = self.to_string()
        if isinstance(res, str):
            return res

        return res.decode()

    def __repr__(self) -> str:
        return "{}(pattern={!r}, case_action={}, invert={!r})".format(
            type(self).__name__, self.pattern, self.case_action, self.inverted
        )

    def __getstate__(self) -> TUPLE_V2[AnyStr, AnyPattern]:
        return (
            polymatch.__version__,
            self.pattern,
            self.case_action,
            self.inverted,
            self._compiled_pattern,
            self._str_type,
            self._empty,
        )

    def __setstate__(self, state: TUPLE_V2[AnyStr, AnyPattern]) -> None:
        (
            version,
            self._raw_pattern,
            self._case_action,
            self._invert,
            _compiled_pattern,
            self._str_type,
            self._empty,
        ) = state
        # This is compatibility code, we can't serialize a pickled object to match this
        if _compiled_pattern is self._empty:  # pragma: no cover
            _compiled_pattern = None

        self._compiled_pattern = _compiled_pattern
        self._compile_func, self._match_func = self._get_case_functions()

        if version != polymatch.__version__ and self.is_compiled():
            self.compile()
