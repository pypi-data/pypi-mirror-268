"""PermissibleAxialLoad"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PERMISSIBLE_AXIAL_LOAD = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule", "PermissibleAxialLoad"
)


__docformat__ = "restructuredtext en"
__all__ = ("PermissibleAxialLoad",)


Self = TypeVar("Self", bound="PermissibleAxialLoad")


class PermissibleAxialLoad(_0.APIBase):
    """PermissibleAxialLoad

    This is a mastapy class.
    """

    TYPE = _PERMISSIBLE_AXIAL_LOAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PermissibleAxialLoad")

    class _Cast_PermissibleAxialLoad:
        """Special nested class for casting PermissibleAxialLoad to subclasses."""

        def __init__(
            self: "PermissibleAxialLoad._Cast_PermissibleAxialLoad",
            parent: "PermissibleAxialLoad",
        ):
            self._parent = parent

        @property
        def permissible_axial_load(
            self: "PermissibleAxialLoad._Cast_PermissibleAxialLoad",
        ) -> "PermissibleAxialLoad":
            return self._parent

        def __getattr__(
            self: "PermissibleAxialLoad._Cast_PermissibleAxialLoad", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PermissibleAxialLoad.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def brief_periods(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BriefPeriods

        if temp is None:
            return 0.0

        return temp

    @property
    def continuous(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Continuous

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_loads(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeakLoads

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "PermissibleAxialLoad._Cast_PermissibleAxialLoad":
        return self._Cast_PermissibleAxialLoad(self)
