from typing import TYPE_CHECKING, AnyStr, Type

if TYPE_CHECKING:
    from polymatch.base import AnyPattern

__all__ = [
    "PatternCompileError",
    "PatternNotCompiledError",
    "PatternTextTypeMismatchError",
    "DuplicateMatcherRegistrationError",
    "NoSuchMatcherError",
    "NoMatchersAvailableError",
]


class PatternCompileError(ValueError):
    pass


class PatternNotCompiledError(ValueError):
    pass


class PatternTextTypeMismatchError(TypeError):
    def __init__(
        self, pattern_type: "Type[AnyPattern]", text_type: Type[AnyStr]
    ) -> None:
        super().__init__(
            "Pattern of type {!r} can not match text of type {!r}".format(
                pattern_type.__name__, text_type.__name__
            )
        )


class DuplicateMatcherRegistrationError(ValueError):
    def __init__(self, name: str) -> None:
        super().__init__(f"Attempted o register a duplicate matcher {name!r}")


class NoSuchMatcherError(LookupError):
    pass


class NoMatchersAvailableError(ValueError):
    pass
