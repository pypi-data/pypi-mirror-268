"""CycloidalDiscCentralBearingConnectionHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5711
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "CycloidalDiscCentralBearingConnectionHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2342
    from mastapy.system_model.analyses_and_results.system_deflections import _2744
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5816,
        _5690,
        _5723,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionHarmonicAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscCentralBearingConnectionHarmonicAnalysis")


class CycloidalDiscCentralBearingConnectionHarmonicAnalysis(
    _5711.CoaxialConnectionHarmonicAnalysis
):
    """CycloidalDiscCentralBearingConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysis"
    )

    class _Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysis:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysis",
            parent: "CycloidalDiscCentralBearingConnectionHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coaxial_connection_harmonic_analysis(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysis",
        ) -> "_5711.CoaxialConnectionHarmonicAnalysis":
            return self._parent._cast(_5711.CoaxialConnectionHarmonicAnalysis)

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysis",
        ) -> "_5816.ShaftToMountableComponentConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5816,
            )

            return self._parent._cast(
                _5816.ShaftToMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysis",
        ) -> "_5690.AbstractShaftToMountableComponentConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5690,
            )

            return self._parent._cast(
                _5690.AbstractShaftToMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysis",
        ) -> "_5723.ConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5723,
            )

            return self._parent._cast(_5723.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysis",
        ) -> "CycloidalDiscCentralBearingConnectionHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysis",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2342.CycloidalDiscCentralBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection

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
    ) -> "_2744.CycloidalDiscCentralBearingConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscCentralBearingConnectionSystemDeflection

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
    ) -> "CycloidalDiscCentralBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysis":
        return self._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysis(self)
