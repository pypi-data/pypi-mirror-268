"""ThreePointContactInternalClearance"""

from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling import _1980
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_THREE_POINT_CONTACT_INTERNAL_CLEARANCE = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "ThreePointContactInternalClearance"
)


__docformat__ = "restructuredtext en"
__all__ = ("ThreePointContactInternalClearance",)


Self = TypeVar("Self", bound="ThreePointContactInternalClearance")


class ThreePointContactInternalClearance(_1980.InternalClearance):
    """ThreePointContactInternalClearance

    This is a mastapy class.
    """

    TYPE = _THREE_POINT_CONTACT_INTERNAL_CLEARANCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ThreePointContactInternalClearance")

    class _Cast_ThreePointContactInternalClearance:
        """Special nested class for casting ThreePointContactInternalClearance to subclasses."""

        def __init__(
            self: "ThreePointContactInternalClearance._Cast_ThreePointContactInternalClearance",
            parent: "ThreePointContactInternalClearance",
        ):
            self._parent = parent

        @property
        def internal_clearance(
            self: "ThreePointContactInternalClearance._Cast_ThreePointContactInternalClearance",
        ) -> "_1980.InternalClearance":
            return self._parent._cast(_1980.InternalClearance)

        @property
        def three_point_contact_internal_clearance(
            self: "ThreePointContactInternalClearance._Cast_ThreePointContactInternalClearance",
        ) -> "ThreePointContactInternalClearance":
            return self._parent

        def __getattr__(
            self: "ThreePointContactInternalClearance._Cast_ThreePointContactInternalClearance",
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
        self: Self, instance_to_wrap: "ThreePointContactInternalClearance.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def operating_free_contact_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OperatingFreeContactAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ThreePointContactInternalClearance._Cast_ThreePointContactInternalClearance":
        return self._Cast_ThreePointContactInternalClearance(self)
