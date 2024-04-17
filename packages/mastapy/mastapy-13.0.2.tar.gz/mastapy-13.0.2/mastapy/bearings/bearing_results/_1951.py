"""ElementForce"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_FORCE = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "ElementForce"
)


__docformat__ = "restructuredtext en"
__all__ = ("ElementForce",)


Self = TypeVar("Self", bound="ElementForce")


class ElementForce(_0.APIBase):
    """ElementForce

    This is a mastapy class.
    """

    TYPE = _ELEMENT_FORCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElementForce")

    class _Cast_ElementForce:
        """Special nested class for casting ElementForce to subclasses."""

        def __init__(self: "ElementForce._Cast_ElementForce", parent: "ElementForce"):
            self._parent = parent

        @property
        def element_force(self: "ElementForce._Cast_ElementForce") -> "ElementForce":
            return self._parent

        def __getattr__(self: "ElementForce._Cast_ElementForce", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElementForce.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Axial

        if temp is None:
            return 0.0

        return temp

    @property
    def moment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Moment

        if temp is None:
            return 0.0

        return temp

    @property
    def radial(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Radial

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "ElementForce._Cast_ElementForce":
        return self._Cast_ElementForce(self)
