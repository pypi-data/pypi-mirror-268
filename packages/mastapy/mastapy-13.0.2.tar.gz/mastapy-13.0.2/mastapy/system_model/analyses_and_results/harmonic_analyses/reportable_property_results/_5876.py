"""ResultsForMultipleOrdersForGroups"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
    _5874,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RESULTS_FOR_MULTIPLE_ORDERS_FOR_GROUPS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults",
    "ResultsForMultipleOrdersForGroups",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5869,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ResultsForMultipleOrdersForGroups",)


Self = TypeVar("Self", bound="ResultsForMultipleOrdersForGroups")


class ResultsForMultipleOrdersForGroups(_5874.ResultsForMultipleOrders):
    """ResultsForMultipleOrdersForGroups

    This is a mastapy class.
    """

    TYPE = _RESULTS_FOR_MULTIPLE_ORDERS_FOR_GROUPS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ResultsForMultipleOrdersForGroups")

    class _Cast_ResultsForMultipleOrdersForGroups:
        """Special nested class for casting ResultsForMultipleOrdersForGroups to subclasses."""

        def __init__(
            self: "ResultsForMultipleOrdersForGroups._Cast_ResultsForMultipleOrdersForGroups",
            parent: "ResultsForMultipleOrdersForGroups",
        ):
            self._parent = parent

        @property
        def results_for_multiple_orders(
            self: "ResultsForMultipleOrdersForGroups._Cast_ResultsForMultipleOrdersForGroups",
        ) -> "_5874.ResultsForMultipleOrders":
            return self._parent._cast(_5874.ResultsForMultipleOrders)

        @property
        def results_for_multiple_orders_for_groups(
            self: "ResultsForMultipleOrdersForGroups._Cast_ResultsForMultipleOrdersForGroups",
        ) -> "ResultsForMultipleOrdersForGroups":
            return self._parent

        def __getattr__(
            self: "ResultsForMultipleOrdersForGroups._Cast_ResultsForMultipleOrdersForGroups",
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
        self: Self, instance_to_wrap: "ResultsForMultipleOrdersForGroups.TYPE"
    ):
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
    ) -> "ResultsForMultipleOrdersForGroups._Cast_ResultsForMultipleOrdersForGroups":
        return self._Cast_ResultsForMultipleOrdersForGroups(self)
