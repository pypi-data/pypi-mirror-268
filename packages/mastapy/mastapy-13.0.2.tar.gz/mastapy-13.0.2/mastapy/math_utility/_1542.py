"""Vector2DListAccessor"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._math.vector_2d import Vector2D
from mastapy._internal import conversion, constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VECTOR_2D_LIST_ACCESSOR = python_net_import(
    "SMT.MastaAPI.MathUtility", "Vector2DListAccessor"
)


__docformat__ = "restructuredtext en"
__all__ = ("Vector2DListAccessor",)


Self = TypeVar("Self", bound="Vector2DListAccessor")


class Vector2DListAccessor(_0.APIBase):
    """Vector2DListAccessor

    This is a mastapy class.
    """

    TYPE = _VECTOR_2D_LIST_ACCESSOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Vector2DListAccessor")

    class _Cast_Vector2DListAccessor:
        """Special nested class for casting Vector2DListAccessor to subclasses."""

        def __init__(
            self: "Vector2DListAccessor._Cast_Vector2DListAccessor",
            parent: "Vector2DListAccessor",
        ):
            self._parent = parent

        @property
        def vector_2d_list_accessor(
            self: "Vector2DListAccessor._Cast_Vector2DListAccessor",
        ) -> "Vector2DListAccessor":
            return self._parent

        def __getattr__(
            self: "Vector2DListAccessor._Cast_Vector2DListAccessor", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Vector2DListAccessor.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @enforce_parameter_types
    def create_new_from_vector_list(
        self: Self, list: "List[Vector2D]"
    ) -> "Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor

        Args:
            list (List[Vector2D])
        """
        list = conversion.mp_to_pn_objects_in_dotnet_list(list)
        method_result = self.wrapped.CreateNewFromVectorList(list)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def get_vector_list(self: Self) -> "List[Vector2D]":
        """List[Vector2D]"""
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.GetVectorList(), Vector2D
        )

    @property
    def cast_to(self: Self) -> "Vector2DListAccessor._Cast_Vector2DListAccessor":
        return self._Cast_Vector2DListAccessor(self)
