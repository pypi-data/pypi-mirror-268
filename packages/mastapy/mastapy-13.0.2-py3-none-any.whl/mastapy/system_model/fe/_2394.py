"""FESubstructureNodeModeShapes"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_SUBSTRUCTURE_NODE_MODE_SHAPES = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "FESubstructureNodeModeShapes"
)

if TYPE_CHECKING:
    from mastapy.system_model.fe import _2392, _2393
    from mastapy.math_utility import _1506


__docformat__ = "restructuredtext en"
__all__ = ("FESubstructureNodeModeShapes",)


Self = TypeVar("Self", bound="FESubstructureNodeModeShapes")


class FESubstructureNodeModeShapes(_0.APIBase):
    """FESubstructureNodeModeShapes

    This is a mastapy class.
    """

    TYPE = _FE_SUBSTRUCTURE_NODE_MODE_SHAPES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FESubstructureNodeModeShapes")

    class _Cast_FESubstructureNodeModeShapes:
        """Special nested class for casting FESubstructureNodeModeShapes to subclasses."""

        def __init__(
            self: "FESubstructureNodeModeShapes._Cast_FESubstructureNodeModeShapes",
            parent: "FESubstructureNodeModeShapes",
        ):
            self._parent = parent

        @property
        def fe_substructure_node_mode_shapes(
            self: "FESubstructureNodeModeShapes._Cast_FESubstructureNodeModeShapes",
        ) -> "FESubstructureNodeModeShapes":
            return self._parent

        def __getattr__(
            self: "FESubstructureNodeModeShapes._Cast_FESubstructureNodeModeShapes",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FESubstructureNodeModeShapes.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def condensation_node(self: Self) -> "_2392.FESubstructureNode":
        """mastapy.system_model.fe.FESubstructureNode

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CondensationNode

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connected_component_local_coordinate_system(
        self: Self,
    ) -> "_1506.CoordinateSystem3D":
        """mastapy.math_utility.CoordinateSystem3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectedComponentLocalCoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mode_shapes_at_condensation_node(
        self: Self,
    ) -> "List[_2393.FESubstructureNodeModeShape]":
        """List[mastapy.system_model.fe.FESubstructureNodeModeShape]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModeShapesAtCondensationNode

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FESubstructureNodeModeShapes._Cast_FESubstructureNodeModeShapes":
        return self._Cast_FESubstructureNodeModeShapes(self)
