"""ConicalGearStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3833
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ConicalGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2530
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3777,
        _3784,
        _3785,
        _3786,
        _3789,
        _3837,
        _3841,
        _3844,
        _3847,
        _3874,
        _3883,
        _3886,
        _3887,
        _3888,
        _3904,
        _3850,
        _3796,
        _3852,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearStabilityAnalysis",)


Self = TypeVar("Self", bound="ConicalGearStabilityAnalysis")


class ConicalGearStabilityAnalysis(_3833.GearStabilityAnalysis):
    """ConicalGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearStabilityAnalysis")

    class _Cast_ConicalGearStabilityAnalysis:
        """Special nested class for casting ConicalGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
            parent: "ConicalGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def gear_stability_analysis(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_3833.GearStabilityAnalysis":
            return self._parent._cast(_3833.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_3850.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3850,
            )

            return self._parent._cast(_3850.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_3796.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3796,
            )

            return self._parent._cast(_3796.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_3852.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(_3852.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_3777.AGMAGleasonConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3777,
            )

            return self._parent._cast(_3777.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def bevel_differential_gear_stability_analysis(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_3784.BevelDifferentialGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3784,
            )

            return self._parent._cast(_3784.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_stability_analysis(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_3785.BevelDifferentialPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3785,
            )

            return self._parent._cast(
                _3785.BevelDifferentialPlanetGearStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_stability_analysis(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_3786.BevelDifferentialSunGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.BevelDifferentialSunGearStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_3789.BevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3789,
            )

            return self._parent._cast(_3789.BevelGearStabilityAnalysis)

        @property
        def hypoid_gear_stability_analysis(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_3837.HypoidGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3837,
            )

            return self._parent._cast(_3837.HypoidGearStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_stability_analysis(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_3841.KlingelnbergCycloPalloidConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(
                _3841.KlingelnbergCycloPalloidConicalGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_stability_analysis(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_3844.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(
                _3844.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_stability_analysis(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_3847.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3847,
            )

            return self._parent._cast(
                _3847.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_stability_analysis(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_3874.SpiralBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3874,
            )

            return self._parent._cast(_3874.SpiralBevelGearStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_stability_analysis(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_3883.StraightBevelDiffGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3883,
            )

            return self._parent._cast(_3883.StraightBevelDiffGearStabilityAnalysis)

        @property
        def straight_bevel_gear_stability_analysis(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_3886.StraightBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3886,
            )

            return self._parent._cast(_3886.StraightBevelGearStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_3887.StraightBevelPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3887,
            )

            return self._parent._cast(_3887.StraightBevelPlanetGearStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_stability_analysis(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_3888.StraightBevelSunGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3888,
            )

            return self._parent._cast(_3888.StraightBevelSunGearStabilityAnalysis)

        @property
        def zerol_bevel_gear_stability_analysis(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "_3904.ZerolBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3904,
            )

            return self._parent._cast(_3904.ZerolBevelGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
        ) -> "ConicalGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2530.ConicalGear":
        """mastapy.system_model.part_model.gears.ConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConicalGearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearStabilityAnalysis._Cast_ConicalGearStabilityAnalysis":
        return self._Cast_ConicalGearStabilityAnalysis(self)
