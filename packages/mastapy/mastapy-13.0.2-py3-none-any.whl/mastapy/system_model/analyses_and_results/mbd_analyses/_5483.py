"""PowerLoadMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5523
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "PowerLoadMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2479
    from mastapy.system_model.analyses_and_results.static_loads import _6948
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5472,
        _5412,
        _5475,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7557, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="PowerLoadMultibodyDynamicsAnalysis")


class PowerLoadMultibodyDynamicsAnalysis(
    _5523.VirtualComponentMultibodyDynamicsAnalysis
):
    """PowerLoadMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerLoadMultibodyDynamicsAnalysis")

    class _Cast_PowerLoadMultibodyDynamicsAnalysis:
        """Special nested class for casting PowerLoadMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "PowerLoadMultibodyDynamicsAnalysis._Cast_PowerLoadMultibodyDynamicsAnalysis",
            parent: "PowerLoadMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_multibody_dynamics_analysis(
            self: "PowerLoadMultibodyDynamicsAnalysis._Cast_PowerLoadMultibodyDynamicsAnalysis",
        ) -> "_5523.VirtualComponentMultibodyDynamicsAnalysis":
            return self._parent._cast(_5523.VirtualComponentMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "PowerLoadMultibodyDynamicsAnalysis._Cast_PowerLoadMultibodyDynamicsAnalysis",
        ) -> "_5472.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5472

            return self._parent._cast(_5472.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "PowerLoadMultibodyDynamicsAnalysis._Cast_PowerLoadMultibodyDynamicsAnalysis",
        ) -> "_5412.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5412

            return self._parent._cast(_5412.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "PowerLoadMultibodyDynamicsAnalysis._Cast_PowerLoadMultibodyDynamicsAnalysis",
        ) -> "_5475.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(_5475.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "PowerLoadMultibodyDynamicsAnalysis._Cast_PowerLoadMultibodyDynamicsAnalysis",
        ) -> "_7557.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7557

            return self._parent._cast(_7557.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PowerLoadMultibodyDynamicsAnalysis._Cast_PowerLoadMultibodyDynamicsAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PowerLoadMultibodyDynamicsAnalysis._Cast_PowerLoadMultibodyDynamicsAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PowerLoadMultibodyDynamicsAnalysis._Cast_PowerLoadMultibodyDynamicsAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadMultibodyDynamicsAnalysis._Cast_PowerLoadMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def power_load_multibody_dynamics_analysis(
            self: "PowerLoadMultibodyDynamicsAnalysis._Cast_PowerLoadMultibodyDynamicsAnalysis",
        ) -> "PowerLoadMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "PowerLoadMultibodyDynamicsAnalysis._Cast_PowerLoadMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "PowerLoadMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_jerk_rate_of_change_of_acceleration(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularJerkRateOfChangeOfAcceleration

        if temp is None:
            return 0.0

        return temp

    @property
    def applied_torque(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AppliedTorque

        if temp is None:
            return 0.0

        return temp

    @applied_torque.setter
    @enforce_parameter_types
    def applied_torque(self: Self, value: "float"):
        self.wrapped.AppliedTorque = float(value) if value is not None else 0.0

    @property
    def controller_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ControllerTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def current_coefficient_of_friction_with_ground(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurrentCoefficientOfFrictionWithGround

        if temp is None:
            return 0.0

        return temp

    @property
    def drag_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DragTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def elastic_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def energy_input(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EnergyInput

        if temp is None:
            return 0.0

        return temp

    @property
    def engine_idle_speed_control_enabled(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EngineIdleSpeedControlEnabled

        if temp is None:
            return False

        return temp

    @property
    def engine_throttle_from_interface(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EngineThrottleFromInterface

        if temp is None:
            return 0.0

        return temp

    @property
    def engine_throttle_position_over_time(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EngineThrottlePositionOverTime

        if temp is None:
            return 0.0

        return temp

    @engine_throttle_position_over_time.setter
    @enforce_parameter_types
    def engine_throttle_position_over_time(self: Self, value: "float"):
        self.wrapped.EngineThrottlePositionOverTime = (
            float(value) if value is not None else 0.0
        )

    @property
    def error_in_engine_idle_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ErrorInEngineIdleSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def error_in_target_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ErrorInTargetSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def filtered_engine_throttle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FilteredEngineThrottle

        if temp is None:
            return 0.0

        return temp

    @property
    def fuel_consumption_instantaneous(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FuelConsumptionInstantaneous

        if temp is None:
            return 0.0

        return temp

    @property
    def interface_input_torque_used_in_solver(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InterfaceInputTorqueUsedInSolver

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
    def is_wheel_using_static_friction(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsWheelUsingStaticFriction

        if temp is None:
            return False

        return temp

    @property
    def lagged_angular_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LaggedAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def longitudinal_slip_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LongitudinalSlipRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def power(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Power

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_from_vehicle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueFromVehicle

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_on_each_wheel(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueOnEachWheel

        if temp is None:
            return 0.0

        return temp

    @property
    def total_fuel_consumed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalFuelConsumed

        if temp is None:
            return 0.0

        return temp

    @property
    def total_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def unfiltered_controller_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UnfilteredControllerTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2479.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6948.PowerLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PowerLoadMultibodyDynamicsAnalysis._Cast_PowerLoadMultibodyDynamicsAnalysis":
        return self._Cast_PowerLoadMultibodyDynamicsAnalysis(self)
