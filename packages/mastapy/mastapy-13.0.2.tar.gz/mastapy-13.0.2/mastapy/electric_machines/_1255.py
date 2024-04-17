"""CADMagnetsForLayer"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy.electric_machines import _1287
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CAD_MAGNETS_FOR_LAYER = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "CADMagnetsForLayer"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1254


__docformat__ = "restructuredtext en"
__all__ = ("CADMagnetsForLayer",)


Self = TypeVar("Self", bound="CADMagnetsForLayer")


class CADMagnetsForLayer(_1287.MagnetDesign):
    """CADMagnetsForLayer

    This is a mastapy class.
    """

    TYPE = _CAD_MAGNETS_FOR_LAYER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CADMagnetsForLayer")

    class _Cast_CADMagnetsForLayer:
        """Special nested class for casting CADMagnetsForLayer to subclasses."""

        def __init__(
            self: "CADMagnetsForLayer._Cast_CADMagnetsForLayer",
            parent: "CADMagnetsForLayer",
        ):
            self._parent = parent

        @property
        def magnet_design(
            self: "CADMagnetsForLayer._Cast_CADMagnetsForLayer",
        ) -> "_1287.MagnetDesign":
            return self._parent._cast(_1287.MagnetDesign)

        @property
        def cad_magnets_for_layer(
            self: "CADMagnetsForLayer._Cast_CADMagnetsForLayer",
        ) -> "CADMagnetsForLayer":
            return self._parent

        def __getattr__(self: "CADMagnetsForLayer._Cast_CADMagnetsForLayer", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CADMagnetsForLayer.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def override_magnetisation_directions(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OverrideMagnetisationDirections

        if temp is None:
            return False

        return temp

    @override_magnetisation_directions.setter
    @enforce_parameter_types
    def override_magnetisation_directions(self: Self, value: "bool"):
        self.wrapped.OverrideMagnetisationDirections = (
            bool(value) if value is not None else False
        )

    @property
    def cad_magnet_details(self: Self) -> "List[_1254.CADMagnetDetails]":
        """List[mastapy.electric_machines.CADMagnetDetails]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CADMagnetDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "CADMagnetsForLayer._Cast_CADMagnetsForLayer":
        return self._Cast_CADMagnetsForLayer(self)
