"""DutyCyclePropertySummaryVeryShortLength"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.property import _1844
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_PROPERTY_SUMMARY_VERY_SHORT_LENGTH = python_net_import(
    "SMT.MastaAPI.Utility.Property", "DutyCyclePropertySummaryVeryShortLength"
)


__docformat__ = "restructuredtext en"
__all__ = ("DutyCyclePropertySummaryVeryShortLength",)


Self = TypeVar("Self", bound="DutyCyclePropertySummaryVeryShortLength")
T = TypeVar("T")


class DutyCyclePropertySummaryVeryShortLength(
    _1844.DutyCyclePropertySummary["_1721.Stress", T]
):
    """DutyCyclePropertySummaryVeryShortLength

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _DUTY_CYCLE_PROPERTY_SUMMARY_VERY_SHORT_LENGTH
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_DutyCyclePropertySummaryVeryShortLength"
    )

    class _Cast_DutyCyclePropertySummaryVeryShortLength:
        """Special nested class for casting DutyCyclePropertySummaryVeryShortLength to subclasses."""

        def __init__(
            self: "DutyCyclePropertySummaryVeryShortLength._Cast_DutyCyclePropertySummaryVeryShortLength",
            parent: "DutyCyclePropertySummaryVeryShortLength",
        ):
            self._parent = parent

        @property
        def duty_cycle_property_summary(
            self: "DutyCyclePropertySummaryVeryShortLength._Cast_DutyCyclePropertySummaryVeryShortLength",
        ) -> "_1844.DutyCyclePropertySummary":
            return self._parent._cast(_1844.DutyCyclePropertySummary)

        @property
        def duty_cycle_property_summary_very_short_length(
            self: "DutyCyclePropertySummaryVeryShortLength._Cast_DutyCyclePropertySummaryVeryShortLength",
        ) -> "DutyCyclePropertySummaryVeryShortLength":
            return self._parent

        def __getattr__(
            self: "DutyCyclePropertySummaryVeryShortLength._Cast_DutyCyclePropertySummaryVeryShortLength",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "DutyCyclePropertySummaryVeryShortLength.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_value(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageValue

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_value(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumValue

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_value(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumValue

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "DutyCyclePropertySummaryVeryShortLength._Cast_DutyCyclePropertySummaryVeryShortLength":
        return self._Cast_DutyCyclePropertySummaryVeryShortLength(self)
