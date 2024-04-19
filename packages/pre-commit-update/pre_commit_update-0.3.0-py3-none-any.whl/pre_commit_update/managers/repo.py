import re
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Tuple

import git
from git import GitCommandError
from packaging.version import InvalidVersion
from packaging.version import parse as parse_version

from ..repo import Repo
from . import MessageManager


class RepoManager:
    def __init__(
        self, repos_data: Dict, all_versions: bool, exclude: Tuple, keep: Tuple
    ) -> None:
        self._all_versions: bool = all_versions
        self._exclude: Tuple = exclude
        self._keep: Tuple = keep
        self._repos_data: Dict = repos_data
        self._repos_tags: List = self._get_repos_git_tags()
        self._repos_list: List[Repo] = self._get_repos_list()

    @property
    def repos_data(self) -> Dict:
        return self._repos_data

    @staticmethod
    def _get_repo_fixed_git_tags(tag_versions: List) -> List:
        # Due to various prefixes that devs choose for tags, strip them down to semantic version numbers only.
        # Store it inside the dict ("ver1.2.3": "1.2.3") and parse the value to get the correct sort.
        # Remove invalid suffixes ("-test", "-split", ...)
        # Return the original value (key) once everything is parsed/sorted.
        fixed_tags: Dict = {}
        for tag in tag_versions:
            for prefix in re.findall("([a-zA-Z ]*)\\d*.*", tag):
                prefix = prefix.strip()
                try:
                    version: str = tag[len(prefix) :]
                    parse_version(version)
                    fixed_tags[tag] = version
                except InvalidVersion:
                    continue
        fixed_tags = {
            k: v
            for k, v in sorted(
                fixed_tags.items(),
                key=lambda item: parse_version(item[1]),
                reverse=True,
            )
        }
        return list(fixed_tags.keys())

    @staticmethod
    def _get_repo_git_tags(repo: Dict) -> List:
        url: str = repo["repo"]
        try:
            remote_tags: List = (
                git.cmd.Git()
                .ls_remote("--exit-code", "--tags", url, sort="v:refname")
                .split("\n")
            )
            tags: List = []
            for tag in remote_tags:
                parsed_tag: str = re.split(r"\t+", tag)[1]
                if parsed_tag.endswith("^{}"):
                    continue
                parsed_tag = parsed_tag.replace("refs/tags/", "")
                tags.append(parsed_tag)
            return tags
        except GitCommandError as ex:
            if ex.status == 2:
                message = f"No tags found for repo: {url}"
            else:
                message = f"Failed to list tags for repo: {url}"
            raise Exception(message)

    def _get_repos_git_tags(self) -> List:
        with ThreadPoolExecutor(max_workers=10) as pool:
            tasks: List = []
            for repo in self._repos_data:
                tasks.append(pool.submit(self._get_repo_git_tags, repo))
        return tasks

    def _get_repos_list(self) -> List[Repo]:
        repo_list: List[Repo] = []
        for i, repo in enumerate(self._repos_data):
            try:
                repo_tags: List = self._get_repo_fixed_git_tags(
                    self._repos_tags[i].result()
                )
            except Exception:
                repo_tags = []
            repo_list.append(Repo(repo, repo_tags, self._all_versions))
        return repo_list

    def _is_repo_excluded(self, repo: Repo) -> bool:
        return repo.name in self._exclude

    def _is_repo_kept(self, repo: Repo) -> bool:
        return repo.name in self._keep

    def get_updates(self, messages: MessageManager) -> None:
        for i, repo in enumerate(self._repos_list):
            if repo.is_local:
                continue
            if self._is_repo_excluded(repo):
                messages.add_excluded_message(repo.name, repo.current_version)
                continue
            if self._is_repo_kept(repo):
                messages.add_kept_message(
                    repo.name, repo.current_version, repo.latest_version
                )
                continue
            if repo.current_version != repo.latest_version:
                messages.add_to_update_message(
                    repo.name, repo.current_version, repo.latest_version
                )
                self._repos_data[i]["rev"] = repo.latest_version
                continue
            messages.add_no_update_message(repo.name, repo.current_version)
