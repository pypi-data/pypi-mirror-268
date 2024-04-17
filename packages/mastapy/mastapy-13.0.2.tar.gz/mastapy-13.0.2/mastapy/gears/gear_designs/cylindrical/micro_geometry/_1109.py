"""CylindricalGearMicroGeometryMap"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_GEOMETRY_MAP = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "CylindricalGearMicroGeometryMap",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1124
    from mastapy.gears.gear_designs.cylindrical import _1029


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMicroGeometryMap",)


Self = TypeVar("Self", bound="CylindricalGearMicroGeometryMap")


class CylindricalGearMicroGeometryMap(_0.APIBase):
    """CylindricalGearMicroGeometryMap

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MICRO_GEOMETRY_MAP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearMicroGeometryMap")

    class _Cast_CylindricalGearMicroGeometryMap:
        """Special nested class for casting CylindricalGearMicroGeometryMap to subclasses."""

        def __init__(
            self: "CylindricalGearMicroGeometryMap._Cast_CylindricalGearMicroGeometryMap",
            parent: "CylindricalGearMicroGeometryMap",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_micro_geometry_map(
            self: "CylindricalGearMicroGeometryMap._Cast_CylindricalGearMicroGeometryMap",
        ) -> "CylindricalGearMicroGeometryMap":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMicroGeometryMap._Cast_CylindricalGearMicroGeometryMap",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearMicroGeometryMap.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def measured_map_data_type(self: Self) -> "_1124.MeasuredMapDataTypes":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.MeasuredMapDataTypes"""
        temp = self.wrapped.MeasuredMapDataType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry.MeasuredMapDataTypes",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical.micro_geometry._1124",
            "MeasuredMapDataTypes",
        )(value)

    @measured_map_data_type.setter
    @enforce_parameter_types
    def measured_map_data_type(self: Self, value: "_1124.MeasuredMapDataTypes"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry.MeasuredMapDataTypes",
        )
        self.wrapped.MeasuredMapDataType = value

    @property
    def profile_factor_for_0_bias_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileFactorFor0BiasRelief

        if temp is None:
            return 0.0

        return temp

    @profile_factor_for_0_bias_relief.setter
    @enforce_parameter_types
    def profile_factor_for_0_bias_relief(self: Self, value: "float"):
        self.wrapped.ProfileFactorFor0BiasRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def zero_bias_relief(self: Self) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZeroBiasRelief

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMicroGeometryMap._Cast_CylindricalGearMicroGeometryMap":
        return self._Cast_CylindricalGearMicroGeometryMap(self)
