"""GuideDxfModelCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5912
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "GuideDxfModelCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5768
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5966,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="GuideDxfModelCompoundHarmonicAnalysis")


class GuideDxfModelCompoundHarmonicAnalysis(_5912.ComponentCompoundHarmonicAnalysis):
    """GuideDxfModelCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GuideDxfModelCompoundHarmonicAnalysis"
    )

    class _Cast_GuideDxfModelCompoundHarmonicAnalysis:
        """Special nested class for casting GuideDxfModelCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "GuideDxfModelCompoundHarmonicAnalysis._Cast_GuideDxfModelCompoundHarmonicAnalysis",
            parent: "GuideDxfModelCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_harmonic_analysis(
            self: "GuideDxfModelCompoundHarmonicAnalysis._Cast_GuideDxfModelCompoundHarmonicAnalysis",
        ) -> "_5912.ComponentCompoundHarmonicAnalysis":
            return self._parent._cast(_5912.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "GuideDxfModelCompoundHarmonicAnalysis._Cast_GuideDxfModelCompoundHarmonicAnalysis",
        ) -> "_5966.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(_5966.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "GuideDxfModelCompoundHarmonicAnalysis._Cast_GuideDxfModelCompoundHarmonicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GuideDxfModelCompoundHarmonicAnalysis._Cast_GuideDxfModelCompoundHarmonicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelCompoundHarmonicAnalysis._Cast_GuideDxfModelCompoundHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def guide_dxf_model_compound_harmonic_analysis(
            self: "GuideDxfModelCompoundHarmonicAnalysis._Cast_GuideDxfModelCompoundHarmonicAnalysis",
        ) -> "GuideDxfModelCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelCompoundHarmonicAnalysis._Cast_GuideDxfModelCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "GuideDxfModelCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2462.GuideDxfModel":
        """mastapy.system_model.part_model.GuideDxfModel

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
    ) -> "List[_5768.GuideDxfModelHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.GuideDxfModelHarmonicAnalysis]

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
    ) -> "List[_5768.GuideDxfModelHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.GuideDxfModelHarmonicAnalysis]

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
    ) -> "GuideDxfModelCompoundHarmonicAnalysis._Cast_GuideDxfModelCompoundHarmonicAnalysis":
        return self._Cast_GuideDxfModelCompoundHarmonicAnalysis(self)
