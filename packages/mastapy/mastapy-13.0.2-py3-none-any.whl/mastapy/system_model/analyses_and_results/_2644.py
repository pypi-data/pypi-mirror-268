"""ModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results import _2628
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "ModalAnalysisAtASpeed"
)

if TYPE_CHECKING:
    from mastapy import _7561


__docformat__ = "restructuredtext en"
__all__ = ("ModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ModalAnalysisAtASpeed")


class ModalAnalysisAtASpeed(_2628.SingleAnalysis):
    """ModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ModalAnalysisAtASpeed")

    class _Cast_ModalAnalysisAtASpeed:
        """Special nested class for casting ModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ModalAnalysisAtASpeed._Cast_ModalAnalysisAtASpeed",
            parent: "ModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def single_analysis(
            self: "ModalAnalysisAtASpeed._Cast_ModalAnalysisAtASpeed",
        ) -> "_2628.SingleAnalysis":
            return self._parent._cast(_2628.SingleAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "ModalAnalysisAtASpeed._Cast_ModalAnalysisAtASpeed",
        ) -> "_7561.MarshalByRefObjectPermanent":
            from mastapy import _7561

            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def modal_analysis_at_a_speed(
            self: "ModalAnalysisAtASpeed._Cast_ModalAnalysisAtASpeed",
        ) -> "ModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ModalAnalysisAtASpeed._Cast_ModalAnalysisAtASpeed", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ModalAnalysisAtASpeed._Cast_ModalAnalysisAtASpeed":
        return self._Cast_ModalAnalysisAtASpeed(self)
