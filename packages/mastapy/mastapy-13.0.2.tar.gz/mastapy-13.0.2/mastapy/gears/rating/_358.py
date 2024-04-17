"""AbstractGearSetRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1223
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating", "AbstractGearSetRating"
)

if TYPE_CHECKING:
    from mastapy.gears import _331
    from mastapy.gears.rating import _356, _357, _365, _366
    from mastapy.gears.rating.zerol_bevel import _374
    from mastapy.gears.rating.worm import _378, _379
    from mastapy.gears.rating.straight_bevel import _400
    from mastapy.gears.rating.straight_bevel_diff import _403
    from mastapy.gears.rating.spiral_bevel import _407
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _410
    from mastapy.gears.rating.klingelnberg_hypoid import _413
    from mastapy.gears.rating.klingelnberg_conical import _416
    from mastapy.gears.rating.hypoid import _443
    from mastapy.gears.rating.face import _452, _453
    from mastapy.gears.rating.cylindrical import _466, _467, _483
    from mastapy.gears.rating.conical import _544, _545
    from mastapy.gears.rating.concept import _555, _556
    from mastapy.gears.rating.bevel import _559
    from mastapy.gears.rating.agma_gleason_conical import _570


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearSetRating",)


Self = TypeVar("Self", bound="AbstractGearSetRating")


class AbstractGearSetRating(_1223.AbstractGearSetAnalysis):
    """AbstractGearSetRating

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractGearSetRating")

    class _Cast_AbstractGearSetRating:
        """Special nested class for casting AbstractGearSetRating to subclasses."""

        def __init__(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
            parent: "AbstractGearSetRating",
        ):
            self._parent = parent

        @property
        def abstract_gear_set_analysis(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_1223.AbstractGearSetAnalysis":
            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_365.GearSetDutyCycleRating":
            from mastapy.gears.rating import _365

            return self._parent._cast(_365.GearSetDutyCycleRating)

        @property
        def gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_366.GearSetRating":
            from mastapy.gears.rating import _366

            return self._parent._cast(_366.GearSetRating)

        @property
        def zerol_bevel_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_374.ZerolBevelGearSetRating":
            from mastapy.gears.rating.zerol_bevel import _374

            return self._parent._cast(_374.ZerolBevelGearSetRating)

        @property
        def worm_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_378.WormGearSetDutyCycleRating":
            from mastapy.gears.rating.worm import _378

            return self._parent._cast(_378.WormGearSetDutyCycleRating)

        @property
        def worm_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_379.WormGearSetRating":
            from mastapy.gears.rating.worm import _379

            return self._parent._cast(_379.WormGearSetRating)

        @property
        def straight_bevel_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_400.StraightBevelGearSetRating":
            from mastapy.gears.rating.straight_bevel import _400

            return self._parent._cast(_400.StraightBevelGearSetRating)

        @property
        def straight_bevel_diff_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_403.StraightBevelDiffGearSetRating":
            from mastapy.gears.rating.straight_bevel_diff import _403

            return self._parent._cast(_403.StraightBevelDiffGearSetRating)

        @property
        def spiral_bevel_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_407.SpiralBevelGearSetRating":
            from mastapy.gears.rating.spiral_bevel import _407

            return self._parent._cast(_407.SpiralBevelGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_410.KlingelnbergCycloPalloidSpiralBevelGearSetRating":
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _410

            return self._parent._cast(
                _410.KlingelnbergCycloPalloidSpiralBevelGearSetRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_413.KlingelnbergCycloPalloidHypoidGearSetRating":
            from mastapy.gears.rating.klingelnberg_hypoid import _413

            return self._parent._cast(_413.KlingelnbergCycloPalloidHypoidGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_416.KlingelnbergCycloPalloidConicalGearSetRating":
            from mastapy.gears.rating.klingelnberg_conical import _416

            return self._parent._cast(_416.KlingelnbergCycloPalloidConicalGearSetRating)

        @property
        def hypoid_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_443.HypoidGearSetRating":
            from mastapy.gears.rating.hypoid import _443

            return self._parent._cast(_443.HypoidGearSetRating)

        @property
        def face_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_452.FaceGearSetDutyCycleRating":
            from mastapy.gears.rating.face import _452

            return self._parent._cast(_452.FaceGearSetDutyCycleRating)

        @property
        def face_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_453.FaceGearSetRating":
            from mastapy.gears.rating.face import _453

            return self._parent._cast(_453.FaceGearSetRating)

        @property
        def cylindrical_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_466.CylindricalGearSetDutyCycleRating":
            from mastapy.gears.rating.cylindrical import _466

            return self._parent._cast(_466.CylindricalGearSetDutyCycleRating)

        @property
        def cylindrical_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_467.CylindricalGearSetRating":
            from mastapy.gears.rating.cylindrical import _467

            return self._parent._cast(_467.CylindricalGearSetRating)

        @property
        def reduced_cylindrical_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_483.ReducedCylindricalGearSetDutyCycleRating":
            from mastapy.gears.rating.cylindrical import _483

            return self._parent._cast(_483.ReducedCylindricalGearSetDutyCycleRating)

        @property
        def conical_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_544.ConicalGearSetDutyCycleRating":
            from mastapy.gears.rating.conical import _544

            return self._parent._cast(_544.ConicalGearSetDutyCycleRating)

        @property
        def conical_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_545.ConicalGearSetRating":
            from mastapy.gears.rating.conical import _545

            return self._parent._cast(_545.ConicalGearSetRating)

        @property
        def concept_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_555.ConceptGearSetDutyCycleRating":
            from mastapy.gears.rating.concept import _555

            return self._parent._cast(_555.ConceptGearSetDutyCycleRating)

        @property
        def concept_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_556.ConceptGearSetRating":
            from mastapy.gears.rating.concept import _556

            return self._parent._cast(_556.ConceptGearSetRating)

        @property
        def bevel_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_559.BevelGearSetRating":
            from mastapy.gears.rating.bevel import _559

            return self._parent._cast(_559.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_570.AGMAGleasonConicalGearSetRating":
            from mastapy.gears.rating.agma_gleason_conical import _570

            return self._parent._cast(_570.AGMAGleasonConicalGearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "AbstractGearSetRating":
            return self._parent

        def __getattr__(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractGearSetRating.TYPE"):
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
    def bending_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingSafetyFactorForStatic

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
    def contact_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_bending_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedBendingSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_bending_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedBendingSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_contact_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedContactSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_contact_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedContactSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_safety_factor_for_fatigue_and_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedSafetyFactorForFatigueAndStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def total_gear_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalGearReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def transmission_properties_gears(self: Self) -> "_331.GearSetDesignGroup":
        """mastapy.gears.GearSetDesignGroup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransmissionPropertiesGears

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_mesh_ratings(self: Self) -> "List[_356.AbstractGearMeshRating]":
        """List[mastapy.gears.rating.AbstractGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_ratings(self: Self) -> "List[_357.AbstractGearRating]":
        """List[mastapy.gears.rating.AbstractGearRating]

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
    def cast_to(self: Self) -> "AbstractGearSetRating._Cast_AbstractGearSetRating":
        return self._Cast_AbstractGearSetRating(self)
