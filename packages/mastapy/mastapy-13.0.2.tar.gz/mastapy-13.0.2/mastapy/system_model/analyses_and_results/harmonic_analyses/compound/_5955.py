"""KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5921
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
        "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5785
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5958,
        _5961,
        _5947,
        _5985,
        _5887,
        _5966,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis"
)


class KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis(
    _5921.ConicalGearSetCompoundHarmonicAnalysis
):
    """KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5921.ConicalGearSetCompoundHarmonicAnalysis":
            return self._parent._cast(_5921.ConicalGearSetCompoundHarmonicAnalysis)

        @property
        def gear_set_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5947.GearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5947,
            )

            return self._parent._cast(_5947.GearSetCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5985.SpecialisedAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5985,
            )

            return self._parent._cast(_5985.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5887.AbstractAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5887,
            )

            return self._parent._cast(_5887.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5966.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(_5966.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5958.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(
                _5958.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5961.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5961,
            )

            return self._parent._cast(
                _5961.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5785.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis]

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
    ) -> "List[_5785.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis]

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
    ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis":
        return (
            self._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis(
                self
            )
        )
