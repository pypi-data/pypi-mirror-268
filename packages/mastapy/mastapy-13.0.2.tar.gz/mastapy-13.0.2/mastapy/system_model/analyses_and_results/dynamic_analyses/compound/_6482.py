"""KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6448
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6485,
        _6488,
        _6474,
        _6493,
        _6441,
        _6495,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis"
)


class KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis(
    _6448.ConicalGearCompoundDynamicAnalysis
):
    """KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis",
        ) -> "_6448.ConicalGearCompoundDynamicAnalysis":
            return self._parent._cast(_6448.ConicalGearCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis",
        ) -> "_6474.GearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6474,
            )

            return self._parent._cast(_6474.GearCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis",
        ) -> "_6493.MountableComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6493,
            )

            return self._parent._cast(_6493.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis",
        ) -> "_6441.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6441,
            )

            return self._parent._cast(_6441.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis",
        ) -> "_6495.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6495,
            )

            return self._parent._cast(_6495.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis",
        ) -> "_6485.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6485,
            )

            return self._parent._cast(
                _6485.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis",
        ) -> "_6488.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6488,
            )

            return self._parent._cast(
                _6488.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6353.KlingelnbergCycloPalloidConicalGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidConicalGearDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6353.KlingelnbergCycloPalloidConicalGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidConicalGearDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis(
            self
        )
