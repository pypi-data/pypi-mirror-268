"""ModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.analysis_cases import _7558
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "ModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543
    from mastapy.system_model.analyses_and_results import _2658


__docformat__ = "restructuredtext en"
__all__ = ("ModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ModalAnalysisAtAStiffness")


class ModalAnalysisAtAStiffness(_7558.StaticLoadAnalysisCase):
    """ModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ModalAnalysisAtAStiffness")

    class _Cast_ModalAnalysisAtAStiffness:
        """Special nested class for casting ModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ModalAnalysisAtAStiffness._Cast_ModalAnalysisAtAStiffness",
            parent: "ModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def static_load_analysis_case(
            self: "ModalAnalysisAtAStiffness._Cast_ModalAnalysisAtAStiffness",
        ) -> "_7558.StaticLoadAnalysisCase":
            return self._parent._cast(_7558.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "ModalAnalysisAtAStiffness._Cast_ModalAnalysisAtAStiffness",
        ) -> "_7543.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.AnalysisCase)

        @property
        def context(
            self: "ModalAnalysisAtAStiffness._Cast_ModalAnalysisAtAStiffness",
        ) -> "_2658.Context":
            from mastapy.system_model.analyses_and_results import _2658

            return self._parent._cast(_2658.Context)

        @property
        def modal_analysis_at_a_stiffness(
            self: "ModalAnalysisAtAStiffness._Cast_ModalAnalysisAtAStiffness",
        ) -> "ModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ModalAnalysisAtAStiffness._Cast_ModalAnalysisAtAStiffness", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ModalAnalysisAtAStiffness.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ModalAnalysisAtAStiffness._Cast_ModalAnalysisAtAStiffness":
        return self._Cast_ModalAnalysisAtAStiffness(self)
