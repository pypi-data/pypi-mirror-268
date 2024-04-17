"""PlanetaryConnectionCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5984
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "PlanetaryConnectionCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2294
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5801
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5890,
        _5922,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="PlanetaryConnectionCompoundHarmonicAnalysis")


class PlanetaryConnectionCompoundHarmonicAnalysis(
    _5984.ShaftToMountableComponentConnectionCompoundHarmonicAnalysis
):
    """PlanetaryConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryConnectionCompoundHarmonicAnalysis"
    )

    class _Cast_PlanetaryConnectionCompoundHarmonicAnalysis:
        """Special nested class for casting PlanetaryConnectionCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryConnectionCompoundHarmonicAnalysis._Cast_PlanetaryConnectionCompoundHarmonicAnalysis",
            parent: "PlanetaryConnectionCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis(
            self: "PlanetaryConnectionCompoundHarmonicAnalysis._Cast_PlanetaryConnectionCompoundHarmonicAnalysis",
        ) -> "_5984.ShaftToMountableComponentConnectionCompoundHarmonicAnalysis":
            return self._parent._cast(
                _5984.ShaftToMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis(
            self: "PlanetaryConnectionCompoundHarmonicAnalysis._Cast_PlanetaryConnectionCompoundHarmonicAnalysis",
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
            self: "PlanetaryConnectionCompoundHarmonicAnalysis._Cast_PlanetaryConnectionCompoundHarmonicAnalysis",
        ) -> "_5922.ConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5922,
            )

            return self._parent._cast(_5922.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "PlanetaryConnectionCompoundHarmonicAnalysis._Cast_PlanetaryConnectionCompoundHarmonicAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryConnectionCompoundHarmonicAnalysis._Cast_PlanetaryConnectionCompoundHarmonicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionCompoundHarmonicAnalysis._Cast_PlanetaryConnectionCompoundHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_connection_compound_harmonic_analysis(
            self: "PlanetaryConnectionCompoundHarmonicAnalysis._Cast_PlanetaryConnectionCompoundHarmonicAnalysis",
        ) -> "PlanetaryConnectionCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionCompoundHarmonicAnalysis._Cast_PlanetaryConnectionCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "PlanetaryConnectionCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2294.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5801.PlanetaryConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.PlanetaryConnectionHarmonicAnalysis]

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
    ) -> "List[_5801.PlanetaryConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.PlanetaryConnectionHarmonicAnalysis]

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
    ) -> "PlanetaryConnectionCompoundHarmonicAnalysis._Cast_PlanetaryConnectionCompoundHarmonicAnalysis":
        return self._Cast_PlanetaryConnectionCompoundHarmonicAnalysis(self)
