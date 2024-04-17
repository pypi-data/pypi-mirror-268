"""ElmerResultsViewable"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.math_utility import _1534
from mastapy.nodal_analysis.elmer import _176
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELMER_RESULTS_VIEWABLE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.Elmer", "ElmerResultsViewable"
)

if TYPE_CHECKING:
    from mastapy.utility_gui import _1858
    from mastapy.electric_machines.results import _1332, _1344


__docformat__ = "restructuredtext en"
__all__ = ("ElmerResultsViewable",)


Self = TypeVar("Self", bound="ElmerResultsViewable")


class ElmerResultsViewable(_0.APIBase):
    """ElmerResultsViewable

    This is a mastapy class.
    """

    TYPE = _ELMER_RESULTS_VIEWABLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElmerResultsViewable")

    class _Cast_ElmerResultsViewable:
        """Special nested class for casting ElmerResultsViewable to subclasses."""

        def __init__(
            self: "ElmerResultsViewable._Cast_ElmerResultsViewable",
            parent: "ElmerResultsViewable",
        ):
            self._parent = parent

        @property
        def electric_machine_mechanical_results_viewable(
            self: "ElmerResultsViewable._Cast_ElmerResultsViewable",
        ) -> "_1332.ElectricMachineMechanicalResultsViewable":
            from mastapy.electric_machines.results import _1332

            return self._parent._cast(_1332.ElectricMachineMechanicalResultsViewable)

        @property
        def electric_machine_results_viewable(
            self: "ElmerResultsViewable._Cast_ElmerResultsViewable",
        ) -> "_1344.ElectricMachineResultsViewable":
            from mastapy.electric_machines.results import _1344

            return self._parent._cast(_1344.ElectricMachineResultsViewable)

        @property
        def elmer_results_viewable(
            self: "ElmerResultsViewable._Cast_ElmerResultsViewable",
        ) -> "ElmerResultsViewable":
            return self._parent

        def __getattr__(
            self: "ElmerResultsViewable._Cast_ElmerResultsViewable", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElmerResultsViewable.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def current_index(self: Self) -> "int":
        """int"""
        temp = self.wrapped.CurrentIndex

        if temp is None:
            return 0

        return temp

    @current_index.setter
    @enforce_parameter_types
    def current_index(self: Self, value: "int"):
        self.wrapped.CurrentIndex = int(value) if value is not None else 0

    @property
    def degree_of_freedom(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ResultOptionsFor3DVector":
        """EnumWithSelectedValue[mastapy.math_utility.ResultOptionsFor3DVector]"""
        temp = self.wrapped.DegreeOfFreedom

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ResultOptionsFor3DVector.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @degree_of_freedom.setter
    @enforce_parameter_types
    def degree_of_freedom(self: Self, value: "_1534.ResultOptionsFor3DVector"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ResultOptionsFor3DVector.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DegreeOfFreedom = value

    @property
    def result_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ElmerResultType":
        """EnumWithSelectedValue[mastapy.nodal_analysis.elmer.ElmerResultType]"""
        temp = self.wrapped.ResultType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ElmerResultType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @result_type.setter
    @enforce_parameter_types
    def result_type(self: Self, value: "_176.ElmerResultType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ElmerResultType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ResultType = value

    @property
    def show_contour_range_for_all_parts(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowContourRangeForAllParts

        if temp is None:
            return False

        return temp

    @show_contour_range_for_all_parts.setter
    @enforce_parameter_types
    def show_contour_range_for_all_parts(self: Self, value: "bool"):
        self.wrapped.ShowContourRangeForAllParts = (
            bool(value) if value is not None else False
        )

    @property
    def show_contour_range_for_all_steps(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowContourRangeForAllSteps

        if temp is None:
            return False

        return temp

    @show_contour_range_for_all_steps.setter
    @enforce_parameter_types
    def show_contour_range_for_all_steps(self: Self, value: "bool"):
        self.wrapped.ShowContourRangeForAllSteps = (
            bool(value) if value is not None else False
        )

    @property
    def show_full_model(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowFullModel

        if temp is None:
            return False

        return temp

    @show_full_model.setter
    @enforce_parameter_types
    def show_full_model(self: Self, value: "bool"):
        self.wrapped.ShowFullModel = bool(value) if value is not None else False

    @property
    def show_in_3d(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowIn3D

        if temp is None:
            return False

        return temp

    @show_in_3d.setter
    @enforce_parameter_types
    def show_in_3d(self: Self, value: "bool"):
        self.wrapped.ShowIn3D = bool(value) if value is not None else False

    @property
    def show_mesh(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowMesh

        if temp is None:
            return False

        return temp

    @show_mesh.setter
    @enforce_parameter_types
    def show_mesh(self: Self, value: "bool"):
        self.wrapped.ShowMesh = bool(value) if value is not None else False

    @property
    def scaling_draw_style(self: Self) -> "_1858.ScalingDrawStyle":
        """mastapy.utility_gui.ScalingDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScalingDrawStyle

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
    def cast_to(self: Self) -> "ElmerResultsViewable._Cast_ElmerResultsViewable":
        return self._Cast_ElmerResultsViewable(self)
