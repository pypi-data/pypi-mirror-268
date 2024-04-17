"""FaceGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6899
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "FaceGearLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2535
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6933,
        _6846,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearLoadCase",)


Self = TypeVar("Self", bound="FaceGearLoadCase")


class FaceGearLoadCase(_6899.GearLoadCase):
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
        def gear_load_case(
            self: "FaceGearLoadCase._Cast_FaceGearLoadCase",
        ) -> "_6899.GearLoadCase":
            return self._parent._cast(_6899.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "FaceGearLoadCase._Cast_FaceGearLoadCase",
        ) -> "_6933.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "FaceGearLoadCase._Cast_FaceGearLoadCase",
        ) -> "_6846.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ComponentLoadCase)

        @property
        def part_load_case(
            self: "FaceGearLoadCase._Cast_FaceGearLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "FaceGearLoadCase._Cast_FaceGearLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearLoadCase._Cast_FaceGearLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearLoadCase._Cast_FaceGearLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

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
    def component_design(self: Self) -> "_2535.FaceGear":
        """mastapy.system_model.part_model.gears.FaceGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "FaceGearLoadCase._Cast_FaceGearLoadCase":
        return self._Cast_FaceGearLoadCase(self)
