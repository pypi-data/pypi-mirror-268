"""DutyCyclePropertySummaryStress"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.property import _1844
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_PROPERTY_SUMMARY_STRESS = python_net_import(
    "SMT.MastaAPI.Utility.Property", "DutyCyclePropertySummaryStress"
)


__docformat__ = "restructuredtext en"
__all__ = ("DutyCyclePropertySummaryStress",)


Self = TypeVar("Self", bound="DutyCyclePropertySummaryStress")
T = TypeVar("T")


class DutyCyclePropertySummaryStress(_1844.DutyCyclePropertySummary["_1721.Stress", T]):
    """DutyCyclePropertySummaryStress

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _DUTY_CYCLE_PROPERTY_SUMMARY_STRESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DutyCyclePropertySummaryStress")

    class _Cast_DutyCyclePropertySummaryStress:
        """Special nested class for casting DutyCyclePropertySummaryStress to subclasses."""

        def __init__(
            self: "DutyCyclePropertySummaryStress._Cast_DutyCyclePropertySummaryStress",
            parent: "DutyCyclePropertySummaryStress",
        ):
            self._parent = parent

        @property
        def duty_cycle_property_summary(
            self: "DutyCyclePropertySummaryStress._Cast_DutyCyclePropertySummaryStress",
        ) -> "_1844.DutyCyclePropertySummary":
            return self._parent._cast(_1844.DutyCyclePropertySummary)

        @property
        def duty_cycle_property_summary_stress(
            self: "DutyCyclePropertySummaryStress._Cast_DutyCyclePropertySummaryStress",
        ) -> "DutyCyclePropertySummaryStress":
            return self._parent

        def __getattr__(
            self: "DutyCyclePropertySummaryStress._Cast_DutyCyclePropertySummaryStress",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DutyCyclePropertySummaryStress.TYPE"):
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
    ) -> "DutyCyclePropertySummaryStress._Cast_DutyCyclePropertySummaryStress":
        return self._Cast_DutyCyclePropertySummaryStress(self)
