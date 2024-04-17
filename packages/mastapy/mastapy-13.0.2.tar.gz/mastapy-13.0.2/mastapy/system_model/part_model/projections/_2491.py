"""SpecifiedConcentricPartGroupDrawingOrder"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.part_model.part_groups import _2494
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIFIED_CONCENTRIC_PART_GROUP_DRAWING_ORDER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Projections",
    "SpecifiedConcentricPartGroupDrawingOrder",
)


__docformat__ = "restructuredtext en"
__all__ = ("SpecifiedConcentricPartGroupDrawingOrder",)


Self = TypeVar("Self", bound="SpecifiedConcentricPartGroupDrawingOrder")


class SpecifiedConcentricPartGroupDrawingOrder(_0.APIBase):
    """SpecifiedConcentricPartGroupDrawingOrder

    This is a mastapy class.
    """

    TYPE = _SPECIFIED_CONCENTRIC_PART_GROUP_DRAWING_ORDER
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecifiedConcentricPartGroupDrawingOrder"
    )

    class _Cast_SpecifiedConcentricPartGroupDrawingOrder:
        """Special nested class for casting SpecifiedConcentricPartGroupDrawingOrder to subclasses."""

        def __init__(
            self: "SpecifiedConcentricPartGroupDrawingOrder._Cast_SpecifiedConcentricPartGroupDrawingOrder",
            parent: "SpecifiedConcentricPartGroupDrawingOrder",
        ):
            self._parent = parent

        @property
        def specified_concentric_part_group_drawing_order(
            self: "SpecifiedConcentricPartGroupDrawingOrder._Cast_SpecifiedConcentricPartGroupDrawingOrder",
        ) -> "SpecifiedConcentricPartGroupDrawingOrder":
            return self._parent

        def __getattr__(
            self: "SpecifiedConcentricPartGroupDrawingOrder._Cast_SpecifiedConcentricPartGroupDrawingOrder",
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
        self: Self, instance_to_wrap: "SpecifiedConcentricPartGroupDrawingOrder.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def concentric_group(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_ConcentricPartGroup":
        """ListWithSelectedItem[mastapy.system_model.part_model.part_groups.ConcentricPartGroup]"""
        temp = self.wrapped.ConcentricGroup

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_ConcentricPartGroup",
        )(temp)

    @concentric_group.setter
    @enforce_parameter_types
    def concentric_group(self: Self, value: "_2494.ConcentricPartGroup"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_ConcentricPartGroup.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_ConcentricPartGroup.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.ConcentricGroup = value

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

    def delete(self: Self):
        """Method does not return."""
        self.wrapped.Delete()

    @property
    def cast_to(
        self: Self,
    ) -> "SpecifiedConcentricPartGroupDrawingOrder._Cast_SpecifiedConcentricPartGroupDrawingOrder":
        return self._Cast_SpecifiedConcentricPartGroupDrawingOrder(self)
