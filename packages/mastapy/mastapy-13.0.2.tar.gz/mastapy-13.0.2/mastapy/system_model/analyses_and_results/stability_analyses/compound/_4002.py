"""ShaftToMountableComponentConnectionCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3908
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STABILITY_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
        "ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3870
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3929,
        _3949,
        _3988,
        _3940,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCompoundStabilityAnalysis",)


Self = TypeVar(
    "Self", bound="ShaftToMountableComponentConnectionCompoundStabilityAnalysis"
)


class ShaftToMountableComponentConnectionCompoundStabilityAnalysis(
    _3908.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis
):
    """ShaftToMountableComponentConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
    )

    class _Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
            parent: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> (
            "_3908.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis"
        ):
            return self._parent._cast(
                _3908.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3940.ConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3940,
            )

            return self._parent._cast(_3940.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_stability_analysis(
            self: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3929.CoaxialConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3929,
            )

            return self._parent._cast(_3929.CoaxialConnectionCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_stability_analysis(
            self: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3949.CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3949,
            )

            return self._parent._cast(
                _3949.CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis
            )

        @property
        def planetary_connection_compound_stability_analysis(
            self: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "_3988.PlanetaryConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3988,
            )

            return self._parent._cast(
                _3988.PlanetaryConnectionCompoundStabilityAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "ShaftToMountableComponentConnectionCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3870.ShaftToMountableComponentConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ShaftToMountableComponentConnectionStabilityAnalysis]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3870.ShaftToMountableComponentConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ShaftToMountableComponentConnectionStabilityAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis":
        return self._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis(
            self
        )
