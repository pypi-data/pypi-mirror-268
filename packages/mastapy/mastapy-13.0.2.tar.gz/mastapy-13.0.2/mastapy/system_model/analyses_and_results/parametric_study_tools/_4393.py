"""ParametricStudyDOEResultVariableForParallelCoordinatesPlot"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARAMETRIC_STUDY_DOE_RESULT_VARIABLE_FOR_PARALLEL_COORDINATES_PLOT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ParametricStudyDOEResultVariableForParallelCoordinatesPlot",
)


__docformat__ = "restructuredtext en"
__all__ = ("ParametricStudyDOEResultVariableForParallelCoordinatesPlot",)


Self = TypeVar(
    "Self", bound="ParametricStudyDOEResultVariableForParallelCoordinatesPlot"
)


class ParametricStudyDOEResultVariableForParallelCoordinatesPlot(_0.APIBase):
    """ParametricStudyDOEResultVariableForParallelCoordinatesPlot

    This is a mastapy class.
    """

    TYPE = _PARAMETRIC_STUDY_DOE_RESULT_VARIABLE_FOR_PARALLEL_COORDINATES_PLOT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ParametricStudyDOEResultVariableForParallelCoordinatesPlot",
    )

    class _Cast_ParametricStudyDOEResultVariableForParallelCoordinatesPlot:
        """Special nested class for casting ParametricStudyDOEResultVariableForParallelCoordinatesPlot to subclasses."""

        def __init__(
            self: "ParametricStudyDOEResultVariableForParallelCoordinatesPlot._Cast_ParametricStudyDOEResultVariableForParallelCoordinatesPlot",
            parent: "ParametricStudyDOEResultVariableForParallelCoordinatesPlot",
        ):
            self._parent = parent

        @property
        def parametric_study_doe_result_variable_for_parallel_coordinates_plot(
            self: "ParametricStudyDOEResultVariableForParallelCoordinatesPlot._Cast_ParametricStudyDOEResultVariableForParallelCoordinatesPlot",
        ) -> "ParametricStudyDOEResultVariableForParallelCoordinatesPlot":
            return self._parent

        def __getattr__(
            self: "ParametricStudyDOEResultVariableForParallelCoordinatesPlot._Cast_ParametricStudyDOEResultVariableForParallelCoordinatesPlot",
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
        self: Self,
        instance_to_wrap: "ParametricStudyDOEResultVariableForParallelCoordinatesPlot.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def entity_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EntityName

        if temp is None:
            return ""

        return temp

    @property
    def parameter_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParameterName

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

    def delete(self: Self):
        """Method does not return."""
        self.wrapped.Delete()

    def move_down(self: Self):
        """Method does not return."""
        self.wrapped.MoveDown()

    def move_up(self: Self):
        """Method does not return."""
        self.wrapped.MoveUp()

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
    ) -> "ParametricStudyDOEResultVariableForParallelCoordinatesPlot._Cast_ParametricStudyDOEResultVariableForParallelCoordinatesPlot":
        return self._Cast_ParametricStudyDOEResultVariableForParallelCoordinatesPlot(
            self
        )
