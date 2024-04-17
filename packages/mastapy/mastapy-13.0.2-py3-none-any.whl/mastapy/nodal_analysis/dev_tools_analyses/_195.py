"""FEModelTabDrawStyle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_MODEL_TAB_DRAW_STYLE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses", "FEModelTabDrawStyle"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.dev_tools_analyses import _181, _189, _191, _194


__docformat__ = "restructuredtext en"
__all__ = ("FEModelTabDrawStyle",)


Self = TypeVar("Self", bound="FEModelTabDrawStyle")


class FEModelTabDrawStyle(_0.APIBase):
    """FEModelTabDrawStyle

    This is a mastapy class.
    """

    TYPE = _FE_MODEL_TAB_DRAW_STYLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEModelTabDrawStyle")

    class _Cast_FEModelTabDrawStyle:
        """Special nested class for casting FEModelTabDrawStyle to subclasses."""

        def __init__(
            self: "FEModelTabDrawStyle._Cast_FEModelTabDrawStyle",
            parent: "FEModelTabDrawStyle",
        ):
            self._parent = parent

        @property
        def fe_model_harmonic_analysis_draw_style(
            self: "FEModelTabDrawStyle._Cast_FEModelTabDrawStyle",
        ) -> "_189.FEModelHarmonicAnalysisDrawStyle":
            from mastapy.nodal_analysis.dev_tools_analyses import _189

            return self._parent._cast(_189.FEModelHarmonicAnalysisDrawStyle)

        @property
        def fe_model_modal_analysis_draw_style(
            self: "FEModelTabDrawStyle._Cast_FEModelTabDrawStyle",
        ) -> "_191.FEModelModalAnalysisDrawStyle":
            from mastapy.nodal_analysis.dev_tools_analyses import _191

            return self._parent._cast(_191.FEModelModalAnalysisDrawStyle)

        @property
        def fe_model_static_analysis_draw_style(
            self: "FEModelTabDrawStyle._Cast_FEModelTabDrawStyle",
        ) -> "_194.FEModelStaticAnalysisDrawStyle":
            from mastapy.nodal_analysis.dev_tools_analyses import _194

            return self._parent._cast(_194.FEModelStaticAnalysisDrawStyle)

        @property
        def fe_model_tab_draw_style(
            self: "FEModelTabDrawStyle._Cast_FEModelTabDrawStyle",
        ) -> "FEModelTabDrawStyle":
            return self._parent

        def __getattr__(
            self: "FEModelTabDrawStyle._Cast_FEModelTabDrawStyle", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEModelTabDrawStyle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def draw_style(self: Self) -> "_181.DrawStyleForFE":
        """mastapy.nodal_analysis.dev_tools_analyses.DrawStyleForFE

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DrawStyle

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
    def cast_to(self: Self) -> "FEModelTabDrawStyle._Cast_FEModelTabDrawStyle":
        return self._Cast_FEModelTabDrawStyle(self)
