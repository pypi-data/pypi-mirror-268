"""SteadyStateSynchronousResponseOnAShaftAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results import _2628
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults",
    "SteadyStateSynchronousResponseOnAShaftAnalysis",
)

if TYPE_CHECKING:
    from mastapy import _7561


__docformat__ = "restructuredtext en"
__all__ = ("SteadyStateSynchronousResponseOnAShaftAnalysis",)


Self = TypeVar("Self", bound="SteadyStateSynchronousResponseOnAShaftAnalysis")


class SteadyStateSynchronousResponseOnAShaftAnalysis(_2628.SingleAnalysis):
    """SteadyStateSynchronousResponseOnAShaftAnalysis

    This is a mastapy class.
    """

    TYPE = _STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SteadyStateSynchronousResponseOnAShaftAnalysis"
    )

    class _Cast_SteadyStateSynchronousResponseOnAShaftAnalysis:
        """Special nested class for casting SteadyStateSynchronousResponseOnAShaftAnalysis to subclasses."""

        def __init__(
            self: "SteadyStateSynchronousResponseOnAShaftAnalysis._Cast_SteadyStateSynchronousResponseOnAShaftAnalysis",
            parent: "SteadyStateSynchronousResponseOnAShaftAnalysis",
        ):
            self._parent = parent

        @property
        def single_analysis(
            self: "SteadyStateSynchronousResponseOnAShaftAnalysis._Cast_SteadyStateSynchronousResponseOnAShaftAnalysis",
        ) -> "_2628.SingleAnalysis":
            return self._parent._cast(_2628.SingleAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "SteadyStateSynchronousResponseOnAShaftAnalysis._Cast_SteadyStateSynchronousResponseOnAShaftAnalysis",
        ) -> "_7561.MarshalByRefObjectPermanent":
            from mastapy import _7561

            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def steady_state_synchronous_response_on_a_shaft_analysis(
            self: "SteadyStateSynchronousResponseOnAShaftAnalysis._Cast_SteadyStateSynchronousResponseOnAShaftAnalysis",
        ) -> "SteadyStateSynchronousResponseOnAShaftAnalysis":
            return self._parent

        def __getattr__(
            self: "SteadyStateSynchronousResponseOnAShaftAnalysis._Cast_SteadyStateSynchronousResponseOnAShaftAnalysis",
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
        instance_to_wrap: "SteadyStateSynchronousResponseOnAShaftAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "SteadyStateSynchronousResponseOnAShaftAnalysis._Cast_SteadyStateSynchronousResponseOnAShaftAnalysis":
        return self._Cast_SteadyStateSynchronousResponseOnAShaftAnalysis(self)
