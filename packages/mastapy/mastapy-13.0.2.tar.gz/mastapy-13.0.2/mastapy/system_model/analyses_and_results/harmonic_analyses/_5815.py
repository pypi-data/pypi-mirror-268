"""ShaftHubConnectionHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5724
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ShaftHubConnectionHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2606
    from mastapy.system_model.analyses_and_results.static_loads import _6958
    from mastapy.system_model.analyses_and_results.system_deflections import _2809
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5794,
        _5713,
        _5796,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnectionHarmonicAnalysis",)


Self = TypeVar("Self", bound="ShaftHubConnectionHarmonicAnalysis")


class ShaftHubConnectionHarmonicAnalysis(_5724.ConnectorHarmonicAnalysis):
    """ShaftHubConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftHubConnectionHarmonicAnalysis")

    class _Cast_ShaftHubConnectionHarmonicAnalysis:
        """Special nested class for casting ShaftHubConnectionHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ShaftHubConnectionHarmonicAnalysis._Cast_ShaftHubConnectionHarmonicAnalysis",
            parent: "ShaftHubConnectionHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def connector_harmonic_analysis(
            self: "ShaftHubConnectionHarmonicAnalysis._Cast_ShaftHubConnectionHarmonicAnalysis",
        ) -> "_5724.ConnectorHarmonicAnalysis":
            return self._parent._cast(_5724.ConnectorHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "ShaftHubConnectionHarmonicAnalysis._Cast_ShaftHubConnectionHarmonicAnalysis",
        ) -> "_5794.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5794,
            )

            return self._parent._cast(_5794.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "ShaftHubConnectionHarmonicAnalysis._Cast_ShaftHubConnectionHarmonicAnalysis",
        ) -> "_5713.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5713,
            )

            return self._parent._cast(_5713.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "ShaftHubConnectionHarmonicAnalysis._Cast_ShaftHubConnectionHarmonicAnalysis",
        ) -> "_5796.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ShaftHubConnectionHarmonicAnalysis._Cast_ShaftHubConnectionHarmonicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftHubConnectionHarmonicAnalysis._Cast_ShaftHubConnectionHarmonicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftHubConnectionHarmonicAnalysis._Cast_ShaftHubConnectionHarmonicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftHubConnectionHarmonicAnalysis._Cast_ShaftHubConnectionHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftHubConnectionHarmonicAnalysis._Cast_ShaftHubConnectionHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def shaft_hub_connection_harmonic_analysis(
            self: "ShaftHubConnectionHarmonicAnalysis._Cast_ShaftHubConnectionHarmonicAnalysis",
        ) -> "ShaftHubConnectionHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftHubConnectionHarmonicAnalysis._Cast_ShaftHubConnectionHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "ShaftHubConnectionHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2606.ShaftHubConnection":
        """mastapy.system_model.part_model.couplings.ShaftHubConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6958.ShaftHubConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2809.ShaftHubConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ShaftHubConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ShaftHubConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ShaftHubConnectionHarmonicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "ShaftHubConnectionHarmonicAnalysis._Cast_ShaftHubConnectionHarmonicAnalysis":
        return self._Cast_ShaftHubConnectionHarmonicAnalysis(self)
