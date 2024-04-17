"""DutyCyclePropertySummary"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_PROPERTY_SUMMARY = python_net_import(
    "SMT.MastaAPI.Utility.Property", "DutyCyclePropertySummary"
)

if TYPE_CHECKING:
    from mastapy.utility.units_and_measurements import _1612
    from mastapy.utility.property import _1845, _1846, _1847, _1848, _1849


__docformat__ = "restructuredtext en"
__all__ = ("DutyCyclePropertySummary",)


Self = TypeVar("Self", bound="DutyCyclePropertySummary")
TMeasurement = TypeVar("TMeasurement", bound="_1612.MeasurementBase")
T = TypeVar("T")


class DutyCyclePropertySummary(_0.APIBase, Generic[TMeasurement, T]):
    """DutyCyclePropertySummary

    This is a mastapy class.

    Generic Types:
        TMeasurement
        T
    """

    TYPE = _DUTY_CYCLE_PROPERTY_SUMMARY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DutyCyclePropertySummary")

    class _Cast_DutyCyclePropertySummary:
        """Special nested class for casting DutyCyclePropertySummary to subclasses."""

        def __init__(
            self: "DutyCyclePropertySummary._Cast_DutyCyclePropertySummary",
            parent: "DutyCyclePropertySummary",
        ):
            self._parent = parent

        @property
        def duty_cycle_property_summary_force(
            self: "DutyCyclePropertySummary._Cast_DutyCyclePropertySummary",
        ) -> "_1845.DutyCyclePropertySummaryForce":
            from mastapy.utility.property import _1845

            return self._parent._cast(_1845.DutyCyclePropertySummaryForce)

        @property
        def duty_cycle_property_summary_percentage(
            self: "DutyCyclePropertySummary._Cast_DutyCyclePropertySummary",
        ) -> "_1846.DutyCyclePropertySummaryPercentage":
            from mastapy.utility.property import _1846

            return self._parent._cast(_1846.DutyCyclePropertySummaryPercentage)

        @property
        def duty_cycle_property_summary_small_angle(
            self: "DutyCyclePropertySummary._Cast_DutyCyclePropertySummary",
        ) -> "_1847.DutyCyclePropertySummarySmallAngle":
            from mastapy.utility.property import _1847

            return self._parent._cast(_1847.DutyCyclePropertySummarySmallAngle)

        @property
        def duty_cycle_property_summary_stress(
            self: "DutyCyclePropertySummary._Cast_DutyCyclePropertySummary",
        ) -> "_1848.DutyCyclePropertySummaryStress":
            from mastapy.utility.property import _1848

            return self._parent._cast(_1848.DutyCyclePropertySummaryStress)

        @property
        def duty_cycle_property_summary_very_short_length(
            self: "DutyCyclePropertySummary._Cast_DutyCyclePropertySummary",
        ) -> "_1849.DutyCyclePropertySummaryVeryShortLength":
            from mastapy.utility.property import _1849

            return self._parent._cast(_1849.DutyCyclePropertySummaryVeryShortLength)

        @property
        def duty_cycle_property_summary(
            self: "DutyCyclePropertySummary._Cast_DutyCyclePropertySummary",
        ) -> "DutyCyclePropertySummary":
            return self._parent

        def __getattr__(
            self: "DutyCyclePropertySummary._Cast_DutyCyclePropertySummary", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DutyCyclePropertySummary.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_absolute_value_load_case(self: Self) -> "T":
        """T

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumAbsoluteValueLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def maximum_value_load_case(self: Self) -> "T":
        """T

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumValueLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def minimum_value_load_case(self: Self) -> "T":
        """T

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumValueLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "DutyCyclePropertySummary._Cast_DutyCyclePropertySummary":
        return self._Cast_DutyCyclePropertySummary(self)
