"""ManufacturingMachine"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.utility.databases import _1836
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MANUFACTURING_MACHINE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ManufacturingMachine"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.bevel import _801, _815


__docformat__ = "restructuredtext en"
__all__ = ("ManufacturingMachine",)


Self = TypeVar("Self", bound="ManufacturingMachine")


class ManufacturingMachine(_1836.NamedDatabaseItem):
    """ManufacturingMachine

    This is a mastapy class.
    """

    TYPE = _MANUFACTURING_MACHINE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ManufacturingMachine")

    class _Cast_ManufacturingMachine:
        """Special nested class for casting ManufacturingMachine to subclasses."""

        def __init__(
            self: "ManufacturingMachine._Cast_ManufacturingMachine",
            parent: "ManufacturingMachine",
        ):
            self._parent = parent

        @property
        def named_database_item(
            self: "ManufacturingMachine._Cast_ManufacturingMachine",
        ) -> "_1836.NamedDatabaseItem":
            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def manufacturing_machine(
            self: "ManufacturingMachine._Cast_ManufacturingMachine",
        ) -> "ManufacturingMachine":
            return self._parent

        def __getattr__(
            self: "ManufacturingMachine._Cast_ManufacturingMachine", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ManufacturingMachine.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def can_work_for_formate(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CanWorkForFormate

        if temp is None:
            return False

        return temp

    @can_work_for_formate.setter
    @enforce_parameter_types
    def can_work_for_formate(self: Self, value: "bool"):
        self.wrapped.CanWorkForFormate = bool(value) if value is not None else False

    @property
    def can_work_for_generating(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CanWorkForGenerating

        if temp is None:
            return False

        return temp

    @can_work_for_generating.setter
    @enforce_parameter_types
    def can_work_for_generating(self: Self, value: "bool"):
        self.wrapped.CanWorkForGenerating = bool(value) if value is not None else False

    @property
    def can_work_for_roller_modification(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CanWorkForRollerModification

        if temp is None:
            return False

        return temp

    @can_work_for_roller_modification.setter
    @enforce_parameter_types
    def can_work_for_roller_modification(self: Self, value: "bool"):
        self.wrapped.CanWorkForRollerModification = (
            bool(value) if value is not None else False
        )

    @property
    def can_work_for_tilt(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CanWorkForTilt

        if temp is None:
            return False

        return temp

    @can_work_for_tilt.setter
    @enforce_parameter_types
    def can_work_for_tilt(self: Self, value: "bool"):
        self.wrapped.CanWorkForTilt = bool(value) if value is not None else False

    @property
    def eccentric_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EccentricDistance

        if temp is None:
            return 0.0

        return temp

    @eccentric_distance.setter
    @enforce_parameter_types
    def eccentric_distance(self: Self, value: "float"):
        self.wrapped.EccentricDistance = float(value) if value is not None else 0.0

    @property
    def machine_type(self: Self) -> "_801.MachineTypes":
        """mastapy.gears.manufacturing.bevel.MachineTypes"""
        temp = self.wrapped.MachineType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Manufacturing.Bevel.MachineTypes"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.manufacturing.bevel._801", "MachineTypes"
        )(value)

    @machine_type.setter
    @enforce_parameter_types
    def machine_type(self: Self, value: "_801.MachineTypes"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Manufacturing.Bevel.MachineTypes"
        )
        self.wrapped.MachineType = value

    @property
    def maximum_tilt_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumTiltAngle

        if temp is None:
            return 0.0

        return temp

    @maximum_tilt_angle.setter
    @enforce_parameter_types
    def maximum_tilt_angle(self: Self, value: "float"):
        self.wrapped.MaximumTiltAngle = float(value) if value is not None else 0.0

    @property
    def tilt_body_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TiltBodyAngle

        if temp is None:
            return 0.0

        return temp

    @tilt_body_angle.setter
    @enforce_parameter_types
    def tilt_body_angle(self: Self, value: "float"):
        self.wrapped.TiltBodyAngle = float(value) if value is not None else 0.0

    @property
    def tilt_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TiltDistance

        if temp is None:
            return 0.0

        return temp

    @tilt_distance.setter
    @enforce_parameter_types
    def tilt_distance(self: Self, value: "float"):
        self.wrapped.TiltDistance = float(value) if value is not None else 0.0

    @property
    def wheel_formate_machine_type(self: Self) -> "_815.WheelFormatMachineTypes":
        """mastapy.gears.manufacturing.bevel.WheelFormatMachineTypes"""
        temp = self.wrapped.WheelFormateMachineType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Manufacturing.Bevel.WheelFormatMachineTypes"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.manufacturing.bevel._815", "WheelFormatMachineTypes"
        )(value)

    @wheel_formate_machine_type.setter
    @enforce_parameter_types
    def wheel_formate_machine_type(self: Self, value: "_815.WheelFormatMachineTypes"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Manufacturing.Bevel.WheelFormatMachineTypes"
        )
        self.wrapped.WheelFormateMachineType = value

    @property
    def cast_to(self: Self) -> "ManufacturingMachine._Cast_ManufacturingMachine":
        return self._Cast_ManufacturingMachine(self)
