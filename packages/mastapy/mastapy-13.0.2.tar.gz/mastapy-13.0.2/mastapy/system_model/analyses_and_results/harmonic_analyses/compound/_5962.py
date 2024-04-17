"""MassDiscCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _6009
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "MassDiscCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2469
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5792
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5964,
        _5912,
        _5966,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("MassDiscCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="MassDiscCompoundHarmonicAnalysis")


class MassDiscCompoundHarmonicAnalysis(_6009.VirtualComponentCompoundHarmonicAnalysis):
    """MassDiscCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MassDiscCompoundHarmonicAnalysis")

    class _Cast_MassDiscCompoundHarmonicAnalysis:
        """Special nested class for casting MassDiscCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "MassDiscCompoundHarmonicAnalysis._Cast_MassDiscCompoundHarmonicAnalysis",
            parent: "MassDiscCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_harmonic_analysis(
            self: "MassDiscCompoundHarmonicAnalysis._Cast_MassDiscCompoundHarmonicAnalysis",
        ) -> "_6009.VirtualComponentCompoundHarmonicAnalysis":
            return self._parent._cast(_6009.VirtualComponentCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "MassDiscCompoundHarmonicAnalysis._Cast_MassDiscCompoundHarmonicAnalysis",
        ) -> "_5964.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5964,
            )

            return self._parent._cast(_5964.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "MassDiscCompoundHarmonicAnalysis._Cast_MassDiscCompoundHarmonicAnalysis",
        ) -> "_5912.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5912,
            )

            return self._parent._cast(_5912.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "MassDiscCompoundHarmonicAnalysis._Cast_MassDiscCompoundHarmonicAnalysis",
        ) -> "_5966.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(_5966.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "MassDiscCompoundHarmonicAnalysis._Cast_MassDiscCompoundHarmonicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MassDiscCompoundHarmonicAnalysis._Cast_MassDiscCompoundHarmonicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MassDiscCompoundHarmonicAnalysis._Cast_MassDiscCompoundHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def mass_disc_compound_harmonic_analysis(
            self: "MassDiscCompoundHarmonicAnalysis._Cast_MassDiscCompoundHarmonicAnalysis",
        ) -> "MassDiscCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "MassDiscCompoundHarmonicAnalysis._Cast_MassDiscCompoundHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MassDiscCompoundHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2469.MassDisc":
        """mastapy.system_model.part_model.MassDisc

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
    ) -> "List[_5792.MassDiscHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.MassDiscHarmonicAnalysis]

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
    def planetaries(self: Self) -> "List[MassDiscCompoundHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.compound.MassDiscCompoundHarmonicAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_5792.MassDiscHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.MassDiscHarmonicAnalysis]

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
    ) -> "MassDiscCompoundHarmonicAnalysis._Cast_MassDiscCompoundHarmonicAnalysis":
        return self._Cast_MassDiscCompoundHarmonicAnalysis(self)
