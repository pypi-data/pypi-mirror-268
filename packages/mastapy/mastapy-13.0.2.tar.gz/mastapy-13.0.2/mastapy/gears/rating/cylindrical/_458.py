"""CylindricalGearDutyCycleRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _361
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_DUTY_CYCLE_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "CylindricalGearDutyCycleRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical import _466, _478, _463
    from mastapy.gears.rating import _362, _357
    from mastapy.gears.analysis import _1221


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearDutyCycleRating",)


Self = TypeVar("Self", bound="CylindricalGearDutyCycleRating")


class CylindricalGearDutyCycleRating(_361.GearDutyCycleRating):
    """CylindricalGearDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_DUTY_CYCLE_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearDutyCycleRating")

    class _Cast_CylindricalGearDutyCycleRating:
        """Special nested class for casting CylindricalGearDutyCycleRating to subclasses."""

        def __init__(
            self: "CylindricalGearDutyCycleRating._Cast_CylindricalGearDutyCycleRating",
            parent: "CylindricalGearDutyCycleRating",
        ):
            self._parent = parent

        @property
        def gear_duty_cycle_rating(
            self: "CylindricalGearDutyCycleRating._Cast_CylindricalGearDutyCycleRating",
        ) -> "_361.GearDutyCycleRating":
            return self._parent._cast(_361.GearDutyCycleRating)

        @property
        def abstract_gear_rating(
            self: "CylindricalGearDutyCycleRating._Cast_CylindricalGearDutyCycleRating",
        ) -> "_357.AbstractGearRating":
            from mastapy.gears.rating import _357

            return self._parent._cast(_357.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "CylindricalGearDutyCycleRating._Cast_CylindricalGearDutyCycleRating",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def cylindrical_gear_duty_cycle_rating(
            self: "CylindricalGearDutyCycleRating._Cast_CylindricalGearDutyCycleRating",
        ) -> "CylindricalGearDutyCycleRating":
            return self._parent

        def __getattr__(
            self: "CylindricalGearDutyCycleRating._Cast_CylindricalGearDutyCycleRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearDutyCycleRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def highest_maximum_material_exposure(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HighestMaximumMaterialExposure

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_against_permanent_deformation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorAgainstPermanentDeformation

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_against_permanent_deformation_with_influence_of_rim(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorAgainstPermanentDeformationWithInfluenceOfRim

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_set_design_duty_cycle(
        self: Self,
    ) -> "_466.CylindricalGearSetDutyCycleRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetDesignDutyCycle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_set_design_duty_cycle(
        self: Self,
    ) -> "_466.CylindricalGearSetDutyCycleRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSetDesignDutyCycle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def left_flank_rating(self: Self) -> "_362.GearFlankRating":
        """mastapy.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank_rating(self: Self) -> "_362.GearFlankRating":
        """mastapy.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_mesh_ratings(self: Self) -> "List[_478.MeshRatingForReports]":
        """List[mastapy.gears.rating.cylindrical.MeshRatingForReports]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_ratings(self: Self) -> "List[_463.CylindricalGearRating]":
        """List[mastapy.gears.rating.cylindrical.CylindricalGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_gear_ratings(self: Self) -> "List[_463.CylindricalGearRating]":
        """List[mastapy.gears.rating.cylindrical.CylindricalGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearDutyCycleRating._Cast_CylindricalGearDutyCycleRating":
        return self._Cast_CylindricalGearDutyCycleRating(self)
