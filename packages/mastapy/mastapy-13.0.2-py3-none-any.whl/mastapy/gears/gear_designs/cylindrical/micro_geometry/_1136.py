"""TotalLeadReliefWithDeviation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1121
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOTAL_LEAD_RELIEF_WITH_DEVIATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "TotalLeadReliefWithDeviation",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1134


__docformat__ = "restructuredtext en"
__all__ = ("TotalLeadReliefWithDeviation",)


Self = TypeVar("Self", bound="TotalLeadReliefWithDeviation")


class TotalLeadReliefWithDeviation(_1121.LeadReliefWithDeviation):
    """TotalLeadReliefWithDeviation

    This is a mastapy class.
    """

    TYPE = _TOTAL_LEAD_RELIEF_WITH_DEVIATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TotalLeadReliefWithDeviation")

    class _Cast_TotalLeadReliefWithDeviation:
        """Special nested class for casting TotalLeadReliefWithDeviation to subclasses."""

        def __init__(
            self: "TotalLeadReliefWithDeviation._Cast_TotalLeadReliefWithDeviation",
            parent: "TotalLeadReliefWithDeviation",
        ):
            self._parent = parent

        @property
        def lead_relief_with_deviation(
            self: "TotalLeadReliefWithDeviation._Cast_TotalLeadReliefWithDeviation",
        ) -> "_1121.LeadReliefWithDeviation":
            return self._parent._cast(_1121.LeadReliefWithDeviation)

        @property
        def relief_with_deviation(
            self: "TotalLeadReliefWithDeviation._Cast_TotalLeadReliefWithDeviation",
        ) -> "_1134.ReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1134

            return self._parent._cast(_1134.ReliefWithDeviation)

        @property
        def total_lead_relief_with_deviation(
            self: "TotalLeadReliefWithDeviation._Cast_TotalLeadReliefWithDeviation",
        ) -> "TotalLeadReliefWithDeviation":
            return self._parent

        def __getattr__(
            self: "TotalLeadReliefWithDeviation._Cast_TotalLeadReliefWithDeviation",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TotalLeadReliefWithDeviation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "TotalLeadReliefWithDeviation._Cast_TotalLeadReliefWithDeviation":
        return self._Cast_TotalLeadReliefWithDeviation(self)
