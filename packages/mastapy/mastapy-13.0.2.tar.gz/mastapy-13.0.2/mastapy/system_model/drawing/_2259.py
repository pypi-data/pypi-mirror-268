"""ModelViewOptionsDrawStyle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.geometry import _310
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODEL_VIEW_OPTIONS_DRAW_STYLE = python_net_import(
    "SMT.MastaAPI.SystemModel.Drawing", "ModelViewOptionsDrawStyle"
)

if TYPE_CHECKING:
    from mastapy.geometry import _311


__docformat__ = "restructuredtext en"
__all__ = ("ModelViewOptionsDrawStyle",)


Self = TypeVar("Self", bound="ModelViewOptionsDrawStyle")


class ModelViewOptionsDrawStyle(_310.DrawStyle):
    """ModelViewOptionsDrawStyle

    This is a mastapy class.
    """

    TYPE = _MODEL_VIEW_OPTIONS_DRAW_STYLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ModelViewOptionsDrawStyle")

    class _Cast_ModelViewOptionsDrawStyle:
        """Special nested class for casting ModelViewOptionsDrawStyle to subclasses."""

        def __init__(
            self: "ModelViewOptionsDrawStyle._Cast_ModelViewOptionsDrawStyle",
            parent: "ModelViewOptionsDrawStyle",
        ):
            self._parent = parent

        @property
        def draw_style(
            self: "ModelViewOptionsDrawStyle._Cast_ModelViewOptionsDrawStyle",
        ) -> "_310.DrawStyle":
            return self._parent._cast(_310.DrawStyle)

        @property
        def draw_style_base(
            self: "ModelViewOptionsDrawStyle._Cast_ModelViewOptionsDrawStyle",
        ) -> "_311.DrawStyleBase":
            from mastapy.geometry import _311

            return self._parent._cast(_311.DrawStyleBase)

        @property
        def model_view_options_draw_style(
            self: "ModelViewOptionsDrawStyle._Cast_ModelViewOptionsDrawStyle",
        ) -> "ModelViewOptionsDrawStyle":
            return self._parent

        def __getattr__(
            self: "ModelViewOptionsDrawStyle._Cast_ModelViewOptionsDrawStyle", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ModelViewOptionsDrawStyle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rigid_elements(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.RigidElements

        if temp is None:
            return False

        return temp

    @rigid_elements.setter
    @enforce_parameter_types
    def rigid_elements(self: Self, value: "bool"):
        self.wrapped.RigidElements = bool(value) if value is not None else False

    @property
    def show_nodes(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowNodes

        if temp is None:
            return False

        return temp

    @show_nodes.setter
    @enforce_parameter_types
    def show_nodes(self: Self, value: "bool"):
        self.wrapped.ShowNodes = bool(value) if value is not None else False

    @property
    def show_part_labels(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowPartLabels

        if temp is None:
            return False

        return temp

    @show_part_labels.setter
    @enforce_parameter_types
    def show_part_labels(self: Self, value: "bool"):
        self.wrapped.ShowPartLabels = bool(value) if value is not None else False

    @property
    def solid_3d_shafts(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.Solid3DShafts

        if temp is None:
            return False

        return temp

    @solid_3d_shafts.setter
    @enforce_parameter_types
    def solid_3d_shafts(self: Self, value: "bool"):
        self.wrapped.Solid3DShafts = bool(value) if value is not None else False

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
    def solid_housing(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SolidHousing

        if temp is None:
            return False

        return temp

    @solid_housing.setter
    @enforce_parameter_types
    def solid_housing(self: Self, value: "bool"):
        self.wrapped.SolidHousing = bool(value) if value is not None else False

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
    ) -> "ModelViewOptionsDrawStyle._Cast_ModelViewOptionsDrawStyle":
        return self._Cast_ModelViewOptionsDrawStyle(self)
