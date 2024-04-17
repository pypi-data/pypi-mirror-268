"""ResultsForMultipleOrdersForFESurface"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
    _5874,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RESULTS_FOR_MULTIPLE_ORDERS_FOR_FE_SURFACE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults",
    "ResultsForMultipleOrdersForFESurface",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5872,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ResultsForMultipleOrdersForFESurface",)


Self = TypeVar("Self", bound="ResultsForMultipleOrdersForFESurface")


class ResultsForMultipleOrdersForFESurface(_5874.ResultsForMultipleOrders):
    """ResultsForMultipleOrdersForFESurface

    This is a mastapy class.
    """

    TYPE = _RESULTS_FOR_MULTIPLE_ORDERS_FOR_FE_SURFACE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ResultsForMultipleOrdersForFESurface")

    class _Cast_ResultsForMultipleOrdersForFESurface:
        """Special nested class for casting ResultsForMultipleOrdersForFESurface to subclasses."""

        def __init__(
            self: "ResultsForMultipleOrdersForFESurface._Cast_ResultsForMultipleOrdersForFESurface",
            parent: "ResultsForMultipleOrdersForFESurface",
        ):
            self._parent = parent

        @property
        def results_for_multiple_orders(
            self: "ResultsForMultipleOrdersForFESurface._Cast_ResultsForMultipleOrdersForFESurface",
        ) -> "_5874.ResultsForMultipleOrders":
            return self._parent._cast(_5874.ResultsForMultipleOrders)

        @property
        def results_for_multiple_orders_for_fe_surface(
            self: "ResultsForMultipleOrdersForFESurface._Cast_ResultsForMultipleOrdersForFESurface",
        ) -> "ResultsForMultipleOrdersForFESurface":
            return self._parent

        def __getattr__(
            self: "ResultsForMultipleOrdersForFESurface._Cast_ResultsForMultipleOrdersForFESurface",
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
        self: Self, instance_to_wrap: "ResultsForMultipleOrdersForFESurface.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fe_surfaces(
        self: Self,
    ) -> "List[_5872.HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FESurfaces

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ResultsForMultipleOrdersForFESurface._Cast_ResultsForMultipleOrdersForFESurface":
        return self._Cast_ResultsForMultipleOrdersForFESurface(self)
