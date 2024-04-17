"""TorqueConverterConnectionMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5424
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "TorqueConverterConnectionMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5520,
        _5457,
        _5422,
    )
    from mastapy.system_model.connections_and_sockets.couplings import _2359
    from mastapy.system_model.analyses_and_results.static_loads import _6981
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterConnectionMultibodyDynamicsAnalysis")


class TorqueConverterConnectionMultibodyDynamicsAnalysis(
    _5424.CouplingConnectionMultibodyDynamicsAnalysis
):
    """TorqueConverterConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis"
    )

    class _Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting TorqueConverterConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis",
            parent: "TorqueConverterConnectionMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_multibody_dynamics_analysis(
            self: "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis",
        ) -> "_5424.CouplingConnectionMultibodyDynamicsAnalysis":
            return self._parent._cast(_5424.CouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis",
        ) -> "_5457.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5457

            return self._parent._cast(
                _5457.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis",
        ) -> "_5422.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5422

            return self._parent._cast(_5422.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis",
        ) -> "_7550.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def torque_converter_connection_multibody_dynamics_analysis(
            self: "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis",
        ) -> "TorqueConverterConnectionMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "TorqueConverterConnectionMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def capacity_factor_k(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CapacityFactorK

        if temp is None:
            return 0.0

        return temp

    @property
    def inverse_capacity_factor_1k(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InverseCapacityFactor1K

        if temp is None:
            return 0.0

        return temp

    @property
    def is_locked(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsLocked

        if temp is None:
            return False

        return temp

    @property
    def lock_up_clutch_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LockUpClutchTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def lock_up_viscous_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LockUpViscousTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def locked_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LockedTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def locking_status(self: Self) -> "_5520.TorqueConverterStatus":
        """mastapy.system_model.analyses_and_results.mbd_analyses.TorqueConverterStatus

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LockingStatus

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.TorqueConverterStatus",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.mbd_analyses._5520",
            "TorqueConverterStatus",
        )(value)

    @property
    def percentage_applied_pressure(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PercentageAppliedPressure

        if temp is None:
            return 0.0

        return temp

    @percentage_applied_pressure.setter
    @enforce_parameter_types
    def percentage_applied_pressure(self: Self, value: "float"):
        self.wrapped.PercentageAppliedPressure = (
            float(value) if value is not None else 0.0
        )

    @property
    def power_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def pump_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PumpTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def speed_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpeedRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def turbine_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TurbineTorque

        if temp is None:
            return 0.0

        return temp

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
    def cast_to(
        self: Self,
    ) -> "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis":
        return self._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis(self)
