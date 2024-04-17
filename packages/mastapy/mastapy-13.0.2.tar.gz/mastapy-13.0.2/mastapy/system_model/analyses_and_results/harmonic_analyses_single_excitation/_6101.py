"""PlanetaryConnectionHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6115,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2294
    from mastapy.system_model.analyses_and_results.static_loads import _6941
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6019,
        _6051,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="PlanetaryConnectionHarmonicAnalysisOfSingleExcitation")


class PlanetaryConnectionHarmonicAnalysisOfSingleExcitation(
    _6115.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
):
    """PlanetaryConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting PlanetaryConnectionHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
            parent: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6115.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6115.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6019.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6019,
            )

            return self._parent._cast(
                _6019.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6051.ConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6051,
            )

            return self._parent._cast(
                _6051.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_connection_harmonic_analysis_of_single_excitation(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation.TYPE",
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
    def cast_to(
        self: Self,
    ) -> "PlanetaryConnectionHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation":
        return self._Cast_PlanetaryConnectionHarmonicAnalysisOfSingleExcitation(self)
