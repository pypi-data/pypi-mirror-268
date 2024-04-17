"""PlanetShaftFromCAD"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.part_model.import_from_cad import _2500
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_SHAFT_FROM_CAD = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD", "PlanetShaftFromCAD"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.import_from_cad import _2502


__docformat__ = "restructuredtext en"
__all__ = ("PlanetShaftFromCAD",)


Self = TypeVar("Self", bound="PlanetShaftFromCAD")


class PlanetShaftFromCAD(_2500.AbstractShaftFromCAD):
    """PlanetShaftFromCAD

    This is a mastapy class.
    """

    TYPE = _PLANET_SHAFT_FROM_CAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetShaftFromCAD")

    class _Cast_PlanetShaftFromCAD:
        """Special nested class for casting PlanetShaftFromCAD to subclasses."""

        def __init__(
            self: "PlanetShaftFromCAD._Cast_PlanetShaftFromCAD",
            parent: "PlanetShaftFromCAD",
        ):
            self._parent = parent

        @property
        def abstract_shaft_from_cad(
            self: "PlanetShaftFromCAD._Cast_PlanetShaftFromCAD",
        ) -> "_2500.AbstractShaftFromCAD":
            return self._parent._cast(_2500.AbstractShaftFromCAD)

        @property
        def component_from_cad(
            self: "PlanetShaftFromCAD._Cast_PlanetShaftFromCAD",
        ) -> "_2502.ComponentFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2502

            return self._parent._cast(_2502.ComponentFromCAD)

        @property
        def planet_shaft_from_cad(
            self: "PlanetShaftFromCAD._Cast_PlanetShaftFromCAD",
        ) -> "PlanetShaftFromCAD":
            return self._parent

        def __getattr__(self: "PlanetShaftFromCAD._Cast_PlanetShaftFromCAD", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetShaftFromCAD.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planet_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PlanetDiameter

        if temp is None:
            return 0.0

        return temp

    @planet_diameter.setter
    @enforce_parameter_types
    def planet_diameter(self: Self, value: "float"):
        self.wrapped.PlanetDiameter = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "PlanetShaftFromCAD._Cast_PlanetShaftFromCAD":
        return self._Cast_PlanetShaftFromCAD(self)
