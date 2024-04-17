"""TotalProfileReliefWithDeviation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1132
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOTAL_PROFILE_RELIEF_WITH_DEVIATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "TotalProfileReliefWithDeviation",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1134


__docformat__ = "restructuredtext en"
__all__ = ("TotalProfileReliefWithDeviation",)


Self = TypeVar("Self", bound="TotalProfileReliefWithDeviation")


class TotalProfileReliefWithDeviation(_1132.ProfileReliefWithDeviation):
    """TotalProfileReliefWithDeviation

    This is a mastapy class.
    """

    TYPE = _TOTAL_PROFILE_RELIEF_WITH_DEVIATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TotalProfileReliefWithDeviation")

    class _Cast_TotalProfileReliefWithDeviation:
        """Special nested class for casting TotalProfileReliefWithDeviation to subclasses."""

        def __init__(
            self: "TotalProfileReliefWithDeviation._Cast_TotalProfileReliefWithDeviation",
            parent: "TotalProfileReliefWithDeviation",
        ):
            self._parent = parent

        @property
        def profile_relief_with_deviation(
            self: "TotalProfileReliefWithDeviation._Cast_TotalProfileReliefWithDeviation",
        ) -> "_1132.ProfileReliefWithDeviation":
            return self._parent._cast(_1132.ProfileReliefWithDeviation)

        @property
        def relief_with_deviation(
            self: "TotalProfileReliefWithDeviation._Cast_TotalProfileReliefWithDeviation",
        ) -> "_1134.ReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1134

            return self._parent._cast(_1134.ReliefWithDeviation)

        @property
        def total_profile_relief_with_deviation(
            self: "TotalProfileReliefWithDeviation._Cast_TotalProfileReliefWithDeviation",
        ) -> "TotalProfileReliefWithDeviation":
            return self._parent

        def __getattr__(
            self: "TotalProfileReliefWithDeviation._Cast_TotalProfileReliefWithDeviation",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TotalProfileReliefWithDeviation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "TotalProfileReliefWithDeviation._Cast_TotalProfileReliefWithDeviation":
        return self._Cast_TotalProfileReliefWithDeviation(self)
