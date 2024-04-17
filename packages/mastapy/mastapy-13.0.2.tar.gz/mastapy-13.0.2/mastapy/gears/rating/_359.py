"""BendingAndContactReportingObject"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BENDING_AND_CONTACT_REPORTING_OBJECT = python_net_import(
    "SMT.MastaAPI.Gears.Rating", "BendingAndContactReportingObject"
)


__docformat__ = "restructuredtext en"
__all__ = ("BendingAndContactReportingObject",)


Self = TypeVar("Self", bound="BendingAndContactReportingObject")


class BendingAndContactReportingObject(_0.APIBase):
    """BendingAndContactReportingObject

    This is a mastapy class.
    """

    TYPE = _BENDING_AND_CONTACT_REPORTING_OBJECT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BendingAndContactReportingObject")

    class _Cast_BendingAndContactReportingObject:
        """Special nested class for casting BendingAndContactReportingObject to subclasses."""

        def __init__(
            self: "BendingAndContactReportingObject._Cast_BendingAndContactReportingObject",
            parent: "BendingAndContactReportingObject",
        ):
            self._parent = parent

        @property
        def bending_and_contact_reporting_object(
            self: "BendingAndContactReportingObject._Cast_BendingAndContactReportingObject",
        ) -> "BendingAndContactReportingObject":
            return self._parent

        def __getattr__(
            self: "BendingAndContactReportingObject._Cast_BendingAndContactReportingObject",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BendingAndContactReportingObject.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Bending

        if temp is None:
            return 0.0

        return temp

    @property
    def contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Contact

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "BendingAndContactReportingObject._Cast_BendingAndContactReportingObject":
        return self._Cast_BendingAndContactReportingObject(self)
