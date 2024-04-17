"""DutyCyclePropertySummaryForce"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.property import _1844
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_PROPERTY_SUMMARY_FORCE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "DutyCyclePropertySummaryForce"
)


__docformat__ = "restructuredtext en"
__all__ = ("DutyCyclePropertySummaryForce",)


Self = TypeVar("Self", bound="DutyCyclePropertySummaryForce")
T = TypeVar("T")


class DutyCyclePropertySummaryForce(_1844.DutyCyclePropertySummary["_1649.Force", T]):
    """DutyCyclePropertySummaryForce

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _DUTY_CYCLE_PROPERTY_SUMMARY_FORCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DutyCyclePropertySummaryForce")

    class _Cast_DutyCyclePropertySummaryForce:
        """Special nested class for casting DutyCyclePropertySummaryForce to subclasses."""

        def __init__(
            self: "DutyCyclePropertySummaryForce._Cast_DutyCyclePropertySummaryForce",
            parent: "DutyCyclePropertySummaryForce",
        ):
            self._parent = parent

        @property
        def duty_cycle_property_summary(
            self: "DutyCyclePropertySummaryForce._Cast_DutyCyclePropertySummaryForce",
        ) -> "_1844.DutyCyclePropertySummary":
            return self._parent._cast(_1844.DutyCyclePropertySummary)

        @property
        def duty_cycle_property_summary_force(
            self: "DutyCyclePropertySummaryForce._Cast_DutyCyclePropertySummaryForce",
        ) -> "DutyCyclePropertySummaryForce":
            return self._parent

        def __getattr__(
            self: "DutyCyclePropertySummaryForce._Cast_DutyCyclePropertySummaryForce",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DutyCyclePropertySummaryForce.TYPE"):
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
    ) -> "DutyCyclePropertySummaryForce._Cast_DutyCyclePropertySummaryForce":
        return self._Cast_DutyCyclePropertySummaryForce(self)
