"""ResultsForOrderIncludingNodes"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
    _5877,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RESULTS_FOR_ORDER_INCLUDING_NODES = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults",
    "ResultsForOrderIncludingNodes",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5871,
        _5880,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ResultsForOrderIncludingNodes",)


Self = TypeVar("Self", bound="ResultsForOrderIncludingNodes")


class ResultsForOrderIncludingNodes(_5877.ResultsForOrder):
    """ResultsForOrderIncludingNodes

    This is a mastapy class.
    """

    TYPE = _RESULTS_FOR_ORDER_INCLUDING_NODES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ResultsForOrderIncludingNodes")

    class _Cast_ResultsForOrderIncludingNodes:
        """Special nested class for casting ResultsForOrderIncludingNodes to subclasses."""

        def __init__(
            self: "ResultsForOrderIncludingNodes._Cast_ResultsForOrderIncludingNodes",
            parent: "ResultsForOrderIncludingNodes",
        ):
            self._parent = parent

        @property
        def results_for_order(
            self: "ResultsForOrderIncludingNodes._Cast_ResultsForOrderIncludingNodes",
        ) -> "_5877.ResultsForOrder":
            return self._parent._cast(_5877.ResultsForOrder)

        @property
        def results_for_order_including_surfaces(
            self: "ResultsForOrderIncludingNodes._Cast_ResultsForOrderIncludingNodes",
        ) -> "_5880.ResultsForOrderIncludingSurfaces":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
                _5880,
            )

            return self._parent._cast(_5880.ResultsForOrderIncludingSurfaces)

        @property
        def results_for_order_including_nodes(
            self: "ResultsForOrderIncludingNodes._Cast_ResultsForOrderIncludingNodes",
        ) -> "ResultsForOrderIncludingNodes":
            return self._parent

        def __getattr__(
            self: "ResultsForOrderIncludingNodes._Cast_ResultsForOrderIncludingNodes",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ResultsForOrderIncludingNodes.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def node_results_global_coordinate_system(
        self: Self,
    ) -> "List[_5871.HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeResultsGlobalCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def node_results_local_coordinate_system(
        self: Self,
    ) -> "List[_5871.HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeResultsLocalCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ResultsForOrderIncludingNodes._Cast_ResultsForOrderIncludingNodes":
        return self._Cast_ResultsForOrderIncludingNodes(self)
