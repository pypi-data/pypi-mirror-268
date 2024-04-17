import io

import yaml

from ..mod.mod import mod_file_path
from os import PathLike
from typing import Sequence, Any, Iterable


def read_yaml(fp: str | PathLike, encoding: str = 'utf-8') -> str:
    with open(fp, mode="rt", encoding=encoding, newline=None) as f:
        data = f.read()
    return data


def mod_yaml(fp: str | PathLike, encoding: str = 'utf-8') -> str:
    """
    从模块同路径读取同名yaml文件
    :param fp:
    :param encoding:
    :return: str 文件内容
    """
    ph = mod_file_path(fp, "yaml")
    yaml_data = read_yaml(ph, encoding)
    return yaml_data


def mod_yaml_object(fp: str | PathLike, encoding: str = 'utf-8') -> Any:
    """
    从模块同路径读取同名yaml文件内容用yaml解析
    :param fp:
    :param encoding:
    :return:
    """
    data = mod_yaml(fp, encoding)
    return yaml.safe_load(data)


class DataTest:
    def __init__(self, data: dict):
        self.__data = data

    def param_names(self, key: str) -> Sequence[str]:
        return self.__data[key]["param_names"]

    def params(self, key: str) -> Iterable[object | Sequence[object]]:
        return self.__data[key]["params"]

    def kv_params(self, key: str) -> Iterable[dict]:
        """
        将参数名称和参数值组成为一个字典
        :param key:
        :return:  返回一个生成器
        """
        # return (dict(zip(self.param_names(key), item)) for item in self.params(key))
        for item in self.params(key):
            yield dict(zip(self.param_names(key), item))

    def name(self, key: str) -> str:
        return self.__data[key]["name"]

    def http(self, key: str) -> dict:
        return self.__data[key]["http"]

    def http_path(self, key: str) -> str:
        return self.__data[key]["http"]["path"]

    def http_head(self, key: str) -> dict:
        return self.__data[key]["http"]["head"]

    def http_body(self, key: str) -> Any:
        return self.__data[key]["http"]["body"]
