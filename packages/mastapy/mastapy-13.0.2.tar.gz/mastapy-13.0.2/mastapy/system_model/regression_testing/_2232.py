"""PerformRegressionTestFromMASTAOptions"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PERFORM_REGRESSION_TEST_FROM_MASTA_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.RegressionTesting",
    "PerformRegressionTestFromMASTAOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("PerformRegressionTestFromMASTAOptions",)


Self = TypeVar("Self", bound="PerformRegressionTestFromMASTAOptions")


class PerformRegressionTestFromMASTAOptions(_0.APIBase):
    """PerformRegressionTestFromMASTAOptions

    This is a mastapy class.
    """

    TYPE = _PERFORM_REGRESSION_TEST_FROM_MASTA_OPTIONS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PerformRegressionTestFromMASTAOptions"
    )

    class _Cast_PerformRegressionTestFromMASTAOptions:
        """Special nested class for casting PerformRegressionTestFromMASTAOptions to subclasses."""

        def __init__(
            self: "PerformRegressionTestFromMASTAOptions._Cast_PerformRegressionTestFromMASTAOptions",
            parent: "PerformRegressionTestFromMASTAOptions",
        ):
            self._parent = parent

        @property
        def perform_regression_test_from_masta_options(
            self: "PerformRegressionTestFromMASTAOptions._Cast_PerformRegressionTestFromMASTAOptions",
        ) -> "PerformRegressionTestFromMASTAOptions":
            return self._parent

        def __getattr__(
            self: "PerformRegressionTestFromMASTAOptions._Cast_PerformRegressionTestFromMASTAOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "PerformRegressionTestFromMASTAOptions.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def selected_version(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.SelectedVersion

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @selected_version.setter
    @enforce_parameter_types
    def selected_version(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.SelectedVersion = value

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

    def run(self: Self):
        """Method does not return."""
        self.wrapped.Run()

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
    ) -> "PerformRegressionTestFromMASTAOptions._Cast_PerformRegressionTestFromMASTAOptions":
        return self._Cast_PerformRegressionTestFromMASTAOptions(self)
