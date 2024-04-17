"""PulleyCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5926
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "PulleyCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2598
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5806
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5929,
        _5964,
        _5912,
        _5966,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PulleyCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="PulleyCompoundHarmonicAnalysis")


class PulleyCompoundHarmonicAnalysis(_5926.CouplingHalfCompoundHarmonicAnalysis):
    """PulleyCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _PULLEY_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PulleyCompoundHarmonicAnalysis")

    class _Cast_PulleyCompoundHarmonicAnalysis:
        """Special nested class for casting PulleyCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "PulleyCompoundHarmonicAnalysis._Cast_PulleyCompoundHarmonicAnalysis",
            parent: "PulleyCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_harmonic_analysis(
            self: "PulleyCompoundHarmonicAnalysis._Cast_PulleyCompoundHarmonicAnalysis",
        ) -> "_5926.CouplingHalfCompoundHarmonicAnalysis":
            return self._parent._cast(_5926.CouplingHalfCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "PulleyCompoundHarmonicAnalysis._Cast_PulleyCompoundHarmonicAnalysis",
        ) -> "_5964.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5964,
            )

            return self._parent._cast(_5964.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "PulleyCompoundHarmonicAnalysis._Cast_PulleyCompoundHarmonicAnalysis",
        ) -> "_5912.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5912,
            )

            return self._parent._cast(_5912.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "PulleyCompoundHarmonicAnalysis._Cast_PulleyCompoundHarmonicAnalysis",
        ) -> "_5966.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(_5966.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "PulleyCompoundHarmonicAnalysis._Cast_PulleyCompoundHarmonicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PulleyCompoundHarmonicAnalysis._Cast_PulleyCompoundHarmonicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PulleyCompoundHarmonicAnalysis._Cast_PulleyCompoundHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_harmonic_analysis(
            self: "PulleyCompoundHarmonicAnalysis._Cast_PulleyCompoundHarmonicAnalysis",
        ) -> "_5929.CVTPulleyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5929,
            )

            return self._parent._cast(_5929.CVTPulleyCompoundHarmonicAnalysis)

        @property
        def pulley_compound_harmonic_analysis(
            self: "PulleyCompoundHarmonicAnalysis._Cast_PulleyCompoundHarmonicAnalysis",
        ) -> "PulleyCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "PulleyCompoundHarmonicAnalysis._Cast_PulleyCompoundHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PulleyCompoundHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2598.Pulley":
        """mastapy.system_model.part_model.couplings.Pulley

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
    ) -> "List[_5806.PulleyHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.PulleyHarmonicAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_5806.PulleyHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.PulleyHarmonicAnalysis]

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
    ) -> "PulleyCompoundHarmonicAnalysis._Cast_PulleyCompoundHarmonicAnalysis":
        return self._Cast_PulleyCompoundHarmonicAnalysis(self)
