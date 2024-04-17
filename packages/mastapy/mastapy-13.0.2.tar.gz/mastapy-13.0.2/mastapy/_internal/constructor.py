"""constructor.py

Module for constructing new mastapy objects. This is a workaround for cyclic
imports, where this module only references sys.modules and does not keep
local copies of modules.
"""

from __future__ import annotations

import sys
import importlib
from typing import Type, TypeVar

from mastapy._internal.constructor_map import _get_mastapy_type


T = TypeVar("T")


def new_from_mastapy(module_path: str, class_name: str):
    """Indirect object constructor using mastapy type.
    Fetches classes from sys.modules.

    Args:
        module_path (str): Module path.
        class_name (str): Name of the class.
    """
    return getattr(importlib.import_module(module_path), class_name)


def new_from_mastapy_class(class_: Type[T]):
    """Indirect object constructor using mastapy type.
    Fetches classes from sys.modules.

    Args:
        class_ (Type[T]): Mastapy class for wrapping
    """
    module_path = class_.__module__
    class_name = class_.__name__
    return getattr(sys.modules[module_path], class_name)


def new(namespace: str, name: str):
    """Indirect object constructor using Python.NET type.
    Fetches classes from sys.modules.

    Args:
        namespace (str): Namespace of the Python.NET type.
        name (str): Name of the Python.NET type.
    """
    new_class = _get_mastapy_type(namespace, name)
    return new_from_mastapy_class(new_class)
