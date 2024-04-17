"""ModalContributionDisplayMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_MODAL_CONTRIBUTION_DISPLAY_METHOD = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Results",
    "ModalContributionDisplayMethod",
)


__docformat__ = "restructuredtext en"
__all__ = ("ModalContributionDisplayMethod",)


Self = TypeVar("Self", bound="ModalContributionDisplayMethod")


class ModalContributionDisplayMethod(Enum):
    """ModalContributionDisplayMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MODAL_CONTRIBUTION_DISPLAY_METHOD

    ALL_MODES = 0
    MODE_INDEX = 1
    MODE_INDEX_RANGE = 2
    MODE_FREQUENCY_RANGE = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ModalContributionDisplayMethod.__setattr__ = __enum_setattr
ModalContributionDisplayMethod.__delattr__ = __enum_delattr
