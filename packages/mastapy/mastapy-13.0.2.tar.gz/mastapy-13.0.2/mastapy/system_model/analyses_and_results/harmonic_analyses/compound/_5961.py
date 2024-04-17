"""KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5955
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
        "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2548
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5791
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5959,
        _5960,
        _5921,
        _5947,
        _5985,
        _5887,
        _5966,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis"
)


class KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis(
    _5955.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis
):
    """KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis",
        ) -> "_5955.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis":
            return self._parent._cast(
                _5955.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def conical_gear_set_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis",
        ) -> "_5921.ConicalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5921,
            )

            return self._parent._cast(_5921.ConicalGearSetCompoundHarmonicAnalysis)

        @property
        def gear_set_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis",
        ) -> "_5947.GearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5947,
            )

            return self._parent._cast(_5947.GearSetCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis",
        ) -> "_5985.SpecialisedAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5985,
            )

            return self._parent._cast(_5985.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis",
        ) -> "_5887.AbstractAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5887,
            )

            return self._parent._cast(_5887.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis",
        ) -> "_5966.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(_5966.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(
        self: Self,
    ) -> "_2548.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(
        self: Self,
    ) -> "_2548.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5791.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis]

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
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_compound_harmonic_analysis(
        self: Self,
    ) -> "List[_5959.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsCompoundHarmonicAnalysis
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_compound_harmonic_analysis(
        self: Self,
    ) -> "List[_5960.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesCompoundHarmonicAnalysis
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5791.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis(
            self
        )
