"""KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6622
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2546
    from mastapy.system_model.analyses_and_results.static_loads import _6926
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6623,
        _6624,
        _6585,
        _6614,
        _6652,
        _6551,
        _6633,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis"
)


class KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis(
    _6622.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",
        ) -> "_6622.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis":
            return self._parent._cast(
                _6622.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def conical_gear_set_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",
        ) -> "_6585.ConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6585,
            )

            return self._parent._cast(_6585.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",
        ) -> "_6614.GearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6614,
            )

            return self._parent._cast(_6614.GearSetCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",
        ) -> "_6652.SpecialisedAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6652,
            )

            return self._parent._cast(_6652.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",
        ) -> "_6551.AbstractAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6551,
            )

            return self._parent._cast(_6551.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",
        ) -> "_6633.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2546.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(
        self: Self,
    ) -> "_6926.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_critical_speed_analysis(
        self: Self,
    ) -> "List[_6623.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_critical_speed_analysis(
        self: Self,
    ) -> "List[_6624.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis(
            self
        )
