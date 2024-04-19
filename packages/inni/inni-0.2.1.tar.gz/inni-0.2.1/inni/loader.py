from importlib import import_module
from typing import Type

from inni.modules.base import BaseModule


def load_module(name: str) -> Type[BaseModule]:
    try:
        mod = import_module("inni.modules." + name)
    except ModuleNotFoundError:
        mod = import_module(name)

    return mod.Module
