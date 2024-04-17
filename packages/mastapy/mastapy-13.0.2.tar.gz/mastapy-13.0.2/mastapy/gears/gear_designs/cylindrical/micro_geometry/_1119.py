"""GearAlignment"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_ALIGNMENT = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry", "GearAlignment"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1029


__docformat__ = "restructuredtext en"
__all__ = ("GearAlignment",)


Self = TypeVar("Self", bound="GearAlignment")


class GearAlignment(_0.APIBase):
    """GearAlignment

    This is a mastapy class.
    """

    TYPE = _GEAR_ALIGNMENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearAlignment")

    class _Cast_GearAlignment:
        """Special nested class for casting GearAlignment to subclasses."""

        def __init__(
            self: "GearAlignment._Cast_GearAlignment", parent: "GearAlignment"
        ):
            self._parent = parent

        @property
        def gear_alignment(
            self: "GearAlignment._Cast_GearAlignment",
        ) -> "GearAlignment":
            return self._parent

        def __getattr__(self: "GearAlignment._Cast_GearAlignment", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearAlignment.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Diameter

        if temp is None:
            return 0.0

        return temp

    @property
    def index_of_reference_tooth(self: Self) -> "int":
        """int"""
        temp = self.wrapped.IndexOfReferenceTooth

        if temp is None:
            return 0

        return temp

    @index_of_reference_tooth.setter
    @enforce_parameter_types
    def index_of_reference_tooth(self: Self, value: "int"):
        self.wrapped.IndexOfReferenceTooth = int(value) if value is not None else 0

    @property
    def radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @property
    def roll_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def roll_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RollDistance

        if temp is None:
            return 0.0

        return temp

    @roll_distance.setter
    @enforce_parameter_types
    def roll_distance(self: Self, value: "float"):
        self.wrapped.RollDistance = float(value) if value is not None else 0.0

    @property
    def profile_measurement_of_the_tooth_at_least_roll_distance(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileMeasurementOfTheToothAtLeastRollDistance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearAlignment._Cast_GearAlignment":
        return self._Cast_GearAlignment(self)
