"""MeasurementSettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item, overridable
from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.utility import _1601
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_SETTINGS = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements", "MeasurementSettings"
)

if TYPE_CHECKING:
    from mastapy.units_and_measurements import _7568
    from mastapy.utility import _1602


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementSettings",)


Self = TypeVar("Self", bound="MeasurementSettings")


class MeasurementSettings(_1601.PerMachineSettings):
    """MeasurementSettings

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MeasurementSettings")

    class _Cast_MeasurementSettings:
        """Special nested class for casting MeasurementSettings to subclasses."""

        def __init__(
            self: "MeasurementSettings._Cast_MeasurementSettings",
            parent: "MeasurementSettings",
        ):
            self._parent = parent

        @property
        def per_machine_settings(
            self: "MeasurementSettings._Cast_MeasurementSettings",
        ) -> "_1601.PerMachineSettings":
            return self._parent._cast(_1601.PerMachineSettings)

        @property
        def persistent_singleton(
            self: "MeasurementSettings._Cast_MeasurementSettings",
        ) -> "_1602.PersistentSingleton":
            from mastapy.utility import _1602

            return self._parent._cast(_1602.PersistentSingleton)

        @property
        def measurement_settings(
            self: "MeasurementSettings._Cast_MeasurementSettings",
        ) -> "MeasurementSettings":
            return self._parent

        def __getattr__(
            self: "MeasurementSettings._Cast_MeasurementSettings", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MeasurementSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def large_number_cutoff(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LargeNumberCutoff

        if temp is None:
            return 0.0

        return temp

    @large_number_cutoff.setter
    @enforce_parameter_types
    def large_number_cutoff(self: Self, value: "float"):
        self.wrapped.LargeNumberCutoff = float(value) if value is not None else 0.0

    @property
    def number_decimal_separator(self: Self) -> "str":
        """str"""
        temp = self.wrapped.NumberDecimalSeparator

        if temp is None:
            return ""

        return temp

    @number_decimal_separator.setter
    @enforce_parameter_types
    def number_decimal_separator(self: Self, value: "str"):
        self.wrapped.NumberDecimalSeparator = str(value) if value is not None else ""

    @property
    def number_group_separator(self: Self) -> "str":
        """str"""
        temp = self.wrapped.NumberGroupSeparator

        if temp is None:
            return ""

        return temp

    @number_group_separator.setter
    @enforce_parameter_types
    def number_group_separator(self: Self, value: "str"):
        self.wrapped.NumberGroupSeparator = str(value) if value is not None else ""

    @property
    def sample_input(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SampleInput

        if temp is None:
            return ""

        return temp

    @property
    def sample_output(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SampleOutput

        if temp is None:
            return ""

        return temp

    @property
    def selected_measurement(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_MeasurementBase":
        """ListWithSelectedItem[mastapy.utility.units_and_measurements.MeasurementBase]"""
        temp = self.wrapped.SelectedMeasurement

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_MeasurementBase",
        )(temp)

    @selected_measurement.setter
    @enforce_parameter_types
    def selected_measurement(self: Self, value: "_1612.MeasurementBase"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_MeasurementBase.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_MeasurementBase.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.SelectedMeasurement = value

    @property
    def show_trailing_zeros(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowTrailingZeros

        if temp is None:
            return False

        return temp

    @show_trailing_zeros.setter
    @enforce_parameter_types
    def show_trailing_zeros(self: Self, value: "bool"):
        self.wrapped.ShowTrailingZeros = bool(value) if value is not None else False

    @property
    def small_number_cutoff(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SmallNumberCutoff

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @small_number_cutoff.setter
    @enforce_parameter_types
    def small_number_cutoff(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SmallNumberCutoff = value

    @property
    def current_selected_measurement(self: Self) -> "_1612.MeasurementBase":
        """mastapy.utility.units_and_measurements.MeasurementBase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def default_to_imperial(self: Self):
        """Method does not return."""
        self.wrapped.DefaultToImperial()

    def default_to_metric(self: Self):
        """Method does not return."""
        self.wrapped.DefaultToMetric()

    @enforce_parameter_types
    def find_measurement_by_name(self: Self, name: "str") -> "_1612.MeasurementBase":
        """mastapy.utility.units_and_measurements.MeasurementBase

        Args:
            name (str)
        """
        name = str(name)
        method_result = self.wrapped.FindMeasurementByName(name if name else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def get_measurement(
        self: Self, measurement_type: "_7568.MeasurementType"
    ) -> "_1612.MeasurementBase":
        """mastapy.utility.units_and_measurements.MeasurementBase

        Args:
            measurement_type (mastapy.units_and_measurements.MeasurementType)
        """
        measurement_type = conversion.mp_to_pn_enum(
            measurement_type, "SMT.MastaAPIUtility.UnitsAndMeasurements.MeasurementType"
        )
        method_result = self.wrapped.GetMeasurement(measurement_type)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "MeasurementSettings._Cast_MeasurementSettings":
        return self._Cast_MeasurementSettings(self)
