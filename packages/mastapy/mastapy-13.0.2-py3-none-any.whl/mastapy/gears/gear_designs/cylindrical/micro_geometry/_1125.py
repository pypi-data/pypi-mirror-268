"""MeshAlignment"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MESH_ALIGNMENT = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry", "MeshAlignment"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1119


__docformat__ = "restructuredtext en"
__all__ = ("MeshAlignment",)


Self = TypeVar("Self", bound="MeshAlignment")


class MeshAlignment(_0.APIBase):
    """MeshAlignment

    This is a mastapy class.
    """

    TYPE = _MESH_ALIGNMENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MeshAlignment")

    class _Cast_MeshAlignment:
        """Special nested class for casting MeshAlignment to subclasses."""

        def __init__(
            self: "MeshAlignment._Cast_MeshAlignment", parent: "MeshAlignment"
        ):
            self._parent = parent

        @property
        def mesh_alignment(
            self: "MeshAlignment._Cast_MeshAlignment",
        ) -> "MeshAlignment":
            return self._parent

        def __getattr__(self: "MeshAlignment._Cast_MeshAlignment", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MeshAlignment.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_a_alignment(self: Self) -> "_1119.GearAlignment":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.GearAlignment

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearAAlignment

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b_alignment(self: Self) -> "_1119.GearAlignment":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.GearAlignment

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBAlignment

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "MeshAlignment._Cast_MeshAlignment":
        return self._Cast_MeshAlignment(self)
