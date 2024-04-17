"""DrawStyleForFE"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DRAW_STYLE_FOR_FE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses", "DrawStyleForFE"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _59


__docformat__ = "restructuredtext en"
__all__ = ("DrawStyleForFE",)


Self = TypeVar("Self", bound="DrawStyleForFE")


class DrawStyleForFE(_0.APIBase):
    """DrawStyleForFE

    This is a mastapy class.
    """

    TYPE = _DRAW_STYLE_FOR_FE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DrawStyleForFE")

    class _Cast_DrawStyleForFE:
        """Special nested class for casting DrawStyleForFE to subclasses."""

        def __init__(
            self: "DrawStyleForFE._Cast_DrawStyleForFE", parent: "DrawStyleForFE"
        ):
            self._parent = parent

        @property
        def draw_style_for_fe(
            self: "DrawStyleForFE._Cast_DrawStyleForFE",
        ) -> "DrawStyleForFE":
            return self._parent

        def __getattr__(self: "DrawStyleForFE._Cast_DrawStyleForFE", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DrawStyleForFE.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def grounded_nodes(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.GroundedNodes

        if temp is None:
            return False

        return temp

    @grounded_nodes.setter
    @enforce_parameter_types
    def grounded_nodes(self: Self, value: "bool"):
        self.wrapped.GroundedNodes = bool(value) if value is not None else False

    @property
    def highlight_bad_elements(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.HighlightBadElements

        if temp is None:
            return False

        return temp

    @highlight_bad_elements.setter
    @enforce_parameter_types
    def highlight_bad_elements(self: Self, value: "bool"):
        self.wrapped.HighlightBadElements = bool(value) if value is not None else False

    @property
    def line_option(self: Self) -> "_59.FEMeshElementEntityOption":
        """mastapy.nodal_analysis.FEMeshElementEntityOption"""
        temp = self.wrapped.LineOption

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.FEMeshElementEntityOption"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis._59", "FEMeshElementEntityOption"
        )(value)

    @line_option.setter
    @enforce_parameter_types
    def line_option(self: Self, value: "_59.FEMeshElementEntityOption"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.NodalAnalysis.FEMeshElementEntityOption"
        )
        self.wrapped.LineOption = value

    @property
    def node_size(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NodeSize

        if temp is None:
            return 0

        return temp

    @node_size.setter
    @enforce_parameter_types
    def node_size(self: Self, value: "int"):
        self.wrapped.NodeSize = int(value) if value is not None else 0

    @property
    def rigid_elements(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.RigidElements

        if temp is None:
            return False

        return temp

    @rigid_elements.setter
    @enforce_parameter_types
    def rigid_elements(self: Self, value: "bool"):
        self.wrapped.RigidElements = bool(value) if value is not None else False

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
    def cast_to(self: Self) -> "DrawStyleForFE._Cast_DrawStyleForFE":
        return self._Cast_DrawStyleForFE(self)
