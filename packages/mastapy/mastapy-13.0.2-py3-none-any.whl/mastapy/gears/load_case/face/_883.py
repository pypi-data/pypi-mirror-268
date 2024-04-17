"""FaceGearSetLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.load_case import _877
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase.Face", "FaceGearSetLoadCase"
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1232, _1223


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetLoadCase",)


Self = TypeVar("Self", bound="FaceGearSetLoadCase")


class FaceGearSetLoadCase(_877.GearSetLoadCaseBase):
    """FaceGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetLoadCase")

    class _Cast_FaceGearSetLoadCase:
        """Special nested class for casting FaceGearSetLoadCase to subclasses."""

        def __init__(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
            parent: "FaceGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def gear_set_load_case_base(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
        ) -> "_877.GearSetLoadCaseBase":
            return self._parent._cast(_877.GearSetLoadCaseBase)

        @property
        def gear_set_design_analysis(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
        ) -> "_1232.GearSetDesignAnalysis":
            from mastapy.gears.analysis import _1232

            return self._parent._cast(_1232.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def face_gear_set_load_case(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
        ) -> "FaceGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase":
        return self._Cast_FaceGearSetLoadCase(self)
