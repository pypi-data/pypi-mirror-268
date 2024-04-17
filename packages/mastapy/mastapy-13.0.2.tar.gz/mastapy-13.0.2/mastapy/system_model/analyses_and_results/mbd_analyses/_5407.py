"""ClutchConnectionMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5424
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "ClutchConnectionMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2349
    from mastapy.system_model.analyses_and_results.static_loads import _6841
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5457, _5422
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ClutchConnectionMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ClutchConnectionMultibodyDynamicsAnalysis")


class ClutchConnectionMultibodyDynamicsAnalysis(
    _5424.CouplingConnectionMultibodyDynamicsAnalysis
):
    """ClutchConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ClutchConnectionMultibodyDynamicsAnalysis"
    )

    class _Cast_ClutchConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting ClutchConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ClutchConnectionMultibodyDynamicsAnalysis._Cast_ClutchConnectionMultibodyDynamicsAnalysis",
            parent: "ClutchConnectionMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_multibody_dynamics_analysis(
            self: "ClutchConnectionMultibodyDynamicsAnalysis._Cast_ClutchConnectionMultibodyDynamicsAnalysis",
        ) -> "_5424.CouplingConnectionMultibodyDynamicsAnalysis":
            return self._parent._cast(_5424.CouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "ClutchConnectionMultibodyDynamicsAnalysis._Cast_ClutchConnectionMultibodyDynamicsAnalysis",
        ) -> "_5457.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5457

            return self._parent._cast(
                _5457.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "ClutchConnectionMultibodyDynamicsAnalysis._Cast_ClutchConnectionMultibodyDynamicsAnalysis",
        ) -> "_5422.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5422

            return self._parent._cast(_5422.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "ClutchConnectionMultibodyDynamicsAnalysis._Cast_ClutchConnectionMultibodyDynamicsAnalysis",
        ) -> "_7550.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ClutchConnectionMultibodyDynamicsAnalysis._Cast_ClutchConnectionMultibodyDynamicsAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ClutchConnectionMultibodyDynamicsAnalysis._Cast_ClutchConnectionMultibodyDynamicsAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchConnectionMultibodyDynamicsAnalysis._Cast_ClutchConnectionMultibodyDynamicsAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchConnectionMultibodyDynamicsAnalysis._Cast_ClutchConnectionMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_connection_multibody_dynamics_analysis(
            self: "ClutchConnectionMultibodyDynamicsAnalysis._Cast_ClutchConnectionMultibodyDynamicsAnalysis",
        ) -> "ClutchConnectionMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ClutchConnectionMultibodyDynamicsAnalysis._Cast_ClutchConnectionMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ClutchConnectionMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def applied_clutch_pressure_at_clutch_plate(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AppliedClutchPressureAtClutchPlate

        if temp is None:
            return 0.0

        return temp

    @applied_clutch_pressure_at_clutch_plate.setter
    @enforce_parameter_types
    def applied_clutch_pressure_at_clutch_plate(self: Self, value: "float"):
        self.wrapped.AppliedClutchPressureAtClutchPlate = (
            float(value) if value is not None else 0.0
        )

    @property
    def applied_clutch_pressure_at_piston(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AppliedClutchPressureAtPiston

        if temp is None:
            return 0.0

        return temp

    @applied_clutch_pressure_at_piston.setter
    @enforce_parameter_types
    def applied_clutch_pressure_at_piston(self: Self, value: "float"):
        self.wrapped.AppliedClutchPressureAtPiston = (
            float(value) if value is not None else 0.0
        )

    @property
    def clutch_connection_elastic_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ClutchConnectionElasticTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def clutch_connection_viscous_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ClutchConnectionViscousTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def clutch_plate_dynamic_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ClutchPlateDynamicTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def clutch_torque_capacity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ClutchTorqueCapacity

        if temp is None:
            return 0.0

        return temp

    @property
    def excess_clutch_torque_capacity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcessClutchTorqueCapacity

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
    def relative_shaft_displacement(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeShaftDisplacement

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_shaft_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeShaftSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self: Self) -> "_2349.ClutchConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ClutchConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6841.ClutchConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase

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
    ) -> "ClutchConnectionMultibodyDynamicsAnalysis._Cast_ClutchConnectionMultibodyDynamicsAnalysis":
        return self._Cast_ClutchConnectionMultibodyDynamicsAnalysis(self)
