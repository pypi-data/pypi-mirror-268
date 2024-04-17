"""CompoundSteadyStateSynchronousResponseAtASpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results import _2627
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults",
    "CompoundSteadyStateSynchronousResponseAtASpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy import _7561


__docformat__ = "restructuredtext en"
__all__ = ("CompoundSteadyStateSynchronousResponseAtASpeedAnalysis",)


Self = TypeVar("Self", bound="CompoundSteadyStateSynchronousResponseAtASpeedAnalysis")


class CompoundSteadyStateSynchronousResponseAtASpeedAnalysis(_2627.CompoundAnalysis):
    """CompoundSteadyStateSynchronousResponseAtASpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CompoundSteadyStateSynchronousResponseAtASpeedAnalysis",
    )

    class _Cast_CompoundSteadyStateSynchronousResponseAtASpeedAnalysis:
        """Special nested class for casting CompoundSteadyStateSynchronousResponseAtASpeedAnalysis to subclasses."""

        def __init__(
            self: "CompoundSteadyStateSynchronousResponseAtASpeedAnalysis._Cast_CompoundSteadyStateSynchronousResponseAtASpeedAnalysis",
            parent: "CompoundSteadyStateSynchronousResponseAtASpeedAnalysis",
        ):
            self._parent = parent

        @property
        def compound_analysis(
            self: "CompoundSteadyStateSynchronousResponseAtASpeedAnalysis._Cast_CompoundSteadyStateSynchronousResponseAtASpeedAnalysis",
        ) -> "_2627.CompoundAnalysis":
            return self._parent._cast(_2627.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "CompoundSteadyStateSynchronousResponseAtASpeedAnalysis._Cast_CompoundSteadyStateSynchronousResponseAtASpeedAnalysis",
        ) -> "_7561.MarshalByRefObjectPermanent":
            from mastapy import _7561

            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def compound_steady_state_synchronous_response_at_a_speed_analysis(
            self: "CompoundSteadyStateSynchronousResponseAtASpeedAnalysis._Cast_CompoundSteadyStateSynchronousResponseAtASpeedAnalysis",
        ) -> "CompoundSteadyStateSynchronousResponseAtASpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CompoundSteadyStateSynchronousResponseAtASpeedAnalysis._Cast_CompoundSteadyStateSynchronousResponseAtASpeedAnalysis",
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
        instance_to_wrap: "CompoundSteadyStateSynchronousResponseAtASpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CompoundSteadyStateSynchronousResponseAtASpeedAnalysis._Cast_CompoundSteadyStateSynchronousResponseAtASpeedAnalysis":
        return self._Cast_CompoundSteadyStateSynchronousResponseAtASpeedAnalysis(self)
