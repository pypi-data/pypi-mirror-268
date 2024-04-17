"""GearOrderForTE"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.utility.modal_analysis.gears import _1811
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_ORDER_FOR_TE = python_net_import(
    "SMT.MastaAPI.Utility.ModalAnalysis.Gears", "GearOrderForTE"
)

if TYPE_CHECKING:
    from mastapy.utility.modal_analysis.gears import _1806, _1809


__docformat__ = "restructuredtext en"
__all__ = ("GearOrderForTE",)


Self = TypeVar("Self", bound="GearOrderForTE")


class GearOrderForTE(_1811.OrderWithRadius):
    """GearOrderForTE

    This is a mastapy class.
    """

    TYPE = _GEAR_ORDER_FOR_TE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearOrderForTE")

    class _Cast_GearOrderForTE:
        """Special nested class for casting GearOrderForTE to subclasses."""

        def __init__(
            self: "GearOrderForTE._Cast_GearOrderForTE", parent: "GearOrderForTE"
        ):
            self._parent = parent

        @property
        def order_with_radius(
            self: "GearOrderForTE._Cast_GearOrderForTE",
        ) -> "_1811.OrderWithRadius":
            return self._parent._cast(_1811.OrderWithRadius)

        @property
        def order_for_te(
            self: "GearOrderForTE._Cast_GearOrderForTE",
        ) -> "_1809.OrderForTE":
            return self._parent._cast(_1809.OrderForTE)

        @property
        def gear_order_for_te(
            self: "GearOrderForTE._Cast_GearOrderForTE",
        ) -> "GearOrderForTE":
            return self._parent

        def __getattr__(self: "GearOrderForTE._Cast_GearOrderForTE", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearOrderForTE.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_teeth(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfTeeth

        if temp is None:
            return 0

        return temp

    @property
    def position(self: Self) -> "_1806.GearPositions":
        """mastapy.utility.modal_analysis.gears.GearPositions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Position

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.ModalAnalysis.Gears.GearPositions"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility.modal_analysis.gears._1806", "GearPositions"
        )(value)

    @property
    def additional_orders_and_harmonics(self: Self) -> "List[_1809.OrderForTE]":
        """List[mastapy.utility.modal_analysis.gears.OrderForTE]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdditionalOrdersAndHarmonics

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "GearOrderForTE._Cast_GearOrderForTE":
        return self._Cast_GearOrderForTE(self)
