"""A module for handling versions."""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class VersionEndMode(Enum):
    """The mode of the end of a version range. This can be inclusive or exclusive."""

    INCLUSIVE = "inclusive"
    EXCLUSIVE = "exclusive"


DONTCARE = VersionEndMode.EXCLUSIVE
"""This is used to represent the end of a version range which's version is not specified."""


def _make_list_fun(lst, ln=2, fun=None):
    return lst + [fun] * (ln - len(lst))


@dataclass
class Version:
    """A version."""

    major: int
    """The major version."""
    minor: int
    """The minor version."""
    patch: int
    """The patch version."""
    prerelease_tags: list[str]
    """The prerelease tags of the version."""
    build_metadata: Optional[str]
    """The build metadata part of the version."""

    @staticmethod
    def from_string(version: str) -> "Version":
        """Create a Version object from a string.
        The string should be in the format of `major.minor.patch`."""
        primary, secondary = _make_list_fun(version.split("-", 1))
        primary = primary.split(".")
        if len(primary) < 2:
            raise ValueError(f"Version string should have at least 2 primary parts: {version}")
        if len(primary) > 3:
            raise ValueError(f"Version string should have at most 3 primary parts: {version}")
        major = int(primary[0])
        minor = int(primary[1])
        patch = int(primary[2]) if len(primary) == 3 else 0
        if len(primary) == 3:
            prerelease, build_metadata = (
                _make_list_fun(secondary.split("+", 1)) if secondary is not None else [None, None]
            )
            prerelease_tags = prerelease.split(".") if prerelease is not None else []
        else:
            prerelease_tags = []
            build_metadata = None
        return Version(major, minor, patch, prerelease_tags, build_metadata)

    def to_string(self) -> str:
        """Convert the version to a string in the format of `major.minor.patch`."""
        return (
            f"{self.major}.{self.minor}"
            + (f".{self.patch}" if self.patch is not None else "")
            + (f"-{'.'.join(self.prerelease_tags)}" if self.prerelease_tags else "")
        )

    def __eq__(self, other: "Version") -> bool:
        return (
            self.major == other.major
            and self.minor == other.minor
            and self.patch == other.patch
            and self.prerelease_tags == other.prerelease_tags
        )

    def __lt__(self, other: "Version") -> bool:
        if (self.major, self.minor, self.patch) == (other.major, other.minor, other.patch):
            return [
                ((False, int(tag)) if tag.isdigit() else (True, tag)) for tag in self.prerelease_tags
            ] < [
                ((False, int(tag)) if tag.isdigit() else (True, tag)) for tag in other.prerelease_tags
            ]
        return (self.major, self.minor, self.patch) < (
            other.major,
            other.minor,
            other.patch
        )

    def __le__(self, other: "Version") -> bool:
        return self == other or self < other

    def __gt__(self, other: "Version") -> bool:
        return not self <= other

    def __ge__(self, other: "Version") -> bool:
        return not self < other

    def __ne__(self, other: "Version") -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((self.major, self.minor, self.patch, '.'.join(self.prerelease_tags)), self.build_metadata)

    def __repr__(self) -> str:
        return f"Version({self.major}, {self.minor}, {self.patch}, {'.'.join(self.prerelease_tags) if self.prerelease_tags else None}, {self.build_metadata})"

    def __str__(self) -> str:
        return self.to_string()


@dataclass
class VersionRange:
    """A range of versions."""

    lower: Optional[Version]
    """The lower bound of the range."""
    lower_mode: VersionEndMode
    """The mode of the lower bound of the range."""
    upper: Optional[Version]
    """The upper bound of the range."""
    upper_mode: VersionEndMode
    """The mode of the upper bound of the range."""

    def __post_init__(self):
        if (
            self.lower is not None
            and self.upper is not None
            and self.lower > self.upper
        ):
            raise ValueError("Invalid range")

    @staticmethod
    def from_string(range_: str) -> "VersionRange":
        """Create a VersionRange object from a string.
        The string should be in the format of `[lower,upper]`. Examples: `[1.0,2.0.1)`, `(1.0,]`.
        """
        if range_.startswith("["):
            lower_mode = VersionEndMode.INCLUSIVE
        elif range_.startswith("("):
            lower_mode = VersionEndMode.EXCLUSIVE
        else:
            return VersionRange(
                Version.from_string(range_),
                DONTCARE,
                Version.from_string(range_),
                DONTCARE,
            )
        if range_.endswith("]"):
            upper_mode = VersionEndMode.INCLUSIVE
        elif range_.endswith(")"):
            upper_mode = VersionEndMode.EXCLUSIVE
        else:
            raise ValueError(
                f"Version range string should end with ']' or ')': {range_}"
            )
        range_ = range_[1:-1]
        parts = range_.split(",")
        if len(parts) != 2:
            raise ValueError(
                f"Version range string should have 2 parts - lower and upper end: {range_}"
            )
        lower = Version.from_string(parts[0]) if parts[0] else None
        upper = Version.from_string(parts[1]) if parts[1] else None
        return VersionRange(lower, lower_mode, upper, upper_mode)

    def to_string(self) -> str:
        """Convert the version range to a string in the format of `[lower,upper]`.
        Examples: `[1.0,2.0.1)`, `(1.0,]`."""
        if (
            self.lower is not None
            and self.upper is not None
            and self.lower == self.upper
        ):
            return self.lower.to_string()
        return (
            (
                ("[" if self.lower_mode == VersionEndMode.INCLUSIVE else "(")
                if self.lower is not None
                else "("
            )
            + (self.lower.to_string() if self.lower else "")
            + ","
            + (self.upper.to_string() if self.upper else "")
            + (
                ("]" if self.upper_mode == VersionEndMode.INCLUSIVE else ")")
                if self.upper is not None
                else ")"
            )
        )

    def contains(self, version: Version) -> bool:
        """Check if the version is in the range."""
        if self.lower is not None:
            if version < self.lower:
                return False
            if self.lower_mode == VersionEndMode.EXCLUSIVE and version == self.lower:
                return False
        if self.upper is not None:
            if version > self.upper:
                return False
            if self.upper_mode == VersionEndMode.EXCLUSIVE and version == self.upper:
                return False
        return True

    def __contains__(self, version: Version) -> bool:
        return self.contains(version)

    def __str__(self) -> str:
        return self.to_string()


def range_from_maven_string(version: str):
    """Create a VersionRange object from a Maven version string."""
    if version == "*":
        return VersionRange(None, DONTCARE, None, DONTCARE)
    if version.startswith(">="):
        lower_mode = VersionEndMode.INCLUSIVE
        lower = Version.from_string(version[2:])
        upper = None
        upper_mode = DONTCARE
    elif version.startswith(">"):
        lower_mode = VersionEndMode.EXCLUSIVE
        lower = Version.from_string(version[1:])
        upper = None
        upper_mode = DONTCARE
    elif version.startswith("<="):
        lower_mode = DONTCARE
        lower = None
        upper = Version.from_string(version[2:])
        upper_mode = VersionEndMode.INCLUSIVE
    elif version.startswith("<"):
        lower_mode = DONTCARE
        lower = None
        upper = Version.from_string(version[1:])
        upper_mode = VersionEndMode.EXCLUSIVE
    else:
        lower_mode = VersionEndMode.INCLUSIVE
        lower = Version.from_string(version)
        upper = Version.from_string(version)
        upper_mode = VersionEndMode.INCLUSIVE
    return VersionRange(lower, lower_mode, upper, upper_mode)
