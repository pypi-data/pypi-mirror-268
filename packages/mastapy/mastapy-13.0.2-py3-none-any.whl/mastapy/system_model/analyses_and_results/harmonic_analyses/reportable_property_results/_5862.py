"""AbstractSingleWhineAnalysisResultsPropertyAccessor"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SINGLE_WHINE_ANALYSIS_RESULTS_PROPERTY_ACCESSOR = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults",
    "AbstractSingleWhineAnalysisResultsPropertyAccessor",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5866,
        _5885,
        _5886,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractSingleWhineAnalysisResultsPropertyAccessor",)


Self = TypeVar("Self", bound="AbstractSingleWhineAnalysisResultsPropertyAccessor")


class AbstractSingleWhineAnalysisResultsPropertyAccessor(_0.APIBase):
    """AbstractSingleWhineAnalysisResultsPropertyAccessor

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SINGLE_WHINE_ANALYSIS_RESULTS_PROPERTY_ACCESSOR
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractSingleWhineAnalysisResultsPropertyAccessor"
    )

    class _Cast_AbstractSingleWhineAnalysisResultsPropertyAccessor:
        """Special nested class for casting AbstractSingleWhineAnalysisResultsPropertyAccessor to subclasses."""

        def __init__(
            self: "AbstractSingleWhineAnalysisResultsPropertyAccessor._Cast_AbstractSingleWhineAnalysisResultsPropertyAccessor",
            parent: "AbstractSingleWhineAnalysisResultsPropertyAccessor",
        ):
            self._parent = parent

        @property
        def fe_part_single_whine_analysis_results_property_accessor(
            self: "AbstractSingleWhineAnalysisResultsPropertyAccessor._Cast_AbstractSingleWhineAnalysisResultsPropertyAccessor",
        ) -> "_5866.FEPartSingleWhineAnalysisResultsPropertyAccessor":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
                _5866,
            )

            return self._parent._cast(
                _5866.FEPartSingleWhineAnalysisResultsPropertyAccessor
            )

        @property
        def root_assembly_single_whine_analysis_results_property_accessor(
            self: "AbstractSingleWhineAnalysisResultsPropertyAccessor._Cast_AbstractSingleWhineAnalysisResultsPropertyAccessor",
        ) -> "_5885.RootAssemblySingleWhineAnalysisResultsPropertyAccessor":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
                _5885,
            )

            return self._parent._cast(
                _5885.RootAssemblySingleWhineAnalysisResultsPropertyAccessor
            )

        @property
        def single_whine_analysis_results_property_accessor(
            self: "AbstractSingleWhineAnalysisResultsPropertyAccessor._Cast_AbstractSingleWhineAnalysisResultsPropertyAccessor",
        ) -> "_5886.SingleWhineAnalysisResultsPropertyAccessor":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
                _5886,
            )

            return self._parent._cast(_5886.SingleWhineAnalysisResultsPropertyAccessor)

        @property
        def abstract_single_whine_analysis_results_property_accessor(
            self: "AbstractSingleWhineAnalysisResultsPropertyAccessor._Cast_AbstractSingleWhineAnalysisResultsPropertyAccessor",
        ) -> "AbstractSingleWhineAnalysisResultsPropertyAccessor":
            return self._parent

        def __getattr__(
            self: "AbstractSingleWhineAnalysisResultsPropertyAccessor._Cast_AbstractSingleWhineAnalysisResultsPropertyAccessor",
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
        instance_to_wrap: "AbstractSingleWhineAnalysisResultsPropertyAccessor.TYPE",
    ):
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
    def cast_to(
        self: Self,
    ) -> "AbstractSingleWhineAnalysisResultsPropertyAccessor._Cast_AbstractSingleWhineAnalysisResultsPropertyAccessor":
        return self._Cast_AbstractSingleWhineAnalysisResultsPropertyAccessor(self)
