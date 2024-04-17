"""FormWheelGrindingProcessSimulation"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.manufacturing.cylindrical.process_simulation import _642
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FORM_WHEEL_GRINDING_PROCESS_SIMULATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.ProcessSimulation",
    "FormWheelGrindingProcessSimulation",
)


__docformat__ = "restructuredtext en"
__all__ = ("FormWheelGrindingProcessSimulation",)


Self = TypeVar("Self", bound="FormWheelGrindingProcessSimulation")


class FormWheelGrindingProcessSimulation(_642.CutterProcessSimulation):
    """FormWheelGrindingProcessSimulation

    This is a mastapy class.
    """

    TYPE = _FORM_WHEEL_GRINDING_PROCESS_SIMULATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FormWheelGrindingProcessSimulation")

    class _Cast_FormWheelGrindingProcessSimulation:
        """Special nested class for casting FormWheelGrindingProcessSimulation to subclasses."""

        def __init__(
            self: "FormWheelGrindingProcessSimulation._Cast_FormWheelGrindingProcessSimulation",
            parent: "FormWheelGrindingProcessSimulation",
        ):
            self._parent = parent

        @property
        def cutter_process_simulation(
            self: "FormWheelGrindingProcessSimulation._Cast_FormWheelGrindingProcessSimulation",
        ) -> "_642.CutterProcessSimulation":
            return self._parent._cast(_642.CutterProcessSimulation)

        @property
        def form_wheel_grinding_process_simulation(
            self: "FormWheelGrindingProcessSimulation._Cast_FormWheelGrindingProcessSimulation",
        ) -> "FormWheelGrindingProcessSimulation":
            return self._parent

        def __getattr__(
            self: "FormWheelGrindingProcessSimulation._Cast_FormWheelGrindingProcessSimulation",
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
        self: Self, instance_to_wrap: "FormWheelGrindingProcessSimulation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_relative_tilt_x(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GearRelativeTiltX

        if temp is None:
            return 0.0

        return temp

    @gear_relative_tilt_x.setter
    @enforce_parameter_types
    def gear_relative_tilt_x(self: Self, value: "float"):
        self.wrapped.GearRelativeTiltX = float(value) if value is not None else 0.0

    @property
    def gear_relative_tilt_y(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GearRelativeTiltY

        if temp is None:
            return 0.0

        return temp

    @gear_relative_tilt_y.setter
    @enforce_parameter_types
    def gear_relative_tilt_y(self: Self, value: "float"):
        self.wrapped.GearRelativeTiltY = float(value) if value is not None else 0.0

    @property
    def grind_wheel_axial_offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GrindWheelAxialOffset

        if temp is None:
            return 0.0

        return temp

    @grind_wheel_axial_offset.setter
    @enforce_parameter_types
    def grind_wheel_axial_offset(self: Self, value: "float"):
        self.wrapped.GrindWheelAxialOffset = float(value) if value is not None else 0.0

    @property
    def grind_wheel_axial_runout_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GrindWheelAxialRunoutRadius

        if temp is None:
            return 0.0

        return temp

    @grind_wheel_axial_runout_radius.setter
    @enforce_parameter_types
    def grind_wheel_axial_runout_radius(self: Self, value: "float"):
        self.wrapped.GrindWheelAxialRunoutRadius = (
            float(value) if value is not None else 0.0
        )

    @property
    def grind_wheel_axial_runout_reading(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GrindWheelAxialRunoutReading

        if temp is None:
            return 0.0

        return temp

    @grind_wheel_axial_runout_reading.setter
    @enforce_parameter_types
    def grind_wheel_axial_runout_reading(self: Self, value: "float"):
        self.wrapped.GrindWheelAxialRunoutReading = (
            float(value) if value is not None else 0.0
        )

    @property
    def grind_wheel_diameter_deviation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GrindWheelDiameterDeviation

        if temp is None:
            return 0.0

        return temp

    @grind_wheel_diameter_deviation.setter
    @enforce_parameter_types
    def grind_wheel_diameter_deviation(self: Self, value: "float"):
        self.wrapped.GrindWheelDiameterDeviation = (
            float(value) if value is not None else 0.0
        )

    @property
    def grind_wheel_tilt_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GrindWheelTiltAngle

        if temp is None:
            return 0.0

        return temp

    @grind_wheel_tilt_angle.setter
    @enforce_parameter_types
    def grind_wheel_tilt_angle(self: Self, value: "float"):
        self.wrapped.GrindWheelTiltAngle = float(value) if value is not None else 0.0

    @property
    def grind_wheel_tilt_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GrindWheelTiltRadius

        if temp is None:
            return 0.0

        return temp

    @grind_wheel_tilt_radius.setter
    @enforce_parameter_types
    def grind_wheel_tilt_radius(self: Self, value: "float"):
        self.wrapped.GrindWheelTiltRadius = float(value) if value is not None else 0.0

    @property
    def left_amplitude(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LeftAmplitude

        if temp is None:
            return 0.0

        return temp

    @left_amplitude.setter
    @enforce_parameter_types
    def left_amplitude(self: Self, value: "float"):
        self.wrapped.LeftAmplitude = float(value) if value is not None else 0.0

    @property
    def left_number_of_cycles(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LeftNumberOfCycles

        if temp is None:
            return 0.0

        return temp

    @left_number_of_cycles.setter
    @enforce_parameter_types
    def left_number_of_cycles(self: Self, value: "float"):
        self.wrapped.LeftNumberOfCycles = float(value) if value is not None else 0.0

    @property
    def left_starting_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LeftStartingAngle

        if temp is None:
            return 0.0

        return temp

    @left_starting_angle.setter
    @enforce_parameter_types
    def left_starting_angle(self: Self, value: "float"):
        self.wrapped.LeftStartingAngle = float(value) if value is not None else 0.0

    @property
    def right_amplitude(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RightAmplitude

        if temp is None:
            return 0.0

        return temp

    @right_amplitude.setter
    @enforce_parameter_types
    def right_amplitude(self: Self, value: "float"):
        self.wrapped.RightAmplitude = float(value) if value is not None else 0.0

    @property
    def right_number_of_cycles(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RightNumberOfCycles

        if temp is None:
            return 0.0

        return temp

    @right_number_of_cycles.setter
    @enforce_parameter_types
    def right_number_of_cycles(self: Self, value: "float"):
        self.wrapped.RightNumberOfCycles = float(value) if value is not None else 0.0

    @property
    def right_starting_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RightStartingAngle

        if temp is None:
            return 0.0

        return temp

    @right_starting_angle.setter
    @enforce_parameter_types
    def right_starting_angle(self: Self, value: "float"):
        self.wrapped.RightStartingAngle = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "FormWheelGrindingProcessSimulation._Cast_FormWheelGrindingProcessSimulation":
        return self._Cast_FormWheelGrindingProcessSimulation(self)
