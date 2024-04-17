import csv
import io
from ..mod.mod import mod_file_path
from os import PathLike
from typing import Sequence


def read_csv(fp: str | PathLike, encoding: str = 'utf-8') -> str:
    with open(fp, mode="rt", encoding=encoding, newline="") as f:
        data = f.read()
    return data


def mod_csv(fp: str | PathLike, encoding: str = 'utf-8') -> str:
    ph = mod_file_path(fp, "csv")
    csv_data = read_csv(ph, encoding)
    return csv_data


class CsvGener:
    def load(self, csv_data: str):
        self.__header = None
        self.__data = None
        reader = csv.reader(io.StringIO(csv_data), dialect="excel")
        data = [d for d in reader]
        if data:
            self.__header = data[0]
        length = len(self.__header)
        data = data[1:]
        if length < 1 or len(data) == 0:
            return
        self.__data = [self._map(r) for r in data]

    def _map(self, row: Sequence[str]) -> Sequence[str]:
        lh = len(self.__header)
        lr = len(row)
        if lh == lr:
            return row
        elif lh > lr:
            return [row[i] if i < lr else None for i in range(lh)]
        else:
            return row[:lh]

    @property
    def header(self):
        return self.__header

    def gener(self):
        yield from self.__data

    def __len__(self):
        return len(self.__data)


def mod_csv_gener(fp: str | PathLike, encoding: str = 'utf-8') -> CsvGener:
    data = mod_csv(fp, encoding)
    ge = CsvGener()
    ge.load(data)
    return ge
