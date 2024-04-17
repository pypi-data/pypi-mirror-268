"""CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6150,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2345
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6062,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6182,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = (
    "CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)


Self = TypeVar(
    "Self",
    bound="CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)


class CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation(
    _6150.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
):
    """CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6150.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6150.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6182.ConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6182,
            )

            return self._parent._cast(
                _6182.ConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_harmonic_analysis_of_single_excitation(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2345.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(
        self: Self,
    ) -> "_2345.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_6062.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6062.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysisOfSingleExcitation]

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
    ) -> "CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
