"""CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6440
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
        "CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6329
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6513,
        _6419,
        _6451,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis",)


Self = TypeVar(
    "Self", bound="CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis"
)


class CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis(
    _6440.CoaxialConnectionCompoundDynamicAnalysis
):
    """CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis",
            parent: "CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_dynamic_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis",
        ) -> "_6440.CoaxialConnectionCompoundDynamicAnalysis":
            return self._parent._cast(_6440.CoaxialConnectionCompoundDynamicAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_dynamic_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis",
        ) -> "_6513.ShaftToMountableComponentConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6513,
            )

            return self._parent._cast(
                _6513.ShaftToMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_dynamic_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis",
        ) -> "_6419.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6419,
            )

            return self._parent._cast(
                _6419.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def connection_compound_dynamic_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis",
        ) -> "_6451.ConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6451,
            )

            return self._parent._cast(_6451.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_dynamic_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_6329.CycloidalDiscCentralBearingConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CycloidalDiscCentralBearingConnectionDynamicAnalysis]

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
    ) -> "List[_6329.CycloidalDiscCentralBearingConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CycloidalDiscCentralBearingConnectionDynamicAnalysis]

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
    ) -> "CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis":
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis(
            self
        )
