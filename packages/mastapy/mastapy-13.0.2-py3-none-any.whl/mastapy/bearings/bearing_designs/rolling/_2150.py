"""BearingProtection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_PROTECTION = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "BearingProtection"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2152


__docformat__ = "restructuredtext en"
__all__ = ("BearingProtection",)


Self = TypeVar("Self", bound="BearingProtection")


class BearingProtection(_0.APIBase):
    """BearingProtection

    This is a mastapy class.
    """

    TYPE = _BEARING_PROTECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingProtection")

    class _Cast_BearingProtection:
        """Special nested class for casting BearingProtection to subclasses."""

        def __init__(
            self: "BearingProtection._Cast_BearingProtection",
            parent: "BearingProtection",
        ):
            self._parent = parent

        @property
        def bearing_protection(
            self: "BearingProtection._Cast_BearingProtection",
        ) -> "BearingProtection":
            return self._parent

        def __getattr__(self: "BearingProtection._Cast_BearingProtection", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingProtection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def advanced_bearing_results_hidden(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdvancedBearingResultsHidden

        if temp is None:
            return ""

        return temp

    @property
    def bearing_is_protected(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingIsProtected

        if temp is None:
            return False

        return temp

    @property
    def internal_geometry_hidden(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InternalGeometryHidden

        if temp is None:
            return ""

        return temp

    @property
    def protection_level(self: Self) -> "_2152.BearingProtectionLevel":
        """mastapy.bearings.bearing_designs.rolling.BearingProtectionLevel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProtectionLevel

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
    def cast_to(self: Self) -> "BearingProtection._Cast_BearingProtection":
        return self._Cast_BearingProtection(self)
