"""ResultsForResponseOfAComponentOrSurfaceInAHarmonic"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RESULTS_FOR_RESPONSE_OF_A_COMPONENT_OR_SURFACE_IN_A_HARMONIC = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults",
    "ResultsForResponseOfAComponentOrSurfaceInAHarmonic",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5883,
        _5863,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ResultsForResponseOfAComponentOrSurfaceInAHarmonic",)


Self = TypeVar("Self", bound="ResultsForResponseOfAComponentOrSurfaceInAHarmonic")


class ResultsForResponseOfAComponentOrSurfaceInAHarmonic(_0.APIBase):
    """ResultsForResponseOfAComponentOrSurfaceInAHarmonic

    This is a mastapy class.
    """

    TYPE = _RESULTS_FOR_RESPONSE_OF_A_COMPONENT_OR_SURFACE_IN_A_HARMONIC
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ResultsForResponseOfAComponentOrSurfaceInAHarmonic"
    )

    class _Cast_ResultsForResponseOfAComponentOrSurfaceInAHarmonic:
        """Special nested class for casting ResultsForResponseOfAComponentOrSurfaceInAHarmonic to subclasses."""

        def __init__(
            self: "ResultsForResponseOfAComponentOrSurfaceInAHarmonic._Cast_ResultsForResponseOfAComponentOrSurfaceInAHarmonic",
            parent: "ResultsForResponseOfAComponentOrSurfaceInAHarmonic",
        ):
            self._parent = parent

        @property
        def results_for_response_of_a_component_or_surface_in_a_harmonic(
            self: "ResultsForResponseOfAComponentOrSurfaceInAHarmonic._Cast_ResultsForResponseOfAComponentOrSurfaceInAHarmonic",
        ) -> "ResultsForResponseOfAComponentOrSurfaceInAHarmonic":
            return self._parent

        def __getattr__(
            self: "ResultsForResponseOfAComponentOrSurfaceInAHarmonic._Cast_ResultsForResponseOfAComponentOrSurfaceInAHarmonic",
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
        instance_to_wrap: "ResultsForResponseOfAComponentOrSurfaceInAHarmonic.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def magnitude(
        self: Self,
    ) -> "_5883.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Magnitude

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def result_at_reference_speed(
        self: Self,
    ) -> "_5863.DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultAtReferenceSpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def data_points(
        self: Self,
    ) -> "List[_5863.DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DataPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ResultsForResponseOfAComponentOrSurfaceInAHarmonic._Cast_ResultsForResponseOfAComponentOrSurfaceInAHarmonic":
        return self._Cast_ResultsForResponseOfAComponentOrSurfaceInAHarmonic(self)
