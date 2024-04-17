"""GearRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating import _357
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_RATING = python_net_import("SMT.MastaAPI.Gears.Rating", "GearRating")

if TYPE_CHECKING:
    from mastapy.materials import _283
    from mastapy.gears.rating import _359
    from mastapy.gears.rating.zerol_bevel import _373
    from mastapy.gears.rating.worm import _377
    from mastapy.gears.rating.straight_bevel import _399
    from mastapy.gears.rating.straight_bevel_diff import _402
    from mastapy.gears.rating.spiral_bevel import _406
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _409
    from mastapy.gears.rating.klingelnberg_hypoid import _412
    from mastapy.gears.rating.klingelnberg_conical import _415
    from mastapy.gears.rating.hypoid import _442
    from mastapy.gears.rating.face import _451
    from mastapy.gears.rating.cylindrical import _463
    from mastapy.gears.rating.conical import _543
    from mastapy.gears.rating.concept import _554
    from mastapy.gears.rating.bevel import _558
    from mastapy.gears.rating.agma_gleason_conical import _569
    from mastapy.gears.analysis import _1221


__docformat__ = "restructuredtext en"
__all__ = ("GearRating",)


Self = TypeVar("Self", bound="GearRating")


class GearRating(_357.AbstractGearRating):
    """GearRating

    This is a mastapy class.
    """

    TYPE = _GEAR_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearRating")

    class _Cast_GearRating:
        """Special nested class for casting GearRating to subclasses."""

        def __init__(self: "GearRating._Cast_GearRating", parent: "GearRating"):
            self._parent = parent

        @property
        def abstract_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_357.AbstractGearRating":
            return self._parent._cast(_357.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "GearRating._Cast_GearRating",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def zerol_bevel_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_373.ZerolBevelGearRating":
            from mastapy.gears.rating.zerol_bevel import _373

            return self._parent._cast(_373.ZerolBevelGearRating)

        @property
        def worm_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_377.WormGearRating":
            from mastapy.gears.rating.worm import _377

            return self._parent._cast(_377.WormGearRating)

        @property
        def straight_bevel_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_399.StraightBevelGearRating":
            from mastapy.gears.rating.straight_bevel import _399

            return self._parent._cast(_399.StraightBevelGearRating)

        @property
        def straight_bevel_diff_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_402.StraightBevelDiffGearRating":
            from mastapy.gears.rating.straight_bevel_diff import _402

            return self._parent._cast(_402.StraightBevelDiffGearRating)

        @property
        def spiral_bevel_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_406.SpiralBevelGearRating":
            from mastapy.gears.rating.spiral_bevel import _406

            return self._parent._cast(_406.SpiralBevelGearRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_409.KlingelnbergCycloPalloidSpiralBevelGearRating":
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _409

            return self._parent._cast(
                _409.KlingelnbergCycloPalloidSpiralBevelGearRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_412.KlingelnbergCycloPalloidHypoidGearRating":
            from mastapy.gears.rating.klingelnberg_hypoid import _412

            return self._parent._cast(_412.KlingelnbergCycloPalloidHypoidGearRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_415.KlingelnbergCycloPalloidConicalGearRating":
            from mastapy.gears.rating.klingelnberg_conical import _415

            return self._parent._cast(_415.KlingelnbergCycloPalloidConicalGearRating)

        @property
        def hypoid_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_442.HypoidGearRating":
            from mastapy.gears.rating.hypoid import _442

            return self._parent._cast(_442.HypoidGearRating)

        @property
        def face_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_451.FaceGearRating":
            from mastapy.gears.rating.face import _451

            return self._parent._cast(_451.FaceGearRating)

        @property
        def cylindrical_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_463.CylindricalGearRating":
            from mastapy.gears.rating.cylindrical import _463

            return self._parent._cast(_463.CylindricalGearRating)

        @property
        def conical_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_543.ConicalGearRating":
            from mastapy.gears.rating.conical import _543

            return self._parent._cast(_543.ConicalGearRating)

        @property
        def concept_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_554.ConceptGearRating":
            from mastapy.gears.rating.concept import _554

            return self._parent._cast(_554.ConceptGearRating)

        @property
        def bevel_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_558.BevelGearRating":
            from mastapy.gears.rating.bevel import _558

            return self._parent._cast(_558.BevelGearRating)

        @property
        def agma_gleason_conical_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_569.AGMAGleasonConicalGearRating":
            from mastapy.gears.rating.agma_gleason_conical import _569

            return self._parent._cast(_569.AGMAGleasonConicalGearRating)

        @property
        def gear_rating(self: "GearRating._Cast_GearRating") -> "GearRating":
            return self._parent

        def __getattr__(self: "GearRating._Cast_GearRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending_safety_factor_results(self: Self) -> "_283.SafetyFactorItem":
        """mastapy.materials.SafetyFactorItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingSafetyFactorResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def contact_safety_factor_results(self: Self) -> "_283.SafetyFactorItem":
        """mastapy.materials.SafetyFactorItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactSafetyFactorResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def static_safety_factor(self: Self) -> "_359.BendingAndContactReportingObject":
        """mastapy.gears.rating.BendingAndContactReportingObject

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticSafetyFactor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearRating._Cast_GearRating":
        return self._Cast_GearRating(self)
