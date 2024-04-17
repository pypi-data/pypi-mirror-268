"""NumberFormatInfoSummary"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NUMBER_FORMAT_INFO_SUMMARY = python_net_import(
    "SMT.MastaAPI.Utility", "NumberFormatInfoSummary"
)


__docformat__ = "restructuredtext en"
__all__ = ("NumberFormatInfoSummary",)


Self = TypeVar("Self", bound="NumberFormatInfoSummary")


class NumberFormatInfoSummary(_0.APIBase):
    """NumberFormatInfoSummary

    This is a mastapy class.
    """

    TYPE = _NUMBER_FORMAT_INFO_SUMMARY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NumberFormatInfoSummary")

    class _Cast_NumberFormatInfoSummary:
        """Special nested class for casting NumberFormatInfoSummary to subclasses."""

        def __init__(
            self: "NumberFormatInfoSummary._Cast_NumberFormatInfoSummary",
            parent: "NumberFormatInfoSummary",
        ):
            self._parent = parent

        @property
        def number_format_info_summary(
            self: "NumberFormatInfoSummary._Cast_NumberFormatInfoSummary",
        ) -> "NumberFormatInfoSummary":
            return self._parent

        def __getattr__(
            self: "NumberFormatInfoSummary._Cast_NumberFormatInfoSummary", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NumberFormatInfoSummary.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def decimal_symbol(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DecimalSymbol

        if temp is None:
            return ""

        return temp

    @property
    def native_digits(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NativeDigits

        if temp is None:
            return ""

        return temp

    @property
    def negative_pattern(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NegativePattern

        if temp is None:
            return ""

        return temp

    @property
    def negative_symbol(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NegativeSymbol

        if temp is None:
            return ""

        return temp

    @property
    def sample_negative_number(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SampleNegativeNumber

        if temp is None:
            return ""

        return temp

    @property
    def sample_positive_number(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SamplePositiveNumber

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(self: Self) -> "NumberFormatInfoSummary._Cast_NumberFormatInfoSummary":
        return self._Cast_NumberFormatInfoSummary(self)
