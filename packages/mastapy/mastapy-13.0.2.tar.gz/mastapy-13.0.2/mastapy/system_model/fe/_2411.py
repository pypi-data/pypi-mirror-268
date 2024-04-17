"""PerLinkExportOptions"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import overridable_enum_runtime, conversion
from mastapy._internal.implicit import overridable
from mastapy.nodal_analysis.dev_tools_analyses import _205
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PER_LINK_EXPORT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "PerLinkExportOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("PerLinkExportOptions",)


Self = TypeVar("Self", bound="PerLinkExportOptions")


class PerLinkExportOptions(_0.APIBase):
    """PerLinkExportOptions

    This is a mastapy class.
    """

    TYPE = _PER_LINK_EXPORT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PerLinkExportOptions")

    class _Cast_PerLinkExportOptions:
        """Special nested class for casting PerLinkExportOptions to subclasses."""

        def __init__(
            self: "PerLinkExportOptions._Cast_PerLinkExportOptions",
            parent: "PerLinkExportOptions",
        ):
            self._parent = parent

        @property
        def per_link_export_options(
            self: "PerLinkExportOptions._Cast_PerLinkExportOptions",
        ) -> "PerLinkExportOptions":
            return self._parent

        def __getattr__(
            self: "PerLinkExportOptions._Cast_PerLinkExportOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PerLinkExportOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def type_of_coupling_to_export(
        self: Self,
    ) -> "overridable.Overridable_RigidCouplingType":
        """Overridable[mastapy.nodal_analysis.dev_tools_analyses.RigidCouplingType]"""
        temp = self.wrapped.TypeOfCouplingToExport

        if temp is None:
            return None

        value = overridable.Overridable_RigidCouplingType.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @type_of_coupling_to_export.setter
    @enforce_parameter_types
    def type_of_coupling_to_export(
        self: Self,
        value: "Union[_205.RigidCouplingType, Tuple[_205.RigidCouplingType, bool]]",
    ):
        wrapper_type = overridable.Overridable_RigidCouplingType.wrapper_type()
        enclosed_type = overridable.Overridable_RigidCouplingType.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.TypeOfCouplingToExport = value

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
    def cast_to(self: Self) -> "PerLinkExportOptions._Cast_PerLinkExportOptions":
        return self._Cast_PerLinkExportOptions(self)
