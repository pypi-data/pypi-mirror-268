"""MutableFillet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.manufacturing.cylindrical.cutters import _722
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MUTABLE_FILLET = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters", "MutableFillet"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters import _706


__docformat__ = "restructuredtext en"
__all__ = ("MutableFillet",)


Self = TypeVar("Self", bound="MutableFillet")


class MutableFillet(_722.MutableCommon):
    """MutableFillet

    This is a mastapy class.
    """

    TYPE = _MUTABLE_FILLET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MutableFillet")

    class _Cast_MutableFillet:
        """Special nested class for casting MutableFillet to subclasses."""

        def __init__(
            self: "MutableFillet._Cast_MutableFillet", parent: "MutableFillet"
        ):
            self._parent = parent

        @property
        def mutable_common(
            self: "MutableFillet._Cast_MutableFillet",
        ) -> "_722.MutableCommon":
            return self._parent._cast(_722.MutableCommon)

        @property
        def curve_in_linked_list(
            self: "MutableFillet._Cast_MutableFillet",
        ) -> "_706.CurveInLinkedList":
            from mastapy.gears.manufacturing.cylindrical.cutters import _706

            return self._parent._cast(_706.CurveInLinkedList)

        @property
        def mutable_fillet(
            self: "MutableFillet._Cast_MutableFillet",
        ) -> "MutableFillet":
            return self._parent

        def __getattr__(self: "MutableFillet._Cast_MutableFillet", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MutableFillet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @radius.setter
    @enforce_parameter_types
    def radius(self: Self, value: "float"):
        self.wrapped.Radius = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "MutableFillet._Cast_MutableFillet":
        return self._Cast_MutableFillet(self)
