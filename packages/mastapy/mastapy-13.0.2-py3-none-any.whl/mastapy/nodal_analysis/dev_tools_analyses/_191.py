"""FEModelModalAnalysisDrawStyle"""

from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.dev_tools_analyses import _195
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_MODEL_MODAL_ANALYSIS_DRAW_STYLE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses", "FEModelModalAnalysisDrawStyle"
)


__docformat__ = "restructuredtext en"
__all__ = ("FEModelModalAnalysisDrawStyle",)


Self = TypeVar("Self", bound="FEModelModalAnalysisDrawStyle")


class FEModelModalAnalysisDrawStyle(_195.FEModelTabDrawStyle):
    """FEModelModalAnalysisDrawStyle

    This is a mastapy class.
    """

    TYPE = _FE_MODEL_MODAL_ANALYSIS_DRAW_STYLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEModelModalAnalysisDrawStyle")

    class _Cast_FEModelModalAnalysisDrawStyle:
        """Special nested class for casting FEModelModalAnalysisDrawStyle to subclasses."""

        def __init__(
            self: "FEModelModalAnalysisDrawStyle._Cast_FEModelModalAnalysisDrawStyle",
            parent: "FEModelModalAnalysisDrawStyle",
        ):
            self._parent = parent

        @property
        def fe_model_tab_draw_style(
            self: "FEModelModalAnalysisDrawStyle._Cast_FEModelModalAnalysisDrawStyle",
        ) -> "_195.FEModelTabDrawStyle":
            return self._parent._cast(_195.FEModelTabDrawStyle)

        @property
        def fe_model_modal_analysis_draw_style(
            self: "FEModelModalAnalysisDrawStyle._Cast_FEModelModalAnalysisDrawStyle",
        ) -> "FEModelModalAnalysisDrawStyle":
            return self._parent

        def __getattr__(
            self: "FEModelModalAnalysisDrawStyle._Cast_FEModelModalAnalysisDrawStyle",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEModelModalAnalysisDrawStyle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "FEModelModalAnalysisDrawStyle._Cast_FEModelModalAnalysisDrawStyle":
        return self._Cast_FEModelModalAnalysisDrawStyle(self)
