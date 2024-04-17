"""ShaftHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5688
from mastapy.system_model.analyses_and_results import _2664
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ShaftHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2489
    from mastapy.system_model.analyses_and_results.static_loads import _6959
    from mastapy.system_model.analyses_and_results.modal_analyses import _4687
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5776,
        _5689,
        _5713,
        _5796,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2812
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHarmonicAnalysis",)


Self = TypeVar("Self", bound="ShaftHarmonicAnalysis")


class ShaftHarmonicAnalysis(
    _5688.AbstractShaftHarmonicAnalysis, _2664.IHaveShaftHarmonicResults
):
    """ShaftHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftHarmonicAnalysis")

    class _Cast_ShaftHarmonicAnalysis:
        """Special nested class for casting ShaftHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis",
            parent: "ShaftHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_harmonic_analysis(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis",
        ) -> "_5688.AbstractShaftHarmonicAnalysis":
            return self._parent._cast(_5688.AbstractShaftHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_harmonic_analysis(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis",
        ) -> "_5689.AbstractShaftOrHousingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5689,
            )

            return self._parent._cast(_5689.AbstractShaftOrHousingHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis",
        ) -> "_5713.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5713,
            )

            return self._parent._cast(_5713.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis",
        ) -> "_5796.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def shaft_harmonic_analysis(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis",
        ) -> "ShaftHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2489.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6959.ShaftLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def coupled_modal_analysis(self: Self) -> "_4687.ShaftModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ShaftModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def export(self: Self) -> "_5776.HarmonicAnalysisShaftExportOptions":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisShaftExportOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Export

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2812.ShaftSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ShaftSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ShaftHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ShaftHarmonicAnalysis]

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
    def cast_to(self: Self) -> "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis":
        return self._Cast_ShaftHarmonicAnalysis(self)
