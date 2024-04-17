"""WindingsViewer"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WINDINGS_VIEWER = python_net_import("SMT.MastaAPI.ElectricMachines", "WindingsViewer")


__docformat__ = "restructuredtext en"
__all__ = ("WindingsViewer",)


Self = TypeVar("Self", bound="WindingsViewer")


class WindingsViewer(_0.APIBase):
    """WindingsViewer

    This is a mastapy class.
    """

    TYPE = _WINDINGS_VIEWER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WindingsViewer")

    class _Cast_WindingsViewer:
        """Special nested class for casting WindingsViewer to subclasses."""

        def __init__(
            self: "WindingsViewer._Cast_WindingsViewer", parent: "WindingsViewer"
        ):
            self._parent = parent

        @property
        def windings_viewer(
            self: "WindingsViewer._Cast_WindingsViewer",
        ) -> "WindingsViewer":
            return self._parent

        def __getattr__(self: "WindingsViewer._Cast_WindingsViewer", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WindingsViewer.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def parallel_path(self: Self) -> "list_with_selected_item.ListWithSelectedItem_int":
        """ListWithSelectedItem[int]"""
        temp = self.wrapped.ParallelPath

        if temp is None:
            return 0

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_int",
        )(temp)

    @parallel_path.setter
    @enforce_parameter_types
    def parallel_path(self: Self, value: "int"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_int.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_int.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0
        )
        self.wrapped.ParallelPath = value

    @property
    def phase(self: Self) -> "list_with_selected_item.ListWithSelectedItem_int":
        """ListWithSelectedItem[int]"""
        temp = self.wrapped.Phase

        if temp is None:
            return 0

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_int",
        )(temp)

    @phase.setter
    @enforce_parameter_types
    def phase(self: Self, value: "int"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_int.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_int.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0
        )
        self.wrapped.Phase = value

    @property
    def show_all_parallel_paths(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowAllParallelPaths

        if temp is None:
            return False

        return temp

    @show_all_parallel_paths.setter
    @enforce_parameter_types
    def show_all_parallel_paths(self: Self, value: "bool"):
        self.wrapped.ShowAllParallelPaths = bool(value) if value is not None else False

    @property
    def show_all_phases(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowAllPhases

        if temp is None:
            return False

        return temp

    @show_all_phases.setter
    @enforce_parameter_types
    def show_all_phases(self: Self, value: "bool"):
        self.wrapped.ShowAllPhases = bool(value) if value is not None else False

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
    def cast_to(self: Self) -> "WindingsViewer._Cast_WindingsViewer":
        return self._Cast_WindingsViewer(self)
