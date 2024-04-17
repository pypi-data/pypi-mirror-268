"""TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7057,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2359
    from mastapy.system_model.analyses_and_results.static_loads import _6981
    from mastapy.system_model.analyses_and_results.system_deflections import _2836
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7085,
        _7054,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation"
)


class TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation(
    _7057.CouplingConnectionAdvancedTimeSteppingAnalysisForModulation
):
    """TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation",
            parent: "TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7057.CouplingConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7057.CouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7085.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7085,
            )

            return self._parent._cast(
                _7085.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7054.ConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7054,
            )

            return self._parent._cast(
                _7054.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def torque_converter_connection_advanced_time_stepping_analysis_for_modulation(
            self: "TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2359.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6981.TorqueConverterConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase

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
    ) -> "_2836.TorqueConverterConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterConnectionSystemDeflection

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
    ) -> "TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation(
            self
        )
