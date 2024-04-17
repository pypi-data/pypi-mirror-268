"""FEModelComponentDrawStyle"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_MODEL_COMPONENT_DRAW_STYLE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses", "FEModelComponentDrawStyle"
)


__docformat__ = "restructuredtext en"
__all__ = ("FEModelComponentDrawStyle",)


Self = TypeVar("Self", bound="FEModelComponentDrawStyle")


class FEModelComponentDrawStyle(_0.APIBase):
    """FEModelComponentDrawStyle

    This is a mastapy class.
    """

    TYPE = _FE_MODEL_COMPONENT_DRAW_STYLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEModelComponentDrawStyle")

    class _Cast_FEModelComponentDrawStyle:
        """Special nested class for casting FEModelComponentDrawStyle to subclasses."""

        def __init__(
            self: "FEModelComponentDrawStyle._Cast_FEModelComponentDrawStyle",
            parent: "FEModelComponentDrawStyle",
        ):
            self._parent = parent

        @property
        def fe_model_component_draw_style(
            self: "FEModelComponentDrawStyle._Cast_FEModelComponentDrawStyle",
        ) -> "FEModelComponentDrawStyle":
            return self._parent

        def __getattr__(
            self: "FEModelComponentDrawStyle._Cast_FEModelComponentDrawStyle", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEModelComponentDrawStyle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connectable_components(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ConnectableComponents

        if temp is None:
            return False

        return temp

    @connectable_components.setter
    @enforce_parameter_types
    def connectable_components(self: Self, value: "bool"):
        self.wrapped.ConnectableComponents = bool(value) if value is not None else False

    @property
    def solid_components(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SolidComponents

        if temp is None:
            return False

        return temp

    @solid_components.setter
    @enforce_parameter_types
    def solid_components(self: Self, value: "bool"):
        self.wrapped.SolidComponents = bool(value) if value is not None else False

    @property
    def solid_shafts(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SolidShafts

        if temp is None:
            return False

        return temp

    @solid_shafts.setter
    @enforce_parameter_types
    def solid_shafts(self: Self, value: "bool"):
        self.wrapped.SolidShafts = bool(value) if value is not None else False

    @property
    def transparent_model(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.TransparentModel

        if temp is None:
            return False

        return temp

    @transparent_model.setter
    @enforce_parameter_types
    def transparent_model(self: Self, value: "bool"):
        self.wrapped.TransparentModel = bool(value) if value is not None else False

    @property
    def cast_to(
        self: Self,
    ) -> "FEModelComponentDrawStyle._Cast_FEModelComponentDrawStyle":
        return self._Cast_FEModelComponentDrawStyle(self)
