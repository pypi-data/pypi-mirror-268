"""GleasonSpiralBevelGearSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.bevel.standards import _564
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GLEASON_SPIRAL_BEVEL_GEAR_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Bevel.Standards",
    "GleasonSpiralBevelGearSingleFlankRating",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.conical import _546
    from mastapy.gears.rating import _367


__docformat__ = "restructuredtext en"
__all__ = ("GleasonSpiralBevelGearSingleFlankRating",)


Self = TypeVar("Self", bound="GleasonSpiralBevelGearSingleFlankRating")


class GleasonSpiralBevelGearSingleFlankRating(_564.SpiralBevelGearSingleFlankRating):
    """GleasonSpiralBevelGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _GLEASON_SPIRAL_BEVEL_GEAR_SINGLE_FLANK_RATING
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GleasonSpiralBevelGearSingleFlankRating"
    )

    class _Cast_GleasonSpiralBevelGearSingleFlankRating:
        """Special nested class for casting GleasonSpiralBevelGearSingleFlankRating to subclasses."""

        def __init__(
            self: "GleasonSpiralBevelGearSingleFlankRating._Cast_GleasonSpiralBevelGearSingleFlankRating",
            parent: "GleasonSpiralBevelGearSingleFlankRating",
        ):
            self._parent = parent

        @property
        def spiral_bevel_gear_single_flank_rating(
            self: "GleasonSpiralBevelGearSingleFlankRating._Cast_GleasonSpiralBevelGearSingleFlankRating",
        ) -> "_564.SpiralBevelGearSingleFlankRating":
            return self._parent._cast(_564.SpiralBevelGearSingleFlankRating)

        @property
        def conical_gear_single_flank_rating(
            self: "GleasonSpiralBevelGearSingleFlankRating._Cast_GleasonSpiralBevelGearSingleFlankRating",
        ) -> "_546.ConicalGearSingleFlankRating":
            from mastapy.gears.rating.conical import _546

            return self._parent._cast(_546.ConicalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(
            self: "GleasonSpiralBevelGearSingleFlankRating._Cast_GleasonSpiralBevelGearSingleFlankRating",
        ) -> "_367.GearSingleFlankRating":
            from mastapy.gears.rating import _367

            return self._parent._cast(_367.GearSingleFlankRating)

        @property
        def gleason_spiral_bevel_gear_single_flank_rating(
            self: "GleasonSpiralBevelGearSingleFlankRating._Cast_GleasonSpiralBevelGearSingleFlankRating",
        ) -> "GleasonSpiralBevelGearSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "GleasonSpiralBevelGearSingleFlankRating._Cast_GleasonSpiralBevelGearSingleFlankRating",
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
        self: Self, instance_to_wrap: "GleasonSpiralBevelGearSingleFlankRating.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def calculated_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculatedBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def calculated_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculatedContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def calculated_scoring_index(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculatedScoringIndex

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_blank_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBlankTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def hardness_ratio_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HardnessRatioFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def working_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorkingBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def working_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorkingContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def working_scoring_index(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorkingScoringIndex

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "GleasonSpiralBevelGearSingleFlankRating._Cast_GleasonSpiralBevelGearSingleFlankRating":
        return self._Cast_GleasonSpiralBevelGearSingleFlankRating(self)
