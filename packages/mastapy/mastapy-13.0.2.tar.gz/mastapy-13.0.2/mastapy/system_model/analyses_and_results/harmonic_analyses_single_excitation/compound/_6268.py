"""UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6269,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2484
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6139,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6224,
        _6172,
        _6226,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation")


class UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation(
    _6269.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation
):
    """UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_harmonic_analysis_of_single_excitation(
            self: "UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6269.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6269.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6224.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6224,
            )

            return self._parent._cast(
                _6224.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6172.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6172,
            )

            return self._parent._cast(
                _6172.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6226.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6226,
            )

            return self._parent._cast(
                _6226.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def unbalanced_mass_compound_harmonic_analysis_of_single_excitation(
            self: "UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2484.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6139.UnbalancedMassHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.UnbalancedMassHarmonicAnalysisOfSingleExcitation]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6139.UnbalancedMassHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.UnbalancedMassHarmonicAnalysisOfSingleExcitation]

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
    def cast_to(
        self: Self,
    ) -> "UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation._Cast_UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation(self)
