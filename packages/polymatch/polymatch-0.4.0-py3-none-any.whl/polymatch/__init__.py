from polymatch.base import CaseAction, PolymorphicMatcher
from polymatch.error import (
    DuplicateMatcherRegistrationError,
    NoMatchersAvailableError,
    NoSuchMatcherError,
    PatternCompileError,
    PatternNotCompiledError,
    PatternTextTypeMismatchError,
)
from polymatch.registry import pattern_registry

__version__ = "0.3.0"

__all__ = [
    "PolymorphicMatcher",
    "CaseAction",
    "pattern_registry",
    "NoSuchMatcherError",
    "NoMatchersAvailableError",
    "PatternNotCompiledError",
    "PatternCompileError",
    "PatternTextTypeMismatchError",
    "DuplicateMatcherRegistrationError",
]
