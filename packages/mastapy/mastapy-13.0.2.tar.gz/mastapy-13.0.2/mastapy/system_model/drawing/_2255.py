"""DynamicAnalysisViewable"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.drawing import _2260
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_ANALYSIS_VIEWABLE = python_net_import(
    "SMT.MastaAPI.SystemModel.Drawing", "DynamicAnalysisViewable"
)

if TYPE_CHECKING:
    from mastapy.system_model.drawing import _2253, _2256, _2258
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6338


__docformat__ = "restructuredtext en"
__all__ = ("DynamicAnalysisViewable",)


Self = TypeVar("Self", bound="DynamicAnalysisViewable")


class DynamicAnalysisViewable(_2260.PartAnalysisCaseWithContourViewable):
    """DynamicAnalysisViewable

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_ANALYSIS_VIEWABLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicAnalysisViewable")

    class _Cast_DynamicAnalysisViewable:
        """Special nested class for casting DynamicAnalysisViewable to subclasses."""

        def __init__(
            self: "DynamicAnalysisViewable._Cast_DynamicAnalysisViewable",
            parent: "DynamicAnalysisViewable",
        ):
            self._parent = parent

        @property
        def part_analysis_case_with_contour_viewable(
            self: "DynamicAnalysisViewable._Cast_DynamicAnalysisViewable",
        ) -> "_2260.PartAnalysisCaseWithContourViewable":
            return self._parent._cast(_2260.PartAnalysisCaseWithContourViewable)

        @property
        def harmonic_analysis_viewable(
            self: "DynamicAnalysisViewable._Cast_DynamicAnalysisViewable",
        ) -> "_2256.HarmonicAnalysisViewable":
            from mastapy.system_model.drawing import _2256

            return self._parent._cast(_2256.HarmonicAnalysisViewable)

        @property
        def modal_analysis_viewable(
            self: "DynamicAnalysisViewable._Cast_DynamicAnalysisViewable",
        ) -> "_2258.ModalAnalysisViewable":
            from mastapy.system_model.drawing import _2258

            return self._parent._cast(_2258.ModalAnalysisViewable)

        @property
        def dynamic_analysis_viewable(
            self: "DynamicAnalysisViewable._Cast_DynamicAnalysisViewable",
        ) -> "DynamicAnalysisViewable":
            return self._parent

        def __getattr__(
            self: "DynamicAnalysisViewable._Cast_DynamicAnalysisViewable", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicAnalysisViewable.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contour_draw_style(self: Self) -> "_2253.ContourDrawStyle":
        """mastapy.system_model.drawing.ContourDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContourDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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

    def fe_results(self: Self):
        """Method does not return."""
        self.wrapped.FEResults()

    @property
    def cast_to(self: Self) -> "DynamicAnalysisViewable._Cast_DynamicAnalysisViewable":
        return self._Cast_DynamicAnalysisViewable(self)
