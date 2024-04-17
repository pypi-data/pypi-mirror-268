"""ShaftFromCAD"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.part_model.import_from_cad import _2500
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_FROM_CAD = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD", "ShaftFromCAD"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.import_from_cad import _2502


__docformat__ = "restructuredtext en"
__all__ = ("ShaftFromCAD",)


Self = TypeVar("Self", bound="ShaftFromCAD")


class ShaftFromCAD(_2500.AbstractShaftFromCAD):
    """ShaftFromCAD

    This is a mastapy class.
    """

    TYPE = _SHAFT_FROM_CAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftFromCAD")

    class _Cast_ShaftFromCAD:
        """Special nested class for casting ShaftFromCAD to subclasses."""

        def __init__(self: "ShaftFromCAD._Cast_ShaftFromCAD", parent: "ShaftFromCAD"):
            self._parent = parent

        @property
        def abstract_shaft_from_cad(
            self: "ShaftFromCAD._Cast_ShaftFromCAD",
        ) -> "_2500.AbstractShaftFromCAD":
            return self._parent._cast(_2500.AbstractShaftFromCAD)

        @property
        def component_from_cad(
            self: "ShaftFromCAD._Cast_ShaftFromCAD",
        ) -> "_2502.ComponentFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2502

            return self._parent._cast(_2502.ComponentFromCAD)

        @property
        def shaft_from_cad(self: "ShaftFromCAD._Cast_ShaftFromCAD") -> "ShaftFromCAD":
            return self._parent

        def __getattr__(self: "ShaftFromCAD._Cast_ShaftFromCAD", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftFromCAD.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def create_assembly(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CreateAssembly

        if temp is None:
            return False

        return temp

    @create_assembly.setter
    @enforce_parameter_types
    def create_assembly(self: Self, value: "bool"):
        self.wrapped.CreateAssembly = bool(value) if value is not None else False

    @property
    def cast_to(self: Self) -> "ShaftFromCAD._Cast_ShaftFromCAD":
        return self._Cast_ShaftFromCAD(self)
