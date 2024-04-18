"""Don't import this module directly."""

from dataclasses import dataclass, field

from dataclasses_hjson import DataClassHjsonMixin

from .mod import RMod


@dataclass
class RRepository(DataClassHjsonMixin):
    """Raw repository data. This is used for deserialization."""

    last_updated: int
    """The timestamp of the last update of the repository."""
    root_id: str
    """The root ID of the repository."""
    mods: list[RMod]
    """A list of mods in the repository."""
    spec_version: int = 2
    """The version of the repository specification."""
    deps: list[str] = field(default_factory=list)
    """A list of repositories that this repository depends on."""
