"""HypoidGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6822
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "HypoidGearLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6853,
        _6899,
        _6933,
        _6846,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearLoadCase",)


Self = TypeVar("Self", bound="HypoidGearLoadCase")


class HypoidGearLoadCase(_6822.AGMAGleasonConicalGearLoadCase):
    """HypoidGearLoadCase

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearLoadCase")

    class _Cast_HypoidGearLoadCase:
        """Special nested class for casting HypoidGearLoadCase to subclasses."""

        def __init__(
            self: "HypoidGearLoadCase._Cast_HypoidGearLoadCase",
            parent: "HypoidGearLoadCase",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_load_case(
            self: "HypoidGearLoadCase._Cast_HypoidGearLoadCase",
        ) -> "_6822.AGMAGleasonConicalGearLoadCase":
            return self._parent._cast(_6822.AGMAGleasonConicalGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "HypoidGearLoadCase._Cast_HypoidGearLoadCase",
        ) -> "_6853.ConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6853

            return self._parent._cast(_6853.ConicalGearLoadCase)

        @property
        def gear_load_case(
            self: "HypoidGearLoadCase._Cast_HypoidGearLoadCase",
        ) -> "_6899.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6899

            return self._parent._cast(_6899.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "HypoidGearLoadCase._Cast_HypoidGearLoadCase",
        ) -> "_6933.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "HypoidGearLoadCase._Cast_HypoidGearLoadCase",
        ) -> "_6846.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ComponentLoadCase)

        @property
        def part_load_case(
            self: "HypoidGearLoadCase._Cast_HypoidGearLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "HypoidGearLoadCase._Cast_HypoidGearLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearLoadCase._Cast_HypoidGearLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearLoadCase._Cast_HypoidGearLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def hypoid_gear_load_case(
            self: "HypoidGearLoadCase._Cast_HypoidGearLoadCase",
        ) -> "HypoidGearLoadCase":
            return self._parent

        def __getattr__(self: "HypoidGearLoadCase._Cast_HypoidGearLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2541.HypoidGear":
        """mastapy.system_model.part_model.gears.HypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "HypoidGearLoadCase._Cast_HypoidGearLoadCase":
        return self._Cast_HypoidGearLoadCase(self)
