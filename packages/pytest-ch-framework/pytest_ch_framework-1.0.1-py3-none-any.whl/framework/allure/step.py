from typing import Any, Callable

import allure


def step(func: Callable[[...], Any], name: str = None ,*args, **kwargs)->Any:
    if not name:
        name = func.__name__
    func = allure.step(name)(func)
    return func(*args, **kwargs)
