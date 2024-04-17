"""CustomRow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.report import _1780
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_ROW = python_net_import("SMT.MastaAPI.Utility.Report", "CustomRow")

if TYPE_CHECKING:
    from mastapy.utility.report import _1751, _1794


__docformat__ = "restructuredtext en"
__all__ = ("CustomRow",)


Self = TypeVar("Self", bound="CustomRow")


class CustomRow(_1780.CustomReportPropertyItem):
    """CustomRow

    This is a mastapy class.
    """

    TYPE = _CUSTOM_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomRow")

    class _Cast_CustomRow:
        """Special nested class for casting CustomRow to subclasses."""

        def __init__(self: "CustomRow._Cast_CustomRow", parent: "CustomRow"):
            self._parent = parent

        @property
        def custom_report_property_item(
            self: "CustomRow._Cast_CustomRow",
        ) -> "_1780.CustomReportPropertyItem":
            return self._parent._cast(_1780.CustomReportPropertyItem)

        @property
        def blank_row(self: "CustomRow._Cast_CustomRow") -> "_1751.BlankRow":
            from mastapy.utility.report import _1751

            return self._parent._cast(_1751.BlankRow)

        @property
        def user_text_row(self: "CustomRow._Cast_CustomRow") -> "_1794.UserTextRow":
            from mastapy.utility.report import _1794

            return self._parent._cast(_1794.UserTextRow)

        @property
        def custom_row(self: "CustomRow._Cast_CustomRow") -> "CustomRow":
            return self._parent

        def __getattr__(self: "CustomRow._Cast_CustomRow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomRow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def calculate_sum_of_values(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CalculateSumOfValues

        if temp is None:
            return False

        return temp

    @calculate_sum_of_values.setter
    @enforce_parameter_types
    def calculate_sum_of_values(self: Self, value: "bool"):
        self.wrapped.CalculateSumOfValues = bool(value) if value is not None else False

    @property
    def count_values(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CountValues

        if temp is None:
            return False

        return temp

    @count_values.setter
    @enforce_parameter_types
    def count_values(self: Self, value: "bool"):
        self.wrapped.CountValues = bool(value) if value is not None else False

    @property
    def is_minor_value(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsMinorValue

        if temp is None:
            return False

        return temp

    @is_minor_value.setter
    @enforce_parameter_types
    def is_minor_value(self: Self, value: "bool"):
        self.wrapped.IsMinorValue = bool(value) if value is not None else False

    @property
    def overridden_property_name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.OverriddenPropertyName

        if temp is None:
            return ""

        return temp

    @overridden_property_name.setter
    @enforce_parameter_types
    def overridden_property_name(self: Self, value: "str"):
        self.wrapped.OverriddenPropertyName = str(value) if value is not None else ""

    @property
    def override_property_name(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OverridePropertyName

        if temp is None:
            return False

        return temp

    @override_property_name.setter
    @enforce_parameter_types
    def override_property_name(self: Self, value: "bool"):
        self.wrapped.OverridePropertyName = bool(value) if value is not None else False

    @property
    def show_maximum_of_absolute_values(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowMaximumOfAbsoluteValues

        if temp is None:
            return False

        return temp

    @show_maximum_of_absolute_values.setter
    @enforce_parameter_types
    def show_maximum_of_absolute_values(self: Self, value: "bool"):
        self.wrapped.ShowMaximumOfAbsoluteValues = (
            bool(value) if value is not None else False
        )

    @property
    def show_maximum_of_values(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowMaximumOfValues

        if temp is None:
            return False

        return temp

    @show_maximum_of_values.setter
    @enforce_parameter_types
    def show_maximum_of_values(self: Self, value: "bool"):
        self.wrapped.ShowMaximumOfValues = bool(value) if value is not None else False

    @property
    def show_minimum_of_values(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowMinimumOfValues

        if temp is None:
            return False

        return temp

    @show_minimum_of_values.setter
    @enforce_parameter_types
    def show_minimum_of_values(self: Self, value: "bool"):
        self.wrapped.ShowMinimumOfValues = bool(value) if value is not None else False

    @property
    def cast_to(self: Self) -> "CustomRow._Cast_CustomRow":
        return self._Cast_CustomRow(self)
