"""
Base Pattern Module
*******************

Module for the :class:`RegexPattern` class.
"""

# pylint: disable=cyclic-import


import re
from typing import Any, Iterator, List, Optional, Tuple, Union

#:
ValidPatternType = Union[re.Pattern, str, "RegexPattern"]

#: Special characters that need to be escaped to be used without their special meanings.
ESCAPED_CHARACTERS = "()[]{}?*+-|^$\\.&~#"


def join(*patterns: ValidPatternType) -> "RegexPattern":
    """Umbrella function for combining :class:`ValidPatternType`'s into a :class:`RegexPattern`."""
    joined = RegexPattern("")
    for pattern in patterns:
        joined += RegexPattern(pattern)
    return joined


def escape(string: str) -> "RegexPattern":
    """Escapes special characters in a string to use them without their special meanings."""
    return RegexPattern(re.escape(string))


class RegexPattern:
    """
    The main object that represents Regular Expression Pattern strings for this library.
    """

    regex: str

    #: The precedence of the pattern. Higher precedence patterns are evaluated first.
    # Precedence order here (https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap09.html#tag_09_04_08)
    precedence: int

    def __init__(self, pattern: ValidPatternType, /, _precedence: int = 1) -> None:
        self.regex = self.get_regex(pattern)
        self.precedence = (
            _precedence if not isinstance(pattern, RegexPattern) else pattern.precedence
        )

    def __repr__(self) -> str:
        raw_regex = f"{self.regex!r}".replace("\\\\", "\\")
        return f"<RegexPattern {raw_regex}>"

    def __str__(self) -> str:
        return self.regex

    def __add__(self, other: ValidPatternType) -> "RegexPattern":
        """Adds two :class:`ValidPatternType`'s together, into a :class:`RegexPattern`"""
        from .patterns import Group  # pylint: disable=import-outside-toplevel

        try:
            other_pattern = (
                RegexPattern(other) if not isinstance(other, RegexPattern) else other
            )
        except TypeError:
            return NotImplemented

        if self.precedence > other_pattern.precedence:
            return RegexPattern(
                self.regex + self.get_regex(Group(other_pattern, capturing=False))
            )
        if self.precedence < other_pattern.precedence:
            return RegexPattern(
                self.get_regex(Group(self, capturing=False)) + other_pattern.regex
            )
        return RegexPattern(self.regex + other_pattern.regex)

    def __radd__(self, other: ValidPatternType) -> "RegexPattern":
        """Adds two :class:`ValidPatternType`'s together, into a :class:`RegexPattern`"""
        from .patterns import Group  # pylint: disable=import-outside-toplevel

        try:
            other_pattern = (
                RegexPattern(other) if not isinstance(other, RegexPattern) else other
            )
        except TypeError:
            return NotImplemented

        if self.precedence > other_pattern.precedence:
            return RegexPattern(
                self.get_regex(Group(other_pattern, capturing=False)) + self.regex
            )
        if self.precedence < other_pattern.precedence:
            return RegexPattern(
                other_pattern.regex + self.get_regex(Group(self, capturing=False))
            )
        return RegexPattern(other_pattern.regex + self.regex)

    def __mul__(self, coefficient: int) -> "RegexPattern":
        """Treats :class:`RegexPattern` as a string and multiplies it by an integer."""
        return RegexPattern(self.regex * coefficient)

    def __eq__(self, other: Any) -> bool:
        """
        Returns whether or not two :class:`ValidPatternType`'s have the same regex.
        Otherwise return false.
        """
        if isinstance(other, (str, re.Pattern, RegexPattern)):
            return (
                self.regex == RegexPattern(other).regex
                and self.precedence == RegexPattern(other).precedence
            )
        return super().__eq__(other)

    def __hash__(self) -> int:
        """Hashes the regex string."""
        return hash(self.regex)

    @staticmethod
    def get_regex(obj: ValidPatternType, /) -> str:
        """
        Extracts the regex content from :class:`RegexPattern` or :class:`re.Pattern` objects
        else return the input :class:`str`.
        """
        if isinstance(obj, RegexPattern):
            return obj.regex
        if isinstance(obj, str):
            return obj
        if isinstance(obj, re.Pattern):
            return obj.pattern
        raise TypeError(f"Can't get regex from {obj.__class__.__qualname__} object.")

    def compile(
        self,
        *,
        flags: int = 0,
    ) -> re.Pattern:
        """See :func:`re.compile`."""
        return re.compile(self.regex, flags=flags)

    def match(
        self,
        content: str,
        /,
        *,
        flags: int = 0,
    ) -> Optional[re.Match]:
        """See :meth:`re.Pattern.match`."""
        return self.compile(flags=flags).match(content)

    def fullmatch(
        self,
        content: str,
        /,
        *,
        flags: int = 0,
    ) -> Optional[re.Match]:
        """See :meth:`re.Pattern.fullmatch`."""
        return self.compile(flags=flags).fullmatch(content)

    def findall(
        self,
        content: str,
        /,
        *,
        flags: int = 0,
    ) -> List[Tuple[str, ...]]:
        """See :meth:`re.Pattern.findall`."""
        return self.compile(flags=flags).findall(content)

    def finditer(
        self,
        content: str,
        /,
        *,
        flags: int = 0,
    ) -> Iterator[re.Match]:
        """See :meth:`re.Pattern.finditer`."""
        return self.compile(flags=flags).finditer(content)

    def split(
        self,
        content: str,
        /,
        maxsplit: int = 0,
        *,
        flags: int = 0,
    ) -> List[Any]:
        """See :meth:`re.Pattern.split`."""
        return self.compile(flags=flags).split(content, maxsplit=maxsplit)

    def sub(
        self,
        replacement: str,
        content: str,
        /,
        count: int = 0,
        *,
        flags: int = 0,
    ) -> str:
        """See :meth:`re.Pattern.sub`."""
        return self.compile(flags=flags).sub(replacement, content, count=count)

    def subn(
        self,
        replacement: str,
        content: str,
        /,
        count: int = 0,
        *,
        flags: int = 0,
    ) -> Tuple[str, int]:
        """See :meth:`re.Pattern.subn`."""
        return self.compile(flags=flags).subn(replacement, content, count=count)

    def search(
        self,
        content: str,
        /,
        pos: int = 0,
        endpos: int = 0,
        *,
        flags: int = 0,
    ) -> Optional[re.Match]:
        """See :meth:`re.Pattern.search`."""
        return self.compile(flags=flags).search(content, pos, endpos)
