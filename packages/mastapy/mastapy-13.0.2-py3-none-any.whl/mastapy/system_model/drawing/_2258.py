"""ModalAnalysisViewable"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.drawing import _2255
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODAL_ANALYSIS_VIEWABLE = python_net_import(
    "SMT.MastaAPI.SystemModel.Drawing", "ModalAnalysisViewable"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6338
    from mastapy.system_model.drawing import _2260


__docformat__ = "restructuredtext en"
__all__ = ("ModalAnalysisViewable",)


Self = TypeVar("Self", bound="ModalAnalysisViewable")


class ModalAnalysisViewable(_2255.DynamicAnalysisViewable):
    """ModalAnalysisViewable

    This is a mastapy class.
    """

    TYPE = _MODAL_ANALYSIS_VIEWABLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ModalAnalysisViewable")

    class _Cast_ModalAnalysisViewable:
        """Special nested class for casting ModalAnalysisViewable to subclasses."""

        def __init__(
            self: "ModalAnalysisViewable._Cast_ModalAnalysisViewable",
            parent: "ModalAnalysisViewable",
        ):
            self._parent = parent

        @property
        def dynamic_analysis_viewable(
            self: "ModalAnalysisViewable._Cast_ModalAnalysisViewable",
        ) -> "_2255.DynamicAnalysisViewable":
            return self._parent._cast(_2255.DynamicAnalysisViewable)

        @property
        def part_analysis_case_with_contour_viewable(
            self: "ModalAnalysisViewable._Cast_ModalAnalysisViewable",
        ) -> "_2260.PartAnalysisCaseWithContourViewable":
            from mastapy.system_model.drawing import _2260

            return self._parent._cast(_2260.PartAnalysisCaseWithContourViewable)

        @property
        def modal_analysis_viewable(
            self: "ModalAnalysisViewable._Cast_ModalAnalysisViewable",
        ) -> "ModalAnalysisViewable":
            return self._parent

        def __getattr__(
            self: "ModalAnalysisViewable._Cast_ModalAnalysisViewable", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ModalAnalysisViewable.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def dynamic_analysis_draw_style(self: Self) -> "_6338.DynamicAnalysisDrawStyle":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.DynamicAnalysisDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ModalAnalysisViewable._Cast_ModalAnalysisViewable":
        return self._Cast_ModalAnalysisViewable(self)
