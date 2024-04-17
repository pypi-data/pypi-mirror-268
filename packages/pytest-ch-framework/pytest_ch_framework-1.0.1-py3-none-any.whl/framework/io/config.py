from collections import UserDict
from os import PathLike
from typing import Iterable, Tuple, TextIO


class Properties(UserDict):
    @classmethod
    def load_from_str(cls, content: Iterable[str]) -> 'Properties':
        data = {}
        for line in content:
            tp = cls.del_with(line)
            if tp is None:
                continue
            data[tp[0]] = tp[1]
        return Properties(data)

    @classmethod
    def load_from_file(cls, file: str | PathLike) -> 'Properties':
        with open(file, 'r', encoding="utf-8", newline=None) as f:
            l = [line.strip().rstrip("\n") for line in f]
        return cls.load_from_str(l)

    @classmethod
    def del_with(cls, line: str) -> Tuple[str, str] | None:
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            return None
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        return key, value

    def write(self, writer: TextIO):
        i = map(lambda x: "=".join(x) + "\n", self.items())
        writer.writelines(i)

    def write_file(self, file: str | PathLike):
        with open(file, 'wt', encoding="utf-8", newline=None) as f:
            self.write(f)
