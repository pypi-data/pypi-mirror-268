"""BearingProtectionDetailsModifier"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_PROTECTION_DETAILS_MODIFIER = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "BearingProtectionDetailsModifier"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2152


__docformat__ = "restructuredtext en"
__all__ = ("BearingProtectionDetailsModifier",)


Self = TypeVar("Self", bound="BearingProtectionDetailsModifier")


class BearingProtectionDetailsModifier(_0.APIBase):
    """BearingProtectionDetailsModifier

    This is a mastapy class.
    """

    TYPE = _BEARING_PROTECTION_DETAILS_MODIFIER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingProtectionDetailsModifier")

    class _Cast_BearingProtectionDetailsModifier:
        """Special nested class for casting BearingProtectionDetailsModifier to subclasses."""

        def __init__(
            self: "BearingProtectionDetailsModifier._Cast_BearingProtectionDetailsModifier",
            parent: "BearingProtectionDetailsModifier",
        ):
            self._parent = parent

        @property
        def bearing_protection_details_modifier(
            self: "BearingProtectionDetailsModifier._Cast_BearingProtectionDetailsModifier",
        ) -> "BearingProtectionDetailsModifier":
            return self._parent

        def __getattr__(
            self: "BearingProtectionDetailsModifier._Cast_BearingProtectionDetailsModifier",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingProtectionDetailsModifier.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def confirm_new_password(self: Self) -> "str":
        """str"""
        temp = self.wrapped.ConfirmNewPassword

        if temp is None:
            return ""

        return temp

    @confirm_new_password.setter
    @enforce_parameter_types
    def confirm_new_password(self: Self, value: "str"):
        self.wrapped.ConfirmNewPassword = str(value) if value is not None else ""

    @property
    def current_password(self: Self) -> "str":
        """str"""
        temp = self.wrapped.CurrentPassword

        if temp is None:
            return ""

        return temp

    @current_password.setter
    @enforce_parameter_types
    def current_password(self: Self, value: "str"):
        self.wrapped.CurrentPassword = str(value) if value is not None else ""

    @property
    def current_protection_level(self: Self) -> "_2152.BearingProtectionLevel":
        """mastapy.bearings.bearing_designs.rolling.BearingProtectionLevel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurrentProtectionLevel

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.BearingDesigns.Rolling.BearingProtectionLevel"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.bearing_designs.rolling._2152", "BearingProtectionLevel"
        )(value)

    @property
    def new_password(self: Self) -> "str":
        """str"""
        temp = self.wrapped.NewPassword

        if temp is None:
            return ""

        return temp

    @new_password.setter
    @enforce_parameter_types
    def new_password(self: Self, value: "str"):
        self.wrapped.NewPassword = str(value) if value is not None else ""

    @property
    def new_protection_level(self: Self) -> "_2152.BearingProtectionLevel":
        """mastapy.bearings.bearing_designs.rolling.BearingProtectionLevel"""
        temp = self.wrapped.NewProtectionLevel

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.BearingDesigns.Rolling.BearingProtectionLevel"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.bearing_designs.rolling._2152", "BearingProtectionLevel"
        )(value)

    @new_protection_level.setter
    @enforce_parameter_types
    def new_protection_level(self: Self, value: "_2152.BearingProtectionLevel"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.BearingDesigns.Rolling.BearingProtectionLevel"
        )
        self.wrapped.NewProtectionLevel = value

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
    def cast_to(
        self: Self,
    ) -> "BearingProtectionDetailsModifier._Cast_BearingProtectionDetailsModifier":
        return self._Cast_BearingProtectionDetailsModifier(self)
