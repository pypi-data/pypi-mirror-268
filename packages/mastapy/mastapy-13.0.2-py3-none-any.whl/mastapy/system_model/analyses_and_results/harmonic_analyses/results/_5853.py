"""ExcitationSourceSelection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.results import _5854
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXCITATION_SOURCE_SELECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Results",
    "ExcitationSourceSelection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.results import (
        _5856,
    )
    from mastapy.math_utility import _1536


__docformat__ = "restructuredtext en"
__all__ = ("ExcitationSourceSelection",)


Self = TypeVar("Self", bound="ExcitationSourceSelection")


class ExcitationSourceSelection(_5854.ExcitationSourceSelectionBase):
    """ExcitationSourceSelection

    This is a mastapy class.
    """

    TYPE = _EXCITATION_SOURCE_SELECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ExcitationSourceSelection")

    class _Cast_ExcitationSourceSelection:
        """Special nested class for casting ExcitationSourceSelection to subclasses."""

        def __init__(
            self: "ExcitationSourceSelection._Cast_ExcitationSourceSelection",
            parent: "ExcitationSourceSelection",
        ):
            self._parent = parent

        @property
        def excitation_source_selection_base(
            self: "ExcitationSourceSelection._Cast_ExcitationSourceSelection",
        ) -> "_5854.ExcitationSourceSelectionBase":
            return self._parent._cast(_5854.ExcitationSourceSelectionBase)

        @property
        def excitation_source_selection(
            self: "ExcitationSourceSelection._Cast_ExcitationSourceSelection",
        ) -> "ExcitationSourceSelection":
            return self._parent

        def __getattr__(
            self: "ExcitationSourceSelection._Cast_ExcitationSourceSelection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ExcitationSourceSelection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def harmonic_selections(self: Self) -> "List[_5856.HarmonicSelection]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.results.HarmonicSelection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicSelections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

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

    def invert_is_included_in_excitations_selection(self: Self):
        """Method does not return."""
        self.wrapped.InvertIsIncludedInExcitationsSelection()

    def invert_is_shown_selection(self: Self):
        """Method does not return."""
        self.wrapped.InvertIsShownSelection()

    @enforce_parameter_types
    def include_only_harmonic_with_order(
        self: Self, order: "_1536.RoundedOrder"
    ) -> "bool":
        """bool

        Args:
            order (mastapy.math_utility.RoundedOrder)
        """
        method_result = self.wrapped.IncludeOnlyHarmonicWithOrder(
            order.wrapped if order else None
        )
        return method_result

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
    ) -> "ExcitationSourceSelection._Cast_ExcitationSourceSelection":
        return self._Cast_ExcitationSourceSelection(self)
