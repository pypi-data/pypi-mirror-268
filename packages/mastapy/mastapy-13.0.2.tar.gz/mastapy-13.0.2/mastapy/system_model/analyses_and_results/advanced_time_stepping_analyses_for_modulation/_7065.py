"""CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7017,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2345
    from mastapy.system_model.analyses_and_results.static_loads import _6869
    from mastapy.system_model.analyses_and_results.system_deflections import _2745
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7054,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = (
    "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
)


Self = TypeVar(
    "Self",
    bound="CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
)


class CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation(
    _7017.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
):
    """CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
            parent: "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7017.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7017.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7054.ConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7054,
            )

            return self._parent._cast(
                _7054.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_advanced_time_stepping_analysis_for_modulation(
            self: "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def connection_load_case(
        self: Self,
    ) -> "_6869.CycloidalDiscPlanetaryBearingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscPlanetaryBearingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2745.CycloidalDiscPlanetaryBearingConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscPlanetaryBearingConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation(
            self
        )
