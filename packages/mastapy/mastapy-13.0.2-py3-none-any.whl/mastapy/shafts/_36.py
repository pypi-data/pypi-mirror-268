"""ShaftSectionDamageResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_SECTION_DAMAGE_RESULTS = python_net_import(
    "SMT.MastaAPI.Shafts", "ShaftSectionDamageResults"
)

if TYPE_CHECKING:
    from mastapy.shafts import _37


__docformat__ = "restructuredtext en"
__all__ = ("ShaftSectionDamageResults",)


Self = TypeVar("Self", bound="ShaftSectionDamageResults")


class ShaftSectionDamageResults(_0.APIBase):
    """ShaftSectionDamageResults

    This is a mastapy class.
    """

    TYPE = _SHAFT_SECTION_DAMAGE_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftSectionDamageResults")

    class _Cast_ShaftSectionDamageResults:
        """Special nested class for casting ShaftSectionDamageResults to subclasses."""

        def __init__(
            self: "ShaftSectionDamageResults._Cast_ShaftSectionDamageResults",
            parent: "ShaftSectionDamageResults",
        ):
            self._parent = parent

        @property
        def shaft_section_damage_results(
            self: "ShaftSectionDamageResults._Cast_ShaftSectionDamageResults",
        ) -> "ShaftSectionDamageResults":
            return self._parent

        def __getattr__(
            self: "ShaftSectionDamageResults._Cast_ShaftSectionDamageResults", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftSectionDamageResults.TYPE"):
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
    def left_end(self: Self) -> "_37.ShaftSectionEndDamageResults":
        """mastapy.shafts.ShaftSectionEndDamageResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftEnd

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_end(self: Self) -> "_37.ShaftSectionEndDamageResults":
        """mastapy.shafts.ShaftSectionEndDamageResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightEnd

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftSectionDamageResults._Cast_ShaftSectionDamageResults":
        return self._Cast_ShaftSectionDamageResults(self)
