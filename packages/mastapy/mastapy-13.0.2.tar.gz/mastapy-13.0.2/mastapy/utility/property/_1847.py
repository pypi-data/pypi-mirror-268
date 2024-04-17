"""DutyCyclePropertySummarySmallAngle"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.property import _1844
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_PROPERTY_SUMMARY_SMALL_ANGLE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "DutyCyclePropertySummarySmallAngle"
)


__docformat__ = "restructuredtext en"
__all__ = ("DutyCyclePropertySummarySmallAngle",)


Self = TypeVar("Self", bound="DutyCyclePropertySummarySmallAngle")
T = TypeVar("T")


class DutyCyclePropertySummarySmallAngle(
    _1844.DutyCyclePropertySummary["_1622.AngleSmall", T]
):
    """DutyCyclePropertySummarySmallAngle

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _DUTY_CYCLE_PROPERTY_SUMMARY_SMALL_ANGLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DutyCyclePropertySummarySmallAngle")

    class _Cast_DutyCyclePropertySummarySmallAngle:
        """Special nested class for casting DutyCyclePropertySummarySmallAngle to subclasses."""

        def __init__(
            self: "DutyCyclePropertySummarySmallAngle._Cast_DutyCyclePropertySummarySmallAngle",
            parent: "DutyCyclePropertySummarySmallAngle",
        ):
            self._parent = parent

        @property
        def duty_cycle_property_summary(
            self: "DutyCyclePropertySummarySmallAngle._Cast_DutyCyclePropertySummarySmallAngle",
        ) -> "_1844.DutyCyclePropertySummary":
            return self._parent._cast(_1844.DutyCyclePropertySummary)

        @property
        def duty_cycle_property_summary_small_angle(
            self: "DutyCyclePropertySummarySmallAngle._Cast_DutyCyclePropertySummarySmallAngle",
        ) -> "DutyCyclePropertySummarySmallAngle":
            return self._parent

        def __getattr__(
            self: "DutyCyclePropertySummarySmallAngle._Cast_DutyCyclePropertySummarySmallAngle",
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
        self: Self, instance_to_wrap: "DutyCyclePropertySummarySmallAngle.TYPE"
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
    def maximum_absolute_value(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumAbsoluteValue

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
    ) -> "DutyCyclePropertySummarySmallAngle._Cast_DutyCyclePropertySummarySmallAngle":
        return self._Cast_DutyCyclePropertySummarySmallAngle(self)
