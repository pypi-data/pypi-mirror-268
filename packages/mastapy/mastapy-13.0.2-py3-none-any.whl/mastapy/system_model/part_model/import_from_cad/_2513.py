"""PulleyFromCAD"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.part_model.import_from_cad import _2511
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_FROM_CAD = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD", "PulleyFromCAD"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.import_from_cad import _2502


__docformat__ = "restructuredtext en"
__all__ = ("PulleyFromCAD",)


Self = TypeVar("Self", bound="PulleyFromCAD")


class PulleyFromCAD(_2511.MountableComponentFromCAD):
    """PulleyFromCAD

    This is a mastapy class.
    """

    TYPE = _PULLEY_FROM_CAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PulleyFromCAD")

    class _Cast_PulleyFromCAD:
        """Special nested class for casting PulleyFromCAD to subclasses."""

        def __init__(
            self: "PulleyFromCAD._Cast_PulleyFromCAD", parent: "PulleyFromCAD"
        ):
            self._parent = parent

        @property
        def mountable_component_from_cad(
            self: "PulleyFromCAD._Cast_PulleyFromCAD",
        ) -> "_2511.MountableComponentFromCAD":
            return self._parent._cast(_2511.MountableComponentFromCAD)

        @property
        def component_from_cad(
            self: "PulleyFromCAD._Cast_PulleyFromCAD",
        ) -> "_2502.ComponentFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2502

            return self._parent._cast(_2502.ComponentFromCAD)

        @property
        def pulley_from_cad(
            self: "PulleyFromCAD._Cast_PulleyFromCAD",
        ) -> "PulleyFromCAD":
            return self._parent

        def __getattr__(self: "PulleyFromCAD._Cast_PulleyFromCAD", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PulleyFromCAD.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def centre_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CentreDistance

        if temp is None:
            return 0.0

        return temp

    @centre_distance.setter
    @enforce_parameter_types
    def centre_distance(self: Self, value: "float"):
        self.wrapped.CentreDistance = float(value) if value is not None else 0.0

    @property
    def outer_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return temp

    @outer_diameter.setter
    @enforce_parameter_types
    def outer_diameter(self: Self, value: "float"):
        self.wrapped.OuterDiameter = float(value) if value is not None else 0.0

    @property
    def width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: Self, value: "float"):
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "PulleyFromCAD._Cast_PulleyFromCAD":
        return self._Cast_PulleyFromCAD(self)
