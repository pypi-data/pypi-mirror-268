"""ISO63361996GearSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.cylindrical.iso6336 import _522
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO63361996_GEAR_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336", "ISO63361996GearSingleFlankRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.din3990 import _535
    from mastapy.gears.rating.cylindrical.iso6336 import _520
    from mastapy.gears.rating.cylindrical import _468
    from mastapy.gears.rating import _367


__docformat__ = "restructuredtext en"
__all__ = ("ISO63361996GearSingleFlankRating",)


Self = TypeVar("Self", bound="ISO63361996GearSingleFlankRating")


class ISO63361996GearSingleFlankRating(_522.ISO6336AbstractMetalGearSingleFlankRating):
    """ISO63361996GearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _ISO63361996_GEAR_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO63361996GearSingleFlankRating")

    class _Cast_ISO63361996GearSingleFlankRating:
        """Special nested class for casting ISO63361996GearSingleFlankRating to subclasses."""

        def __init__(
            self: "ISO63361996GearSingleFlankRating._Cast_ISO63361996GearSingleFlankRating",
            parent: "ISO63361996GearSingleFlankRating",
        ):
            self._parent = parent

        @property
        def iso6336_abstract_metal_gear_single_flank_rating(
            self: "ISO63361996GearSingleFlankRating._Cast_ISO63361996GearSingleFlankRating",
        ) -> "_522.ISO6336AbstractMetalGearSingleFlankRating":
            return self._parent._cast(_522.ISO6336AbstractMetalGearSingleFlankRating)

        @property
        def iso6336_abstract_gear_single_flank_rating(
            self: "ISO63361996GearSingleFlankRating._Cast_ISO63361996GearSingleFlankRating",
        ) -> "_520.ISO6336AbstractGearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _520

            return self._parent._cast(_520.ISO6336AbstractGearSingleFlankRating)

        @property
        def cylindrical_gear_single_flank_rating(
            self: "ISO63361996GearSingleFlankRating._Cast_ISO63361996GearSingleFlankRating",
        ) -> "_468.CylindricalGearSingleFlankRating":
            from mastapy.gears.rating.cylindrical import _468

            return self._parent._cast(_468.CylindricalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(
            self: "ISO63361996GearSingleFlankRating._Cast_ISO63361996GearSingleFlankRating",
        ) -> "_367.GearSingleFlankRating":
            from mastapy.gears.rating import _367

            return self._parent._cast(_367.GearSingleFlankRating)

        @property
        def din3990_gear_single_flank_rating(
            self: "ISO63361996GearSingleFlankRating._Cast_ISO63361996GearSingleFlankRating",
        ) -> "_535.DIN3990GearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.din3990 import _535

            return self._parent._cast(_535.DIN3990GearSingleFlankRating)

        @property
        def iso63361996_gear_single_flank_rating(
            self: "ISO63361996GearSingleFlankRating._Cast_ISO63361996GearSingleFlankRating",
        ) -> "ISO63361996GearSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "ISO63361996GearSingleFlankRating._Cast_ISO63361996GearSingleFlankRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO63361996GearSingleFlankRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def nominal_tooth_root_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalToothRootStress

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ISO63361996GearSingleFlankRating._Cast_ISO63361996GearSingleFlankRating":
        return self._Cast_ISO63361996GearSingleFlankRating(self)
