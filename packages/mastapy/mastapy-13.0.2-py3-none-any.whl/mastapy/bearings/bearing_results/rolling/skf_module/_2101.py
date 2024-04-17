"""RotationalFrequency"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROTATIONAL_FREQUENCY = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule", "RotationalFrequency"
)


__docformat__ = "restructuredtext en"
__all__ = ("RotationalFrequency",)


Self = TypeVar("Self", bound="RotationalFrequency")


class RotationalFrequency(_0.APIBase):
    """RotationalFrequency

    This is a mastapy class.
    """

    TYPE = _ROTATIONAL_FREQUENCY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RotationalFrequency")

    class _Cast_RotationalFrequency:
        """Special nested class for casting RotationalFrequency to subclasses."""

        def __init__(
            self: "RotationalFrequency._Cast_RotationalFrequency",
            parent: "RotationalFrequency",
        ):
            self._parent = parent

        @property
        def rotational_frequency(
            self: "RotationalFrequency._Cast_RotationalFrequency",
        ) -> "RotationalFrequency":
            return self._parent

        def __getattr__(
            self: "RotationalFrequency._Cast_RotationalFrequency", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RotationalFrequency.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def inner_ring(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRing

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_ring(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRing

        if temp is None:
            return 0.0

        return temp

    @property
    def rolling_element_about_its_axis(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollingElementAboutItsAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def rolling_element_set_ampersand_cage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollingElementSetAmpersandCage

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "RotationalFrequency._Cast_RotationalFrequency":
        return self._Cast_RotationalFrequency(self)
