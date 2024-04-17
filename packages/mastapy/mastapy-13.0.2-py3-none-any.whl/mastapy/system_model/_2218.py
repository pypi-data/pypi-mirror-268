"""IncludeDutyCycleOption"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INCLUDE_DUTY_CYCLE_OPTION = python_net_import(
    "SMT.MastaAPI.SystemModel", "IncludeDutyCycleOption"
)


__docformat__ = "restructuredtext en"
__all__ = ("IncludeDutyCycleOption",)


Self = TypeVar("Self", bound="IncludeDutyCycleOption")


class IncludeDutyCycleOption(_0.APIBase):
    """IncludeDutyCycleOption

    This is a mastapy class.
    """

    TYPE = _INCLUDE_DUTY_CYCLE_OPTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_IncludeDutyCycleOption")

    class _Cast_IncludeDutyCycleOption:
        """Special nested class for casting IncludeDutyCycleOption to subclasses."""

        def __init__(
            self: "IncludeDutyCycleOption._Cast_IncludeDutyCycleOption",
            parent: "IncludeDutyCycleOption",
        ):
            self._parent = parent

        @property
        def include_duty_cycle_option(
            self: "IncludeDutyCycleOption._Cast_IncludeDutyCycleOption",
        ) -> "IncludeDutyCycleOption":
            return self._parent

        def __getattr__(
            self: "IncludeDutyCycleOption._Cast_IncludeDutyCycleOption", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "IncludeDutyCycleOption.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def import_(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.Import

        if temp is None:
            return False

        return temp

    @import_.setter
    @enforce_parameter_types
    def import_(self: Self, value: "bool"):
        self.wrapped.Import = bool(value) if value is not None else False

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(self: Self) -> "IncludeDutyCycleOption._Cast_IncludeDutyCycleOption":
        return self._Cast_IncludeDutyCycleOption(self)
