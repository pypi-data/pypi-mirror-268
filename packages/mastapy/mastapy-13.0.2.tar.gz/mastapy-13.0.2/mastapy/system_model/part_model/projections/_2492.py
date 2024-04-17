"""SpecifiedParallelPartGroupDrawingOrder"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIFIED_PARALLEL_PART_GROUP_DRAWING_ORDER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Projections",
    "SpecifiedParallelPartGroupDrawingOrder",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.projections import _2491


__docformat__ = "restructuredtext en"
__all__ = ("SpecifiedParallelPartGroupDrawingOrder",)


Self = TypeVar("Self", bound="SpecifiedParallelPartGroupDrawingOrder")


class SpecifiedParallelPartGroupDrawingOrder(_0.APIBase):
    """SpecifiedParallelPartGroupDrawingOrder

    This is a mastapy class.
    """

    TYPE = _SPECIFIED_PARALLEL_PART_GROUP_DRAWING_ORDER
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecifiedParallelPartGroupDrawingOrder"
    )

    class _Cast_SpecifiedParallelPartGroupDrawingOrder:
        """Special nested class for casting SpecifiedParallelPartGroupDrawingOrder to subclasses."""

        def __init__(
            self: "SpecifiedParallelPartGroupDrawingOrder._Cast_SpecifiedParallelPartGroupDrawingOrder",
            parent: "SpecifiedParallelPartGroupDrawingOrder",
        ):
            self._parent = parent

        @property
        def specified_parallel_part_group_drawing_order(
            self: "SpecifiedParallelPartGroupDrawingOrder._Cast_SpecifiedParallelPartGroupDrawingOrder",
        ) -> "SpecifiedParallelPartGroupDrawingOrder":
            return self._parent

        def __getattr__(
            self: "SpecifiedParallelPartGroupDrawingOrder._Cast_SpecifiedParallelPartGroupDrawingOrder",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "SpecifiedParallelPartGroupDrawingOrder.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def specified_groups(
        self: Self,
    ) -> "List[_2491.SpecifiedConcentricPartGroupDrawingOrder]":
        """List[mastapy.system_model.part_model.projections.SpecifiedConcentricPartGroupDrawingOrder]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpecifiedGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpecifiedParallelPartGroupDrawingOrder._Cast_SpecifiedParallelPartGroupDrawingOrder":
        return self._Cast_SpecifiedParallelPartGroupDrawingOrder(self)
