"""KlingelnbergCycloPalloidHypoidGearSetRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.klingelnberg_conical import _416
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.KlingelnbergHypoid",
    "KlingelnbergCycloPalloidHypoidGearSetRating",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _983
    from mastapy.gears.rating.klingelnberg_hypoid import _412, _411
    from mastapy.gears.rating.conical import _545
    from mastapy.gears.rating import _366, _358
    from mastapy.gears.analysis import _1223


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSetRating",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearSetRating")


class KlingelnbergCycloPalloidHypoidGearSetRating(
    _416.KlingelnbergCycloPalloidConicalGearSetRating
):
    """KlingelnbergCycloPalloidHypoidGearSetRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_RATING
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetRating"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetRating:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetRating to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetRating._Cast_KlingelnbergCycloPalloidHypoidGearSetRating",
            parent: "KlingelnbergCycloPalloidHypoidGearSetRating",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_rating(
            self: "KlingelnbergCycloPalloidHypoidGearSetRating._Cast_KlingelnbergCycloPalloidHypoidGearSetRating",
        ) -> "_416.KlingelnbergCycloPalloidConicalGearSetRating":
            return self._parent._cast(_416.KlingelnbergCycloPalloidConicalGearSetRating)

        @property
        def conical_gear_set_rating(
            self: "KlingelnbergCycloPalloidHypoidGearSetRating._Cast_KlingelnbergCycloPalloidHypoidGearSetRating",
        ) -> "_545.ConicalGearSetRating":
            from mastapy.gears.rating.conical import _545

            return self._parent._cast(_545.ConicalGearSetRating)

        @property
        def gear_set_rating(
            self: "KlingelnbergCycloPalloidHypoidGearSetRating._Cast_KlingelnbergCycloPalloidHypoidGearSetRating",
        ) -> "_366.GearSetRating":
            from mastapy.gears.rating import _366

            return self._parent._cast(_366.GearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "KlingelnbergCycloPalloidHypoidGearSetRating._Cast_KlingelnbergCycloPalloidHypoidGearSetRating",
        ) -> "_358.AbstractGearSetRating":
            from mastapy.gears.rating import _358

            return self._parent._cast(_358.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetRating._Cast_KlingelnbergCycloPalloidHypoidGearSetRating",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_rating(
            self: "KlingelnbergCycloPalloidHypoidGearSetRating._Cast_KlingelnbergCycloPalloidHypoidGearSetRating",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetRating":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetRating._Cast_KlingelnbergCycloPalloidHypoidGearSetRating",
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
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetRating.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set(
        self: Self,
    ) -> "_983.KlingelnbergCycloPalloidHypoidGearSetDesign":
        """mastapy.gears.gear_designs.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_ratings(
        self: Self,
    ) -> "List[_412.KlingelnbergCycloPalloidHypoidGearRating]":
        """List[mastapy.gears.rating.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_mesh_ratings(
        self: Self,
    ) -> "List[_411.KlingelnbergCycloPalloidHypoidGearMeshRating]":
        """List[mastapy.gears.rating.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSetRating._Cast_KlingelnbergCycloPalloidHypoidGearSetRating":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetRating(self)
