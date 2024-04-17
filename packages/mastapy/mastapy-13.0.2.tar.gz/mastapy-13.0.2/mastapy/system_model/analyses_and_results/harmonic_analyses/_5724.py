"""ConnectorHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5794
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ConnectorHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.system_deflections import _2736
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5695,
        _5795,
        _5815,
        _5713,
        _5796,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConnectorHarmonicAnalysis")


class ConnectorHarmonicAnalysis(_5794.MountableComponentHarmonicAnalysis):
    """ConnectorHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorHarmonicAnalysis")

    class _Cast_ConnectorHarmonicAnalysis:
        """Special nested class for casting ConnectorHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
            parent: "ConnectorHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_5794.MountableComponentHarmonicAnalysis":
            return self._parent._cast(_5794.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_5713.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5713,
            )

            return self._parent._cast(_5713.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_5796.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bearing_harmonic_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_5695.BearingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5695,
            )

            return self._parent._cast(_5695.BearingHarmonicAnalysis)

        @property
        def oil_seal_harmonic_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_5795.OilSealHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5795,
            )

            return self._parent._cast(_5795.OilSealHarmonicAnalysis)

        @property
        def shaft_hub_connection_harmonic_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "_5815.ShaftHubConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5815,
            )

            return self._parent._cast(_5815.ShaftHubConnectionHarmonicAnalysis)

        @property
        def connector_harmonic_analysis(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis",
        ) -> "ConnectorHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2454.Connector":
        """mastapy.system_model.part_model.Connector

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2736.ConnectorSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConnectorSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectorHarmonicAnalysis._Cast_ConnectorHarmonicAnalysis":
        return self._Cast_ConnectorHarmonicAnalysis(self)
