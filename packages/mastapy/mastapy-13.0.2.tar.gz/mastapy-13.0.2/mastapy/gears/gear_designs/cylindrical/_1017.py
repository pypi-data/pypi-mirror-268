"""CylindricalGearDesignConstraint"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.utility.model_validation import _1802
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_DESIGN_CONSTRAINT = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalGearDesignConstraint"
)

if TYPE_CHECKING:
    from mastapy.utility import _1595
    from mastapy.math_utility import _1496


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearDesignConstraint",)


Self = TypeVar("Self", bound="CylindricalGearDesignConstraint")


class CylindricalGearDesignConstraint(_0.APIBase):
    """CylindricalGearDesignConstraint

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_DESIGN_CONSTRAINT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearDesignConstraint")

    class _Cast_CylindricalGearDesignConstraint:
        """Special nested class for casting CylindricalGearDesignConstraint to subclasses."""

        def __init__(
            self: "CylindricalGearDesignConstraint._Cast_CylindricalGearDesignConstraint",
            parent: "CylindricalGearDesignConstraint",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_design_constraint(
            self: "CylindricalGearDesignConstraint._Cast_CylindricalGearDesignConstraint",
        ) -> "CylindricalGearDesignConstraint":
            return self._parent

        def __getattr__(
            self: "CylindricalGearDesignConstraint._Cast_CylindricalGearDesignConstraint",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearDesignConstraint.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def class_of_error(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_StatusItemSeverity":
        """EnumWithSelectedValue[mastapy.utility.model_validation.StatusItemSeverity]"""
        temp = self.wrapped.ClassOfError

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_StatusItemSeverity.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @class_of_error.setter
    @enforce_parameter_types
    def class_of_error(self: Self, value: "_1802.StatusItemSeverity"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_StatusItemSeverity.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ClassOfError = value

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
    def is_active(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsActive

        if temp is None:
            return False

        return temp

    @is_active.setter
    @enforce_parameter_types
    def is_active(self: Self, value: "bool"):
        self.wrapped.IsActive = bool(value) if value is not None else False

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
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    def delete(self: Self):
        """Method does not return."""
        self.wrapped.Delete()

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearDesignConstraint._Cast_CylindricalGearDesignConstraint":
        return self._Cast_CylindricalGearDesignConstraint(self)
