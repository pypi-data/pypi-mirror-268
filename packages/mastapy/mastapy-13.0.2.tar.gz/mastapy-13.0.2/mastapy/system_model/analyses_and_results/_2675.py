"""CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results import _2627
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_DYNAMIC_MODEL_FOR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults",
        "CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy import _7561


__docformat__ = "restructuredtext en"
__all__ = ("CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis",)


Self = TypeVar(
    "Self", bound="CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis"
)


class CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis(
    _2627.CompoundAnalysis
):
    """CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_DYNAMIC_MODEL_FOR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis",
    )

    class _Cast_CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis:
        """Special nested class for casting CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis to subclasses."""

        def __init__(
            self: "CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis._Cast_CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis",
            parent: "CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis",
        ):
            self._parent = parent

        @property
        def compound_analysis(
            self: "CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis._Cast_CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis",
        ) -> "_2627.CompoundAnalysis":
            return self._parent._cast(_2627.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis._Cast_CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis",
        ) -> "_7561.MarshalByRefObjectPermanent":
            from mastapy import _7561

            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def compound_dynamic_model_for_steady_state_synchronous_response_analysis(
            self: "CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis._Cast_CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis",
        ) -> "CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis":
            return self._parent

        def __getattr__(
            self: "CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis._Cast_CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis",
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
        instance_to_wrap: "CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis._Cast_CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis":
        return self._Cast_CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis(
            self
        )
