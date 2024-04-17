"""CompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results import _2627
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "CompoundModalAnalysisAtASpeed"
)

if TYPE_CHECKING:
    from mastapy import _7561


__docformat__ = "restructuredtext en"
__all__ = ("CompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CompoundModalAnalysisAtASpeed")


class CompoundModalAnalysisAtASpeed(_2627.CompoundAnalysis):
    """CompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CompoundModalAnalysisAtASpeed")

    class _Cast_CompoundModalAnalysisAtASpeed:
        """Special nested class for casting CompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CompoundModalAnalysisAtASpeed._Cast_CompoundModalAnalysisAtASpeed",
            parent: "CompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def compound_analysis(
            self: "CompoundModalAnalysisAtASpeed._Cast_CompoundModalAnalysisAtASpeed",
        ) -> "_2627.CompoundAnalysis":
            return self._parent._cast(_2627.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "CompoundModalAnalysisAtASpeed._Cast_CompoundModalAnalysisAtASpeed",
        ) -> "_7561.MarshalByRefObjectPermanent":
            from mastapy import _7561

            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def compound_modal_analysis_at_a_speed(
            self: "CompoundModalAnalysisAtASpeed._Cast_CompoundModalAnalysisAtASpeed",
        ) -> "CompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CompoundModalAnalysisAtASpeed._Cast_CompoundModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CompoundModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CompoundModalAnalysisAtASpeed._Cast_CompoundModalAnalysisAtASpeed":
        return self._Cast_CompoundModalAnalysisAtASpeed(self)
