"""OperatingViscosity"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OPERATING_VISCOSITY = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule", "OperatingViscosity"
)


__docformat__ = "restructuredtext en"
__all__ = ("OperatingViscosity",)


Self = TypeVar("Self", bound="OperatingViscosity")


class OperatingViscosity(_0.APIBase):
    """OperatingViscosity

    This is a mastapy class.
    """

    TYPE = _OPERATING_VISCOSITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OperatingViscosity")

    class _Cast_OperatingViscosity:
        """Special nested class for casting OperatingViscosity to subclasses."""

        def __init__(
            self: "OperatingViscosity._Cast_OperatingViscosity",
            parent: "OperatingViscosity",
        ):
            self._parent = parent

        @property
        def operating_viscosity(
            self: "OperatingViscosity._Cast_OperatingViscosity",
        ) -> "OperatingViscosity":
            return self._parent

        def __getattr__(self: "OperatingViscosity._Cast_OperatingViscosity", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OperatingViscosity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def actual(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Actual

        if temp is None:
            return 0.0

        return temp

    @property
    def rated(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rated

        if temp is None:
            return 0.0

        return temp

    @property
    def rated_at_40_degrees_c(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatedAt40DegreesC

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "OperatingViscosity._Cast_OperatingViscosity":
        return self._Cast_OperatingViscosity(self)
