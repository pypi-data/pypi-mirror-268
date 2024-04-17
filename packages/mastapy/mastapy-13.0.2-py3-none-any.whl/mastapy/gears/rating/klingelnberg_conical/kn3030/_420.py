"""KlingelnbergCycloPalloidHypoidGearSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.klingelnberg_conical.kn3030 import _419
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.KlingelnbergConical.KN3030",
    "KlingelnbergCycloPalloidHypoidGearSingleFlankRating",
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _367


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSingleFlankRating",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearSingleFlankRating")


class KlingelnbergCycloPalloidHypoidGearSingleFlankRating(
    _419.KlingelnbergCycloPalloidConicalGearSingleFlankRating
):
    """KlingelnbergCycloPalloidHypoidGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SINGLE_FLANK_RATING
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearSingleFlankRating"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSingleFlankRating:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSingleFlankRating to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSingleFlankRating._Cast_KlingelnbergCycloPalloidHypoidGearSingleFlankRating",
            parent: "KlingelnbergCycloPalloidHypoidGearSingleFlankRating",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_single_flank_rating(
            self: "KlingelnbergCycloPalloidHypoidGearSingleFlankRating._Cast_KlingelnbergCycloPalloidHypoidGearSingleFlankRating",
        ) -> "_419.KlingelnbergCycloPalloidConicalGearSingleFlankRating":
            return self._parent._cast(
                _419.KlingelnbergCycloPalloidConicalGearSingleFlankRating
            )

        @property
        def gear_single_flank_rating(
            self: "KlingelnbergCycloPalloidHypoidGearSingleFlankRating._Cast_KlingelnbergCycloPalloidHypoidGearSingleFlankRating",
        ) -> "_367.GearSingleFlankRating":
            from mastapy.gears.rating import _367

            return self._parent._cast(_367.GearSingleFlankRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_single_flank_rating(
            self: "KlingelnbergCycloPalloidHypoidGearSingleFlankRating._Cast_KlingelnbergCycloPalloidHypoidGearSingleFlankRating",
        ) -> "KlingelnbergCycloPalloidHypoidGearSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSingleFlankRating._Cast_KlingelnbergCycloPalloidHypoidGearSingleFlankRating",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSingleFlankRating.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def tangential_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSingleFlankRating._Cast_KlingelnbergCycloPalloidHypoidGearSingleFlankRating":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSingleFlankRating(self)
