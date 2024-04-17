"""FEModelTransparencyDrawStyle"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_MODEL_TRANSPARENCY_DRAW_STYLE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses", "FEModelTransparencyDrawStyle"
)


__docformat__ = "restructuredtext en"
__all__ = ("FEModelTransparencyDrawStyle",)


Self = TypeVar("Self", bound="FEModelTransparencyDrawStyle")


class FEModelTransparencyDrawStyle(_0.APIBase):
    """FEModelTransparencyDrawStyle

    This is a mastapy class.
    """

    TYPE = _FE_MODEL_TRANSPARENCY_DRAW_STYLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEModelTransparencyDrawStyle")

    class _Cast_FEModelTransparencyDrawStyle:
        """Special nested class for casting FEModelTransparencyDrawStyle to subclasses."""

        def __init__(
            self: "FEModelTransparencyDrawStyle._Cast_FEModelTransparencyDrawStyle",
            parent: "FEModelTransparencyDrawStyle",
        ):
            self._parent = parent

        @property
        def fe_model_transparency_draw_style(
            self: "FEModelTransparencyDrawStyle._Cast_FEModelTransparencyDrawStyle",
        ) -> "FEModelTransparencyDrawStyle":
            return self._parent

        def __getattr__(
            self: "FEModelTransparencyDrawStyle._Cast_FEModelTransparencyDrawStyle",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEModelTransparencyDrawStyle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def show_fe3d_axes(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowFE3DAxes

        if temp is None:
            return False

        return temp

    @show_fe3d_axes.setter
    @enforce_parameter_types
    def show_fe3d_axes(self: Self, value: "bool"):
        self.wrapped.ShowFE3DAxes = bool(value) if value is not None else False

    @property
    def cast_to(
        self: Self,
    ) -> "FEModelTransparencyDrawStyle._Cast_FEModelTransparencyDrawStyle":
        return self._Cast_FEModelTransparencyDrawStyle(self)
