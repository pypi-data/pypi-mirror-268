"""MBDAnalysisDrawStyle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.drawing import _2253
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MBD_ANALYSIS_DRAW_STYLE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses", "MBDAnalysisDrawStyle"
)

if TYPE_CHECKING:
    from mastapy.geometry import _311


__docformat__ = "restructuredtext en"
__all__ = ("MBDAnalysisDrawStyle",)


Self = TypeVar("Self", bound="MBDAnalysisDrawStyle")


class MBDAnalysisDrawStyle(_2253.ContourDrawStyle):
    """MBDAnalysisDrawStyle

    This is a mastapy class.
    """

    TYPE = _MBD_ANALYSIS_DRAW_STYLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MBDAnalysisDrawStyle")

    class _Cast_MBDAnalysisDrawStyle:
        """Special nested class for casting MBDAnalysisDrawStyle to subclasses."""

        def __init__(
            self: "MBDAnalysisDrawStyle._Cast_MBDAnalysisDrawStyle",
            parent: "MBDAnalysisDrawStyle",
        ):
            self._parent = parent

        @property
        def contour_draw_style(
            self: "MBDAnalysisDrawStyle._Cast_MBDAnalysisDrawStyle",
        ) -> "_2253.ContourDrawStyle":
            return self._parent._cast(_2253.ContourDrawStyle)

        @property
        def draw_style_base(
            self: "MBDAnalysisDrawStyle._Cast_MBDAnalysisDrawStyle",
        ) -> "_311.DrawStyleBase":
            from mastapy.geometry import _311

            return self._parent._cast(_311.DrawStyleBase)

        @property
        def mbd_analysis_draw_style(
            self: "MBDAnalysisDrawStyle._Cast_MBDAnalysisDrawStyle",
        ) -> "MBDAnalysisDrawStyle":
            return self._parent

        def __getattr__(
            self: "MBDAnalysisDrawStyle._Cast_MBDAnalysisDrawStyle", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MBDAnalysisDrawStyle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "MBDAnalysisDrawStyle._Cast_MBDAnalysisDrawStyle":
        return self._Cast_MBDAnalysisDrawStyle(self)
