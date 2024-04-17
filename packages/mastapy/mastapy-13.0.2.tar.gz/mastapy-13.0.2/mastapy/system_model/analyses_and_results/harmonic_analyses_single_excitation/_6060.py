"""CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6040,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
        "CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2342
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6115,
        _6019,
        _6051,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self",
    bound="CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation",
)


class CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation(
    _6040.CoaxialConnectionHarmonicAnalysisOfSingleExcitation
):
    """CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation",
            parent: "CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def coaxial_connection_harmonic_analysis_of_single_excitation(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6040.CoaxialConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6040.CoaxialConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6115.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6115,
            )

            return self._parent._cast(
                _6115.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6019.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6019,
            )

            return self._parent._cast(
                _6019.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6051.ConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6051,
            )

            return self._parent._cast(
                _6051.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis_of_single_excitation(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation.TYPE",
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
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation(
            self
        )
