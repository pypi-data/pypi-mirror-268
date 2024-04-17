"""CompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results import _2627
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "CompoundModalAnalysisAtAStiffness"
)

if TYPE_CHECKING:
    from mastapy import _7561


__docformat__ = "restructuredtext en"
__all__ = ("CompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CompoundModalAnalysisAtAStiffness")


class CompoundModalAnalysisAtAStiffness(_2627.CompoundAnalysis):
    """CompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CompoundModalAnalysisAtAStiffness")

    class _Cast_CompoundModalAnalysisAtAStiffness:
        """Special nested class for casting CompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CompoundModalAnalysisAtAStiffness._Cast_CompoundModalAnalysisAtAStiffness",
            parent: "CompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def compound_analysis(
            self: "CompoundModalAnalysisAtAStiffness._Cast_CompoundModalAnalysisAtAStiffness",
        ) -> "_2627.CompoundAnalysis":
            return self._parent._cast(_2627.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "CompoundModalAnalysisAtAStiffness._Cast_CompoundModalAnalysisAtAStiffness",
        ) -> "_7561.MarshalByRefObjectPermanent":
            from mastapy import _7561

            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def compound_modal_analysis_at_a_stiffness(
            self: "CompoundModalAnalysisAtAStiffness._Cast_CompoundModalAnalysisAtAStiffness",
        ) -> "CompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CompoundModalAnalysisAtAStiffness._Cast_CompoundModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "CompoundModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CompoundModalAnalysisAtAStiffness._Cast_CompoundModalAnalysisAtAStiffness":
        return self._Cast_CompoundModalAnalysisAtAStiffness(self)
