"""PlanetaryConnectionHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5816
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "PlanetaryConnectionHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2294
    from mastapy.system_model.analyses_and_results.static_loads import _6941
    from mastapy.system_model.analyses_and_results.system_deflections import _2797
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5690, _5723
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionHarmonicAnalysis",)


Self = TypeVar("Self", bound="PlanetaryConnectionHarmonicAnalysis")


class PlanetaryConnectionHarmonicAnalysis(
    _5816.ShaftToMountableComponentConnectionHarmonicAnalysis
):
    """PlanetaryConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryConnectionHarmonicAnalysis")

    class _Cast_PlanetaryConnectionHarmonicAnalysis:
        """Special nested class for casting PlanetaryConnectionHarmonicAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis",
            parent: "PlanetaryConnectionHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis(
            self: "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis",
        ) -> "_5816.ShaftToMountableComponentConnectionHarmonicAnalysis":
            return self._parent._cast(
                _5816.ShaftToMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis(
            self: "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis",
        ) -> "_5690.AbstractShaftToMountableComponentConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5690,
            )

            return self._parent._cast(
                _5690.AbstractShaftToMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis",
        ) -> "_5723.ConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5723,
            )

            return self._parent._cast(_5723.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_connection_harmonic_analysis(
            self: "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis",
        ) -> "PlanetaryConnectionHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "PlanetaryConnectionHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2294.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6941.PlanetaryConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2797.PlanetaryConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PlanetaryConnectionSystemDeflection

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
    ) -> (
        "PlanetaryConnectionHarmonicAnalysis._Cast_PlanetaryConnectionHarmonicAnalysis"
    ):
        return self._Cast_PlanetaryConnectionHarmonicAnalysis(self)
