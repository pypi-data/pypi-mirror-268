"""KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6585
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_CRITICAL_SPEED_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
        "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6625,
        _6628,
        _6614,
        _6652,
        _6551,
        _6633,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis"
)


class KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis(
    _6585.ConicalGearSetCriticalSpeedAnalysis
):
    """KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6585.ConicalGearSetCriticalSpeedAnalysis":
            return self._parent._cast(_6585.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6614.GearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6614,
            )

            return self._parent._cast(_6614.GearSetCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6652.SpecialisedAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6652,
            )

            return self._parent._cast(_6652.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6551.AbstractAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6551,
            )

            return self._parent._cast(_6551.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6633.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6625.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(
                _6625.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "_6628.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6628,
            )

            return self._parent._cast(
                _6628.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2544.KlingelnbergCycloPalloidConicalGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet

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
    ) -> "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis(
            self
        )
