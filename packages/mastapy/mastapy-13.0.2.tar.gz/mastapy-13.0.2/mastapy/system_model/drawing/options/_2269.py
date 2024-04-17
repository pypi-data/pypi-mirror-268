"""ExcitationAnalysisViewOption"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_EXCITATION_ANALYSIS_VIEW_OPTION = python_net_import(
    "SMT.MastaAPI.SystemModel.Drawing.Options", "ExcitationAnalysisViewOption"
)


__docformat__ = "restructuredtext en"
__all__ = ("ExcitationAnalysisViewOption",)


Self = TypeVar("Self", bound="ExcitationAnalysisViewOption")


class ExcitationAnalysisViewOption(Enum):
    """ExcitationAnalysisViewOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _EXCITATION_ANALYSIS_VIEW_OPTION

    COUPLED_MODES = 0
    UNCOUPLED_MODES = 1
    OPERATING_DEFLECTION_SHAPES_BY_EXCITATION = 2
    OPERATING_DEFLECTION_SHAPES_BY_ORDER = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ExcitationAnalysisViewOption.__setattr__ = __enum_setattr
ExcitationAnalysisViewOption.__delattr__ = __enum_delattr
