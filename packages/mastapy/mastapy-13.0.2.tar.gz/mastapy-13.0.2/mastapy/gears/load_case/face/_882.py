"""FaceGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.load_case import _876
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase.Face", "FaceGearLoadCase"
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1224, _1221


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearLoadCase",)


Self = TypeVar("Self", bound="FaceGearLoadCase")


class FaceGearLoadCase(_876.GearLoadCaseBase):
    """FaceGearLoadCase

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearLoadCase")

    class _Cast_FaceGearLoadCase:
        """Special nested class for casting FaceGearLoadCase to subclasses."""

        def __init__(
            self: "FaceGearLoadCase._Cast_FaceGearLoadCase", parent: "FaceGearLoadCase"
        ):
            self._parent = parent

        @property
        def gear_load_case_base(
            self: "FaceGearLoadCase._Cast_FaceGearLoadCase",
        ) -> "_876.GearLoadCaseBase":
            return self._parent._cast(_876.GearLoadCaseBase)

        @property
        def gear_design_analysis(
            self: "FaceGearLoadCase._Cast_FaceGearLoadCase",
        ) -> "_1224.GearDesignAnalysis":
            from mastapy.gears.analysis import _1224

            return self._parent._cast(_1224.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "FaceGearLoadCase._Cast_FaceGearLoadCase",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def face_gear_load_case(
            self: "FaceGearLoadCase._Cast_FaceGearLoadCase",
        ) -> "FaceGearLoadCase":
            return self._parent

        def __getattr__(self: "FaceGearLoadCase._Cast_FaceGearLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "FaceGearLoadCase._Cast_FaceGearLoadCase":
        return self._Cast_FaceGearLoadCase(self)
