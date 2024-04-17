"""GleasonHypoidGearSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.conical import _546
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GLEASON_HYPOID_GEAR_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Hypoid.Standards", "GleasonHypoidGearSingleFlankRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _367


__docformat__ = "restructuredtext en"
__all__ = ("GleasonHypoidGearSingleFlankRating",)


Self = TypeVar("Self", bound="GleasonHypoidGearSingleFlankRating")


class GleasonHypoidGearSingleFlankRating(_546.ConicalGearSingleFlankRating):
    """GleasonHypoidGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _GLEASON_HYPOID_GEAR_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GleasonHypoidGearSingleFlankRating")

    class _Cast_GleasonHypoidGearSingleFlankRating:
        """Special nested class for casting GleasonHypoidGearSingleFlankRating to subclasses."""

        def __init__(
            self: "GleasonHypoidGearSingleFlankRating._Cast_GleasonHypoidGearSingleFlankRating",
            parent: "GleasonHypoidGearSingleFlankRating",
        ):
            self._parent = parent

        @property
        def conical_gear_single_flank_rating(
            self: "GleasonHypoidGearSingleFlankRating._Cast_GleasonHypoidGearSingleFlankRating",
        ) -> "_546.ConicalGearSingleFlankRating":
            return self._parent._cast(_546.ConicalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(
            self: "GleasonHypoidGearSingleFlankRating._Cast_GleasonHypoidGearSingleFlankRating",
        ) -> "_367.GearSingleFlankRating":
            from mastapy.gears.rating import _367

            return self._parent._cast(_367.GearSingleFlankRating)

        @property
        def gleason_hypoid_gear_single_flank_rating(
            self: "GleasonHypoidGearSingleFlankRating._Cast_GleasonHypoidGearSingleFlankRating",
        ) -> "GleasonHypoidGearSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "GleasonHypoidGearSingleFlankRating._Cast_GleasonHypoidGearSingleFlankRating",
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
        self: Self, instance_to_wrap: "GleasonHypoidGearSingleFlankRating.TYPE"
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
    def geometry_factor_j(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryFactorJ

        if temp is None:
            return 0.0

        return temp

    @property
    def life_factor_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def life_factor_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeFactorContact

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
    def cast_to(
        self: Self,
    ) -> "GleasonHypoidGearSingleFlankRating._Cast_GleasonHypoidGearSingleFlankRating":
        return self._Cast_GleasonHypoidGearSingleFlankRating(self)
