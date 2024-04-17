"""BevelGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6822
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BevelGearLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2526
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6831,
        _6834,
        _6835,
        _6962,
        _6968,
        _6971,
        _6974,
        _6975,
        _6994,
        _6853,
        _6899,
        _6933,
        _6846,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearLoadCase",)


Self = TypeVar("Self", bound="BevelGearLoadCase")


class BevelGearLoadCase(_6822.AGMAGleasonConicalGearLoadCase):
    """BevelGearLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearLoadCase")

    class _Cast_BevelGearLoadCase:
        """Special nested class for casting BevelGearLoadCase to subclasses."""

        def __init__(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
            parent: "BevelGearLoadCase",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6822.AGMAGleasonConicalGearLoadCase":
            return self._parent._cast(_6822.AGMAGleasonConicalGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6853.ConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6853

            return self._parent._cast(_6853.ConicalGearLoadCase)

        @property
        def gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6899.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6899

            return self._parent._cast(_6899.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6933.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6846.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ComponentLoadCase)

        @property
        def part_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6831.BevelDifferentialGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6831

            return self._parent._cast(_6831.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6834.BevelDifferentialPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6834

            return self._parent._cast(_6834.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6835.BevelDifferentialSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6835

            return self._parent._cast(_6835.BevelDifferentialSunGearLoadCase)

        @property
        def spiral_bevel_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6962.SpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6962

            return self._parent._cast(_6962.SpiralBevelGearLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6968.StraightBevelDiffGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6968

            return self._parent._cast(_6968.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6971.StraightBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6971

            return self._parent._cast(_6971.StraightBevelGearLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6974.StraightBevelPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6974

            return self._parent._cast(_6974.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6975.StraightBevelSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6975

            return self._parent._cast(_6975.StraightBevelSunGearLoadCase)

        @property
        def zerol_bevel_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "_6994.ZerolBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6994

            return self._parent._cast(_6994.ZerolBevelGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "BevelGearLoadCase._Cast_BevelGearLoadCase",
        ) -> "BevelGearLoadCase":
            return self._parent

        def __getattr__(self: "BevelGearLoadCase._Cast_BevelGearLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2526.BevelGear":
        """mastapy.system_model.part_model.gears.BevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BevelGearLoadCase._Cast_BevelGearLoadCase":
        return self._Cast_BevelGearLoadCase(self)
