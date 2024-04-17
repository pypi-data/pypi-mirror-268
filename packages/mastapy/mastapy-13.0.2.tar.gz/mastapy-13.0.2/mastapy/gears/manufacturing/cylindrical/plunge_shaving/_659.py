"""ShaverPointOfInterest"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAVER_POINT_OF_INTEREST = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving",
    "ShaverPointOfInterest",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _656


__docformat__ = "restructuredtext en"
__all__ = ("ShaverPointOfInterest",)


Self = TypeVar("Self", bound="ShaverPointOfInterest")


class ShaverPointOfInterest(_0.APIBase):
    """ShaverPointOfInterest

    This is a mastapy class.
    """

    TYPE = _SHAVER_POINT_OF_INTEREST
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaverPointOfInterest")

    class _Cast_ShaverPointOfInterest:
        """Special nested class for casting ShaverPointOfInterest to subclasses."""

        def __init__(
            self: "ShaverPointOfInterest._Cast_ShaverPointOfInterest",
            parent: "ShaverPointOfInterest",
        ):
            self._parent = parent

        @property
        def shaver_point_of_interest(
            self: "ShaverPointOfInterest._Cast_ShaverPointOfInterest",
        ) -> "ShaverPointOfInterest":
            return self._parent

        def __getattr__(
            self: "ShaverPointOfInterest._Cast_ShaverPointOfInterest", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaverPointOfInterest.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def error(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Error

        if temp is None:
            return 0.0

        return temp

    @property
    def shaver_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaverRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def shaver_z_plane(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaverZPlane

        if temp is None:
            return 0.0

        return temp

    @property
    def point_of_interest_on_the_gear(self: Self) -> "_656.PointOfInterest":
        """mastapy.gears.manufacturing.cylindrical.plunge_shaving.PointOfInterest

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PointOfInterestOnTheGear

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
    def cast_to(self: Self) -> "ShaverPointOfInterest._Cast_ShaverPointOfInterest":
        return self._Cast_ShaverPointOfInterest(self)
