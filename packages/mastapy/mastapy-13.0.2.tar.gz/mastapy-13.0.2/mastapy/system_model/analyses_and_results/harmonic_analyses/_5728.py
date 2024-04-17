"""CVTBeltConnectionHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5696
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "CVTBeltConnectionHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2280
    from mastapy.system_model.analyses_and_results.system_deflections import _2740
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5782, _5723
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionHarmonicAnalysis",)


Self = TypeVar("Self", bound="CVTBeltConnectionHarmonicAnalysis")


class CVTBeltConnectionHarmonicAnalysis(_5696.BeltConnectionHarmonicAnalysis):
    """CVTBeltConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTBeltConnectionHarmonicAnalysis")

    class _Cast_CVTBeltConnectionHarmonicAnalysis:
        """Special nested class for casting CVTBeltConnectionHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CVTBeltConnectionHarmonicAnalysis._Cast_CVTBeltConnectionHarmonicAnalysis",
            parent: "CVTBeltConnectionHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def belt_connection_harmonic_analysis(
            self: "CVTBeltConnectionHarmonicAnalysis._Cast_CVTBeltConnectionHarmonicAnalysis",
        ) -> "_5696.BeltConnectionHarmonicAnalysis":
            return self._parent._cast(_5696.BeltConnectionHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "CVTBeltConnectionHarmonicAnalysis._Cast_CVTBeltConnectionHarmonicAnalysis",
        ) -> "_5782.InterMountableComponentConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5782,
            )

            return self._parent._cast(
                _5782.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "CVTBeltConnectionHarmonicAnalysis._Cast_CVTBeltConnectionHarmonicAnalysis",
        ) -> "_5723.ConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5723,
            )

            return self._parent._cast(_5723.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CVTBeltConnectionHarmonicAnalysis._Cast_CVTBeltConnectionHarmonicAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CVTBeltConnectionHarmonicAnalysis._Cast_CVTBeltConnectionHarmonicAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CVTBeltConnectionHarmonicAnalysis._Cast_CVTBeltConnectionHarmonicAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTBeltConnectionHarmonicAnalysis._Cast_CVTBeltConnectionHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionHarmonicAnalysis._Cast_CVTBeltConnectionHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_harmonic_analysis(
            self: "CVTBeltConnectionHarmonicAnalysis._Cast_CVTBeltConnectionHarmonicAnalysis",
        ) -> "CVTBeltConnectionHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionHarmonicAnalysis._Cast_CVTBeltConnectionHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "CVTBeltConnectionHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2280.CVTBeltConnection":
        """mastapy.system_model.connections_and_sockets.CVTBeltConnection

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
    ) -> "_2740.CVTBeltConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CVTBeltConnectionSystemDeflection

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
    ) -> "CVTBeltConnectionHarmonicAnalysis._Cast_CVTBeltConnectionHarmonicAnalysis":
        return self._Cast_CVTBeltConnectionHarmonicAnalysis(self)
