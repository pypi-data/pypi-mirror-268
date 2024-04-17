"""TorqueConverterConnectionHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5725
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "TorqueConverterConnectionHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2359
    from mastapy.system_model.analyses_and_results.static_loads import _6981
    from mastapy.system_model.analyses_and_results.system_deflections import _2836
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5782, _5723
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionHarmonicAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterConnectionHarmonicAnalysis")


class TorqueConverterConnectionHarmonicAnalysis(
    _5725.CouplingConnectionHarmonicAnalysis
):
    """TorqueConverterConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterConnectionHarmonicAnalysis"
    )

    class _Cast_TorqueConverterConnectionHarmonicAnalysis:
        """Special nested class for casting TorqueConverterConnectionHarmonicAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionHarmonicAnalysis._Cast_TorqueConverterConnectionHarmonicAnalysis",
            parent: "TorqueConverterConnectionHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_harmonic_analysis(
            self: "TorqueConverterConnectionHarmonicAnalysis._Cast_TorqueConverterConnectionHarmonicAnalysis",
        ) -> "_5725.CouplingConnectionHarmonicAnalysis":
            return self._parent._cast(_5725.CouplingConnectionHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "TorqueConverterConnectionHarmonicAnalysis._Cast_TorqueConverterConnectionHarmonicAnalysis",
        ) -> "_5782.InterMountableComponentConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5782,
            )

            return self._parent._cast(
                _5782.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "TorqueConverterConnectionHarmonicAnalysis._Cast_TorqueConverterConnectionHarmonicAnalysis",
        ) -> "_5723.ConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5723,
            )

            return self._parent._cast(_5723.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "TorqueConverterConnectionHarmonicAnalysis._Cast_TorqueConverterConnectionHarmonicAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "TorqueConverterConnectionHarmonicAnalysis._Cast_TorqueConverterConnectionHarmonicAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "TorqueConverterConnectionHarmonicAnalysis._Cast_TorqueConverterConnectionHarmonicAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterConnectionHarmonicAnalysis._Cast_TorqueConverterConnectionHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionHarmonicAnalysis._Cast_TorqueConverterConnectionHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def torque_converter_connection_harmonic_analysis(
            self: "TorqueConverterConnectionHarmonicAnalysis._Cast_TorqueConverterConnectionHarmonicAnalysis",
        ) -> "TorqueConverterConnectionHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionHarmonicAnalysis._Cast_TorqueConverterConnectionHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "TorqueConverterConnectionHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2359.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6981.TorqueConverterConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase

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
    ) -> "_2836.TorqueConverterConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterConnectionSystemDeflection

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
    ) -> "TorqueConverterConnectionHarmonicAnalysis._Cast_TorqueConverterConnectionHarmonicAnalysis":
        return self._Cast_TorqueConverterConnectionHarmonicAnalysis(self)
