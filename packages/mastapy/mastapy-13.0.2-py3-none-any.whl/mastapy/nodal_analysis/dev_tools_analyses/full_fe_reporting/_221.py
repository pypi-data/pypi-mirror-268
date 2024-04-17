"""NodeDetailsForFEModel"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal import conversion
from mastapy._math.vector_3d import Vector3D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODE_DETAILS_FOR_FE_MODEL = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting",
    "NodeDetailsForFEModel",
)


__docformat__ = "restructuredtext en"
__all__ = ("NodeDetailsForFEModel",)


Self = TypeVar("Self", bound="NodeDetailsForFEModel")


class NodeDetailsForFEModel(_0.APIBase):
    """NodeDetailsForFEModel

    This is a mastapy class.
    """

    TYPE = _NODE_DETAILS_FOR_FE_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NodeDetailsForFEModel")

    class _Cast_NodeDetailsForFEModel:
        """Special nested class for casting NodeDetailsForFEModel to subclasses."""

        def __init__(
            self: "NodeDetailsForFEModel._Cast_NodeDetailsForFEModel",
            parent: "NodeDetailsForFEModel",
        ):
            self._parent = parent

        @property
        def node_details_for_fe_model(
            self: "NodeDetailsForFEModel._Cast_NodeDetailsForFEModel",
        ) -> "NodeDetailsForFEModel":
            return self._parent

        def __getattr__(
            self: "NodeDetailsForFEModel._Cast_NodeDetailsForFEModel", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NodeDetailsForFEModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def external_ids(self: Self) -> "List[int]":
        """List[int]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExternalIDs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, int)

        if value is None:
            return None

        return value

    @property
    def node_positions(self: Self) -> "List[Vector3D]":
        """List[Vector3D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodePositions

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "NodeDetailsForFEModel._Cast_NodeDetailsForFEModel":
        return self._Cast_NodeDetailsForFEModel(self)
