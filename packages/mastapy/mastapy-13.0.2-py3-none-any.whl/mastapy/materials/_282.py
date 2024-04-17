"""SafetyFactorGroup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAFETY_FACTOR_GROUP = python_net_import("SMT.MastaAPI.Materials", "SafetyFactorGroup")

if TYPE_CHECKING:
    from mastapy.materials import _283


__docformat__ = "restructuredtext en"
__all__ = ("SafetyFactorGroup",)


Self = TypeVar("Self", bound="SafetyFactorGroup")


class SafetyFactorGroup(_0.APIBase):
    """SafetyFactorGroup

    This is a mastapy class.
    """

    TYPE = _SAFETY_FACTOR_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SafetyFactorGroup")

    class _Cast_SafetyFactorGroup:
        """Special nested class for casting SafetyFactorGroup to subclasses."""

        def __init__(
            self: "SafetyFactorGroup._Cast_SafetyFactorGroup",
            parent: "SafetyFactorGroup",
        ):
            self._parent = parent

        @property
        def safety_factor_group(
            self: "SafetyFactorGroup._Cast_SafetyFactorGroup",
        ) -> "SafetyFactorGroup":
            return self._parent

        def __getattr__(self: "SafetyFactorGroup._Cast_SafetyFactorGroup", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SafetyFactorGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def items(self: Self) -> "List[_283.SafetyFactorItem]":
        """List[mastapy.materials.SafetyFactorItem]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Items

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "SafetyFactorGroup._Cast_SafetyFactorGroup":
        return self._Cast_SafetyFactorGroup(self)
