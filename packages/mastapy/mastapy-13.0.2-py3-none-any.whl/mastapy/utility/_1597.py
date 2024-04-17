"""MethodOutcome"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_METHOD_OUTCOME = python_net_import("SMT.MastaAPI.Utility", "MethodOutcome")

if TYPE_CHECKING:
    from mastapy.utility import _1598


__docformat__ = "restructuredtext en"
__all__ = ("MethodOutcome",)


Self = TypeVar("Self", bound="MethodOutcome")


class MethodOutcome(_0.APIBase):
    """MethodOutcome

    This is a mastapy class.
    """

    TYPE = _METHOD_OUTCOME
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MethodOutcome")

    class _Cast_MethodOutcome:
        """Special nested class for casting MethodOutcome to subclasses."""

        def __init__(
            self: "MethodOutcome._Cast_MethodOutcome", parent: "MethodOutcome"
        ):
            self._parent = parent

        @property
        def method_outcome_with_result(
            self: "MethodOutcome._Cast_MethodOutcome",
        ) -> "_1598.MethodOutcomeWithResult":
            from mastapy.utility import _1598

            return self._parent._cast(_1598.MethodOutcomeWithResult)

        @property
        def method_outcome(
            self: "MethodOutcome._Cast_MethodOutcome",
        ) -> "MethodOutcome":
            return self._parent

        def __getattr__(self: "MethodOutcome._Cast_MethodOutcome", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MethodOutcome.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def failure_message(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FailureMessage

        if temp is None:
            return ""

        return temp

    @property
    def successful(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Successful

        if temp is None:
            return False

        return temp

    @property
    def cast_to(self: Self) -> "MethodOutcome._Cast_MethodOutcome":
        return self._Cast_MethodOutcome(self)
