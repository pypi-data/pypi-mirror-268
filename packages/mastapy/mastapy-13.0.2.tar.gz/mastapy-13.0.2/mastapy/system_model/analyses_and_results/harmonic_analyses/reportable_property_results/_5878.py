"""ResultsForOrderIncludingGroups"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
    _5877,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RESULTS_FOR_ORDER_INCLUDING_GROUPS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults",
    "ResultsForOrderIncludingGroups",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5869,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ResultsForOrderIncludingGroups",)


Self = TypeVar("Self", bound="ResultsForOrderIncludingGroups")


class ResultsForOrderIncludingGroups(_5877.ResultsForOrder):
    """ResultsForOrderIncludingGroups

    This is a mastapy class.
    """

    TYPE = _RESULTS_FOR_ORDER_INCLUDING_GROUPS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ResultsForOrderIncludingGroups")

    class _Cast_ResultsForOrderIncludingGroups:
        """Special nested class for casting ResultsForOrderIncludingGroups to subclasses."""

        def __init__(
            self: "ResultsForOrderIncludingGroups._Cast_ResultsForOrderIncludingGroups",
            parent: "ResultsForOrderIncludingGroups",
        ):
            self._parent = parent

        @property
        def results_for_order(
            self: "ResultsForOrderIncludingGroups._Cast_ResultsForOrderIncludingGroups",
        ) -> "_5877.ResultsForOrder":
            return self._parent._cast(_5877.ResultsForOrder)

        @property
        def results_for_order_including_groups(
            self: "ResultsForOrderIncludingGroups._Cast_ResultsForOrderIncludingGroups",
        ) -> "ResultsForOrderIncludingGroups":
            return self._parent

        def __getattr__(
            self: "ResultsForOrderIncludingGroups._Cast_ResultsForOrderIncludingGroups",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ResultsForOrderIncludingGroups.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def groups(
        self: Self,
    ) -> "List[_5869.HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Groups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ResultsForOrderIncludingGroups._Cast_ResultsForOrderIncludingGroups":
        return self._Cast_ResultsForOrderIncludingGroups(self)
