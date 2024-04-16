# from contextlib import contextmanager
import logging
from pathlib import Path
from typing import Callable

import yaml
from pydantic import BaseModel

from snowd import Client, Git, timestampfilestate

log = logging.getLogger(__name__)


class Context:
    def __init__(
        self,
        resource,
        get_save=None,
        commit_message="Automatic commit",
        validator=None,
    ) -> None:
        self._is_open = True
        self.client = None
        self.git = None
        self.last = None
        self.now = None
        self.resource = None
        self.data = None
        _validator = validator
        if issubclass(_validator, BaseModel):

            def _validator(d):
                return validator.model_validate(d).model_dump()

        self.validator = _validator
        self._resource = resource
        self.commit_message = commit_message
        if isinstance(get_save, tuple):
            get, save = get_save
        elif isinstance(get_save, Callable):
            get, save = get_save()
        else:
            if not get_save:
                get_save = "timestamp.txt"
            if isinstance(get_save, (str, Path)):
                get, save = timestampfilestate(get_save)
            else:
                raise Exception(f"Invalid value for get_save: {get_save}")
        self.get = get
        self.save = save
        self._is_open = False

    def __getattribute__(self, attr):
        open_only = {"client", "git", "last", "now", "resource", "data", "save", "get"}
        is_open = object.__getattribute__(self, "_is_open")
        if attr in open_only and not is_open:
            raise Exception(
                f"Attribute {attr} of {Context} can only be access when open."
            )
        return object.__getattribute__(self, attr)

    @property
    def path(self):
        return Path(self.git.path)

    def open(self):
        if self._is_open:
            raise Exception("Context is already open")
        self._is_open = True
        self.client = Client(use_env_variables=True)
        self.git = Git(use_env_variables=True)
        self.last = self.get()
        self.now = self.client.now()
        self.resource = self.client.resource(self._resource)
        log.debug(f"Retrieving from {self.last} -> {self.now}")
        data = self.client.get_all_since(self.resource, self.last, self.now)
        if self.validator:
            data = [self.validator(d) for d in data]
        self.data = data
        return self

    def close(self, commit_message=None):
        if not self._is_open:
            raise Exception("Context is already closed")
        if not commit_message:
            commit_message = self.commit_message
        self.git.commit_push_everything(commit_message)
        self.save(self.now)
        self.client = Client(use_env_variables=True)
        self.git = Git(use_env_variables=True)
        self.client = None
        self.git = None
        self.last = None
        self.now = None
        self.resource = None
        self.data = None
        self._is_open = False

    def __enter__(self):
        return self.open()

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.close()


ID_KEY = "sys_id"


def records2dict(data):
    return dict(t for t in ((d.get(ID_KEY), d) for d in data) if t[0])


def update_yaml(file, data):
    file = Path(file)
    file.touch()
    local = records2dict(yaml.safe_load(file.read_text()) or [])
    for d in data:
        local[d[ID_KEY]] = d
    file.write_text(yaml.dump(sorted(local.values(), key=lambda x: x[ID_KEY])))
