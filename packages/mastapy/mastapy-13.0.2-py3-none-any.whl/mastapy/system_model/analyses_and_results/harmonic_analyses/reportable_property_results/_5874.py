"""ResultsForMultipleOrders"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RESULTS_FOR_MULTIPLE_ORDERS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults",
    "ResultsForMultipleOrders",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5875,
        _5876,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ResultsForMultipleOrders",)


Self = TypeVar("Self", bound="ResultsForMultipleOrders")


class ResultsForMultipleOrders(_0.APIBase):
    """ResultsForMultipleOrders

    This is a mastapy class.
    """

    TYPE = _RESULTS_FOR_MULTIPLE_ORDERS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ResultsForMultipleOrders")

    class _Cast_ResultsForMultipleOrders:
        """Special nested class for casting ResultsForMultipleOrders to subclasses."""

        def __init__(
            self: "ResultsForMultipleOrders._Cast_ResultsForMultipleOrders",
            parent: "ResultsForMultipleOrders",
        ):
            self._parent = parent

        @property
        def results_for_multiple_orders_for_fe_surface(
            self: "ResultsForMultipleOrders._Cast_ResultsForMultipleOrders",
        ) -> "_5875.ResultsForMultipleOrdersForFESurface":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
                _5875,
            )

            return self._parent._cast(_5875.ResultsForMultipleOrdersForFESurface)

        @property
        def results_for_multiple_orders_for_groups(
            self: "ResultsForMultipleOrders._Cast_ResultsForMultipleOrders",
        ) -> "_5876.ResultsForMultipleOrdersForGroups":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
                _5876,
            )

            return self._parent._cast(_5876.ResultsForMultipleOrdersForGroups)

        @property
        def results_for_multiple_orders(
            self: "ResultsForMultipleOrders._Cast_ResultsForMultipleOrders",
        ) -> "ResultsForMultipleOrders":
            return self._parent

        def __getattr__(
            self: "ResultsForMultipleOrders._Cast_ResultsForMultipleOrders", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ResultsForMultipleOrders.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def combined_excitations_harmonics_and_orders(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CombinedExcitationsHarmonicsAndOrders

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ResultsForMultipleOrders._Cast_ResultsForMultipleOrders":
        return self._Cast_ResultsForMultipleOrders(self)
