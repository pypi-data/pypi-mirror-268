"""Eigenmodes"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EIGENMODES = python_net_import("SMT.MastaAPI.MathUtility", "Eigenmodes")

if TYPE_CHECKING:
    from mastapy.math_utility import _1514


__docformat__ = "restructuredtext en"
__all__ = ("Eigenmodes",)


Self = TypeVar("Self", bound="Eigenmodes")


class Eigenmodes(_0.APIBase):
    """Eigenmodes

    This is a mastapy class.
    """

    TYPE = _EIGENMODES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Eigenmodes")

    class _Cast_Eigenmodes:
        """Special nested class for casting Eigenmodes to subclasses."""

        def __init__(self: "Eigenmodes._Cast_Eigenmodes", parent: "Eigenmodes"):
            self._parent = parent

        @property
        def eigenmodes(self: "Eigenmodes._Cast_Eigenmodes") -> "Eigenmodes":
            return self._parent

        def __getattr__(self: "Eigenmodes._Cast_Eigenmodes", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Eigenmodes.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def items(self: Self) -> "List[_1514.Eigenmode]":
        """List[mastapy.math_utility.Eigenmode]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Items

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "Eigenmodes._Cast_Eigenmodes":
        return self._Cast_Eigenmodes(self)
