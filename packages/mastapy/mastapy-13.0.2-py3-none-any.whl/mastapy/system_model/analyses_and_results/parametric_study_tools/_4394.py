"""ParametricStudyHistogram"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.report import _1767
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARAMETRIC_STUDY_HISTOGRAM = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ParametricStudyHistogram",
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1778, _1770


__docformat__ = "restructuredtext en"
__all__ = ("ParametricStudyHistogram",)


Self = TypeVar("Self", bound="ParametricStudyHistogram")


class ParametricStudyHistogram(_1767.CustomReportDefinitionItem):
    """ParametricStudyHistogram

    This is a mastapy class.
    """

    TYPE = _PARAMETRIC_STUDY_HISTOGRAM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ParametricStudyHistogram")

    class _Cast_ParametricStudyHistogram:
        """Special nested class for casting ParametricStudyHistogram to subclasses."""

        def __init__(
            self: "ParametricStudyHistogram._Cast_ParametricStudyHistogram",
            parent: "ParametricStudyHistogram",
        ):
            self._parent = parent

        @property
        def custom_report_definition_item(
            self: "ParametricStudyHistogram._Cast_ParametricStudyHistogram",
        ) -> "_1767.CustomReportDefinitionItem":
            return self._parent._cast(_1767.CustomReportDefinitionItem)

        @property
        def custom_report_nameable_item(
            self: "ParametricStudyHistogram._Cast_ParametricStudyHistogram",
        ) -> "_1778.CustomReportNameableItem":
            from mastapy.utility.report import _1778

            return self._parent._cast(_1778.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "ParametricStudyHistogram._Cast_ParametricStudyHistogram",
        ) -> "_1770.CustomReportItem":
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportItem)

        @property
        def parametric_study_histogram(
            self: "ParametricStudyHistogram._Cast_ParametricStudyHistogram",
        ) -> "ParametricStudyHistogram":
            return self._parent

        def __getattr__(
            self: "ParametricStudyHistogram._Cast_ParametricStudyHistogram", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ParametricStudyHistogram.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def height(self: Self) -> "int":
        """int"""
        temp = self.wrapped.Height

        if temp is None:
            return 0

        return temp

    @height.setter
    @enforce_parameter_types
    def height(self: Self, value: "int"):
        self.wrapped.Height = int(value) if value is not None else 0

    @property
    def number_of_bins(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfBins

        if temp is None:
            return 0

        return temp

    @number_of_bins.setter
    @enforce_parameter_types
    def number_of_bins(self: Self, value: "int"):
        self.wrapped.NumberOfBins = int(value) if value is not None else 0

    @property
    def use_bin_range_for_label(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseBinRangeForLabel

        if temp is None:
            return False

        return temp

    @use_bin_range_for_label.setter
    @enforce_parameter_types
    def use_bin_range_for_label(self: Self, value: "bool"):
        self.wrapped.UseBinRangeForLabel = bool(value) if value is not None else False

    @property
    def width(self: Self) -> "int":
        """int"""
        temp = self.wrapped.Width

        if temp is None:
            return 0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: Self, value: "int"):
        self.wrapped.Width = int(value) if value is not None else 0

    @property
    def cast_to(
        self: Self,
    ) -> "ParametricStudyHistogram._Cast_ParametricStudyHistogram":
        return self._Cast_ParametricStudyHistogram(self)
