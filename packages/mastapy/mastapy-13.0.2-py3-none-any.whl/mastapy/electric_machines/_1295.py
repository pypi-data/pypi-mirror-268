"""NotchSpecification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NOTCH_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "NotchSpecification"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1294


__docformat__ = "restructuredtext en"
__all__ = ("NotchSpecification",)


Self = TypeVar("Self", bound="NotchSpecification")


class NotchSpecification(_0.APIBase):
    """NotchSpecification

    This is a mastapy class.
    """

    TYPE = _NOTCH_SPECIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NotchSpecification")

    class _Cast_NotchSpecification:
        """Special nested class for casting NotchSpecification to subclasses."""

        def __init__(
            self: "NotchSpecification._Cast_NotchSpecification",
            parent: "NotchSpecification",
        ):
            self._parent = parent

        @property
        def notch_specification(
            self: "NotchSpecification._Cast_NotchSpecification",
        ) -> "NotchSpecification":
            return self._parent

        def __getattr__(self: "NotchSpecification._Cast_NotchSpecification", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NotchSpecification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def first_notch_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FirstNotchAngle

        if temp is None:
            return 0.0

        return temp

    @first_notch_angle.setter
    @enforce_parameter_types
    def first_notch_angle(self: Self, value: "float"):
        self.wrapped.FirstNotchAngle = float(value) if value is not None else 0.0

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def notch_depth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NotchDepth

        if temp is None:
            return 0.0

        return temp

    @notch_depth.setter
    @enforce_parameter_types
    def notch_depth(self: Self, value: "float"):
        self.wrapped.NotchDepth = float(value) if value is not None else 0.0

    @property
    def notch_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NotchDiameter

        if temp is None:
            return 0.0

        return temp

    @notch_diameter.setter
    @enforce_parameter_types
    def notch_diameter(self: Self, value: "float"):
        self.wrapped.NotchDiameter = float(value) if value is not None else 0.0

    @property
    def notch_offset_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NotchOffsetFactor

        if temp is None:
            return 0.0

        return temp

    @notch_offset_factor.setter
    @enforce_parameter_types
    def notch_offset_factor(self: Self, value: "float"):
        self.wrapped.NotchOffsetFactor = float(value) if value is not None else 0.0

    @property
    def notch_shape(self: Self) -> "_1294.NotchShape":
        """mastapy.electric_machines.NotchShape"""
        temp = self.wrapped.NotchShape

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.ElectricMachines.NotchShape"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines._1294", "NotchShape"
        )(value)

    @notch_shape.setter
    @enforce_parameter_types
    def notch_shape(self: Self, value: "_1294.NotchShape"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.ElectricMachines.NotchShape"
        )
        self.wrapped.NotchShape = value

    @property
    def notch_width_lower(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NotchWidthLower

        if temp is None:
            return 0.0

        return temp

    @notch_width_lower.setter
    @enforce_parameter_types
    def notch_width_lower(self: Self, value: "float"):
        self.wrapped.NotchWidthLower = float(value) if value is not None else 0.0

    @property
    def notch_width_upper(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NotchWidthUpper

        if temp is None:
            return 0.0

        return temp

    @notch_width_upper.setter
    @enforce_parameter_types
    def notch_width_upper(self: Self, value: "float"):
        self.wrapped.NotchWidthUpper = float(value) if value is not None else 0.0

    @property
    def number_of_notches(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfNotches

        if temp is None:
            return 0

        return temp

    @number_of_notches.setter
    @enforce_parameter_types
    def number_of_notches(self: Self, value: "int"):
        self.wrapped.NumberOfNotches = int(value) if value is not None else 0

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
    def cast_to(self: Self) -> "NotchSpecification._Cast_NotchSpecification":
        return self._Cast_NotchSpecification(self)
