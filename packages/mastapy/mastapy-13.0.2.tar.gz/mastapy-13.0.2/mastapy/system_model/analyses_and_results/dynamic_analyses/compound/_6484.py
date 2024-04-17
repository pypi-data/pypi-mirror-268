"""KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6450
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
        "KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6487,
        _6490,
        _6476,
        _6514,
        _6416,
        _6495,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis"
)


class KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis(
    _6450.ConicalGearSetCompoundDynamicAnalysis
):
    """KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis",
        ) -> "_6450.ConicalGearSetCompoundDynamicAnalysis":
            return self._parent._cast(_6450.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis",
        ) -> "_6476.GearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6476,
            )

            return self._parent._cast(_6476.GearSetCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis",
        ) -> "_6514.SpecialisedAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6514,
            )

            return self._parent._cast(_6514.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis",
        ) -> "_6416.AbstractAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6416,
            )

            return self._parent._cast(_6416.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis",
        ) -> "_6495.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6495,
            )

            return self._parent._cast(_6495.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis",
        ) -> "_6487.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(
                _6487.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis",
        ) -> "_6490.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6490,
            )

            return self._parent._cast(
                _6490.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6355.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6355.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis(
            self
        )
