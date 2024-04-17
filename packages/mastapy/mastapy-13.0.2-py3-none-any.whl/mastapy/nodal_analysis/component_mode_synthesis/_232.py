"""CMSResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CMS_RESULTS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis", "CMSResults"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.component_mode_synthesis import _233, _234, _235, _238


__docformat__ = "restructuredtext en"
__all__ = ("CMSResults",)


Self = TypeVar("Self", bound="CMSResults")


class CMSResults(_0.APIBase):
    """CMSResults

    This is a mastapy class.
    """

    TYPE = _CMS_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CMSResults")

    class _Cast_CMSResults:
        """Special nested class for casting CMSResults to subclasses."""

        def __init__(self: "CMSResults._Cast_CMSResults", parent: "CMSResults"):
            self._parent = parent

        @property
        def harmonic_cms_results(
            self: "CMSResults._Cast_CMSResults",
        ) -> "_233.HarmonicCMSResults":
            from mastapy.nodal_analysis.component_mode_synthesis import _233

            return self._parent._cast(_233.HarmonicCMSResults)

        @property
        def modal_cms_results(
            self: "CMSResults._Cast_CMSResults",
        ) -> "_234.ModalCMSResults":
            from mastapy.nodal_analysis.component_mode_synthesis import _234

            return self._parent._cast(_234.ModalCMSResults)

        @property
        def real_cms_results(
            self: "CMSResults._Cast_CMSResults",
        ) -> "_235.RealCMSResults":
            from mastapy.nodal_analysis.component_mode_synthesis import _235

            return self._parent._cast(_235.RealCMSResults)

        @property
        def static_cms_results(
            self: "CMSResults._Cast_CMSResults",
        ) -> "_238.StaticCMSResults":
            from mastapy.nodal_analysis.component_mode_synthesis import _238

            return self._parent._cast(_238.StaticCMSResults)

        @property
        def cms_results(self: "CMSResults._Cast_CMSResults") -> "CMSResults":
            return self._parent

        def __getattr__(self: "CMSResults._Cast_CMSResults", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CMSResults.TYPE"):
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

    def calculate_displacements(self: Self):
        """Method does not return."""
        self.wrapped.CalculateDisplacements()

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
    def cast_to(self: Self) -> "CMSResults._Cast_CMSResults":
        return self._Cast_CMSResults(self)
