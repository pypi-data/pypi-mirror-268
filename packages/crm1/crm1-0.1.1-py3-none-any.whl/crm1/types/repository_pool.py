"""Don't import this module directly."""

import warnings
from typing import Optional, overload

from .mod import Mod
from .repository import Repository


class RepositoryPool:
    """A pool of repositories."""

    repositories: dict[str, Repository]
    """The repositories in the pool."""

    def __init__(self):
        self.repositories = {}

    def add_repository(self, repo: Repository):
        """Adds a repository to the pool."""
        if not isinstance(repo, Repository):
            raise TypeError("Invalid repository type", type(repo))
        if repo.data.spec_version >= 2:
            for drepo in repo.data.deps:
                drepo_obj = Repository.from_address(drepo)
                if drepo_obj.data.root_id in self.repositories:
                    # Prevent loops
                    continue
                self.add_repository(drepo_obj)
        self.repositories[repo.data.root_id] = repo

    def get_repository(self, root_id: str) -> Repository:
        """Gets a repository by its root ID."""
        return self.repositories[root_id]

    def get_mod(self, id_: str) -> Optional[Mod]:
        """Gets a mod by its ID."""
        found_mods = self.get_mods(id_)
        if len(found_mods) == 0:
            return None
        if len(found_mods) > 1:
            warnings.warn(
                "Multiple mods with the same ID. "
                "Use .get_mods() to get all matching mods, not only the first one.",
                UserWarning,
            )
        return found_mods[0]

    def get_mods(self, id_: str) -> list[Mod]:
        """Gets all mods with the same ID."""
        mods = []
        for repo in self.repositories.values():
            mods.extend(repo.get_mods(id_))
        return mods

    def has_mod(self, id_: str) -> bool:
        """Checks if a mod exists in the pool."""
        return self.get_mod(id_) is not None

    def where_is(self, id_: str) -> Optional[Repository]:
        """Gets the repository that contains the mod."""
        for repo in self.repositories.values():
            if repo.has_mod(id_):
                return repo
        return None

    def update_repositories(self):
        """Updates all repositories in the pool."""
        for repo in self.repositories.values():
            repo.update()

    @overload
    @classmethod
    def make(cls, repos: list[Repository]) -> "RepositoryPool":
        """Creates a repository pool from a list of repositories."""

    @overload
    @classmethod
    def make(cls, *repos: Repository) -> "RepositoryPool":
        """Creates a repository pool from multiple repositories."""

    @classmethod
    def make(cls, *repos):
        """Creates a repository pool from repositories."""
        if len(repos) == 1 and isinstance(repos[0], list):
            repos = repos[0]
        pool = RepositoryPool()
        for repo in repos:
            if not isinstance(repo, Repository):
                raise TypeError("Invalid repository", repo)
            pool.add_repository(repo)
        return pool

    def __getitem__(self, key: str) -> Repository:
        return self.get_repository(key)
