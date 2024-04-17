"""WormGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6899
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "WormGearLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2558
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6933,
        _6846,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("WormGearLoadCase",)


Self = TypeVar("Self", bound="WormGearLoadCase")


class WormGearLoadCase(_6899.GearLoadCase):
    """WormGearLoadCase

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearLoadCase")

    class _Cast_WormGearLoadCase:
        """Special nested class for casting WormGearLoadCase to subclasses."""

        def __init__(
            self: "WormGearLoadCase._Cast_WormGearLoadCase", parent: "WormGearLoadCase"
        ):
            self._parent = parent

        @property
        def gear_load_case(
            self: "WormGearLoadCase._Cast_WormGearLoadCase",
        ) -> "_6899.GearLoadCase":
            return self._parent._cast(_6899.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "WormGearLoadCase._Cast_WormGearLoadCase",
        ) -> "_6933.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "WormGearLoadCase._Cast_WormGearLoadCase",
        ) -> "_6846.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ComponentLoadCase)

        @property
        def part_load_case(
            self: "WormGearLoadCase._Cast_WormGearLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "WormGearLoadCase._Cast_WormGearLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearLoadCase._Cast_WormGearLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearLoadCase._Cast_WormGearLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def worm_gear_load_case(
            self: "WormGearLoadCase._Cast_WormGearLoadCase",
        ) -> "WormGearLoadCase":
            return self._parent

        def __getattr__(self: "WormGearLoadCase._Cast_WormGearLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2558.WormGear":
        """mastapy.system_model.part_model.gears.WormGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "WormGearLoadCase._Cast_WormGearLoadCase":
        return self._Cast_WormGearLoadCase(self)
