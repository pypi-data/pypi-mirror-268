"""DesignConstraint"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.utility.model_validation import _1799
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_CONSTRAINT = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns", "DesignConstraint"
)

if TYPE_CHECKING:
    from mastapy.utility import _1595
    from mastapy.math_utility import _1496


__docformat__ = "restructuredtext en"
__all__ = ("DesignConstraint",)


Self = TypeVar("Self", bound="DesignConstraint")


class DesignConstraint(_0.APIBase):
    """DesignConstraint

    This is a mastapy class.
    """

    TYPE = _DESIGN_CONSTRAINT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DesignConstraint")

    class _Cast_DesignConstraint:
        """Special nested class for casting DesignConstraint to subclasses."""

        def __init__(
            self: "DesignConstraint._Cast_DesignConstraint", parent: "DesignConstraint"
        ):
            self._parent = parent

        @property
        def design_constraint(
            self: "DesignConstraint._Cast_DesignConstraint",
        ) -> "DesignConstraint":
            return self._parent

        def __getattr__(self: "DesignConstraint._Cast_DesignConstraint", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DesignConstraint.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def integer_range(self: Self) -> "_1595.IntegerRange":
        """mastapy.utility.IntegerRange"""
        temp = self.wrapped.IntegerRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @integer_range.setter
    @enforce_parameter_types
    def integer_range(self: Self, value: "_1595.IntegerRange"):
        self.wrapped.IntegerRange = value.wrapped

    @property
    def property_(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Property

        if temp is None:
            return ""

        return temp

    @property
    def range(self: Self) -> "_1496.Range":
        """mastapy.math_utility.Range"""
        temp = self.wrapped.Range

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @range.setter
    @enforce_parameter_types
    def range(self: Self, value: "_1496.Range"):
        self.wrapped.Range = value.wrapped

    @property
    def severity(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_Severity":
        """EnumWithSelectedValue[mastapy.utility.model_validation.Severity]"""
        temp = self.wrapped.Severity

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_Severity.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value)

    @severity.setter
    @enforce_parameter_types
    def severity(self: Self, value: "_1799.Severity"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_Severity.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.Severity = value

    @property
    def type_(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Type

        if temp is None:
            return ""

        return temp

    @property
    def unit(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Unit

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(self: Self) -> "DesignConstraint._Cast_DesignConstraint":
        return self._Cast_DesignConstraint(self)
