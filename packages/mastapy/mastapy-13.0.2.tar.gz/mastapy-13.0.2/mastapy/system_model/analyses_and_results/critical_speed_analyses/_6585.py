"""ConicalGearSetCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6614
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ConicalGearSetCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2531
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6557,
        _6564,
        _6569,
        _6618,
        _6622,
        _6625,
        _6628,
        _6655,
        _6661,
        _6664,
        _6682,
        _6652,
        _6551,
        _6633,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConicalGearSetCriticalSpeedAnalysis")


class ConicalGearSetCriticalSpeedAnalysis(_6614.GearSetCriticalSpeedAnalysis):
    """ConicalGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetCriticalSpeedAnalysis")

    class _Cast_ConicalGearSetCriticalSpeedAnalysis:
        """Special nested class for casting ConicalGearSetCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
            parent: "ConicalGearSetCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6614.GearSetCriticalSpeedAnalysis":
            return self._parent._cast(_6614.GearSetCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6652.SpecialisedAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6652,
            )

            return self._parent._cast(_6652.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6551.AbstractAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6551,
            )

            return self._parent._cast(_6551.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6633.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6557.AGMAGleasonConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6557,
            )

            return self._parent._cast(
                _6557.AGMAGleasonConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6564.BevelDifferentialGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(
                _6564.BevelDifferentialGearSetCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6569.BevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6569,
            )

            return self._parent._cast(_6569.BevelGearSetCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6618.HypoidGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6618,
            )

            return self._parent._cast(_6618.HypoidGearSetCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6622.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(
                _6622.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6625.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(
                _6625.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6628.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6628,
            )

            return self._parent._cast(
                _6628.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6655.SpiralBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6655,
            )

            return self._parent._cast(_6655.SpiralBevelGearSetCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6661.StraightBevelDiffGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6661,
            )

            return self._parent._cast(
                _6661.StraightBevelDiffGearSetCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6664.StraightBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6664,
            )

            return self._parent._cast(_6664.StraightBevelGearSetCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6682.ZerolBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6682,
            )

            return self._parent._cast(_6682.ZerolBevelGearSetCriticalSpeedAnalysis)

        @property
        def conical_gear_set_critical_speed_analysis(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
        ) -> "ConicalGearSetCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "ConicalGearSetCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2531.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "ConicalGearSetCriticalSpeedAnalysis._Cast_ConicalGearSetCriticalSpeedAnalysis"
    ):
        return self._Cast_ConicalGearSetCriticalSpeedAnalysis(self)
