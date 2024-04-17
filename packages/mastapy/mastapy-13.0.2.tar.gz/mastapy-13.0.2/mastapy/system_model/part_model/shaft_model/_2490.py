"""ShaftBow"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_BOW = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.ShaftModel", "ShaftBow"
)


__docformat__ = "restructuredtext en"
__all__ = ("ShaftBow",)


Self = TypeVar("Self", bound="ShaftBow")


class ShaftBow(_0.APIBase):
    """ShaftBow

    This is a mastapy class.
    """

    TYPE = _SHAFT_BOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftBow")

    class _Cast_ShaftBow:
        """Special nested class for casting ShaftBow to subclasses."""

        def __init__(self: "ShaftBow._Cast_ShaftBow", parent: "ShaftBow"):
            self._parent = parent

        @property
        def shaft_bow(self: "ShaftBow._Cast_ShaftBow") -> "ShaftBow":
            return self._parent

        def __getattr__(self: "ShaftBow._Cast_ShaftBow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftBow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def linear_displacement(self: Self) -> "List[Vector3D]":
        """List[Vector3D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ShaftBow._Cast_ShaftBow":
        return self._Cast_ShaftBow(self)
