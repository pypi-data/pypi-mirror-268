"""FEPartCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5889
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "FEPartCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2460
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5758
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5912,
        _5966,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("FEPartCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="FEPartCompoundHarmonicAnalysis")


class FEPartCompoundHarmonicAnalysis(
    _5889.AbstractShaftOrHousingCompoundHarmonicAnalysis
):
    """FEPartCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _FE_PART_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartCompoundHarmonicAnalysis")

    class _Cast_FEPartCompoundHarmonicAnalysis:
        """Special nested class for casting FEPartCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "FEPartCompoundHarmonicAnalysis._Cast_FEPartCompoundHarmonicAnalysis",
            parent: "FEPartCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis(
            self: "FEPartCompoundHarmonicAnalysis._Cast_FEPartCompoundHarmonicAnalysis",
        ) -> "_5889.AbstractShaftOrHousingCompoundHarmonicAnalysis":
            return self._parent._cast(
                _5889.AbstractShaftOrHousingCompoundHarmonicAnalysis
            )

        @property
        def component_compound_harmonic_analysis(
            self: "FEPartCompoundHarmonicAnalysis._Cast_FEPartCompoundHarmonicAnalysis",
        ) -> "_5912.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5912,
            )

            return self._parent._cast(_5912.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "FEPartCompoundHarmonicAnalysis._Cast_FEPartCompoundHarmonicAnalysis",
        ) -> "_5966.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(_5966.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "FEPartCompoundHarmonicAnalysis._Cast_FEPartCompoundHarmonicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FEPartCompoundHarmonicAnalysis._Cast_FEPartCompoundHarmonicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartCompoundHarmonicAnalysis._Cast_FEPartCompoundHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def fe_part_compound_harmonic_analysis(
            self: "FEPartCompoundHarmonicAnalysis._Cast_FEPartCompoundHarmonicAnalysis",
        ) -> "FEPartCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "FEPartCompoundHarmonicAnalysis._Cast_FEPartCompoundHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEPartCompoundHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2460.FEPart":
        """mastapy.system_model.part_model.FEPart

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
    ) -> "List[_5758.FEPartHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.FEPartHarmonicAnalysis]

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
    def planetaries(self: Self) -> "List[FEPartCompoundHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.compound.FEPartCompoundHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(self: Self) -> "List[_5758.FEPartHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.FEPartHarmonicAnalysis]

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
    ) -> "FEPartCompoundHarmonicAnalysis._Cast_FEPartCompoundHarmonicAnalysis":
        return self._Cast_FEPartCompoundHarmonicAnalysis(self)
