"""LeadFormReliefWithDeviation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1121
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LEAD_FORM_RELIEF_WITH_DEVIATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "LeadFormReliefWithDeviation",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1134


__docformat__ = "restructuredtext en"
__all__ = ("LeadFormReliefWithDeviation",)


Self = TypeVar("Self", bound="LeadFormReliefWithDeviation")


class LeadFormReliefWithDeviation(_1121.LeadReliefWithDeviation):
    """LeadFormReliefWithDeviation

    This is a mastapy class.
    """

    TYPE = _LEAD_FORM_RELIEF_WITH_DEVIATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LeadFormReliefWithDeviation")

    class _Cast_LeadFormReliefWithDeviation:
        """Special nested class for casting LeadFormReliefWithDeviation to subclasses."""

        def __init__(
            self: "LeadFormReliefWithDeviation._Cast_LeadFormReliefWithDeviation",
            parent: "LeadFormReliefWithDeviation",
        ):
            self._parent = parent

        @property
        def lead_relief_with_deviation(
            self: "LeadFormReliefWithDeviation._Cast_LeadFormReliefWithDeviation",
        ) -> "_1121.LeadReliefWithDeviation":
            return self._parent._cast(_1121.LeadReliefWithDeviation)

        @property
        def relief_with_deviation(
            self: "LeadFormReliefWithDeviation._Cast_LeadFormReliefWithDeviation",
        ) -> "_1134.ReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1134

            return self._parent._cast(_1134.ReliefWithDeviation)

        @property
        def lead_form_relief_with_deviation(
            self: "LeadFormReliefWithDeviation._Cast_LeadFormReliefWithDeviation",
        ) -> "LeadFormReliefWithDeviation":
            return self._parent

        def __getattr__(
            self: "LeadFormReliefWithDeviation._Cast_LeadFormReliefWithDeviation",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LeadFormReliefWithDeviation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LeadFormReliefWithDeviation._Cast_LeadFormReliefWithDeviation":
        return self._Cast_LeadFormReliefWithDeviation(self)
