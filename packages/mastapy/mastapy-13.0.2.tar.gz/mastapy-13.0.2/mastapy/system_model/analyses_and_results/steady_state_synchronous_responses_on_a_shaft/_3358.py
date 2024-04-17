"""SteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7558
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "SteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3099,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543
    from mastapy.system_model.analyses_and_results import _2658


__docformat__ = "restructuredtext en"
__all__ = ("SteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="SteadyStateSynchronousResponseOnAShaft")


class SteadyStateSynchronousResponseOnAShaft(_7558.StaticLoadAnalysisCase):
    """SteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_SteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting SteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "SteadyStateSynchronousResponseOnAShaft._Cast_SteadyStateSynchronousResponseOnAShaft",
            parent: "SteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def static_load_analysis_case(
            self: "SteadyStateSynchronousResponseOnAShaft._Cast_SteadyStateSynchronousResponseOnAShaft",
        ) -> "_7558.StaticLoadAnalysisCase":
            return self._parent._cast(_7558.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "SteadyStateSynchronousResponseOnAShaft._Cast_SteadyStateSynchronousResponseOnAShaft",
        ) -> "_7543.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.AnalysisCase)

        @property
        def context(
            self: "SteadyStateSynchronousResponseOnAShaft._Cast_SteadyStateSynchronousResponseOnAShaft",
        ) -> "_2658.Context":
            from mastapy.system_model.analyses_and_results import _2658

            return self._parent._cast(_2658.Context)

        @property
        def steady_state_synchronous_response_on_a_shaft(
            self: "SteadyStateSynchronousResponseOnAShaft._Cast_SteadyStateSynchronousResponseOnAShaft",
        ) -> "SteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "SteadyStateSynchronousResponseOnAShaft._Cast_SteadyStateSynchronousResponseOnAShaft",
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
        self: Self, instance_to_wrap: "SteadyStateSynchronousResponseOnAShaft.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def options(self: Self) -> "_3099.SteadyStateSynchronousResponseOptions":
        """mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SteadyStateSynchronousResponseOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Options

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SteadyStateSynchronousResponseOnAShaft._Cast_SteadyStateSynchronousResponseOnAShaft":
        return self._Cast_SteadyStateSynchronousResponseOnAShaft(self)
