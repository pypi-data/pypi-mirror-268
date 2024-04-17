"""MagnetMaterial"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.materials import _272
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MAGNET_MATERIAL = python_net_import("SMT.MastaAPI.ElectricMachines", "MagnetMaterial")

if TYPE_CHECKING:
    from mastapy.utility.databases import _1836


__docformat__ = "restructuredtext en"
__all__ = ("MagnetMaterial",)


Self = TypeVar("Self", bound="MagnetMaterial")


class MagnetMaterial(_272.Material):
    """MagnetMaterial

    This is a mastapy class.
    """

    TYPE = _MAGNET_MATERIAL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MagnetMaterial")

    class _Cast_MagnetMaterial:
        """Special nested class for casting MagnetMaterial to subclasses."""

        def __init__(
            self: "MagnetMaterial._Cast_MagnetMaterial", parent: "MagnetMaterial"
        ):
            self._parent = parent

        @property
        def material(self: "MagnetMaterial._Cast_MagnetMaterial") -> "_272.Material":
            return self._parent._cast(_272.Material)

        @property
        def named_database_item(
            self: "MagnetMaterial._Cast_MagnetMaterial",
        ) -> "_1836.NamedDatabaseItem":
            from mastapy.utility.databases import _1836

            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def magnet_material(
            self: "MagnetMaterial._Cast_MagnetMaterial",
        ) -> "MagnetMaterial":
            return self._parent

        def __getattr__(self: "MagnetMaterial._Cast_MagnetMaterial", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MagnetMaterial.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def country(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Country

        if temp is None:
            return ""

        return temp

    @country.setter
    @enforce_parameter_types
    def country(self: Self, value: "str"):
        self.wrapped.Country = str(value) if value is not None else ""

    @property
    def electrical_resistivity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ElectricalResistivity

        if temp is None:
            return 0.0

        return temp

    @electrical_resistivity.setter
    @enforce_parameter_types
    def electrical_resistivity(self: Self, value: "float"):
        self.wrapped.ElectricalResistivity = float(value) if value is not None else 0.0

    @property
    def grade(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Grade

        if temp is None:
            return ""

        return temp

    @grade.setter
    @enforce_parameter_types
    def grade(self: Self, value: "str"):
        self.wrapped.Grade = str(value) if value is not None else ""

    @property
    def manufacturer(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Manufacturer

        if temp is None:
            return ""

        return temp

    @manufacturer.setter
    @enforce_parameter_types
    def manufacturer(self: Self, value: "str"):
        self.wrapped.Manufacturer = str(value) if value is not None else ""

    @property
    def material_category(self: Self) -> "str":
        """str"""
        temp = self.wrapped.MaterialCategory

        if temp is None:
            return ""

        return temp

    @material_category.setter
    @enforce_parameter_types
    def material_category(self: Self, value: "str"):
        self.wrapped.MaterialCategory = str(value) if value is not None else ""

    @property
    def relative_permeability(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RelativePermeability

        if temp is None:
            return 0.0

        return temp

    @relative_permeability.setter
    @enforce_parameter_types
    def relative_permeability(self: Self, value: "float"):
        self.wrapped.RelativePermeability = float(value) if value is not None else 0.0

    @property
    def remanence_at_20_degrees_c(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RemanenceAt20DegreesC

        if temp is None:
            return 0.0

        return temp

    @remanence_at_20_degrees_c.setter
    @enforce_parameter_types
    def remanence_at_20_degrees_c(self: Self, value: "float"):
        self.wrapped.RemanenceAt20DegreesC = float(value) if value is not None else 0.0

    @property
    def temperature_coefficient_for_remanence(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TemperatureCoefficientForRemanence

        if temp is None:
            return 0.0

        return temp

    @temperature_coefficient_for_remanence.setter
    @enforce_parameter_types
    def temperature_coefficient_for_remanence(self: Self, value: "float"):
        self.wrapped.TemperatureCoefficientForRemanence = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(self: Self) -> "MagnetMaterial._Cast_MagnetMaterial":
        return self._Cast_MagnetMaterial(self)
