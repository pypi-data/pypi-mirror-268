"""CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5911
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
        "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5732
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5984,
        _5890,
        _5922,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",)


Self = TypeVar(
    "Self", bound="CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis"
)


class CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis(
    _5911.CoaxialConnectionCompoundHarmonicAnalysis
):
    """CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
            parent: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_harmonic_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> "_5911.CoaxialConnectionCompoundHarmonicAnalysis":
            return self._parent._cast(_5911.CoaxialConnectionCompoundHarmonicAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> "_5984.ShaftToMountableComponentConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5984,
            )

            return self._parent._cast(
                _5984.ShaftToMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> (
            "_5890.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5890,
            )

            return self._parent._cast(
                _5890.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> "_5922.ConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5922,
            )

            return self._parent._cast(_5922.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_harmonic_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5732.CycloidalDiscCentralBearingConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CycloidalDiscCentralBearingConnectionHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5732.CycloidalDiscCentralBearingConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CycloidalDiscCentralBearingConnectionHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis":
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis(
            self
        )
