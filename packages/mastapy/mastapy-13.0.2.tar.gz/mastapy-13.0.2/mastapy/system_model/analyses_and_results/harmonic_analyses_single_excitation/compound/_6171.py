"""CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6244,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2276
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6040,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6191,
        _6150,
        _6182,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation"
)


class CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation(
    _6244.ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
):
    """CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6244.ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6244.ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6150.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6150,
            )

            return self._parent._cast(
                _6150.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(
            self: "CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6182.ConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6182,
            )

            return self._parent._cast(
                _6182.ConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_analysis(
            self: "CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_harmonic_analysis_of_single_excitation(
            self: "CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6191.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6191,
            )

            return self._parent._cast(
                _6191.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coaxial_connection_compound_harmonic_analysis_of_single_excitation(
            self: "CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2276.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2276.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

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
    ) -> "List[_6040.CoaxialConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CoaxialConnectionHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6040.CoaxialConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CoaxialConnectionHarmonicAnalysisOfSingleExcitation]

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
    ) -> "CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
