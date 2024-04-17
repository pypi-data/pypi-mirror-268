"""CylindricalGearRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating import _364
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "CylindricalGearRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1016
    from mastapy.gears.rating import _362, _357
    from mastapy.gears.rating.cylindrical import _491
    from mastapy.gears.analysis import _1221


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearRating",)


Self = TypeVar("Self", bound="CylindricalGearRating")


class CylindricalGearRating(_364.GearRating):
    """CylindricalGearRating

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearRating")

    class _Cast_CylindricalGearRating:
        """Special nested class for casting CylindricalGearRating to subclasses."""

        def __init__(
            self: "CylindricalGearRating._Cast_CylindricalGearRating",
            parent: "CylindricalGearRating",
        ):
            self._parent = parent

        @property
        def gear_rating(
            self: "CylindricalGearRating._Cast_CylindricalGearRating",
        ) -> "_364.GearRating":
            return self._parent._cast(_364.GearRating)

        @property
        def abstract_gear_rating(
            self: "CylindricalGearRating._Cast_CylindricalGearRating",
        ) -> "_357.AbstractGearRating":
            from mastapy.gears.rating import _357

            return self._parent._cast(_357.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "CylindricalGearRating._Cast_CylindricalGearRating",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def cylindrical_gear_rating(
            self: "CylindricalGearRating._Cast_CylindricalGearRating",
        ) -> "CylindricalGearRating":
            return self._parent

        def __getattr__(
            self: "CylindricalGearRating._Cast_CylindricalGearRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def damage_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DamageBending

        if temp is None:
            return 0.0

        return temp

    @property
    def damage_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DamageContact

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_crack_initiation_safety_factor_with_influence_of_rim(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorstCrackInitiationSafetyFactorWithInfluenceOfRim

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_fatigue_fracture_safety_factor_with_influence_of_rim(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorstFatigueFractureSafetyFactorWithInfluenceOfRim

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_permanent_deformation_safety_factor_with_influence_of_rim(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorstPermanentDeformationSafetyFactorWithInfluenceOfRim

        if temp is None:
            return 0.0

        return temp

    @property
    def cylindrical_gear(self: Self) -> "_1016.CylindricalGearDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGear

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
    def vdi2737_safety_factor(self: Self) -> "_491.VDI2737SafetyFactorReportingObject":
        """mastapy.gears.rating.cylindrical.VDI2737SafetyFactorReportingObject

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VDI2737SafetyFactor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CylindricalGearRating._Cast_CylindricalGearRating":
        return self._Cast_CylindricalGearRating(self)
