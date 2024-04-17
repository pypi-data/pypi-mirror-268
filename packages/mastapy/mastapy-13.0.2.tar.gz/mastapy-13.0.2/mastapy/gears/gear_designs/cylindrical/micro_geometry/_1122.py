"""LeadSlopeReliefWithDeviation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1121
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LEAD_SLOPE_RELIEF_WITH_DEVIATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "LeadSlopeReliefWithDeviation",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1134


__docformat__ = "restructuredtext en"
__all__ = ("LeadSlopeReliefWithDeviation",)


Self = TypeVar("Self", bound="LeadSlopeReliefWithDeviation")


class LeadSlopeReliefWithDeviation(_1121.LeadReliefWithDeviation):
    """LeadSlopeReliefWithDeviation

    This is a mastapy class.
    """

    TYPE = _LEAD_SLOPE_RELIEF_WITH_DEVIATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LeadSlopeReliefWithDeviation")

    class _Cast_LeadSlopeReliefWithDeviation:
        """Special nested class for casting LeadSlopeReliefWithDeviation to subclasses."""

        def __init__(
            self: "LeadSlopeReliefWithDeviation._Cast_LeadSlopeReliefWithDeviation",
            parent: "LeadSlopeReliefWithDeviation",
        ):
            self._parent = parent

        @property
        def lead_relief_with_deviation(
            self: "LeadSlopeReliefWithDeviation._Cast_LeadSlopeReliefWithDeviation",
        ) -> "_1121.LeadReliefWithDeviation":
            return self._parent._cast(_1121.LeadReliefWithDeviation)

        @property
        def relief_with_deviation(
            self: "LeadSlopeReliefWithDeviation._Cast_LeadSlopeReliefWithDeviation",
        ) -> "_1134.ReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1134

            return self._parent._cast(_1134.ReliefWithDeviation)

        @property
        def lead_slope_relief_with_deviation(
            self: "LeadSlopeReliefWithDeviation._Cast_LeadSlopeReliefWithDeviation",
        ) -> "LeadSlopeReliefWithDeviation":
            return self._parent

        def __getattr__(
            self: "LeadSlopeReliefWithDeviation._Cast_LeadSlopeReliefWithDeviation",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LeadSlopeReliefWithDeviation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LeadSlopeReliefWithDeviation._Cast_LeadSlopeReliefWithDeviation":
        return self._Cast_LeadSlopeReliefWithDeviation(self)
