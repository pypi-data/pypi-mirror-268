"""ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6172,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2459
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6068,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6226,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation"
)


class ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation(
    _6172.ComponentCompoundHarmonicAnalysisOfSingleExcitation
):
    """ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation._Cast_ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation._Cast_ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6172.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6172.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation._Cast_ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6226.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6226,
            )

            return self._parent._cast(
                _6226.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation._Cast_ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation._Cast_ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation._Cast_ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def external_cad_model_compound_harmonic_analysis_of_single_excitation(
            self: "ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation._Cast_ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation._Cast_ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2459.ExternalCADModel":
        """mastapy.system_model.part_model.ExternalCADModel

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
    ) -> "List[_6068.ExternalCADModelHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.ExternalCADModelHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6068.ExternalCADModelHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.ExternalCADModelHarmonicAnalysisOfSingleExcitation]

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
    ) -> "ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation._Cast_ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
