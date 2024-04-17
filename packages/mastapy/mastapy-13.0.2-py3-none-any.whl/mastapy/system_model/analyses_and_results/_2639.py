"""DynamicModelForSteadyStateSynchronousResponseAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results import _2628
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_MODEL_FOR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults",
    "DynamicModelForSteadyStateSynchronousResponseAnalysis",
)

if TYPE_CHECKING:
    from mastapy import _7561


__docformat__ = "restructuredtext en"
__all__ = ("DynamicModelForSteadyStateSynchronousResponseAnalysis",)


Self = TypeVar("Self", bound="DynamicModelForSteadyStateSynchronousResponseAnalysis")


class DynamicModelForSteadyStateSynchronousResponseAnalysis(_2628.SingleAnalysis):
    """DynamicModelForSteadyStateSynchronousResponseAnalysis

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_MODEL_FOR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_DynamicModelForSteadyStateSynchronousResponseAnalysis"
    )

    class _Cast_DynamicModelForSteadyStateSynchronousResponseAnalysis:
        """Special nested class for casting DynamicModelForSteadyStateSynchronousResponseAnalysis to subclasses."""

        def __init__(
            self: "DynamicModelForSteadyStateSynchronousResponseAnalysis._Cast_DynamicModelForSteadyStateSynchronousResponseAnalysis",
            parent: "DynamicModelForSteadyStateSynchronousResponseAnalysis",
        ):
            self._parent = parent

        @property
        def single_analysis(
            self: "DynamicModelForSteadyStateSynchronousResponseAnalysis._Cast_DynamicModelForSteadyStateSynchronousResponseAnalysis",
        ) -> "_2628.SingleAnalysis":
            return self._parent._cast(_2628.SingleAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "DynamicModelForSteadyStateSynchronousResponseAnalysis._Cast_DynamicModelForSteadyStateSynchronousResponseAnalysis",
        ) -> "_7561.MarshalByRefObjectPermanent":
            from mastapy import _7561

            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def dynamic_model_for_steady_state_synchronous_response_analysis(
            self: "DynamicModelForSteadyStateSynchronousResponseAnalysis._Cast_DynamicModelForSteadyStateSynchronousResponseAnalysis",
        ) -> "DynamicModelForSteadyStateSynchronousResponseAnalysis":
            return self._parent

        def __getattr__(
            self: "DynamicModelForSteadyStateSynchronousResponseAnalysis._Cast_DynamicModelForSteadyStateSynchronousResponseAnalysis",
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
        instance_to_wrap: "DynamicModelForSteadyStateSynchronousResponseAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "DynamicModelForSteadyStateSynchronousResponseAnalysis._Cast_DynamicModelForSteadyStateSynchronousResponseAnalysis":
        return self._Cast_DynamicModelForSteadyStateSynchronousResponseAnalysis(self)
