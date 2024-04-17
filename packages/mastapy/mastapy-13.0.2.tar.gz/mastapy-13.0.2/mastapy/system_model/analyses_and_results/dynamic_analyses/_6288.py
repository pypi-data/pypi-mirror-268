"""AbstractShaftToMountableComponentConnectionDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6320
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "AbstractShaftToMountableComponentConnectionDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2272
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6309,
        _6329,
        _6331,
        _6370,
        _6384,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7548,
        _7549,
        _7546,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionDynamicAnalysis",)


Self = TypeVar(
    "Self", bound="AbstractShaftToMountableComponentConnectionDynamicAnalysis"
)


class AbstractShaftToMountableComponentConnectionDynamicAnalysis(
    _6320.ConnectionDynamicAnalysis
):
    """AbstractShaftToMountableComponentConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionDynamicAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
            parent: "AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def connection_dynamic_analysis(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "_6320.ConnectionDynamicAnalysis":
            return self._parent._cast(_6320.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "_7548.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def coaxial_connection_dynamic_analysis(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "_6309.CoaxialConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309

            return self._parent._cast(_6309.CoaxialConnectionDynamicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_dynamic_analysis(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "_6329.CycloidalDiscCentralBearingConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6329

            return self._parent._cast(
                _6329.CycloidalDiscCentralBearingConnectionDynamicAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_dynamic_analysis(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "_6331.CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6331

            return self._parent._cast(
                _6331.CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis
            )

        @property
        def planetary_connection_dynamic_analysis(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "_6370.PlanetaryConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6370

            return self._parent._cast(_6370.PlanetaryConnectionDynamicAnalysis)

        @property
        def shaft_to_mountable_component_connection_dynamic_analysis(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "_6384.ShaftToMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(
                _6384.ShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_dynamic_analysis(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "AbstractShaftToMountableComponentConnectionDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2272.AbstractShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection

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
    ) -> "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis":
        return self._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis(
            self
        )
