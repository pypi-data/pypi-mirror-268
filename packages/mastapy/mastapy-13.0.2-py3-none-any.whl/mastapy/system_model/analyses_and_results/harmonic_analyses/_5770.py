"""HarmonicAnalysisDrawStyle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.dynamic_analyses import _6338
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_DRAW_STYLE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "HarmonicAnalysisDrawStyle",
)

if TYPE_CHECKING:
    from mastapy.system_model.drawing import _2253
    from mastapy.geometry import _311


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicAnalysisDrawStyle",)


Self = TypeVar("Self", bound="HarmonicAnalysisDrawStyle")


class HarmonicAnalysisDrawStyle(_6338.DynamicAnalysisDrawStyle):
    """HarmonicAnalysisDrawStyle

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_DRAW_STYLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HarmonicAnalysisDrawStyle")

    class _Cast_HarmonicAnalysisDrawStyle:
        """Special nested class for casting HarmonicAnalysisDrawStyle to subclasses."""

        def __init__(
            self: "HarmonicAnalysisDrawStyle._Cast_HarmonicAnalysisDrawStyle",
            parent: "HarmonicAnalysisDrawStyle",
        ):
            self._parent = parent

        @property
        def dynamic_analysis_draw_style(
            self: "HarmonicAnalysisDrawStyle._Cast_HarmonicAnalysisDrawStyle",
        ) -> "_6338.DynamicAnalysisDrawStyle":
            return self._parent._cast(_6338.DynamicAnalysisDrawStyle)

        @property
        def contour_draw_style(
            self: "HarmonicAnalysisDrawStyle._Cast_HarmonicAnalysisDrawStyle",
        ) -> "_2253.ContourDrawStyle":
            from mastapy.system_model.drawing import _2253

            return self._parent._cast(_2253.ContourDrawStyle)

        @property
        def draw_style_base(
            self: "HarmonicAnalysisDrawStyle._Cast_HarmonicAnalysisDrawStyle",
        ) -> "_311.DrawStyleBase":
            from mastapy.geometry import _311

            return self._parent._cast(_311.DrawStyleBase)

        @property
        def harmonic_analysis_draw_style(
            self: "HarmonicAnalysisDrawStyle._Cast_HarmonicAnalysisDrawStyle",
        ) -> "HarmonicAnalysisDrawStyle":
            return self._parent

        def __getattr__(
            self: "HarmonicAnalysisDrawStyle._Cast_HarmonicAnalysisDrawStyle", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HarmonicAnalysisDrawStyle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "HarmonicAnalysisDrawStyle._Cast_HarmonicAnalysisDrawStyle":
        return self._Cast_HarmonicAnalysisDrawStyle(self)
