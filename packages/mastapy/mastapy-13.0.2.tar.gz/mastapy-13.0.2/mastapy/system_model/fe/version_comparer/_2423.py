"""LoadCasesToRun"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_LOAD_CASES_TO_RUN = python_net_import(
    "SMT.MastaAPI.SystemModel.FE.VersionComparer", "LoadCasesToRun"
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadCasesToRun",)


Self = TypeVar("Self", bound="LoadCasesToRun")


class LoadCasesToRun(Enum):
    """LoadCasesToRun

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _LOAD_CASES_TO_RUN

    HIGHEST_LOAD_IN_EACH_DESIGN_STATE = 0
    HIGHEST_LOAD = 1
    ALL = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


LoadCasesToRun.__setattr__ = __enum_setattr
LoadCasesToRun.__delattr__ = __enum_delattr
