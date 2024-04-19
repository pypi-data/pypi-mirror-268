from typing import Any, Dict

from ruamel.yaml import YAML


class YAMLManager:
    def __init__(self, path: str) -> None:
        self._file: YAML = YAML()
        self._path: str = path
        self._data: Any = None
        self._configure()
        self._load()

    @property
    def data(self) -> Any:
        return self._data

    @data.setter
    def data(self, value: Dict) -> None:
        self._data = value

    def _configure(self) -> None:
        self._file.indent(sequence=4)
        self._file.preserve_quotes = True

    def _load(self) -> None:
        with open(self._path, encoding="utf-8") as f:
            self._data = self._file.load(f.read())

    def dump(self) -> None:
        with open(self._path, "w", encoding="utf-8") as f:
            self._file.dump(self.data, f)
