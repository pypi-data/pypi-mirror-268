"""PlanetaryConnectionCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4002
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "PlanetaryConnectionCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2294
    from mastapy.system_model.analyses_and_results.stability_analyses import _3856
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3908,
        _3940,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="PlanetaryConnectionCompoundStabilityAnalysis")


class PlanetaryConnectionCompoundStabilityAnalysis(
    _4002.ShaftToMountableComponentConnectionCompoundStabilityAnalysis
):
    """PlanetaryConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryConnectionCompoundStabilityAnalysis"
    )

    class _Cast_PlanetaryConnectionCompoundStabilityAnalysis:
        """Special nested class for casting PlanetaryConnectionCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryConnectionCompoundStabilityAnalysis._Cast_PlanetaryConnectionCompoundStabilityAnalysis",
            parent: "PlanetaryConnectionCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "PlanetaryConnectionCompoundStabilityAnalysis._Cast_PlanetaryConnectionCompoundStabilityAnalysis",
        ) -> "_4002.ShaftToMountableComponentConnectionCompoundStabilityAnalysis":
            return self._parent._cast(
                _4002.ShaftToMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "PlanetaryConnectionCompoundStabilityAnalysis._Cast_PlanetaryConnectionCompoundStabilityAnalysis",
        ) -> (
            "_3908.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3908,
            )

            return self._parent._cast(
                _3908.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "PlanetaryConnectionCompoundStabilityAnalysis._Cast_PlanetaryConnectionCompoundStabilityAnalysis",
        ) -> "_3940.ConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3940,
            )

            return self._parent._cast(_3940.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "PlanetaryConnectionCompoundStabilityAnalysis._Cast_PlanetaryConnectionCompoundStabilityAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryConnectionCompoundStabilityAnalysis._Cast_PlanetaryConnectionCompoundStabilityAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionCompoundStabilityAnalysis._Cast_PlanetaryConnectionCompoundStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_connection_compound_stability_analysis(
            self: "PlanetaryConnectionCompoundStabilityAnalysis._Cast_PlanetaryConnectionCompoundStabilityAnalysis",
        ) -> "PlanetaryConnectionCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionCompoundStabilityAnalysis._Cast_PlanetaryConnectionCompoundStabilityAnalysis",
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
        instance_to_wrap: "PlanetaryConnectionCompoundStabilityAnalysis.TYPE",
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
    ) -> "List[_3856.PlanetaryConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.PlanetaryConnectionStabilityAnalysis]

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
    ) -> "List[_3856.PlanetaryConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.PlanetaryConnectionStabilityAnalysis]

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
    ) -> "PlanetaryConnectionCompoundStabilityAnalysis._Cast_PlanetaryConnectionCompoundStabilityAnalysis":
        return self._Cast_PlanetaryConnectionCompoundStabilityAnalysis(self)
