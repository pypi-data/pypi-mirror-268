"""CylindricalGearSpecification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation",
    "CylindricalGearSpecification",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1092


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSpecification",)


Self = TypeVar("Self", bound="CylindricalGearSpecification")


class CylindricalGearSpecification(_0.APIBase):
    """CylindricalGearSpecification

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SPECIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearSpecification")

    class _Cast_CylindricalGearSpecification:
        """Special nested class for casting CylindricalGearSpecification to subclasses."""

        def __init__(
            self: "CylindricalGearSpecification._Cast_CylindricalGearSpecification",
            parent: "CylindricalGearSpecification",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_specification(
            self: "CylindricalGearSpecification._Cast_CylindricalGearSpecification",
        ) -> "CylindricalGearSpecification":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSpecification._Cast_CylindricalGearSpecification",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearSpecification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def helix_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelixAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def normal_module(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalModule

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_pressure_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @normal_pressure_angle.setter
    @enforce_parameter_types
    def normal_pressure_angle(self: Self, value: "float"):
        self.wrapped.NormalPressureAngle = float(value) if value is not None else 0.0

    @property
    def number_of_teeth_unsigned(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfTeethUnsigned

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_thickness_specification(
        self: Self,
    ) -> "_1092.ToothThicknessSpecificationBase":
        """mastapy.gears.gear_designs.cylindrical.ToothThicknessSpecificationBase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothThicknessSpecification

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSpecification._Cast_CylindricalGearSpecification":
        return self._Cast_CylindricalGearSpecification(self)
