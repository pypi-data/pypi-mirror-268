"""Micropitting"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.gears import _341
from mastapy.utility import _1593
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MICROPITTING = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "Micropitting"
)


__docformat__ = "restructuredtext en"
__all__ = ("Micropitting",)


Self = TypeVar("Self", bound="Micropitting")


class Micropitting(_1593.IndependentReportablePropertiesBase["Micropitting"]):
    """Micropitting

    This is a mastapy class.
    """

    TYPE = _MICROPITTING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Micropitting")

    class _Cast_Micropitting:
        """Special nested class for casting Micropitting to subclasses."""

        def __init__(self: "Micropitting._Cast_Micropitting", parent: "Micropitting"):
            self._parent = parent

        @property
        def independent_reportable_properties_base(
            self: "Micropitting._Cast_Micropitting",
        ) -> "_1593.IndependentReportablePropertiesBase":
            pass

            return self._parent._cast(_1593.IndependentReportablePropertiesBase)

        @property
        def micropitting(self: "Micropitting._Cast_Micropitting") -> "Micropitting":
            return self._parent

        def __getattr__(self: "Micropitting._Cast_Micropitting", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Micropitting.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def estimate_bulk_temperature(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.EstimateBulkTemperature

        if temp is None:
            return False

        return temp

    @estimate_bulk_temperature.setter
    @enforce_parameter_types
    def estimate_bulk_temperature(self: Self, value: "bool"):
        self.wrapped.EstimateBulkTemperature = (
            bool(value) if value is not None else False
        )

    @property
    def method_a_coefficient_of_friction_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_MicropittingCoefficientOfFrictionCalculationMethod":
        """EnumWithSelectedValue[mastapy.gears.MicropittingCoefficientOfFrictionCalculationMethod]"""
        temp = self.wrapped.MethodACoefficientOfFrictionMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_MicropittingCoefficientOfFrictionCalculationMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @method_a_coefficient_of_friction_method.setter
    @enforce_parameter_types
    def method_a_coefficient_of_friction_method(
        self: Self, value: "_341.MicropittingCoefficientOfFrictionCalculationMethod"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_MicropittingCoefficientOfFrictionCalculationMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.MethodACoefficientOfFrictionMethod = value

    @property
    def cast_to(self: Self) -> "Micropitting._Cast_Micropitting":
        return self._Cast_Micropitting(self)
