"""FaceGearDiameterFaceWidthSpecificationMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FACE_GEAR_DIAMETER_FACE_WIDTH_SPECIFICATION_METHOD = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Face",
    "FaceGearDiameterFaceWidthSpecificationMethod",
)


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearDiameterFaceWidthSpecificationMethod",)


Self = TypeVar("Self", bound="FaceGearDiameterFaceWidthSpecificationMethod")


class FaceGearDiameterFaceWidthSpecificationMethod(Enum):
    """FaceGearDiameterFaceWidthSpecificationMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FACE_GEAR_DIAMETER_FACE_WIDTH_SPECIFICATION_METHOD

    FACE_WIDTH_AND_FACE_WIDTH_OFFSET = 0
    INNER_AND_OUTER_DIAMETER = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FaceGearDiameterFaceWidthSpecificationMethod.__setattr__ = __enum_setattr
FaceGearDiameterFaceWidthSpecificationMethod.__delattr__ = __enum_delattr
