"""SteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.analysis_cases import _7558
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "SteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543
    from mastapy.system_model.analyses_and_results import _2658


__docformat__ = "restructuredtext en"
__all__ = ("SteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="SteadyStateSynchronousResponseAtASpeed")


class SteadyStateSynchronousResponseAtASpeed(_7558.StaticLoadAnalysisCase):
    """SteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_SteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting SteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "SteadyStateSynchronousResponseAtASpeed._Cast_SteadyStateSynchronousResponseAtASpeed",
            parent: "SteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def static_load_analysis_case(
            self: "SteadyStateSynchronousResponseAtASpeed._Cast_SteadyStateSynchronousResponseAtASpeed",
        ) -> "_7558.StaticLoadAnalysisCase":
            return self._parent._cast(_7558.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "SteadyStateSynchronousResponseAtASpeed._Cast_SteadyStateSynchronousResponseAtASpeed",
        ) -> "_7543.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.AnalysisCase)

        @property
        def context(
            self: "SteadyStateSynchronousResponseAtASpeed._Cast_SteadyStateSynchronousResponseAtASpeed",
        ) -> "_2658.Context":
            from mastapy.system_model.analyses_and_results import _2658

            return self._parent._cast(_2658.Context)

        @property
        def steady_state_synchronous_response_at_a_speed(
            self: "SteadyStateSynchronousResponseAtASpeed._Cast_SteadyStateSynchronousResponseAtASpeed",
        ) -> "SteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "SteadyStateSynchronousResponseAtASpeed._Cast_SteadyStateSynchronousResponseAtASpeed",
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
        self: Self, instance_to_wrap: "SteadyStateSynchronousResponseAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "SteadyStateSynchronousResponseAtASpeed._Cast_SteadyStateSynchronousResponseAtASpeed":
        return self._Cast_SteadyStateSynchronousResponseAtASpeed(self)
