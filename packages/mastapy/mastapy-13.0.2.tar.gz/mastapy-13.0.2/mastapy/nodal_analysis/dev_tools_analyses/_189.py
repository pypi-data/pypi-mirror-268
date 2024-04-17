"""FEModelHarmonicAnalysisDrawStyle"""

from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.dev_tools_analyses import _195
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_MODEL_HARMONIC_ANALYSIS_DRAW_STYLE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses", "FEModelHarmonicAnalysisDrawStyle"
)


__docformat__ = "restructuredtext en"
__all__ = ("FEModelHarmonicAnalysisDrawStyle",)


Self = TypeVar("Self", bound="FEModelHarmonicAnalysisDrawStyle")


class FEModelHarmonicAnalysisDrawStyle(_195.FEModelTabDrawStyle):
    """FEModelHarmonicAnalysisDrawStyle

    This is a mastapy class.
    """

    TYPE = _FE_MODEL_HARMONIC_ANALYSIS_DRAW_STYLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEModelHarmonicAnalysisDrawStyle")

    class _Cast_FEModelHarmonicAnalysisDrawStyle:
        """Special nested class for casting FEModelHarmonicAnalysisDrawStyle to subclasses."""

        def __init__(
            self: "FEModelHarmonicAnalysisDrawStyle._Cast_FEModelHarmonicAnalysisDrawStyle",
            parent: "FEModelHarmonicAnalysisDrawStyle",
        ):
            self._parent = parent

        @property
        def fe_model_tab_draw_style(
            self: "FEModelHarmonicAnalysisDrawStyle._Cast_FEModelHarmonicAnalysisDrawStyle",
        ) -> "_195.FEModelTabDrawStyle":
            return self._parent._cast(_195.FEModelTabDrawStyle)

        @property
        def fe_model_harmonic_analysis_draw_style(
            self: "FEModelHarmonicAnalysisDrawStyle._Cast_FEModelHarmonicAnalysisDrawStyle",
        ) -> "FEModelHarmonicAnalysisDrawStyle":
            return self._parent

        def __getattr__(
            self: "FEModelHarmonicAnalysisDrawStyle._Cast_FEModelHarmonicAnalysisDrawStyle",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEModelHarmonicAnalysisDrawStyle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "FEModelHarmonicAnalysisDrawStyle._Cast_FEModelHarmonicAnalysisDrawStyle":
        return self._Cast_FEModelHarmonicAnalysisDrawStyle(self)
