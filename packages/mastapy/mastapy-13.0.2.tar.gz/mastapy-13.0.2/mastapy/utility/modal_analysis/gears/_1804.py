"""GearMeshForTE"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy.utility.modal_analysis.gears import _1809
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_FOR_TE = python_net_import(
    "SMT.MastaAPI.Utility.ModalAnalysis.Gears", "GearMeshForTE"
)

if TYPE_CHECKING:
    from mastapy.utility.modal_analysis.gears import _1805


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshForTE",)


Self = TypeVar("Self", bound="GearMeshForTE")


class GearMeshForTE(_1809.OrderForTE):
    """GearMeshForTE

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_FOR_TE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshForTE")

    class _Cast_GearMeshForTE:
        """Special nested class for casting GearMeshForTE to subclasses."""

        def __init__(
            self: "GearMeshForTE._Cast_GearMeshForTE", parent: "GearMeshForTE"
        ):
            self._parent = parent

        @property
        def order_for_te(
            self: "GearMeshForTE._Cast_GearMeshForTE",
        ) -> "_1809.OrderForTE":
            return self._parent._cast(_1809.OrderForTE)

        @property
        def gear_mesh_for_te(
            self: "GearMeshForTE._Cast_GearMeshForTE",
        ) -> "GearMeshForTE":
            return self._parent

        def __getattr__(self: "GearMeshForTE._Cast_GearMeshForTE", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshForTE.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_teeth(self: Self) -> "str":
        """str"""
        temp = self.wrapped.NumberOfTeeth

        if temp is None:
            return ""

        return temp

    @number_of_teeth.setter
    @enforce_parameter_types
    def number_of_teeth(self: Self, value: "str"):
        self.wrapped.NumberOfTeeth = str(value) if value is not None else ""

    @property
    def attached_gears(self: Self) -> "List[_1805.GearOrderForTE]":
        """List[mastapy.utility.modal_analysis.gears.GearOrderForTE]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AttachedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "GearMeshForTE._Cast_GearMeshForTE":
        return self._Cast_GearMeshForTE(self)
