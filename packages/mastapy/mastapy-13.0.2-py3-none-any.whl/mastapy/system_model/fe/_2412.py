"""PerNodeExportOptions"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import overridable_enum_runtime, conversion
from mastapy._internal.implicit import overridable
from mastapy.nodal_analysis.fe_export_utility import _168
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PER_NODE_EXPORT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "PerNodeExportOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("PerNodeExportOptions",)


Self = TypeVar("Self", bound="PerNodeExportOptions")


class PerNodeExportOptions(_0.APIBase):
    """PerNodeExportOptions

    This is a mastapy class.
    """

    TYPE = _PER_NODE_EXPORT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PerNodeExportOptions")

    class _Cast_PerNodeExportOptions:
        """Special nested class for casting PerNodeExportOptions to subclasses."""

        def __init__(
            self: "PerNodeExportOptions._Cast_PerNodeExportOptions",
            parent: "PerNodeExportOptions",
        ):
            self._parent = parent

        @property
        def per_node_export_options(
            self: "PerNodeExportOptions._Cast_PerNodeExportOptions",
        ) -> "PerNodeExportOptions":
            return self._parent

        def __getattr__(
            self: "PerNodeExportOptions._Cast_PerNodeExportOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PerNodeExportOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def external_id(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExternalID

        if temp is None:
            return 0

        return temp

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
    def type_of_result_to_export(
        self: Self,
    ) -> "overridable.Overridable_BoundaryConditionType":
        """Overridable[mastapy.nodal_analysis.fe_export_utility.BoundaryConditionType]"""
        temp = self.wrapped.TypeOfResultToExport

        if temp is None:
            return None

        value = overridable.Overridable_BoundaryConditionType.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @type_of_result_to_export.setter
    @enforce_parameter_types
    def type_of_result_to_export(
        self: Self,
        value: "Union[_168.BoundaryConditionType, Tuple[_168.BoundaryConditionType, bool]]",
    ):
        wrapper_type = overridable.Overridable_BoundaryConditionType.wrapper_type()
        enclosed_type = overridable.Overridable_BoundaryConditionType.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.TypeOfResultToExport = value

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
    def cast_to(self: Self) -> "PerNodeExportOptions._Cast_PerNodeExportOptions":
        return self._Cast_PerNodeExportOptions(self)
