"""SteadyStateSynchronousResponseAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results import _2628
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STEADY_STATE_SYNCHRONOUS_RESPONSE_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults",
    "SteadyStateSynchronousResponseAnalysis",
)

if TYPE_CHECKING:
    from mastapy import _7561


__docformat__ = "restructuredtext en"
__all__ = ("SteadyStateSynchronousResponseAnalysis",)


Self = TypeVar("Self", bound="SteadyStateSynchronousResponseAnalysis")


class SteadyStateSynchronousResponseAnalysis(_2628.SingleAnalysis):
    """SteadyStateSynchronousResponseAnalysis

    This is a mastapy class.
    """

    TYPE = _STEADY_STATE_SYNCHRONOUS_RESPONSE_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SteadyStateSynchronousResponseAnalysis"
    )

    class _Cast_SteadyStateSynchronousResponseAnalysis:
        """Special nested class for casting SteadyStateSynchronousResponseAnalysis to subclasses."""

        def __init__(
            self: "SteadyStateSynchronousResponseAnalysis._Cast_SteadyStateSynchronousResponseAnalysis",
            parent: "SteadyStateSynchronousResponseAnalysis",
        ):
            self._parent = parent

        @property
        def single_analysis(
            self: "SteadyStateSynchronousResponseAnalysis._Cast_SteadyStateSynchronousResponseAnalysis",
        ) -> "_2628.SingleAnalysis":
            return self._parent._cast(_2628.SingleAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "SteadyStateSynchronousResponseAnalysis._Cast_SteadyStateSynchronousResponseAnalysis",
        ) -> "_7561.MarshalByRefObjectPermanent":
            from mastapy import _7561

            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def steady_state_synchronous_response_analysis(
            self: "SteadyStateSynchronousResponseAnalysis._Cast_SteadyStateSynchronousResponseAnalysis",
        ) -> "SteadyStateSynchronousResponseAnalysis":
            return self._parent

        def __getattr__(
            self: "SteadyStateSynchronousResponseAnalysis._Cast_SteadyStateSynchronousResponseAnalysis",
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
        self: Self, instance_to_wrap: "SteadyStateSynchronousResponseAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "SteadyStateSynchronousResponseAnalysis._Cast_SteadyStateSynchronousResponseAnalysis":
        return self._Cast_SteadyStateSynchronousResponseAnalysis(self)
