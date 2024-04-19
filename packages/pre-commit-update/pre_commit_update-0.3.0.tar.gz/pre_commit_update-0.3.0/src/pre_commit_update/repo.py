import string
from typing import Dict, List

import git
from packaging.version import InvalidVersion
from packaging.version import parse as parse_version


class Repo:
    def __init__(self, repo: Dict, git_tags: List, all_versions: bool = False) -> None:
        self._url: str = repo["repo"]
        self._name: str = repo["repo"].split("/")[-1]
        self._git_tags: List = git_tags
        self._current_version: str = repo.get("rev", "N/A")
        self._latest_version: str = self._get_latest_version(all_versions)

    @property
    def _is_hash(self) -> bool:
        # The minimum length for an abbreviated hash is 4:
        # <https://git-scm.com/docs/git-config#Documentation/git-config.txt-coreabbrev>.
        if len(self._current_version) < 4:
            return False
        else:
            # Credit goes to Levon (https://stackoverflow.com/users/1209279/levon)
            # for this idea: <https://stackoverflow.com/a/11592279/7593853>.
            return all(
                character in string.hexdigits for character in self._current_version
            )

    @property
    def is_local(self) -> bool:
        return not self._url.startswith("http")

    @property
    def name(self) -> str:
        return self._name

    @property
    def current_version(self) -> str:
        return self._current_version

    @property
    def latest_version(self) -> str:
        return self._latest_version

    def _get_latest_tag(self, all_versions: bool) -> str:
        if all_versions:
            return self._git_tags[0]
        for t in self._git_tags:
            if not any(v in t for v in ("a", "b", "rc")):
                return t
        return self._git_tags[0]

    def _get_latest_hash(self) -> str:
        return git.cmd.Git().ls_remote("--exit-code", self._url, "HEAD").split()[0]

    def _get_latest_version(self, all_versions: bool) -> str:
        try:
            parse_version(self._current_version)
            return self._get_latest_tag(all_versions)
        except InvalidVersion:
            pass
        if self._is_hash:
            return self._get_latest_hash()
        return self._current_version
