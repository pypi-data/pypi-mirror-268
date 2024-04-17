"""WindingMaterial"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.materials import _272
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WINDING_MATERIAL = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "WindingMaterial"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1836


__docformat__ = "restructuredtext en"
__all__ = ("WindingMaterial",)


Self = TypeVar("Self", bound="WindingMaterial")


class WindingMaterial(_272.Material):
    """WindingMaterial

    This is a mastapy class.
    """

    TYPE = _WINDING_MATERIAL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WindingMaterial")

    class _Cast_WindingMaterial:
        """Special nested class for casting WindingMaterial to subclasses."""

        def __init__(
            self: "WindingMaterial._Cast_WindingMaterial", parent: "WindingMaterial"
        ):
            self._parent = parent

        @property
        def material(self: "WindingMaterial._Cast_WindingMaterial") -> "_272.Material":
            return self._parent._cast(_272.Material)

        @property
        def named_database_item(
            self: "WindingMaterial._Cast_WindingMaterial",
        ) -> "_1836.NamedDatabaseItem":
            from mastapy.utility.databases import _1836

            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def winding_material(
            self: "WindingMaterial._Cast_WindingMaterial",
        ) -> "WindingMaterial":
            return self._parent

        def __getattr__(self: "WindingMaterial._Cast_WindingMaterial", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WindingMaterial.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def temperature_coefficient_for_winding_resistivity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TemperatureCoefficientForWindingResistivity

        if temp is None:
            return 0.0

        return temp

    @temperature_coefficient_for_winding_resistivity.setter
    @enforce_parameter_types
    def temperature_coefficient_for_winding_resistivity(self: Self, value: "float"):
        self.wrapped.TemperatureCoefficientForWindingResistivity = (
            float(value) if value is not None else 0.0
        )

    @property
    def winding_resistivity_at_20_degrees_c(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WindingResistivityAt20DegreesC

        if temp is None:
            return 0.0

        return temp

    @winding_resistivity_at_20_degrees_c.setter
    @enforce_parameter_types
    def winding_resistivity_at_20_degrees_c(self: Self, value: "float"):
        self.wrapped.WindingResistivityAt20DegreesC = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(self: Self) -> "WindingMaterial._Cast_WindingMaterial":
        return self._Cast_WindingMaterial(self)
