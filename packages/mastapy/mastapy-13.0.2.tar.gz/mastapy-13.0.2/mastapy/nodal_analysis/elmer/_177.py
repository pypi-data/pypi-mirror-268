"""MechanicalContactSpecification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MECHANICAL_CONTACT_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.Elmer", "MechanicalContactSpecification"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.elmer import _171


__docformat__ = "restructuredtext en"
__all__ = ("MechanicalContactSpecification",)


Self = TypeVar("Self", bound="MechanicalContactSpecification")


class MechanicalContactSpecification(_0.APIBase):
    """MechanicalContactSpecification

    This is a mastapy class.
    """

    TYPE = _MECHANICAL_CONTACT_SPECIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MechanicalContactSpecification")

    class _Cast_MechanicalContactSpecification:
        """Special nested class for casting MechanicalContactSpecification to subclasses."""

        def __init__(
            self: "MechanicalContactSpecification._Cast_MechanicalContactSpecification",
            parent: "MechanicalContactSpecification",
        ):
            self._parent = parent

        @property
        def mechanical_contact_specification(
            self: "MechanicalContactSpecification._Cast_MechanicalContactSpecification",
        ) -> "MechanicalContactSpecification":
            return self._parent

        def __getattr__(
            self: "MechanicalContactSpecification._Cast_MechanicalContactSpecification",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MechanicalContactSpecification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_type(self: Self) -> "_171.ContactType":
        """mastapy.nodal_analysis.elmer.ContactType"""
        temp = self.wrapped.ContactType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.Elmer.ContactType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis.elmer._171", "ContactType"
        )(value)

    @contact_type.setter
    @enforce_parameter_types
    def contact_type(self: Self, value: "_171.ContactType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.NodalAnalysis.Elmer.ContactType"
        )
        self.wrapped.ContactType = value

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
    ) -> "MechanicalContactSpecification._Cast_MechanicalContactSpecification":
        return self._Cast_MechanicalContactSpecification(self)
