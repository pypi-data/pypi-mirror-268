"""StraightBevelSunGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6968
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelSunGearLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2557
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6836,
        _6822,
        _6853,
        _6899,
        _6933,
        _6846,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearLoadCase",)


Self = TypeVar("Self", bound="StraightBevelSunGearLoadCase")


class StraightBevelSunGearLoadCase(_6968.StraightBevelDiffGearLoadCase):
    """StraightBevelSunGearLoadCase

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelSunGearLoadCase")

    class _Cast_StraightBevelSunGearLoadCase:
        """Special nested class for casting StraightBevelSunGearLoadCase to subclasses."""

        def __init__(
            self: "StraightBevelSunGearLoadCase._Cast_StraightBevelSunGearLoadCase",
            parent: "StraightBevelSunGearLoadCase",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_load_case(
            self: "StraightBevelSunGearLoadCase._Cast_StraightBevelSunGearLoadCase",
        ) -> "_6968.StraightBevelDiffGearLoadCase":
            return self._parent._cast(_6968.StraightBevelDiffGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "StraightBevelSunGearLoadCase._Cast_StraightBevelSunGearLoadCase",
        ) -> "_6836.BevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6836

            return self._parent._cast(_6836.BevelGearLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "StraightBevelSunGearLoadCase._Cast_StraightBevelSunGearLoadCase",
        ) -> "_6822.AGMAGleasonConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6822

            return self._parent._cast(_6822.AGMAGleasonConicalGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "StraightBevelSunGearLoadCase._Cast_StraightBevelSunGearLoadCase",
        ) -> "_6853.ConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6853

            return self._parent._cast(_6853.ConicalGearLoadCase)

        @property
        def gear_load_case(
            self: "StraightBevelSunGearLoadCase._Cast_StraightBevelSunGearLoadCase",
        ) -> "_6899.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6899

            return self._parent._cast(_6899.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "StraightBevelSunGearLoadCase._Cast_StraightBevelSunGearLoadCase",
        ) -> "_6933.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "StraightBevelSunGearLoadCase._Cast_StraightBevelSunGearLoadCase",
        ) -> "_6846.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ComponentLoadCase)

        @property
        def part_load_case(
            self: "StraightBevelSunGearLoadCase._Cast_StraightBevelSunGearLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "StraightBevelSunGearLoadCase._Cast_StraightBevelSunGearLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelSunGearLoadCase._Cast_StraightBevelSunGearLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearLoadCase._Cast_StraightBevelSunGearLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "StraightBevelSunGearLoadCase._Cast_StraightBevelSunGearLoadCase",
        ) -> "StraightBevelSunGearLoadCase":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearLoadCase._Cast_StraightBevelSunGearLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelSunGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2557.StraightBevelSunGear":
        """mastapy.system_model.part_model.gears.StraightBevelSunGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelSunGearLoadCase._Cast_StraightBevelSunGearLoadCase":
        return self._Cast_StraightBevelSunGearLoadCase(self)
