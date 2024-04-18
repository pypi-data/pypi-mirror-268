"""Don't import this module directly."""

from typing import TYPE_CHECKING, Optional, Union, overload

from .. import spec

if TYPE_CHECKING:
    from .mod import Mod
    from .repository import Repository
    from .repository_pool import RepositoryPool


class Dependency:
    """A mod dependency."""

    id: str
    """The ID of the mod."""
    version: str
    """The version of the mod."""
    source: Optional[str]
    """The repository rootId of the mod."""
    mod: Optional["Mod"] = None

    def __init__(self, meta: spec.RDependency):
        self.id = meta.id
        self.version = meta.version
        self.source = meta.source
        self.mod = None

    @overload
    def resolve(self, pool: "RepositoryPool") -> "Mod":
        """
        Resolves the dependency using the given pool.

        WARNING: This does not yet check for source (if using pools) or version.
        """

    @overload
    def resolve(self, repository: "Repository") -> "Mod":
        """
        Resolves the dependency using the given repository.

        WARNING: This does not yet check for source (if using pools) or version.
        """

    def resolve(self, repo: Union["RepositoryPool", "Repository"]):
        """
        Resolves the dependency.

        WARNING: This does not yet check for source (if using pools) or version.
        """
        self.mod = repo.get_mod(self.id)
        return self.mod

    @overload
    def resolves(self, pool: "RepositoryPool") -> "Mod":
        """
        Resolves the dependency using the given pool.

        WARNING: This does not yet check for source (if using pools) or version.
        """

    @overload
    def resolves(self, repository: "Repository") -> "Mod":
        """
        Resolves the dependency using the given repository.

        WARNING: This does not yet check for source (if using pools) or version.
        """

    def resolves(self, repo: Union["RepositoryPool", "Repository"]):
        """
        Resolves the dependency.

        WARNING: This does not yet check for source (if using pools) or version.
        """
        self.mod = repo.get_mods(self.id)
        return self.mod
