"""LookupTableBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.math_utility import _1517
from mastapy._internal import enum_with_selected_value_runtime, conversion
from mastapy.utility import _1593
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOOKUP_TABLE_BASE = python_net_import(
    "SMT.MastaAPI.MathUtility.MeasuredData", "LookupTableBase"
)

if TYPE_CHECKING:
    from mastapy.math_utility.measured_data import _1574, _1575


__docformat__ = "restructuredtext en"
__all__ = ("LookupTableBase",)


Self = TypeVar("Self", bound="LookupTableBase")
T = TypeVar("T", bound="LookupTableBase")


class LookupTableBase(_1593.IndependentReportablePropertiesBase[T]):
    """LookupTableBase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _LOOKUP_TABLE_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LookupTableBase")

    class _Cast_LookupTableBase:
        """Special nested class for casting LookupTableBase to subclasses."""

        def __init__(
            self: "LookupTableBase._Cast_LookupTableBase", parent: "LookupTableBase"
        ):
            self._parent = parent

        @property
        def independent_reportable_properties_base(
            self: "LookupTableBase._Cast_LookupTableBase",
        ) -> "_1593.IndependentReportablePropertiesBase":
            return self._parent._cast(_1593.IndependentReportablePropertiesBase)

        @property
        def onedimensional_function_lookup_table(
            self: "LookupTableBase._Cast_LookupTableBase",
        ) -> "_1574.OnedimensionalFunctionLookupTable":
            from mastapy.math_utility.measured_data import _1574

            return self._parent._cast(_1574.OnedimensionalFunctionLookupTable)

        @property
        def twodimensional_function_lookup_table(
            self: "LookupTableBase._Cast_LookupTableBase",
        ) -> "_1575.TwodimensionalFunctionLookupTable":
            from mastapy.math_utility.measured_data import _1575

            return self._parent._cast(_1575.TwodimensionalFunctionLookupTable)

        @property
        def lookup_table_base(
            self: "LookupTableBase._Cast_LookupTableBase",
        ) -> "LookupTableBase":
            return self._parent

        def __getattr__(self: "LookupTableBase._Cast_LookupTableBase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LookupTableBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def extrapolation_option(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions":
        """EnumWithSelectedValue[mastapy.math_utility.ExtrapolationOptions]"""
        temp = self.wrapped.ExtrapolationOption

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @extrapolation_option.setter
    @enforce_parameter_types
    def extrapolation_option(self: Self, value: "_1517.ExtrapolationOptions"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ExtrapolationOption = value

    @property
    def cast_to(self: Self) -> "LookupTableBase._Cast_LookupTableBase":
        return self._Cast_LookupTableBase(self)
