"""FEModelStaticAnalysisDrawStyle"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.nodal_analysis.dev_tools_analyses import _195
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_MODEL_STATIC_ANALYSIS_DRAW_STYLE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses", "FEModelStaticAnalysisDrawStyle"
)


__docformat__ = "restructuredtext en"
__all__ = ("FEModelStaticAnalysisDrawStyle",)


Self = TypeVar("Self", bound="FEModelStaticAnalysisDrawStyle")


class FEModelStaticAnalysisDrawStyle(_195.FEModelTabDrawStyle):
    """FEModelStaticAnalysisDrawStyle

    This is a mastapy class.
    """

    TYPE = _FE_MODEL_STATIC_ANALYSIS_DRAW_STYLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEModelStaticAnalysisDrawStyle")

    class _Cast_FEModelStaticAnalysisDrawStyle:
        """Special nested class for casting FEModelStaticAnalysisDrawStyle to subclasses."""

        def __init__(
            self: "FEModelStaticAnalysisDrawStyle._Cast_FEModelStaticAnalysisDrawStyle",
            parent: "FEModelStaticAnalysisDrawStyle",
        ):
            self._parent = parent

        @property
        def fe_model_tab_draw_style(
            self: "FEModelStaticAnalysisDrawStyle._Cast_FEModelStaticAnalysisDrawStyle",
        ) -> "_195.FEModelTabDrawStyle":
            return self._parent._cast(_195.FEModelTabDrawStyle)

        @property
        def fe_model_static_analysis_draw_style(
            self: "FEModelStaticAnalysisDrawStyle._Cast_FEModelStaticAnalysisDrawStyle",
        ) -> "FEModelStaticAnalysisDrawStyle":
            return self._parent

        def __getattr__(
            self: "FEModelStaticAnalysisDrawStyle._Cast_FEModelStaticAnalysisDrawStyle",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEModelStaticAnalysisDrawStyle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def show_force_arrows(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowForceArrows

        if temp is None:
            return False

        return temp

    @show_force_arrows.setter
    @enforce_parameter_types
    def show_force_arrows(self: Self, value: "bool"):
        self.wrapped.ShowForceArrows = bool(value) if value is not None else False

    @property
    def cast_to(
        self: Self,
    ) -> "FEModelStaticAnalysisDrawStyle._Cast_FEModelStaticAnalysisDrawStyle":
        return self._Cast_FEModelStaticAnalysisDrawStyle(self)
