"""ClippingPlane"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLIPPING_PLANE = python_net_import("SMT.MastaAPI.Geometry", "ClippingPlane")

if TYPE_CHECKING:
    from mastapy.math_utility import _1499


__docformat__ = "restructuredtext en"
__all__ = ("ClippingPlane",)


Self = TypeVar("Self", bound="ClippingPlane")


class ClippingPlane(_0.APIBase):
    """ClippingPlane

    This is a mastapy class.
    """

    TYPE = _CLIPPING_PLANE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClippingPlane")

    class _Cast_ClippingPlane:
        """Special nested class for casting ClippingPlane to subclasses."""

        def __init__(
            self: "ClippingPlane._Cast_ClippingPlane", parent: "ClippingPlane"
        ):
            self._parent = parent

        @property
        def clipping_plane(
            self: "ClippingPlane._Cast_ClippingPlane",
        ) -> "ClippingPlane":
            return self._parent

        def __getattr__(self: "ClippingPlane._Cast_ClippingPlane", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClippingPlane.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axis(self: Self) -> "_1499.Axis":
        """mastapy.math_utility.Axis"""
        temp = self.wrapped.Axis

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.MathUtility.Axis")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.math_utility._1499", "Axis")(value)

    @axis.setter
    @enforce_parameter_types
    def axis(self: Self, value: "_1499.Axis"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.MathUtility.Axis")
        self.wrapped.Axis = value

    @property
    def is_enabled(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsEnabled

        if temp is None:
            return False

        return temp

    @is_enabled.setter
    @enforce_parameter_types
    def is_enabled(self: Self, value: "bool"):
        self.wrapped.IsEnabled = bool(value) if value is not None else False

    @property
    def is_flipped(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsFlipped

        if temp is None:
            return False

        return temp

    @is_flipped.setter
    @enforce_parameter_types
    def is_flipped(self: Self, value: "bool"):
        self.wrapped.IsFlipped = bool(value) if value is not None else False

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
    def cast_to(self: Self) -> "ClippingPlane._Cast_ClippingPlane":
        return self._Cast_ClippingPlane(self)
