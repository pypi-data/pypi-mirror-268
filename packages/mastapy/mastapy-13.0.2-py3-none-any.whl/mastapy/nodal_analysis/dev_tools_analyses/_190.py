"""FEModelInstanceDrawStyle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_MODEL_INSTANCE_DRAW_STYLE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses", "FEModelInstanceDrawStyle"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.dev_tools_analyses import _181


__docformat__ = "restructuredtext en"
__all__ = ("FEModelInstanceDrawStyle",)


Self = TypeVar("Self", bound="FEModelInstanceDrawStyle")


class FEModelInstanceDrawStyle(_0.APIBase):
    """FEModelInstanceDrawStyle

    This is a mastapy class.
    """

    TYPE = _FE_MODEL_INSTANCE_DRAW_STYLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEModelInstanceDrawStyle")

    class _Cast_FEModelInstanceDrawStyle:
        """Special nested class for casting FEModelInstanceDrawStyle to subclasses."""

        def __init__(
            self: "FEModelInstanceDrawStyle._Cast_FEModelInstanceDrawStyle",
            parent: "FEModelInstanceDrawStyle",
        ):
            self._parent = parent

        @property
        def fe_model_instance_draw_style(
            self: "FEModelInstanceDrawStyle._Cast_FEModelInstanceDrawStyle",
        ) -> "FEModelInstanceDrawStyle":
            return self._parent

        def __getattr__(
            self: "FEModelInstanceDrawStyle._Cast_FEModelInstanceDrawStyle", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEModelInstanceDrawStyle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def model_draw_style(self: Self) -> "_181.DrawStyleForFE":
        """mastapy.nodal_analysis.dev_tools_analyses.DrawStyleForFE

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModelDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "FEModelInstanceDrawStyle._Cast_FEModelInstanceDrawStyle":
        return self._Cast_FEModelInstanceDrawStyle(self)
