"""ModificationSegment"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODIFICATION_SEGMENT = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical", "ModificationSegment"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _635, _640


__docformat__ = "restructuredtext en"
__all__ = ("ModificationSegment",)


Self = TypeVar("Self", bound="ModificationSegment")


class ModificationSegment(_0.APIBase):
    """ModificationSegment

    This is a mastapy class.
    """

    TYPE = _MODIFICATION_SEGMENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ModificationSegment")

    class _Cast_ModificationSegment:
        """Special nested class for casting ModificationSegment to subclasses."""

        def __init__(
            self: "ModificationSegment._Cast_ModificationSegment",
            parent: "ModificationSegment",
        ):
            self._parent = parent

        @property
        def lead_modification_segment(
            self: "ModificationSegment._Cast_ModificationSegment",
        ) -> "_635.LeadModificationSegment":
            from mastapy.gears.manufacturing.cylindrical import _635

            return self._parent._cast(_635.LeadModificationSegment)

        @property
        def profile_modification_segment(
            self: "ModificationSegment._Cast_ModificationSegment",
        ) -> "_640.ProfileModificationSegment":
            from mastapy.gears.manufacturing.cylindrical import _640

            return self._parent._cast(_640.ProfileModificationSegment)

        @property
        def modification_segment(
            self: "ModificationSegment._Cast_ModificationSegment",
        ) -> "ModificationSegment":
            return self._parent

        def __getattr__(
            self: "ModificationSegment._Cast_ModificationSegment", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ModificationSegment.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crown(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Crown

        if temp is None:
            return 0.0

        return temp

    @crown.setter
    @enforce_parameter_types
    def crown(self: Self, value: "float"):
        self.wrapped.Crown = float(value) if value is not None else 0.0

    @property
    def slope(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Slope

        if temp is None:
            return 0.0

        return temp

    @slope.setter
    @enforce_parameter_types
    def slope(self: Self, value: "float"):
        self.wrapped.Slope = float(value) if value is not None else 0.0

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
    def cast_to(self: Self) -> "ModificationSegment._Cast_ModificationSegment":
        return self._Cast_ModificationSegment(self)
