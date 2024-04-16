import logging
import re
from pathlib import Path

from git import Repo

from .envvars import (
    GIT_AUTHOR_EMAIL,
    GIT_AUTHOR_NAME,
    GIT_BRANCH,
    GIT_PASSWORD,
    GIT_SRC_BRANCH,
    GIT_URL,
    GIT_USER,
)

log = logging.getLogger(__name__)

# Regex to match git url
GIT_URL_REG = re.compile(
    "(?P<scheme>https://|http://|ssh://|)"
    "(?P<creds>.*@)?"
    "(?P<host>[^:/]*)"
    "(?::(?P<port>\d+))?"
    "(?P<pathsep>(?:/|:)?)"
    "(?P<path>.*)$"
)
# m = GIT_URL_REG.match("https://www.gitlab.com/network/snow-catalog.git")
# m.groupdict()
# m = GIT_URL_REG.match("https://www.gitlab.com:80/network/snow-catalog.git")
# m.groupdict()
# m = GIT_URL_REG.match("git@gitlab.com:network/snow-catalog.git")
# m.groupdict()


def url_ensure_creds(url, username, password):
    m = GIT_URL_REG.match(url)
    if not m:
        raise ValueError(f"Invalid git url: {url}")
    scheme, creds, host, port, pathsep, path = m.groups()
    if creds:
        return url
    if not username:
        if not password:
            return url
        username = "token_user"  # password may be a token
    port_ = f":{port}" if port else ""
    return f"{scheme}{username}:{password}@{host}{port_}{pathsep}{path}"


DEFAULT_GIT_FOLDER = "workdir"
DEFAULT_AUTHOR = "Anonymous"
DEFAULT_AUTHOR_DOMAIN = "example.com"


class Git:
    def __init__(
        self,
        url=None,
        path=DEFAULT_GIT_FOLDER,
        username=None,
        password=None,
        author=None,
        email=None,
        src_branch=None,
        branch=None,
        use_env_variables=False,
    ):
        """
        Utility class to manage repository update from scripts
        Nb: If multiple operations need to be performed, prefer to re-clone the repository

        url: the url of the remote repository (if folder already exists, replace the remote)
        path: the path of the cloned repository
        username: username for the login (not required with ssh. Can be random with some token authentication)
        password: password/token for the login
        src_branch: the initial branch for the repository (useful to edit another branch than the default branch)
        branch: the work branch
        use_env_variables: Use environment variables to configure the instance
        """
        if use_env_variables:
            url = url or GIT_URL
            username = username or GIT_USER
            password = password or GIT_PASSWORD
            author = author or GIT_AUTHOR_NAME or username or DEFAULT_AUTHOR
            email = (
                email or GIT_AUTHOR_EMAIL or f"{author.lower()}@{DEFAULT_AUTHOR_DOMAIN}"
            )
            src_branch = src_branch or GIT_SRC_BRANCH
            branch = branch or GIT_BRANCH
        path = Path(path)
        self._url = url_ensure_creds(url, username, password)
        self._path = Path(path).resolve()
        # https://git-scm.com/book/en/v2/Git-Internals-Environment-Variables
        # https://gitpython.readthedocs.io/en/stable/reference.html?highlight=custom_environment#git.cmd.Git.custom_environment
        self._envvars = {
            "GIT_AUTHOR_NAME": author,
            "GIT_AUTHOR_EMAIL": email,
        }
        if self._path.exists():
            repo = Repo(self._path)
        else:
            repo = Repo.clone_from(
                self._url,
                self._path,
            )
        self.repo = repo
        if src_branch:
            self.change_branch(src_branch, auto_create=False)
        if branch:
            self.change_branch(branch)

    @property
    def path(self):
        return Path(self._path)

    def is_dirty(self):
        return self.repo.is_dirty(untracked_files=True)

    # def available_branches(self):
    #     branches = set()
    #     for remote in self._repo.remotes:
    #         for ref in remote.refs:
    #             branches.add(ref.remote_head)
    #     return branches

    def change_branch(self, branch, auto_create=True):
        # Try a simple checkout
        try:
            # Be sure to have all the remotes available
            self.fetch()
            self.repo.git.checkout(branch)
            return
        except Exception:
            if not auto_create:
                raise
        # Branch doesn't exist: try to create it
        self.repo.git.checkout("-b", branch)

    def restore_files(self, *files):
        self.repo.git.checkout(".", "--", *files)

    def add_files(self, *files, all=False):
        if all:
            self.repo.git.add("-A")
            return
        self.repo.git.add(*files)

    def commit(self, message: str):
        with self.repo.git.custom_environment(**self._envvars):
            self.repo.git.commit("-m", message)

    def push(self):
        args = []
        tracking_branch = self.repo.active_branch.tracking_branch()
        if not tracking_branch:
            remote = self.repo.remote().name
            branch = self.repo.active_branch.name
            args += ["--set-upstream", remote, branch]
        self.repo.git.push(*args)

    def fetch(self):
        self.repo.git.fetch()

    def _replace_remote(self, remote, url):
        try:
            self.repo.git.remote("remove", remote)
        except Exception:
            log.warning("Failed to remove remote")
        self.repo.git.remote("add", remote, url)

    def commit_push_everything(self, message):
        if not self.is_dirty():
            log.info("Nothing to commit")
            return
        self.add_files(all=True)
        self.commit(message)
        self.push()
