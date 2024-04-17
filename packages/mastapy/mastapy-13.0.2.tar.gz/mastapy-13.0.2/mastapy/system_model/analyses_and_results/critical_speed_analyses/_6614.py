"""GearSetCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6652
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "GearSetCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6557,
        _6564,
        _6569,
        _6582,
        _6585,
        _6603,
        _6609,
        _6618,
        _6622,
        _6625,
        _6628,
        _6638,
        _6655,
        _6661,
        _6664,
        _6679,
        _6682,
        _6551,
        _6633,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearSetCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="GearSetCriticalSpeedAnalysis")


class GearSetCriticalSpeedAnalysis(_6652.SpecialisedAssemblyCriticalSpeedAnalysis):
    """GearSetCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetCriticalSpeedAnalysis")

    class _Cast_GearSetCriticalSpeedAnalysis:
        """Special nested class for casting GearSetCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
            parent: "GearSetCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6652.SpecialisedAssemblyCriticalSpeedAnalysis":
            return self._parent._cast(_6652.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6551.AbstractAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6551,
            )

            return self._parent._cast(_6551.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6633.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6557.AGMAGleasonConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6557,
            )

            return self._parent._cast(
                _6557.AGMAGleasonConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6564.BevelDifferentialGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(
                _6564.BevelDifferentialGearSetCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6569.BevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6569,
            )

            return self._parent._cast(_6569.BevelGearSetCriticalSpeedAnalysis)

        @property
        def concept_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6582.ConceptGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6582,
            )

            return self._parent._cast(_6582.ConceptGearSetCriticalSpeedAnalysis)

        @property
        def conical_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6585.ConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6585,
            )

            return self._parent._cast(_6585.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6603.CylindricalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6603,
            )

            return self._parent._cast(_6603.CylindricalGearSetCriticalSpeedAnalysis)

        @property
        def face_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6609.FaceGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6609,
            )

            return self._parent._cast(_6609.FaceGearSetCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6618.HypoidGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6618,
            )

            return self._parent._cast(_6618.HypoidGearSetCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6622.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(
                _6622.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6625.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(
                _6625.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6628.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6628,
            )

            return self._parent._cast(
                _6628.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
            )

        @property
        def planetary_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6638.PlanetaryGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6638,
            )

            return self._parent._cast(_6638.PlanetaryGearSetCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6655.SpiralBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6655,
            )

            return self._parent._cast(_6655.SpiralBevelGearSetCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6661.StraightBevelDiffGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6661,
            )

            return self._parent._cast(
                _6661.StraightBevelDiffGearSetCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6664.StraightBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6664,
            )

            return self._parent._cast(_6664.StraightBevelGearSetCriticalSpeedAnalysis)

        @property
        def worm_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6679.WormGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6679,
            )

            return self._parent._cast(_6679.WormGearSetCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6682.ZerolBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6682,
            )

            return self._parent._cast(_6682.ZerolBevelGearSetCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "GearSetCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2539.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

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
    ) -> "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis":
        return self._Cast_GearSetCriticalSpeedAnalysis(self)
