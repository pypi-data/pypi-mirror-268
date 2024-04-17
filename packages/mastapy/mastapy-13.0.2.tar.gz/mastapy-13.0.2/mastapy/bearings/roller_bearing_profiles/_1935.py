"""ProfileSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PROFILE_SET = python_net_import(
    "SMT.MastaAPI.Bearings.RollerBearingProfiles", "ProfileSet"
)

if TYPE_CHECKING:
    from mastapy.bearings import _1898
    from mastapy.bearings.roller_bearing_profiles import _1943


__docformat__ = "restructuredtext en"
__all__ = ("ProfileSet",)


Self = TypeVar("Self", bound="ProfileSet")


class ProfileSet(_0.APIBase):
    """ProfileSet

    This is a mastapy class.
    """

    TYPE = _PROFILE_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ProfileSet")

    class _Cast_ProfileSet:
        """Special nested class for casting ProfileSet to subclasses."""

        def __init__(self: "ProfileSet._Cast_ProfileSet", parent: "ProfileSet"):
            self._parent = parent

        @property
        def profile_set(self: "ProfileSet._Cast_ProfileSet") -> "ProfileSet":
            return self._parent

        def __getattr__(self: "ProfileSet._Cast_ProfileSet", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ProfileSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_profile_type(self: Self) -> "_1898.RollerBearingProfileTypes":
        """mastapy.bearings.RollerBearingProfileTypes"""
        temp = self.wrapped.ActiveProfileType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.RollerBearingProfileTypes"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings._1898", "RollerBearingProfileTypes"
        )(value)

    @active_profile_type.setter
    @enforce_parameter_types
    def active_profile_type(self: Self, value: "_1898.RollerBearingProfileTypes"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.RollerBearingProfileTypes"
        )
        self.wrapped.ActiveProfileType = value

    @property
    def active_profile(self: Self) -> "_1943.RollerBearingProfile":
        """mastapy.bearings.roller_bearing_profiles.RollerBearingProfile

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def cast_to(self: Self) -> "ProfileSet._Cast_ProfileSet":
        return self._Cast_ProfileSet(self)
