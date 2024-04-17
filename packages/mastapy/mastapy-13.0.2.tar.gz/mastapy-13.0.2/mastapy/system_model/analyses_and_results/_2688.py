"""CompoundSteadyStateSynchronousResponseOnAShaftAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results import _2627
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults",
    "CompoundSteadyStateSynchronousResponseOnAShaftAnalysis",
)

if TYPE_CHECKING:
    from mastapy import _7561


__docformat__ = "restructuredtext en"
__all__ = ("CompoundSteadyStateSynchronousResponseOnAShaftAnalysis",)


Self = TypeVar("Self", bound="CompoundSteadyStateSynchronousResponseOnAShaftAnalysis")


class CompoundSteadyStateSynchronousResponseOnAShaftAnalysis(_2627.CompoundAnalysis):
    """CompoundSteadyStateSynchronousResponseOnAShaftAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CompoundSteadyStateSynchronousResponseOnAShaftAnalysis",
    )

    class _Cast_CompoundSteadyStateSynchronousResponseOnAShaftAnalysis:
        """Special nested class for casting CompoundSteadyStateSynchronousResponseOnAShaftAnalysis to subclasses."""

        def __init__(
            self: "CompoundSteadyStateSynchronousResponseOnAShaftAnalysis._Cast_CompoundSteadyStateSynchronousResponseOnAShaftAnalysis",
            parent: "CompoundSteadyStateSynchronousResponseOnAShaftAnalysis",
        ):
            self._parent = parent

        @property
        def compound_analysis(
            self: "CompoundSteadyStateSynchronousResponseOnAShaftAnalysis._Cast_CompoundSteadyStateSynchronousResponseOnAShaftAnalysis",
        ) -> "_2627.CompoundAnalysis":
            return self._parent._cast(_2627.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "CompoundSteadyStateSynchronousResponseOnAShaftAnalysis._Cast_CompoundSteadyStateSynchronousResponseOnAShaftAnalysis",
        ) -> "_7561.MarshalByRefObjectPermanent":
            from mastapy import _7561

            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def compound_steady_state_synchronous_response_on_a_shaft_analysis(
            self: "CompoundSteadyStateSynchronousResponseOnAShaftAnalysis._Cast_CompoundSteadyStateSynchronousResponseOnAShaftAnalysis",
        ) -> "CompoundSteadyStateSynchronousResponseOnAShaftAnalysis":
            return self._parent

        def __getattr__(
            self: "CompoundSteadyStateSynchronousResponseOnAShaftAnalysis._Cast_CompoundSteadyStateSynchronousResponseOnAShaftAnalysis",
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
        instance_to_wrap: "CompoundSteadyStateSynchronousResponseOnAShaftAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CompoundSteadyStateSynchronousResponseOnAShaftAnalysis._Cast_CompoundSteadyStateSynchronousResponseOnAShaftAnalysis":
        return self._Cast_CompoundSteadyStateSynchronousResponseOnAShaftAnalysis(self)
