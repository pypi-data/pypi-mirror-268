"""PlanetaryConnectionDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "PlanetaryConnectionDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2294
    from mastapy.system_model.analyses_and_results.static_loads import _6941
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6288, _6320
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7548,
        _7549,
        _7546,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionDynamicAnalysis",)


Self = TypeVar("Self", bound="PlanetaryConnectionDynamicAnalysis")


class PlanetaryConnectionDynamicAnalysis(
    _6384.ShaftToMountableComponentConnectionDynamicAnalysis
):
    """PlanetaryConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryConnectionDynamicAnalysis")

    class _Cast_PlanetaryConnectionDynamicAnalysis:
        """Special nested class for casting PlanetaryConnectionDynamicAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryConnectionDynamicAnalysis._Cast_PlanetaryConnectionDynamicAnalysis",
            parent: "PlanetaryConnectionDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_dynamic_analysis(
            self: "PlanetaryConnectionDynamicAnalysis._Cast_PlanetaryConnectionDynamicAnalysis",
        ) -> "_6384.ShaftToMountableComponentConnectionDynamicAnalysis":
            return self._parent._cast(
                _6384.ShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_dynamic_analysis(
            self: "PlanetaryConnectionDynamicAnalysis._Cast_PlanetaryConnectionDynamicAnalysis",
        ) -> "_6288.AbstractShaftToMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6288

            return self._parent._cast(
                _6288.AbstractShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "PlanetaryConnectionDynamicAnalysis._Cast_PlanetaryConnectionDynamicAnalysis",
        ) -> "_6320.ConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6320

            return self._parent._cast(_6320.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "PlanetaryConnectionDynamicAnalysis._Cast_PlanetaryConnectionDynamicAnalysis",
        ) -> "_7548.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "PlanetaryConnectionDynamicAnalysis._Cast_PlanetaryConnectionDynamicAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PlanetaryConnectionDynamicAnalysis._Cast_PlanetaryConnectionDynamicAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PlanetaryConnectionDynamicAnalysis._Cast_PlanetaryConnectionDynamicAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryConnectionDynamicAnalysis._Cast_PlanetaryConnectionDynamicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionDynamicAnalysis._Cast_PlanetaryConnectionDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_connection_dynamic_analysis(
            self: "PlanetaryConnectionDynamicAnalysis._Cast_PlanetaryConnectionDynamicAnalysis",
        ) -> "PlanetaryConnectionDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionDynamicAnalysis._Cast_PlanetaryConnectionDynamicAnalysis",
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
        self: Self, instance_to_wrap: "PlanetaryConnectionDynamicAnalysis.TYPE"
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
    ) -> "PlanetaryConnectionDynamicAnalysis._Cast_PlanetaryConnectionDynamicAnalysis":
        return self._Cast_PlanetaryConnectionDynamicAnalysis(self)
