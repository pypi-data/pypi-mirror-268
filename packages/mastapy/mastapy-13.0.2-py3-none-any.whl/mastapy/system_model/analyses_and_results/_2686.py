"""CompoundSteadyStateSynchronousResponseAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results import _2627
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults",
    "CompoundSteadyStateSynchronousResponseAnalysis",
)

if TYPE_CHECKING:
    from mastapy import _7561


__docformat__ = "restructuredtext en"
__all__ = ("CompoundSteadyStateSynchronousResponseAnalysis",)


Self = TypeVar("Self", bound="CompoundSteadyStateSynchronousResponseAnalysis")


class CompoundSteadyStateSynchronousResponseAnalysis(_2627.CompoundAnalysis):
    """CompoundSteadyStateSynchronousResponseAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CompoundSteadyStateSynchronousResponseAnalysis"
    )

    class _Cast_CompoundSteadyStateSynchronousResponseAnalysis:
        """Special nested class for casting CompoundSteadyStateSynchronousResponseAnalysis to subclasses."""

        def __init__(
            self: "CompoundSteadyStateSynchronousResponseAnalysis._Cast_CompoundSteadyStateSynchronousResponseAnalysis",
            parent: "CompoundSteadyStateSynchronousResponseAnalysis",
        ):
            self._parent = parent

        @property
        def compound_analysis(
            self: "CompoundSteadyStateSynchronousResponseAnalysis._Cast_CompoundSteadyStateSynchronousResponseAnalysis",
        ) -> "_2627.CompoundAnalysis":
            return self._parent._cast(_2627.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "CompoundSteadyStateSynchronousResponseAnalysis._Cast_CompoundSteadyStateSynchronousResponseAnalysis",
        ) -> "_7561.MarshalByRefObjectPermanent":
            from mastapy import _7561

            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def compound_steady_state_synchronous_response_analysis(
            self: "CompoundSteadyStateSynchronousResponseAnalysis._Cast_CompoundSteadyStateSynchronousResponseAnalysis",
        ) -> "CompoundSteadyStateSynchronousResponseAnalysis":
            return self._parent

        def __getattr__(
            self: "CompoundSteadyStateSynchronousResponseAnalysis._Cast_CompoundSteadyStateSynchronousResponseAnalysis",
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
        instance_to_wrap: "CompoundSteadyStateSynchronousResponseAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CompoundSteadyStateSynchronousResponseAnalysis._Cast_CompoundSteadyStateSynchronousResponseAnalysis":
        return self._Cast_CompoundSteadyStateSynchronousResponseAnalysis(self)
