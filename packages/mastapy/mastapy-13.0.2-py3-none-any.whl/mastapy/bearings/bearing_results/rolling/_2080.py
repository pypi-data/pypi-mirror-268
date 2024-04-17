"""StressAtPosition"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRESS_AT_POSITION = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "StressAtPosition"
)


__docformat__ = "restructuredtext en"
__all__ = ("StressAtPosition",)


Self = TypeVar("Self", bound="StressAtPosition")


class StressAtPosition(_0.APIBase):
    """StressAtPosition

    This is a mastapy class.
    """

    TYPE = _STRESS_AT_POSITION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StressAtPosition")

    class _Cast_StressAtPosition:
        """Special nested class for casting StressAtPosition to subclasses."""

        def __init__(
            self: "StressAtPosition._Cast_StressAtPosition", parent: "StressAtPosition"
        ):
            self._parent = parent

        @property
        def stress_at_position(
            self: "StressAtPosition._Cast_StressAtPosition",
        ) -> "StressAtPosition":
            return self._parent

        def __getattr__(self: "StressAtPosition._Cast_StressAtPosition", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StressAtPosition.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def position(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Position

        if temp is None:
            return 0.0

        return temp

    @property
    def stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Stress

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "StressAtPosition._Cast_StressAtPosition":
        return self._Cast_StressAtPosition(self)
