"""ConicalGearCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ConicalGearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2530
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6555,
        _6562,
        _6565,
        _6566,
        _6567,
        _6616,
        _6620,
        _6623,
        _6626,
        _6653,
        _6659,
        _6662,
        _6665,
        _6666,
        _6680,
        _6631,
        _6576,
        _6633,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConicalGearCriticalSpeedAnalysis")


class ConicalGearCriticalSpeedAnalysis(_6612.GearCriticalSpeedAnalysis):
    """ConicalGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearCriticalSpeedAnalysis")

    class _Cast_ConicalGearCriticalSpeedAnalysis:
        """Special nested class for casting ConicalGearCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
            parent: "ConicalGearCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6612.GearCriticalSpeedAnalysis":
            return self._parent._cast(_6612.GearCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6631.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6631,
            )

            return self._parent._cast(_6631.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6576.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6576,
            )

            return self._parent._cast(_6576.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6633.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6555.AGMAGleasonConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6555,
            )

            return self._parent._cast(_6555.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6562.BevelDifferentialGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6562,
            )

            return self._parent._cast(_6562.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6565.BevelDifferentialPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6565,
            )

            return self._parent._cast(
                _6565.BevelDifferentialPlanetGearCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6566.BevelDifferentialSunGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6566,
            )

            return self._parent._cast(
                _6566.BevelDifferentialSunGearCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6567.BevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6567,
            )

            return self._parent._cast(_6567.BevelGearCriticalSpeedAnalysis)

        @property
        def hypoid_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6616.HypoidGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6616,
            )

            return self._parent._cast(_6616.HypoidGearCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6620.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6620,
            )

            return self._parent._cast(
                _6620.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6623.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6623,
            )

            return self._parent._cast(
                _6623.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6626.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6626,
            )

            return self._parent._cast(
                _6626.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6653.SpiralBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6653,
            )

            return self._parent._cast(_6653.SpiralBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6659.StraightBevelDiffGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6659,
            )

            return self._parent._cast(_6659.StraightBevelDiffGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6662.StraightBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6662,
            )

            return self._parent._cast(_6662.StraightBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6665.StraightBevelPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6665,
            )

            return self._parent._cast(
                _6665.StraightBevelPlanetGearCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6666.StraightBevelSunGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6666,
            )

            return self._parent._cast(_6666.StraightBevelSunGearCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6680.ZerolBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6680,
            )

            return self._parent._cast(_6680.ZerolBevelGearCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "ConicalGearCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearCriticalSpeedAnalysis.TYPE"):
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
    def planetaries(self: Self) -> "List[ConicalGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConicalGearCriticalSpeedAnalysis]

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
    ) -> "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis":
        return self._Cast_ConicalGearCriticalSpeedAnalysis(self)
