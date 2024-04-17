"""LeadModificationSegment"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.manufacturing.cylindrical import _639
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LEAD_MODIFICATION_SEGMENT = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical", "LeadModificationSegment"
)


__docformat__ = "restructuredtext en"
__all__ = ("LeadModificationSegment",)


Self = TypeVar("Self", bound="LeadModificationSegment")


class LeadModificationSegment(_639.ModificationSegment):
    """LeadModificationSegment

    This is a mastapy class.
    """

    TYPE = _LEAD_MODIFICATION_SEGMENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LeadModificationSegment")

    class _Cast_LeadModificationSegment:
        """Special nested class for casting LeadModificationSegment to subclasses."""

        def __init__(
            self: "LeadModificationSegment._Cast_LeadModificationSegment",
            parent: "LeadModificationSegment",
        ):
            self._parent = parent

        @property
        def modification_segment(
            self: "LeadModificationSegment._Cast_LeadModificationSegment",
        ) -> "_639.ModificationSegment":
            return self._parent._cast(_639.ModificationSegment)

        @property
        def lead_modification_segment(
            self: "LeadModificationSegment._Cast_LeadModificationSegment",
        ) -> "LeadModificationSegment":
            return self._parent

        def __getattr__(
            self: "LeadModificationSegment._Cast_LeadModificationSegment", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LeadModificationSegment.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def distance_from_centre(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DistanceFromCentre

        if temp is None:
            return 0.0

        return temp

    @distance_from_centre.setter
    @enforce_parameter_types
    def distance_from_centre(self: Self, value: "float"):
        self.wrapped.DistanceFromCentre = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "LeadModificationSegment._Cast_LeadModificationSegment":
        return self._Cast_LeadModificationSegment(self)
