"""ElmerResultType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ELMER_RESULT_TYPE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.Elmer", "ElmerResultType"
)


__docformat__ = "restructuredtext en"
__all__ = ("ElmerResultType",)


Self = TypeVar("Self", bound="ElmerResultType")


class ElmerResultType(Enum):
    """ElmerResultType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ELMER_RESULT_TYPE

    MAGNETIC_FLUX_DENSITY = 0
    MAGNETIC_VECTOR_POTENTIAL = 1
    CURRENT_DENSITY = 2
    NODAL_FORCE = 3
    TOTAL_CORE_LOSS = 4
    NODAL_CORE_LOSS = 5
    GEOMETRY_ID = 6
    HYSTERESIS_CORE_LOSS = 7
    EDDY_CURRENT_CORE_LOSS = 8
    EXCESS_CORE_LOSS = 9
    MAGNET_LOSS = 10
    MAGNET_EDDY_CURRENT_DENSITY = 11
    WINDING_AC_LOSS = 12
    WINDING_AC_LOSS_AVERAGE = 13
    WINDING_EDDY_CURRENT_DENSITY = 14
    DISPLACEMENT = 15
    STRESS_XX = 16
    STRESS_YY = 17
    STRESS_XY = 18
    VON_MISES_STRESS = 19
    CONTACT_NORMAL_LOAD = 20
    CONTACT_SLIP_LOAD = 21
    ACTIVE_CONTACT = 22
    CONTACT_DISTANCE = 23
    CONTACT_GAP = 24
    NONE = 25
    TEMPERATURE = 26


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ElmerResultType.__setattr__ = __enum_setattr
ElmerResultType.__delattr__ = __enum_delattr
