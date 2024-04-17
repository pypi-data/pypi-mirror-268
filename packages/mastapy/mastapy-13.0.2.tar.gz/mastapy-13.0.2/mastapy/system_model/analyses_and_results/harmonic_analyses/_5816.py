"""ShaftToMountableComponentConnectionHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5690
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ShaftToMountableComponentConnectionHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2302
    from mastapy.system_model.analyses_and_results.system_deflections import _2813
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5711,
        _5732,
        _5801,
        _5723,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionHarmonicAnalysis",)


Self = TypeVar("Self", bound="ShaftToMountableComponentConnectionHarmonicAnalysis")


class ShaftToMountableComponentConnectionHarmonicAnalysis(
    _5690.AbstractShaftToMountableComponentConnectionHarmonicAnalysis
):
    """ShaftToMountableComponentConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftToMountableComponentConnectionHarmonicAnalysis"
    )

    class _Cast_ShaftToMountableComponentConnectionHarmonicAnalysis:
        """Special nested class for casting ShaftToMountableComponentConnectionHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
            parent: "ShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "_5690.AbstractShaftToMountableComponentConnectionHarmonicAnalysis":
            return self._parent._cast(
                _5690.AbstractShaftToMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "_5723.ConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5723,
            )

            return self._parent._cast(_5723.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def coaxial_connection_harmonic_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "_5711.CoaxialConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5711,
            )

            return self._parent._cast(_5711.CoaxialConnectionHarmonicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "_5732.CycloidalDiscCentralBearingConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5732,
            )

            return self._parent._cast(
                _5732.CycloidalDiscCentralBearingConnectionHarmonicAnalysis
            )

        @property
        def planetary_connection_harmonic_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "_5801.PlanetaryConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5801,
            )

            return self._parent._cast(_5801.PlanetaryConnectionHarmonicAnalysis)

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "ShaftToMountableComponentConnectionHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2302.ShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2813.ShaftToMountableComponentConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ShaftToMountableComponentConnectionSystemDeflection

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
    ) -> "ShaftToMountableComponentConnectionHarmonicAnalysis._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis":
        return self._Cast_ShaftToMountableComponentConnectionHarmonicAnalysis(self)
