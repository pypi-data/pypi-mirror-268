"""MethodOutcomeWithResult"""

from __future__ import annotations

from typing import TypeVar, Generic

from mastapy._internal import constructor
from mastapy.utility import _1597
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_METHOD_OUTCOME_WITH_RESULT = python_net_import(
    "SMT.MastaAPI.Utility", "MethodOutcomeWithResult"
)


__docformat__ = "restructuredtext en"
__all__ = ("MethodOutcomeWithResult",)


Self = TypeVar("Self", bound="MethodOutcomeWithResult")
T = TypeVar("T")


class MethodOutcomeWithResult(_1597.MethodOutcome, Generic[T]):
    """MethodOutcomeWithResult

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _METHOD_OUTCOME_WITH_RESULT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MethodOutcomeWithResult")

    class _Cast_MethodOutcomeWithResult:
        """Special nested class for casting MethodOutcomeWithResult to subclasses."""

        def __init__(
            self: "MethodOutcomeWithResult._Cast_MethodOutcomeWithResult",
            parent: "MethodOutcomeWithResult",
        ):
            self._parent = parent

        @property
        def method_outcome(
            self: "MethodOutcomeWithResult._Cast_MethodOutcomeWithResult",
        ) -> "_1597.MethodOutcome":
            return self._parent._cast(_1597.MethodOutcome)

        @property
        def method_outcome_with_result(
            self: "MethodOutcomeWithResult._Cast_MethodOutcomeWithResult",
        ) -> "MethodOutcomeWithResult":
            return self._parent

        def __getattr__(
            self: "MethodOutcomeWithResult._Cast_MethodOutcomeWithResult", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MethodOutcomeWithResult.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def result(self: Self) -> "T":
        """T

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Result

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "MethodOutcomeWithResult._Cast_MethodOutcomeWithResult":
        return self._Cast_MethodOutcomeWithResult(self)
