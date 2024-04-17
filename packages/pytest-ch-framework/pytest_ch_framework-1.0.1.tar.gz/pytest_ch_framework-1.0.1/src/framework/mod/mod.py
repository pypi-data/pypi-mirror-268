import pathlib
from os import PathLike


def mod_file_path(fp: str | PathLike, ext: str) -> str:
    mp = pathlib.Path(fp)
    df = mp.parent / f"{mp.stem}.{ext}"
    return str(df)