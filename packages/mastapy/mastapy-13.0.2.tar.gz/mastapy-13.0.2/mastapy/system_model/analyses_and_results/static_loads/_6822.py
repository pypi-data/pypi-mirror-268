"""AGMAGleasonConicalGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6853
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AGMAGleasonConicalGearLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2520
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6831,
        _6834,
        _6835,
        _6836,
        _6914,
        _6962,
        _6968,
        _6971,
        _6974,
        _6975,
        _6994,
        _6899,
        _6933,
        _6846,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearLoadCase",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearLoadCase")


class AGMAGleasonConicalGearLoadCase(_6853.ConicalGearLoadCase):
    """AGMAGleasonConicalGearLoadCase

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearLoadCase")

    class _Cast_AGMAGleasonConicalGearLoadCase:
        """Special nested class for casting AGMAGleasonConicalGearLoadCase to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
            parent: "AGMAGleasonConicalGearLoadCase",
        ):
            self._parent = parent

        @property
        def conical_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6853.ConicalGearLoadCase":
            return self._parent._cast(_6853.ConicalGearLoadCase)

        @property
        def gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6899.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6899

            return self._parent._cast(_6899.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6933.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6846.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ComponentLoadCase)

        @property
        def part_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6831.BevelDifferentialGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6831

            return self._parent._cast(_6831.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6834.BevelDifferentialPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6834

            return self._parent._cast(_6834.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6835.BevelDifferentialSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6835

            return self._parent._cast(_6835.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6836.BevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6836

            return self._parent._cast(_6836.BevelGearLoadCase)

        @property
        def hypoid_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6914.HypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6914

            return self._parent._cast(_6914.HypoidGearLoadCase)

        @property
        def spiral_bevel_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6962.SpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6962

            return self._parent._cast(_6962.SpiralBevelGearLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6968.StraightBevelDiffGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6968

            return self._parent._cast(_6968.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6971.StraightBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6971

            return self._parent._cast(_6971.StraightBevelGearLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6974.StraightBevelPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6974

            return self._parent._cast(_6974.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6975.StraightBevelSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6975

            return self._parent._cast(_6975.StraightBevelSunGearLoadCase)

        @property
        def zerol_bevel_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6994.ZerolBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6994

            return self._parent._cast(_6994.ZerolBevelGearLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "AGMAGleasonConicalGearLoadCase":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2520.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

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
    ) -> "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase":
        return self._Cast_AGMAGleasonConicalGearLoadCase(self)
