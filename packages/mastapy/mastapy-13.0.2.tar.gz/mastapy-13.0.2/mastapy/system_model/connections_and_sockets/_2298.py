"""RealignmentResult"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_REALIGNMENT_RESULT = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "RealignmentResult"
)


__docformat__ = "restructuredtext en"
__all__ = ("RealignmentResult",)


Self = TypeVar("Self", bound="RealignmentResult")


class RealignmentResult(_0.APIBase):
    """RealignmentResult

    This is a mastapy class.
    """

    TYPE = _REALIGNMENT_RESULT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RealignmentResult")

    class _Cast_RealignmentResult:
        """Special nested class for casting RealignmentResult to subclasses."""

        def __init__(
            self: "RealignmentResult._Cast_RealignmentResult",
            parent: "RealignmentResult",
        ):
            self._parent = parent

        @property
        def realignment_result(
            self: "RealignmentResult._Cast_RealignmentResult",
        ) -> "RealignmentResult":
            return self._parent

        def __getattr__(self: "RealignmentResult._Cast_RealignmentResult", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RealignmentResult.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def successful(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.Successful

        if temp is None:
            return False

        return temp

    @successful.setter
    @enforce_parameter_types
    def successful(self: Self, value: "bool"):
        self.wrapped.Successful = bool(value) if value is not None else False

    @property
    def cast_to(self: Self) -> "RealignmentResult._Cast_RealignmentResult":
        return self._Cast_RealignmentResult(self)
