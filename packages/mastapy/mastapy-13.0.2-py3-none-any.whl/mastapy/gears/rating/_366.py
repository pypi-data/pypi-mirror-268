"""GearSetRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _358
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_RATING = python_net_import("SMT.MastaAPI.Gears.Rating", "GearSetRating")

if TYPE_CHECKING:
    from mastapy.materials import _270
    from mastapy.gears.rating import _363, _364
    from mastapy.gears.rating.zerol_bevel import _374
    from mastapy.gears.rating.worm import _379
    from mastapy.gears.rating.straight_bevel import _400
    from mastapy.gears.rating.straight_bevel_diff import _403
    from mastapy.gears.rating.spiral_bevel import _407
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _410
    from mastapy.gears.rating.klingelnberg_hypoid import _413
    from mastapy.gears.rating.klingelnberg_conical import _416
    from mastapy.gears.rating.hypoid import _443
    from mastapy.gears.rating.face import _453
    from mastapy.gears.rating.cylindrical import _467
    from mastapy.gears.rating.conical import _545
    from mastapy.gears.rating.concept import _556
    from mastapy.gears.rating.bevel import _559
    from mastapy.gears.rating.agma_gleason_conical import _570
    from mastapy.gears.analysis import _1223


__docformat__ = "restructuredtext en"
__all__ = ("GearSetRating",)


Self = TypeVar("Self", bound="GearSetRating")


class GearSetRating(_358.AbstractGearSetRating):
    """GearSetRating

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetRating")

    class _Cast_GearSetRating:
        """Special nested class for casting GearSetRating to subclasses."""

        def __init__(
            self: "GearSetRating._Cast_GearSetRating", parent: "GearSetRating"
        ):
            self._parent = parent

        @property
        def abstract_gear_set_rating(
            self: "GearSetRating._Cast_GearSetRating",
        ) -> "_358.AbstractGearSetRating":
            return self._parent._cast(_358.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "GearSetRating._Cast_GearSetRating",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def zerol_bevel_gear_set_rating(
            self: "GearSetRating._Cast_GearSetRating",
        ) -> "_374.ZerolBevelGearSetRating":
            from mastapy.gears.rating.zerol_bevel import _374

            return self._parent._cast(_374.ZerolBevelGearSetRating)

        @property
        def worm_gear_set_rating(
            self: "GearSetRating._Cast_GearSetRating",
        ) -> "_379.WormGearSetRating":
            from mastapy.gears.rating.worm import _379

            return self._parent._cast(_379.WormGearSetRating)

        @property
        def straight_bevel_gear_set_rating(
            self: "GearSetRating._Cast_GearSetRating",
        ) -> "_400.StraightBevelGearSetRating":
            from mastapy.gears.rating.straight_bevel import _400

            return self._parent._cast(_400.StraightBevelGearSetRating)

        @property
        def straight_bevel_diff_gear_set_rating(
            self: "GearSetRating._Cast_GearSetRating",
        ) -> "_403.StraightBevelDiffGearSetRating":
            from mastapy.gears.rating.straight_bevel_diff import _403

            return self._parent._cast(_403.StraightBevelDiffGearSetRating)

        @property
        def spiral_bevel_gear_set_rating(
            self: "GearSetRating._Cast_GearSetRating",
        ) -> "_407.SpiralBevelGearSetRating":
            from mastapy.gears.rating.spiral_bevel import _407

            return self._parent._cast(_407.SpiralBevelGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(
            self: "GearSetRating._Cast_GearSetRating",
        ) -> "_410.KlingelnbergCycloPalloidSpiralBevelGearSetRating":
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _410

            return self._parent._cast(
                _410.KlingelnbergCycloPalloidSpiralBevelGearSetRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_rating(
            self: "GearSetRating._Cast_GearSetRating",
        ) -> "_413.KlingelnbergCycloPalloidHypoidGearSetRating":
            from mastapy.gears.rating.klingelnberg_hypoid import _413

            return self._parent._cast(_413.KlingelnbergCycloPalloidHypoidGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_rating(
            self: "GearSetRating._Cast_GearSetRating",
        ) -> "_416.KlingelnbergCycloPalloidConicalGearSetRating":
            from mastapy.gears.rating.klingelnberg_conical import _416

            return self._parent._cast(_416.KlingelnbergCycloPalloidConicalGearSetRating)

        @property
        def hypoid_gear_set_rating(
            self: "GearSetRating._Cast_GearSetRating",
        ) -> "_443.HypoidGearSetRating":
            from mastapy.gears.rating.hypoid import _443

            return self._parent._cast(_443.HypoidGearSetRating)

        @property
        def face_gear_set_rating(
            self: "GearSetRating._Cast_GearSetRating",
        ) -> "_453.FaceGearSetRating":
            from mastapy.gears.rating.face import _453

            return self._parent._cast(_453.FaceGearSetRating)

        @property
        def cylindrical_gear_set_rating(
            self: "GearSetRating._Cast_GearSetRating",
        ) -> "_467.CylindricalGearSetRating":
            from mastapy.gears.rating.cylindrical import _467

            return self._parent._cast(_467.CylindricalGearSetRating)

        @property
        def conical_gear_set_rating(
            self: "GearSetRating._Cast_GearSetRating",
        ) -> "_545.ConicalGearSetRating":
            from mastapy.gears.rating.conical import _545

            return self._parent._cast(_545.ConicalGearSetRating)

        @property
        def concept_gear_set_rating(
            self: "GearSetRating._Cast_GearSetRating",
        ) -> "_556.ConceptGearSetRating":
            from mastapy.gears.rating.concept import _556

            return self._parent._cast(_556.ConceptGearSetRating)

        @property
        def bevel_gear_set_rating(
            self: "GearSetRating._Cast_GearSetRating",
        ) -> "_559.BevelGearSetRating":
            from mastapy.gears.rating.bevel import _559

            return self._parent._cast(_559.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(
            self: "GearSetRating._Cast_GearSetRating",
        ) -> "_570.AGMAGleasonConicalGearSetRating":
            from mastapy.gears.rating.agma_gleason_conical import _570

            return self._parent._cast(_570.AGMAGleasonConicalGearSetRating)

        @property
        def gear_set_rating(
            self: "GearSetRating._Cast_GearSetRating",
        ) -> "GearSetRating":
            return self._parent

        def __getattr__(self: "GearSetRating._Cast_GearSetRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def rating(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return ""

        return temp

    @property
    def total_gear_set_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalGearSetReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def lubrication_detail(self: Self) -> "_270.LubricationDetail":
        """mastapy.materials.LubricationDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricationDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_mesh_ratings(self: Self) -> "List[_363.GearMeshRating]":
        """List[mastapy.gears.rating.GearMeshRating]

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
    def gear_ratings(self: Self) -> "List[_364.GearRating]":
        """List[mastapy.gears.rating.GearRating]

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
    def cast_to(self: Self) -> "GearSetRating._Cast_GearSetRating":
        return self._Cast_GearSetRating(self)
