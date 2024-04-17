"""InternalClearance"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTERNAL_CLEARANCE = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "InternalClearance"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2081


__docformat__ = "restructuredtext en"
__all__ = ("InternalClearance",)


Self = TypeVar("Self", bound="InternalClearance")


class InternalClearance(_0.APIBase):
    """InternalClearance

    This is a mastapy class.
    """

    TYPE = _INTERNAL_CLEARANCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InternalClearance")

    class _Cast_InternalClearance:
        """Special nested class for casting InternalClearance to subclasses."""

        def __init__(
            self: "InternalClearance._Cast_InternalClearance",
            parent: "InternalClearance",
        ):
            self._parent = parent

        @property
        def three_point_contact_internal_clearance(
            self: "InternalClearance._Cast_InternalClearance",
        ) -> "_2081.ThreePointContactInternalClearance":
            from mastapy.bearings.bearing_results.rolling import _2081

            return self._parent._cast(_2081.ThreePointContactInternalClearance)

        @property
        def internal_clearance(
            self: "InternalClearance._Cast_InternalClearance",
        ) -> "InternalClearance":
            return self._parent

        def __getattr__(self: "InternalClearance._Cast_InternalClearance", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InternalClearance.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Axial

        if temp is None:
            return 0.0

        return temp

    @property
    def radial(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Radial

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "InternalClearance._Cast_InternalClearance":
        return self._Cast_InternalClearance(self)
