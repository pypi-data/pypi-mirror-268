"""RawMaterial"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.databases import _1836
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RAW_MATERIAL = python_net_import("SMT.MastaAPI.Gears.Materials", "RawMaterial")


__docformat__ = "restructuredtext en"
__all__ = ("RawMaterial",)


Self = TypeVar("Self", bound="RawMaterial")


class RawMaterial(_1836.NamedDatabaseItem):
    """RawMaterial

    This is a mastapy class.
    """

    TYPE = _RAW_MATERIAL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RawMaterial")

    class _Cast_RawMaterial:
        """Special nested class for casting RawMaterial to subclasses."""

        def __init__(self: "RawMaterial._Cast_RawMaterial", parent: "RawMaterial"):
            self._parent = parent

        @property
        def named_database_item(
            self: "RawMaterial._Cast_RawMaterial",
        ) -> "_1836.NamedDatabaseItem":
            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def raw_material(self: "RawMaterial._Cast_RawMaterial") -> "RawMaterial":
            return self._parent

        def __getattr__(self: "RawMaterial._Cast_RawMaterial", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RawMaterial.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cost_per_kilogram(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CostPerKilogram

        if temp is None:
            return 0.0

        return temp

    @cost_per_kilogram.setter
    @enforce_parameter_types
    def cost_per_kilogram(self: Self, value: "float"):
        self.wrapped.CostPerKilogram = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "RawMaterial._Cast_RawMaterial":
        return self._Cast_RawMaterial(self)
