"""TorqueConverterLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.system_model.analyses_and_results.mbd_analyses import _5517
from mastapy.system_model.analyses_and_results.static_loads import _6862
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "TorqueConverterLoadCase"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1542
    from mastapy.system_model.part_model.couplings import _2615
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6961,
        _6815,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterLoadCase",)


Self = TypeVar("Self", bound="TorqueConverterLoadCase")


class TorqueConverterLoadCase(_6862.CouplingLoadCase):
    """TorqueConverterLoadCase

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterLoadCase")

    class _Cast_TorqueConverterLoadCase:
        """Special nested class for casting TorqueConverterLoadCase to subclasses."""

        def __init__(
            self: "TorqueConverterLoadCase._Cast_TorqueConverterLoadCase",
            parent: "TorqueConverterLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_load_case(
            self: "TorqueConverterLoadCase._Cast_TorqueConverterLoadCase",
        ) -> "_6862.CouplingLoadCase":
            return self._parent._cast(_6862.CouplingLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "TorqueConverterLoadCase._Cast_TorqueConverterLoadCase",
        ) -> "_6961.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6961

            return self._parent._cast(_6961.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "TorqueConverterLoadCase._Cast_TorqueConverterLoadCase",
        ) -> "_6815.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6815

            return self._parent._cast(_6815.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "TorqueConverterLoadCase._Cast_TorqueConverterLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "TorqueConverterLoadCase._Cast_TorqueConverterLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterLoadCase._Cast_TorqueConverterLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterLoadCase._Cast_TorqueConverterLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def torque_converter_load_case(
            self: "TorqueConverterLoadCase._Cast_TorqueConverterLoadCase",
        ) -> "TorqueConverterLoadCase":
            return self._parent

        def __getattr__(
            self: "TorqueConverterLoadCase._Cast_TorqueConverterLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverterLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def initial_lock_up_clutch_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InitialLockUpClutchTemperature

        if temp is None:
            return 0.0

        return temp

    @initial_lock_up_clutch_temperature.setter
    @enforce_parameter_types
    def initial_lock_up_clutch_temperature(self: Self, value: "float"):
        self.wrapped.InitialLockUpClutchTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def initially_locked(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.InitiallyLocked

        if temp is None:
            return False

        return temp

    @initially_locked.setter
    @enforce_parameter_types
    def initially_locked(self: Self, value: "bool"):
        self.wrapped.InitiallyLocked = bool(value) if value is not None else False

    @property
    def lock_up_clutch_pressure_for_no_torque_converter_operation(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.LockUpClutchPressureForNoTorqueConverterOperation

        if temp is None:
            return 0.0

        return temp

    @lock_up_clutch_pressure_for_no_torque_converter_operation.setter
    @enforce_parameter_types
    def lock_up_clutch_pressure_for_no_torque_converter_operation(
        self: Self, value: "float"
    ):
        self.wrapped.LockUpClutchPressureForNoTorqueConverterOperation = (
            float(value) if value is not None else 0.0
        )

    @property
    def lock_up_clutch_pressure_time_profile(
        self: Self,
    ) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.LockUpClutchPressureTimeProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @lock_up_clutch_pressure_time_profile.setter
    @enforce_parameter_types
    def lock_up_clutch_pressure_time_profile(
        self: Self, value: "_1542.Vector2DListAccessor"
    ):
        self.wrapped.LockUpClutchPressureTimeProfile = value.wrapped

    @property
    def lock_up_clutch_rule(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_TorqueConverterLockupRule":
        """EnumWithSelectedValue[mastapy.system_model.analyses_and_results.mbd_analyses.TorqueConverterLockupRule]"""
        temp = self.wrapped.LockUpClutchRule

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_TorqueConverterLockupRule.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @lock_up_clutch_rule.setter
    @enforce_parameter_types
    def lock_up_clutch_rule(self: Self, value: "_5517.TorqueConverterLockupRule"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_TorqueConverterLockupRule.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LockUpClutchRule = value

    @property
    def locking_speed_ratio_threshold(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LockingSpeedRatioThreshold

        if temp is None:
            return 0.0

        return temp

    @locking_speed_ratio_threshold.setter
    @enforce_parameter_types
    def locking_speed_ratio_threshold(self: Self, value: "float"):
        self.wrapped.LockingSpeedRatioThreshold = (
            float(value) if value is not None else 0.0
        )

    @property
    def time_for_full_clutch_pressure(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TimeForFullClutchPressure

        if temp is None:
            return 0.0

        return temp

    @time_for_full_clutch_pressure.setter
    @enforce_parameter_types
    def time_for_full_clutch_pressure(self: Self, value: "float"):
        self.wrapped.TimeForFullClutchPressure = (
            float(value) if value is not None else 0.0
        )

    @property
    def time_to_change_locking_state(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TimeToChangeLockingState

        if temp is None:
            return 0.0

        return temp

    @time_to_change_locking_state.setter
    @enforce_parameter_types
    def time_to_change_locking_state(self: Self, value: "float"):
        self.wrapped.TimeToChangeLockingState = (
            float(value) if value is not None else 0.0
        )

    @property
    def transient_time_to_change_locking_status(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TransientTimeToChangeLockingStatus

        if temp is None:
            return 0.0

        return temp

    @transient_time_to_change_locking_status.setter
    @enforce_parameter_types
    def transient_time_to_change_locking_status(self: Self, value: "float"):
        self.wrapped.TransientTimeToChangeLockingStatus = (
            float(value) if value is not None else 0.0
        )

    @property
    def vehicle_speed_to_unlock(self: Self) -> "float":
        """float"""
        temp = self.wrapped.VehicleSpeedToUnlock

        if temp is None:
            return 0.0

        return temp

    @vehicle_speed_to_unlock.setter
    @enforce_parameter_types
    def vehicle_speed_to_unlock(self: Self, value: "float"):
        self.wrapped.VehicleSpeedToUnlock = float(value) if value is not None else 0.0

    @property
    def assembly_design(self: Self) -> "_2615.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "TorqueConverterLoadCase._Cast_TorqueConverterLoadCase":
        return self._Cast_TorqueConverterLoadCase(self)
