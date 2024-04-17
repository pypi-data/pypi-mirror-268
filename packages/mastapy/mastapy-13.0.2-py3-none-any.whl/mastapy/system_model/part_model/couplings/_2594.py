"""CVT"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.part_model.couplings import _2583
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Couplings", "CVT")

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2483, _2441, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("CVT",)


Self = TypeVar("Self", bound="CVT")


class CVT(_2583.BeltDrive):
    """CVT

    This is a mastapy class.
    """

    TYPE = _CVT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVT")

    class _Cast_CVT:
        """Special nested class for casting CVT to subclasses."""

        def __init__(self: "CVT._Cast_CVT", parent: "CVT"):
            self._parent = parent

        @property
        def belt_drive(self: "CVT._Cast_CVT") -> "_2583.BeltDrive":
            return self._parent._cast(_2583.BeltDrive)

        @property
        def specialised_assembly(self: "CVT._Cast_CVT") -> "_2483.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2483

            return self._parent._cast(_2483.SpecialisedAssembly)

        @property
        def abstract_assembly(self: "CVT._Cast_CVT") -> "_2441.AbstractAssembly":
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.AbstractAssembly)

        @property
        def part(self: "CVT._Cast_CVT") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(self: "CVT._Cast_CVT") -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def cvt(self: "CVT._Cast_CVT") -> "CVT":
            return self._parent

        def __getattr__(self: "CVT._Cast_CVT", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVT.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def belt_loss_constant(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BeltLossConstant

        if temp is None:
            return 0.0

        return temp

    @belt_loss_constant.setter
    @enforce_parameter_types
    def belt_loss_constant(self: Self, value: "float"):
        self.wrapped.BeltLossConstant = float(value) if value is not None else 0.0

    @property
    def coefficient_of_static_friction_with_lubrication(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CoefficientOfStaticFrictionWithLubrication

        if temp is None:
            return 0.0

        return temp

    @coefficient_of_static_friction_with_lubrication.setter
    @enforce_parameter_types
    def coefficient_of_static_friction_with_lubrication(self: Self, value: "float"):
        self.wrapped.CoefficientOfStaticFrictionWithLubrication = (
            float(value) if value is not None else 0.0
        )

    @property
    def contact_stiffness_for_unit_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ContactStiffnessForUnitLength

        if temp is None:
            return 0.0

        return temp

    @contact_stiffness_for_unit_length.setter
    @enforce_parameter_types
    def contact_stiffness_for_unit_length(self: Self, value: "float"):
        self.wrapped.ContactStiffnessForUnitLength = (
            float(value) if value is not None else 0.0
        )

    @property
    def cross_sectional_area_of_the_pump_outlet(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CrossSectionalAreaOfThePumpOutlet

        if temp is None:
            return 0.0

        return temp

    @cross_sectional_area_of_the_pump_outlet.setter
    @enforce_parameter_types
    def cross_sectional_area_of_the_pump_outlet(self: Self, value: "float"):
        self.wrapped.CrossSectionalAreaOfThePumpOutlet = (
            float(value) if value is not None else 0.0
        )

    @property
    def pulley_sheave_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PulleySheaveAngle

        if temp is None:
            return 0.0

        return temp

    @pulley_sheave_angle.setter
    @enforce_parameter_types
    def pulley_sheave_angle(self: Self, value: "float"):
        self.wrapped.PulleySheaveAngle = float(value) if value is not None else 0.0

    @property
    def pump_displacement_per_revolution(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PumpDisplacementPerRevolution

        if temp is None:
            return 0.0

        return temp

    @pump_displacement_per_revolution.setter
    @enforce_parameter_types
    def pump_displacement_per_revolution(self: Self, value: "float"):
        self.wrapped.PumpDisplacementPerRevolution = (
            float(value) if value is not None else 0.0
        )

    @property
    def pump_pressure_loss_constant(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PumpPressureLossConstant

        if temp is None:
            return 0.0

        return temp

    @pump_pressure_loss_constant.setter
    @enforce_parameter_types
    def pump_pressure_loss_constant(self: Self, value: "float"):
        self.wrapped.PumpPressureLossConstant = (
            float(value) if value is not None else 0.0
        )

    @property
    def pump_speed_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PumpSpeedFactor

        if temp is None:
            return 0.0

        return temp

    @pump_speed_factor.setter
    @enforce_parameter_types
    def pump_speed_factor(self: Self, value: "float"):
        self.wrapped.PumpSpeedFactor = float(value) if value is not None else 0.0

    @property
    def pump_speed_loss_constant(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PumpSpeedLossConstant

        if temp is None:
            return 0.0

        return temp

    @pump_speed_loss_constant.setter
    @enforce_parameter_types
    def pump_speed_loss_constant(self: Self, value: "float"):
        self.wrapped.PumpSpeedLossConstant = float(value) if value is not None else 0.0

    @property
    def tangential_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TangentialStiffness

        if temp is None:
            return 0.0

        return temp

    @tangential_stiffness.setter
    @enforce_parameter_types
    def tangential_stiffness(self: Self, value: "float"):
        self.wrapped.TangentialStiffness = float(value) if value is not None else 0.0

    @property
    def use_improved_model(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseImprovedModel

        if temp is None:
            return False

        return temp

    @use_improved_model.setter
    @enforce_parameter_types
    def use_improved_model(self: Self, value: "bool"):
        self.wrapped.UseImprovedModel = bool(value) if value is not None else False

    @property
    def cast_to(self: Self) -> "CVT._Cast_CVT":
        return self._Cast_CVT(self)
