"""ClutchFromCAD"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.part_model.import_from_cad import _2511
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_FROM_CAD = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD", "ClutchFromCAD"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.import_from_cad import _2502


__docformat__ = "restructuredtext en"
__all__ = ("ClutchFromCAD",)


Self = TypeVar("Self", bound="ClutchFromCAD")


class ClutchFromCAD(_2511.MountableComponentFromCAD):
    """ClutchFromCAD

    This is a mastapy class.
    """

    TYPE = _CLUTCH_FROM_CAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchFromCAD")

    class _Cast_ClutchFromCAD:
        """Special nested class for casting ClutchFromCAD to subclasses."""

        def __init__(
            self: "ClutchFromCAD._Cast_ClutchFromCAD", parent: "ClutchFromCAD"
        ):
            self._parent = parent

        @property
        def mountable_component_from_cad(
            self: "ClutchFromCAD._Cast_ClutchFromCAD",
        ) -> "_2511.MountableComponentFromCAD":
            return self._parent._cast(_2511.MountableComponentFromCAD)

        @property
        def component_from_cad(
            self: "ClutchFromCAD._Cast_ClutchFromCAD",
        ) -> "_2502.ComponentFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2502

            return self._parent._cast(_2502.ComponentFromCAD)

        @property
        def clutch_from_cad(
            self: "ClutchFromCAD._Cast_ClutchFromCAD",
        ) -> "ClutchFromCAD":
            return self._parent

        def __getattr__(self: "ClutchFromCAD._Cast_ClutchFromCAD", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchFromCAD.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def clutch_name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.ClutchName

        if temp is None:
            return ""

        return temp

    @clutch_name.setter
    @enforce_parameter_types
    def clutch_name(self: Self, value: "str"):
        self.wrapped.ClutchName = str(value) if value is not None else ""

    @property
    def length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    @enforce_parameter_types
    def length(self: Self, value: "float"):
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "ClutchFromCAD._Cast_ClutchFromCAD":
        return self._Cast_ClutchFromCAD(self)
