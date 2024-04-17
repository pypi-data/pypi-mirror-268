"""Scuffing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.gears.gear_designs.cylindrical import _1077
from mastapy.utility import _1593
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SCUFFING = python_net_import("SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "Scuffing")

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1078, _1079


__docformat__ = "restructuredtext en"
__all__ = ("Scuffing",)


Self = TypeVar("Self", bound="Scuffing")


class Scuffing(_1593.IndependentReportablePropertiesBase["Scuffing"]):
    """Scuffing

    This is a mastapy class.
    """

    TYPE = _SCUFFING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Scuffing")

    class _Cast_Scuffing:
        """Special nested class for casting Scuffing to subclasses."""

        def __init__(self: "Scuffing._Cast_Scuffing", parent: "Scuffing"):
            self._parent = parent

        @property
        def independent_reportable_properties_base(
            self: "Scuffing._Cast_Scuffing",
        ) -> "_1593.IndependentReportablePropertiesBase":
            pass

            return self._parent._cast(_1593.IndependentReportablePropertiesBase)

        @property
        def scuffing(self: "Scuffing._Cast_Scuffing") -> "Scuffing":
            return self._parent

        def __getattr__(self: "Scuffing._Cast_Scuffing", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Scuffing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bulk_tooth_temperature_of_test_gears_flash_temperature_method(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.BulkToothTemperatureOfTestGearsFlashTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @bulk_tooth_temperature_of_test_gears_flash_temperature_method.setter
    @enforce_parameter_types
    def bulk_tooth_temperature_of_test_gears_flash_temperature_method(
        self: Self, value: "float"
    ):
        self.wrapped.BulkToothTemperatureOfTestGearsFlashTemperatureMethod = (
            float(value) if value is not None else 0.0
        )

    @property
    def bulk_tooth_temperature_of_test_gears_integral_temperature_method(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.BulkToothTemperatureOfTestGearsIntegralTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @bulk_tooth_temperature_of_test_gears_integral_temperature_method.setter
    @enforce_parameter_types
    def bulk_tooth_temperature_of_test_gears_integral_temperature_method(
        self: Self, value: "float"
    ):
        self.wrapped.BulkToothTemperatureOfTestGearsIntegralTemperatureMethod = (
            float(value) if value is not None else 0.0
        )

    @property
    def coefficient_of_friction_method_flash_temperature_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ScuffingCoefficientOfFrictionMethods":
        """EnumWithSelectedValue[mastapy.gears.gear_designs.cylindrical.ScuffingCoefficientOfFrictionMethods]"""
        temp = self.wrapped.CoefficientOfFrictionMethodFlashTemperatureMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ScuffingCoefficientOfFrictionMethods.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @coefficient_of_friction_method_flash_temperature_method.setter
    @enforce_parameter_types
    def coefficient_of_friction_method_flash_temperature_method(
        self: Self, value: "_1077.ScuffingCoefficientOfFrictionMethods"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ScuffingCoefficientOfFrictionMethods.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.CoefficientOfFrictionMethodFlashTemperatureMethod = value

    @property
    def contact_time_at_high_velocity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ContactTimeAtHighVelocity

        if temp is None:
            return 0.0

        return temp

    @contact_time_at_high_velocity.setter
    @enforce_parameter_types
    def contact_time_at_high_velocity(self: Self, value: "float"):
        self.wrapped.ContactTimeAtHighVelocity = (
            float(value) if value is not None else 0.0
        )

    @property
    def contact_time_at_medium_velocity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ContactTimeAtMediumVelocity

        if temp is None:
            return 0.0

        return temp

    @contact_time_at_medium_velocity.setter
    @enforce_parameter_types
    def contact_time_at_medium_velocity(self: Self, value: "float"):
        self.wrapped.ContactTimeAtMediumVelocity = (
            float(value) if value is not None else 0.0
        )

    @property
    def estimate_oil_test_results_for_long_contact_times(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.EstimateOilTestResultsForLongContactTimes

        if temp is None:
            return False

        return temp

    @estimate_oil_test_results_for_long_contact_times.setter
    @enforce_parameter_types
    def estimate_oil_test_results_for_long_contact_times(self: Self, value: "bool"):
        self.wrapped.EstimateOilTestResultsForLongContactTimes = (
            bool(value) if value is not None else False
        )

    @property
    def estimate_tooth_temperature(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.EstimateToothTemperature

        if temp is None:
            return False

        return temp

    @estimate_tooth_temperature.setter
    @enforce_parameter_types
    def estimate_tooth_temperature(self: Self, value: "bool"):
        self.wrapped.EstimateToothTemperature = (
            bool(value) if value is not None else False
        )

    @property
    def maximum_flash_temperature_of_test_gears_flash_temperature_method(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.MaximumFlashTemperatureOfTestGearsFlashTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @maximum_flash_temperature_of_test_gears_flash_temperature_method.setter
    @enforce_parameter_types
    def maximum_flash_temperature_of_test_gears_flash_temperature_method(
        self: Self, value: "float"
    ):
        self.wrapped.MaximumFlashTemperatureOfTestGearsFlashTemperatureMethod = (
            float(value) if value is not None else 0.0
        )

    @property
    def mean_coefficient_of_friction_flash_temperature_method(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MeanCoefficientOfFrictionFlashTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @mean_coefficient_of_friction_flash_temperature_method.setter
    @enforce_parameter_types
    def mean_coefficient_of_friction_flash_temperature_method(
        self: Self, value: "float"
    ):
        self.wrapped.MeanCoefficientOfFrictionFlashTemperatureMethod = (
            float(value) if value is not None else 0.0
        )

    @property
    def mean_flash_temperature_of_test_gears_integral_temperature_method(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.MeanFlashTemperatureOfTestGearsIntegralTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @mean_flash_temperature_of_test_gears_integral_temperature_method.setter
    @enforce_parameter_types
    def mean_flash_temperature_of_test_gears_integral_temperature_method(
        self: Self, value: "float"
    ):
        self.wrapped.MeanFlashTemperatureOfTestGearsIntegralTemperatureMethod = (
            float(value) if value is not None else 0.0
        )

    @property
    def scuffing_temperature_at_high_velocity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ScuffingTemperatureAtHighVelocity

        if temp is None:
            return 0.0

        return temp

    @scuffing_temperature_at_high_velocity.setter
    @enforce_parameter_types
    def scuffing_temperature_at_high_velocity(self: Self, value: "float"):
        self.wrapped.ScuffingTemperatureAtHighVelocity = (
            float(value) if value is not None else 0.0
        )

    @property
    def scuffing_temperature_at_medium_velocity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ScuffingTemperatureAtMediumVelocity

        if temp is None:
            return 0.0

        return temp

    @scuffing_temperature_at_medium_velocity.setter
    @enforce_parameter_types
    def scuffing_temperature_at_medium_velocity(self: Self, value: "float"):
        self.wrapped.ScuffingTemperatureAtMediumVelocity = (
            float(value) if value is not None else 0.0
        )

    @property
    def scuffing_temperature_method_agma(
        self: Self,
    ) -> "_1078.ScuffingTemperatureMethodsAGMA":
        """mastapy.gears.gear_designs.cylindrical.ScuffingTemperatureMethodsAGMA"""
        temp = self.wrapped.ScuffingTemperatureMethodAGMA

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.ScuffingTemperatureMethodsAGMA",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1078",
            "ScuffingTemperatureMethodsAGMA",
        )(value)

    @scuffing_temperature_method_agma.setter
    @enforce_parameter_types
    def scuffing_temperature_method_agma(
        self: Self, value: "_1078.ScuffingTemperatureMethodsAGMA"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.ScuffingTemperatureMethodsAGMA",
        )
        self.wrapped.ScuffingTemperatureMethodAGMA = value

    @property
    def scuffing_temperature_method_iso(
        self: Self,
    ) -> "_1079.ScuffingTemperatureMethodsISO":
        """mastapy.gears.gear_designs.cylindrical.ScuffingTemperatureMethodsISO"""
        temp = self.wrapped.ScuffingTemperatureMethodISO

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.ScuffingTemperatureMethodsISO",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1079",
            "ScuffingTemperatureMethodsISO",
        )(value)

    @scuffing_temperature_method_iso.setter
    @enforce_parameter_types
    def scuffing_temperature_method_iso(
        self: Self, value: "_1079.ScuffingTemperatureMethodsISO"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.ScuffingTemperatureMethodsISO",
        )
        self.wrapped.ScuffingTemperatureMethodISO = value

    @property
    def user_input_scuffing_integral_temperature_for_long_contact_times(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.UserInputScuffingIntegralTemperatureForLongContactTimes

        if temp is None:
            return 0.0

        return temp

    @user_input_scuffing_integral_temperature_for_long_contact_times.setter
    @enforce_parameter_types
    def user_input_scuffing_integral_temperature_for_long_contact_times(
        self: Self, value: "float"
    ):
        self.wrapped.UserInputScuffingIntegralTemperatureForLongContactTimes = (
            float(value) if value is not None else 0.0
        )

    @property
    def user_input_scuffing_temperature_flash_temperature_method(self: Self) -> "float":
        """float"""
        temp = self.wrapped.UserInputScuffingTemperatureFlashTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @user_input_scuffing_temperature_flash_temperature_method.setter
    @enforce_parameter_types
    def user_input_scuffing_temperature_flash_temperature_method(
        self: Self, value: "float"
    ):
        self.wrapped.UserInputScuffingTemperatureFlashTemperatureMethod = (
            float(value) if value is not None else 0.0
        )

    @property
    def user_input_scuffing_temperature_integral_temperature_method(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.UserInputScuffingTemperatureIntegralTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @user_input_scuffing_temperature_integral_temperature_method.setter
    @enforce_parameter_types
    def user_input_scuffing_temperature_integral_temperature_method(
        self: Self, value: "float"
    ):
        self.wrapped.UserInputScuffingTemperatureIntegralTemperatureMethod = (
            float(value) if value is not None else 0.0
        )

    @property
    def user_input_scuffing_temperature_for_long_contact_times(self: Self) -> "float":
        """float"""
        temp = self.wrapped.UserInputScuffingTemperatureForLongContactTimes

        if temp is None:
            return 0.0

        return temp

    @user_input_scuffing_temperature_for_long_contact_times.setter
    @enforce_parameter_types
    def user_input_scuffing_temperature_for_long_contact_times(
        self: Self, value: "float"
    ):
        self.wrapped.UserInputScuffingTemperatureForLongContactTimes = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(self: Self) -> "Scuffing._Cast_Scuffing":
        return self._Cast_Scuffing(self)
