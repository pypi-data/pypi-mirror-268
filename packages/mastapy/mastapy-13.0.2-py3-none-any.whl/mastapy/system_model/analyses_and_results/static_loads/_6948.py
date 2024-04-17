"""PowerLoadLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.implicit import (
    overridable,
    list_with_selected_item,
    enum_with_selected_value,
)
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.fe import _2380
from mastapy.system_model.analyses_and_results.static_loads import _6986, _6990
from mastapy.system_model import _2224
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PowerLoadLoadCase"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1542
    from mastapy.system_model import _2223, _2225
    from mastapy.math_utility.measured_data import _1572
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5524
    from mastapy.nodal_analysis.varying_input_components import _100
    from mastapy.system_model.part_model import _2479
    from mastapy.math_utility.control import _1583
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6880,
        _6933,
        _6846,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadLoadCase",)


Self = TypeVar("Self", bound="PowerLoadLoadCase")


class PowerLoadLoadCase(_6990.VirtualComponentLoadCase):
    """PowerLoadLoadCase

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerLoadLoadCase")

    class _Cast_PowerLoadLoadCase:
        """Special nested class for casting PowerLoadLoadCase to subclasses."""

        def __init__(
            self: "PowerLoadLoadCase._Cast_PowerLoadLoadCase",
            parent: "PowerLoadLoadCase",
        ):
            self._parent = parent

        @property
        def virtual_component_load_case(
            self: "PowerLoadLoadCase._Cast_PowerLoadLoadCase",
        ) -> "_6990.VirtualComponentLoadCase":
            return self._parent._cast(_6990.VirtualComponentLoadCase)

        @property
        def mountable_component_load_case(
            self: "PowerLoadLoadCase._Cast_PowerLoadLoadCase",
        ) -> "_6933.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "PowerLoadLoadCase._Cast_PowerLoadLoadCase",
        ) -> "_6846.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ComponentLoadCase)

        @property
        def part_load_case(
            self: "PowerLoadLoadCase._Cast_PowerLoadLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "PowerLoadLoadCase._Cast_PowerLoadLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PowerLoadLoadCase._Cast_PowerLoadLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadLoadCase._Cast_PowerLoadLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def power_load_load_case(
            self: "PowerLoadLoadCase._Cast_PowerLoadLoadCase",
        ) -> "PowerLoadLoadCase":
            return self._parent

        def __getattr__(self: "PowerLoadLoadCase._Cast_PowerLoadLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PowerLoadLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def constant_resistance_coefficient(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ConstantResistanceCoefficient

        if temp is None:
            return 0.0

        return temp

    @constant_resistance_coefficient.setter
    @enforce_parameter_types
    def constant_resistance_coefficient(self: Self, value: "float"):
        self.wrapped.ConstantResistanceCoefficient = (
            float(value) if value is not None else 0.0
        )

    @property
    def constant_resistance_coefficient_time_profile(
        self: Self,
    ) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.ConstantResistanceCoefficientTimeProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @constant_resistance_coefficient_time_profile.setter
    @enforce_parameter_types
    def constant_resistance_coefficient_time_profile(
        self: Self, value: "_1542.Vector2DListAccessor"
    ):
        self.wrapped.ConstantResistanceCoefficientTimeProfile = value.wrapped

    @property
    def constant_torque(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ConstantTorque

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @constant_torque.setter
    @enforce_parameter_types
    def constant_torque(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ConstantTorque = value

    @property
    def drag_torque_specification_method(
        self: Self,
    ) -> "_2223.PowerLoadDragTorqueSpecificationMethod":
        """mastapy.system_model.PowerLoadDragTorqueSpecificationMethod"""
        temp = self.wrapped.DragTorqueSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.PowerLoadDragTorqueSpecificationMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model._2223", "PowerLoadDragTorqueSpecificationMethod"
        )(value)

    @drag_torque_specification_method.setter
    @enforce_parameter_types
    def drag_torque_specification_method(
        self: Self, value: "_2223.PowerLoadDragTorqueSpecificationMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.PowerLoadDragTorqueSpecificationMethod"
        )
        self.wrapped.DragTorqueSpecificationMethod = value

    @property
    def drag_torque_vs_speed_and_time(self: Self) -> "_1572.GriddedSurfaceAccessor":
        """mastapy.math_utility.measured_data.GriddedSurfaceAccessor"""
        temp = self.wrapped.DragTorqueVsSpeedAndTime

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @drag_torque_vs_speed_and_time.setter
    @enforce_parameter_types
    def drag_torque_vs_speed_and_time(
        self: Self, value: "_1572.GriddedSurfaceAccessor"
    ):
        self.wrapped.DragTorqueVsSpeedAndTime = value.wrapped

    @property
    def dynamic_torsional_stiffness(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DynamicTorsionalStiffness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @dynamic_torsional_stiffness.setter
    @enforce_parameter_types
    def dynamic_torsional_stiffness(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DynamicTorsionalStiffness = value

    @property
    def electric_machine_data_set_selector(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_ElectricMachineDataSet":
        """ListWithSelectedItem[mastapy.system_model.fe.ElectricMachineDataSet]"""
        temp = self.wrapped.ElectricMachineDataSetSelector

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_ElectricMachineDataSet",
        )(temp)

    @electric_machine_data_set_selector.setter
    @enforce_parameter_types
    def electric_machine_data_set_selector(
        self: Self, value: "_2380.ElectricMachineDataSet"
    ):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_ElectricMachineDataSet.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_ElectricMachineDataSet.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.ElectricMachineDataSetSelector = value

    @property
    def engine_throttle_position(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EngineThrottlePosition

        if temp is None:
            return 0.0

        return temp

    @engine_throttle_position.setter
    @enforce_parameter_types
    def engine_throttle_position(self: Self, value: "float"):
        self.wrapped.EngineThrottlePosition = float(value) if value is not None else 0.0

    @property
    def engine_throttle_time_profile(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.EngineThrottleTimeProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @engine_throttle_time_profile.setter
    @enforce_parameter_types
    def engine_throttle_time_profile(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.EngineThrottleTimeProfile = value.wrapped

    @property
    def first_order_lag_cutoff_frequency(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FirstOrderLagCutoffFrequency

        if temp is None:
            return 0.0

        return temp

    @first_order_lag_cutoff_frequency.setter
    @enforce_parameter_types
    def first_order_lag_cutoff_frequency(self: Self, value: "float"):
        self.wrapped.FirstOrderLagCutoffFrequency = (
            float(value) if value is not None else 0.0
        )

    @property
    def first_order_lag_time_constant(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FirstOrderLagTimeConstant

        if temp is None:
            return 0.0

        return temp

    @first_order_lag_time_constant.setter
    @enforce_parameter_types
    def first_order_lag_time_constant(self: Self, value: "float"):
        self.wrapped.FirstOrderLagTimeConstant = (
            float(value) if value is not None else 0.0
        )

    @property
    def include_in_torsional_stiffness_calculation(
        self: Self,
    ) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.IncludeInTorsionalStiffnessCalculation

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @include_in_torsional_stiffness_calculation.setter
    @enforce_parameter_types
    def include_in_torsional_stiffness_calculation(
        self: Self, value: "Union[bool, Tuple[bool, bool]]"
    ):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.IncludeInTorsionalStiffnessCalculation = value

    @property
    def initial_angular_acceleration(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InitialAngularAcceleration

        if temp is None:
            return 0.0

        return temp

    @initial_angular_acceleration.setter
    @enforce_parameter_types
    def initial_angular_acceleration(self: Self, value: "float"):
        self.wrapped.InitialAngularAcceleration = (
            float(value) if value is not None else 0.0
        )

    @property
    def initial_angular_displacement(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InitialAngularDisplacement

        if temp is None:
            return 0.0

        return temp

    @initial_angular_displacement.setter
    @enforce_parameter_types
    def initial_angular_displacement(self: Self, value: "float"):
        self.wrapped.InitialAngularDisplacement = (
            float(value) if value is not None else 0.0
        )

    @property
    def initial_angular_velocity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InitialAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @initial_angular_velocity.setter
    @enforce_parameter_types
    def initial_angular_velocity(self: Self, value: "float"):
        self.wrapped.InitialAngularVelocity = float(value) if value is not None else 0.0

    @property
    def is_wheel_using_static_friction_initially(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsWheelUsingStaticFrictionInitially

        if temp is None:
            return False

        return temp

    @is_wheel_using_static_friction_initially.setter
    @enforce_parameter_types
    def is_wheel_using_static_friction_initially(self: Self, value: "bool"):
        self.wrapped.IsWheelUsingStaticFrictionInitially = (
            bool(value) if value is not None else False
        )

    @property
    def linear_resistance_coefficient(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LinearResistanceCoefficient

        if temp is None:
            return 0.0

        return temp

    @linear_resistance_coefficient.setter
    @enforce_parameter_types
    def linear_resistance_coefficient(self: Self, value: "float"):
        self.wrapped.LinearResistanceCoefficient = (
            float(value) if value is not None else 0.0
        )

    @property
    def linear_resistance_coefficient_time_profile(
        self: Self,
    ) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.LinearResistanceCoefficientTimeProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @linear_resistance_coefficient_time_profile.setter
    @enforce_parameter_types
    def linear_resistance_coefficient_time_profile(
        self: Self, value: "_1542.Vector2DListAccessor"
    ):
        self.wrapped.LinearResistanceCoefficientTimeProfile = value.wrapped

    @property
    def maximum_throttle_in_drive_cycle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumThrottleInDriveCycle

        if temp is None:
            return 0.0

        return temp

    @maximum_throttle_in_drive_cycle.setter
    @enforce_parameter_types
    def maximum_throttle_in_drive_cycle(self: Self, value: "float"):
        self.wrapped.MaximumThrottleInDriveCycle = (
            float(value) if value is not None else 0.0
        )

    @property
    def power(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Power

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @power.setter
    @enforce_parameter_types
    def power(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Power = value

    @property
    def power_load_for_pid_control(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.PowerLoadForPIDControl

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @power_load_for_pid_control.setter
    @enforce_parameter_types
    def power_load_for_pid_control(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.PowerLoadForPIDControl = value

    @property
    def proportion_of_vehicle_weight_carried(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ProportionOfVehicleWeightCarried

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @proportion_of_vehicle_weight_carried.setter
    @enforce_parameter_types
    def proportion_of_vehicle_weight_carried(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ProportionOfVehicleWeightCarried = value

    @property
    def quadratic_resistance_coefficient(self: Self) -> "float":
        """float"""
        temp = self.wrapped.QuadraticResistanceCoefficient

        if temp is None:
            return 0.0

        return temp

    @quadratic_resistance_coefficient.setter
    @enforce_parameter_types
    def quadratic_resistance_coefficient(self: Self, value: "float"):
        self.wrapped.QuadraticResistanceCoefficient = (
            float(value) if value is not None else 0.0
        )

    @property
    def quadratic_resistance_coefficient_time_profile(
        self: Self,
    ) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.QuadraticResistanceCoefficientTimeProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @quadratic_resistance_coefficient_time_profile.setter
    @enforce_parameter_types
    def quadratic_resistance_coefficient_time_profile(
        self: Self, value: "_1542.Vector2DListAccessor"
    ):
        self.wrapped.QuadraticResistanceCoefficientTimeProfile = value.wrapped

    @property
    def specified_angle_for_input_torque(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpecifiedAngleForInputTorque

        if temp is None:
            return 0.0

        return temp

    @specified_angle_for_input_torque.setter
    @enforce_parameter_types
    def specified_angle_for_input_torque(self: Self, value: "float"):
        self.wrapped.SpecifiedAngleForInputTorque = (
            float(value) if value is not None else 0.0
        )

    @property
    def specified_time_for_input_torque(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpecifiedTimeForInputTorque

        if temp is None:
            return 0.0

        return temp

    @specified_time_for_input_torque.setter
    @enforce_parameter_types
    def specified_time_for_input_torque(self: Self, value: "float"):
        self.wrapped.SpecifiedTimeForInputTorque = (
            float(value) if value is not None else 0.0
        )

    @property
    def specify_initial_acceleration(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyInitialAcceleration

        if temp is None:
            return False

        return temp

    @specify_initial_acceleration.setter
    @enforce_parameter_types
    def specify_initial_acceleration(self: Self, value: "bool"):
        self.wrapped.SpecifyInitialAcceleration = (
            bool(value) if value is not None else False
        )

    @property
    def specify_initial_displacement(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyInitialDisplacement

        if temp is None:
            return False

        return temp

    @specify_initial_displacement.setter
    @enforce_parameter_types
    def specify_initial_displacement(self: Self, value: "bool"):
        self.wrapped.SpecifyInitialDisplacement = (
            bool(value) if value is not None else False
        )

    @property
    def specify_initial_velocity(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyInitialVelocity

        if temp is None:
            return False

        return temp

    @specify_initial_velocity.setter
    @enforce_parameter_types
    def specify_initial_velocity(self: Self, value: "bool"):
        self.wrapped.SpecifyInitialVelocity = (
            bool(value) if value is not None else False
        )

    @property
    def speed(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @speed.setter
    @enforce_parameter_types
    def speed(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Speed = value

    @property
    def speed_vs_time(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.SpeedVsTime

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @speed_vs_time.setter
    @enforce_parameter_types
    def speed_vs_time(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.SpeedVsTime = value.wrapped

    @property
    def system_deflection_torque_also_applies_to_advanced_system_deflection(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = self.wrapped.SystemDeflectionTorqueAlsoAppliesToAdvancedSystemDeflection

        if temp is None:
            return False

        return temp

    @system_deflection_torque_also_applies_to_advanced_system_deflection.setter
    @enforce_parameter_types
    def system_deflection_torque_also_applies_to_advanced_system_deflection(
        self: Self, value: "bool"
    ):
        self.wrapped.SystemDeflectionTorqueAlsoAppliesToAdvancedSystemDeflection = (
            bool(value) if value is not None else False
        )

    @property
    def system_deflection_torque_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_TorqueSpecificationForSystemDeflection":
        """EnumWithSelectedValue[mastapy.system_model.analyses_and_results.static_loads.TorqueSpecificationForSystemDeflection]"""
        temp = self.wrapped.SystemDeflectionTorqueMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_TorqueSpecificationForSystemDeflection.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @system_deflection_torque_method.setter
    @enforce_parameter_types
    def system_deflection_torque_method(
        self: Self, value: "_6986.TorqueSpecificationForSystemDeflection"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_TorqueSpecificationForSystemDeflection.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.SystemDeflectionTorqueMethod = value

    @property
    def target_engine_idle_speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TargetEngineIdleSpeed

        if temp is None:
            return 0.0

        return temp

    @target_engine_idle_speed.setter
    @enforce_parameter_types
    def target_engine_idle_speed(self: Self, value: "float"):
        self.wrapped.TargetEngineIdleSpeed = float(value) if value is not None else 0.0

    @property
    def target_speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TargetSpeed

        if temp is None:
            return 0.0

        return temp

    @target_speed.setter
    @enforce_parameter_types
    def target_speed(self: Self, value: "float"):
        self.wrapped.TargetSpeed = float(value) if value is not None else 0.0

    @property
    def target_speed_input_type(
        self: Self,
    ) -> "_2225.PowerLoadPIDControlSpeedInputType":
        """mastapy.system_model.PowerLoadPIDControlSpeedInputType"""
        temp = self.wrapped.TargetSpeedInputType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.PowerLoadPIDControlSpeedInputType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model._2225", "PowerLoadPIDControlSpeedInputType"
        )(value)

    @target_speed_input_type.setter
    @enforce_parameter_types
    def target_speed_input_type(
        self: Self, value: "_2225.PowerLoadPIDControlSpeedInputType"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.PowerLoadPIDControlSpeedInputType"
        )
        self.wrapped.TargetSpeedInputType = value

    @property
    def target_speed_vs_time(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.TargetSpeedVsTime

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @target_speed_vs_time.setter
    @enforce_parameter_types
    def target_speed_vs_time(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.TargetSpeedVsTime = value.wrapped

    @property
    def torque(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @torque.setter
    @enforce_parameter_types
    def torque(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Torque = value

    @property
    def torque_input_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod":
        """EnumWithSelectedValue[mastapy.system_model.PowerLoadInputTorqueSpecificationMethod]"""
        temp = self.wrapped.TorqueInputMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @torque_input_method.setter
    @enforce_parameter_types
    def torque_input_method(
        self: Self, value: "_2224.PowerLoadInputTorqueSpecificationMethod"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.TorqueInputMethod = value

    @property
    def torque_time_profile_repeats(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.TorqueTimeProfileRepeats

        if temp is None:
            return False

        return temp

    @torque_time_profile_repeats.setter
    @enforce_parameter_types
    def torque_time_profile_repeats(self: Self, value: "bool"):
        self.wrapped.TorqueTimeProfileRepeats = (
            bool(value) if value is not None else False
        )

    @property
    def torque_vs_angle(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.TorqueVsAngle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @torque_vs_angle.setter
    @enforce_parameter_types
    def torque_vs_angle(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.TorqueVsAngle = value.wrapped

    @property
    def torque_vs_angle_and_speed(self: Self) -> "_1572.GriddedSurfaceAccessor":
        """mastapy.math_utility.measured_data.GriddedSurfaceAccessor"""
        temp = self.wrapped.TorqueVsAngleAndSpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @torque_vs_angle_and_speed.setter
    @enforce_parameter_types
    def torque_vs_angle_and_speed(self: Self, value: "_1572.GriddedSurfaceAccessor"):
        self.wrapped.TorqueVsAngleAndSpeed = value.wrapped

    @property
    def torque_vs_time(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.TorqueVsTime

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @torque_vs_time.setter
    @enforce_parameter_types
    def torque_vs_time(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.TorqueVsTime = value.wrapped

    @property
    def total_mean_rotor_x_force_over_all_nodes(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalMeanRotorXForceOverAllNodes

        if temp is None:
            return 0.0

        return temp

    @property
    def total_mean_rotor_y_force_over_all_nodes(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalMeanRotorYForceOverAllNodes

        if temp is None:
            return 0.0

        return temp

    @property
    def unbalanced_magnetic_pull_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.UnbalancedMagneticPullStiffness

        if temp is None:
            return 0.0

        return temp

    @unbalanced_magnetic_pull_stiffness.setter
    @enforce_parameter_types
    def unbalanced_magnetic_pull_stiffness(self: Self, value: "float"):
        self.wrapped.UnbalancedMagneticPullStiffness = (
            float(value) if value is not None else 0.0
        )

    @property
    def use_engine_idle_speed_control(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseEngineIdleSpeedControl

        if temp is None:
            return False

        return temp

    @use_engine_idle_speed_control.setter
    @enforce_parameter_types
    def use_engine_idle_speed_control(self: Self, value: "bool"):
        self.wrapped.UseEngineIdleSpeedControl = (
            bool(value) if value is not None else False
        )

    @property
    def use_time_dependent_constant_resistance_coefficient(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseTimeDependentConstantResistanceCoefficient

        if temp is None:
            return False

        return temp

    @use_time_dependent_constant_resistance_coefficient.setter
    @enforce_parameter_types
    def use_time_dependent_constant_resistance_coefficient(self: Self, value: "bool"):
        self.wrapped.UseTimeDependentConstantResistanceCoefficient = (
            bool(value) if value is not None else False
        )

    @property
    def use_time_dependent_linear_resistance_coefficient(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseTimeDependentLinearResistanceCoefficient

        if temp is None:
            return False

        return temp

    @use_time_dependent_linear_resistance_coefficient.setter
    @enforce_parameter_types
    def use_time_dependent_linear_resistance_coefficient(self: Self, value: "bool"):
        self.wrapped.UseTimeDependentLinearResistanceCoefficient = (
            bool(value) if value is not None else False
        )

    @property
    def use_time_dependent_quadratic_resistance_coefficient(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseTimeDependentQuadraticResistanceCoefficient

        if temp is None:
            return False

        return temp

    @use_time_dependent_quadratic_resistance_coefficient.setter
    @enforce_parameter_types
    def use_time_dependent_quadratic_resistance_coefficient(self: Self, value: "bool"):
        self.wrapped.UseTimeDependentQuadraticResistanceCoefficient = (
            bool(value) if value is not None else False
        )

    @property
    def use_time_dependent_throttle(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseTimeDependentThrottle

        if temp is None:
            return False

        return temp

    @use_time_dependent_throttle.setter
    @enforce_parameter_types
    def use_time_dependent_throttle(self: Self, value: "bool"):
        self.wrapped.UseTimeDependentThrottle = (
            bool(value) if value is not None else False
        )

    @property
    def vehicle_speed_to_start_idle_control(self: Self) -> "float":
        """float"""
        temp = self.wrapped.VehicleSpeedToStartIdleControl

        if temp is None:
            return 0.0

        return temp

    @vehicle_speed_to_start_idle_control.setter
    @enforce_parameter_types
    def vehicle_speed_to_start_idle_control(self: Self, value: "float"):
        self.wrapped.VehicleSpeedToStartIdleControl = (
            float(value) if value is not None else 0.0
        )

    @property
    def vehicle_speed_to_stop_idle_control(self: Self) -> "float":
        """float"""
        temp = self.wrapped.VehicleSpeedToStopIdleControl

        if temp is None:
            return 0.0

        return temp

    @vehicle_speed_to_stop_idle_control.setter
    @enforce_parameter_types
    def vehicle_speed_to_stop_idle_control(self: Self, value: "float"):
        self.wrapped.VehicleSpeedToStopIdleControl = (
            float(value) if value is not None else 0.0
        )

    @property
    def velocity_first_order_lag_cutoff_frequency(self: Self) -> "float":
        """float"""
        temp = self.wrapped.VelocityFirstOrderLagCutoffFrequency

        if temp is None:
            return 0.0

        return temp

    @velocity_first_order_lag_cutoff_frequency.setter
    @enforce_parameter_types
    def velocity_first_order_lag_cutoff_frequency(self: Self, value: "float"):
        self.wrapped.VelocityFirstOrderLagCutoffFrequency = (
            float(value) if value is not None else 0.0
        )

    @property
    def velocity_first_order_lag_time_constant(self: Self) -> "float":
        """float"""
        temp = self.wrapped.VelocityFirstOrderLagTimeConstant

        if temp is None:
            return 0.0

        return temp

    @velocity_first_order_lag_time_constant.setter
    @enforce_parameter_types
    def velocity_first_order_lag_time_constant(self: Self, value: "float"):
        self.wrapped.VelocityFirstOrderLagTimeConstant = (
            float(value) if value is not None else 0.0
        )

    @property
    def wheel_slip_model(self: Self) -> "_5524.WheelSlipType":
        """mastapy.system_model.analyses_and_results.mbd_analyses.WheelSlipType"""
        temp = self.wrapped.WheelSlipModel

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.WheelSlipType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.mbd_analyses._5524",
            "WheelSlipType",
        )(value)

    @wheel_slip_model.setter
    @enforce_parameter_types
    def wheel_slip_model(self: Self, value: "_5524.WheelSlipType"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.WheelSlipType",
        )
        self.wrapped.WheelSlipModel = value

    @property
    def wheel_static_to_dynamic_friction_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelStaticToDynamicFrictionRatio

        if temp is None:
            return 0.0

        return temp

    @wheel_static_to_dynamic_friction_ratio.setter
    @enforce_parameter_types
    def wheel_static_to_dynamic_friction_ratio(self: Self, value: "float"):
        self.wrapped.WheelStaticToDynamicFrictionRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def wheel_to_vehicle_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelToVehicleStiffness

        if temp is None:
            return 0.0

        return temp

    @wheel_to_vehicle_stiffness.setter
    @enforce_parameter_types
    def wheel_to_vehicle_stiffness(self: Self, value: "float"):
        self.wrapped.WheelToVehicleStiffness = (
            float(value) if value is not None else 0.0
        )

    @property
    def coefficient_of_friction_with_ground(
        self: Self,
    ) -> "_100.NonDimensionalInputComponent":
        """mastapy.nodal_analysis.varying_input_components.NonDimensionalInputComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoefficientOfFrictionWithGround

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def engine_idle_speed_control_pid_settings(
        self: Self,
    ) -> "_1583.PIDControlSettings":
        """mastapy.math_utility.control.PIDControlSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EngineIdleSpeedControlPIDSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pid_control_settings(self: Self) -> "_1583.PIDControlSettings":
        """mastapy.math_utility.control.PIDControlSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PIDControlSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def get_harmonic_load_data_for_import(
        self: Self,
    ) -> "_6880.ElectricMachineHarmonicLoadData":
        """mastapy.system_model.analyses_and_results.static_loads.ElectricMachineHarmonicLoadData"""
        method_result = self.wrapped.GetHarmonicLoadDataForImport()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "PowerLoadLoadCase._Cast_PowerLoadLoadCase":
        return self._Cast_PowerLoadLoadCase(self)
