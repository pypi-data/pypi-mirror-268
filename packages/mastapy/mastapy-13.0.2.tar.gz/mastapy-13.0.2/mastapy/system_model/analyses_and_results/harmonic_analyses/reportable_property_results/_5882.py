"""ResultsForResponseOfANodeOnAHarmonic"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RESULTS_FOR_RESPONSE_OF_A_NODE_ON_A_HARMONIC = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults",
    "ResultsForResponseOfANodeOnAHarmonic",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5883,
        _5864,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ResultsForResponseOfANodeOnAHarmonic",)


Self = TypeVar("Self", bound="ResultsForResponseOfANodeOnAHarmonic")


class ResultsForResponseOfANodeOnAHarmonic(_0.APIBase):
    """ResultsForResponseOfANodeOnAHarmonic

    This is a mastapy class.
    """

    TYPE = _RESULTS_FOR_RESPONSE_OF_A_NODE_ON_A_HARMONIC
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ResultsForResponseOfANodeOnAHarmonic")

    class _Cast_ResultsForResponseOfANodeOnAHarmonic:
        """Special nested class for casting ResultsForResponseOfANodeOnAHarmonic to subclasses."""

        def __init__(
            self: "ResultsForResponseOfANodeOnAHarmonic._Cast_ResultsForResponseOfANodeOnAHarmonic",
            parent: "ResultsForResponseOfANodeOnAHarmonic",
        ):
            self._parent = parent

        @property
        def results_for_response_of_a_node_on_a_harmonic(
            self: "ResultsForResponseOfANodeOnAHarmonic._Cast_ResultsForResponseOfANodeOnAHarmonic",
        ) -> "ResultsForResponseOfANodeOnAHarmonic":
            return self._parent

        def __getattr__(
            self: "ResultsForResponseOfANodeOnAHarmonic._Cast_ResultsForResponseOfANodeOnAHarmonic",
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
        self: Self, instance_to_wrap: "ResultsForResponseOfANodeOnAHarmonic.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_magnitude(
        self: Self,
    ) -> "_5883.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularMagnitude

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def linear_magnitude(
        self: Self,
    ) -> "_5883.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearMagnitude

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def radial_angular_magnitude(
        self: Self,
    ) -> "_5883.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialAngularMagnitude

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def radial_magnitude(
        self: Self,
    ) -> "_5883.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialMagnitude

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def result_at_reference_speed(
        self: Self,
    ) -> "_5864.DataPointForResponseOfANodeAtAFrequencyToAHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.DataPointForResponseOfANodeAtAFrequencyToAHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultAtReferenceSpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def theta_x(
        self: Self,
    ) -> "_5883.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThetaX

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def theta_y(
        self: Self,
    ) -> "_5883.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThetaY

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def theta_z(
        self: Self,
    ) -> "_5883.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThetaZ

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def x(
        self: Self,
    ) -> "_5883.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.X

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def y(
        self: Self,
    ) -> "_5883.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Y

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def z(
        self: Self,
    ) -> "_5883.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Z

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def data_points(
        self: Self,
    ) -> "List[_5864.DataPointForResponseOfANodeAtAFrequencyToAHarmonic]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.DataPointForResponseOfANodeAtAFrequencyToAHarmonic]

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
    ) -> "ResultsForResponseOfANodeOnAHarmonic._Cast_ResultsForResponseOfANodeOnAHarmonic":
        return self._Cast_ResultsForResponseOfANodeOnAHarmonic(self)
