"""KlingelnbergCycloPalloidConicalGearRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.conical import _543
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.KlingelnbergConical",
    "KlingelnbergCycloPalloidConicalGearRating",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _409
    from mastapy.gears.rating.klingelnberg_hypoid import _412
    from mastapy.gears.rating import _364, _357
    from mastapy.gears.analysis import _1221


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearRating",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearRating")


class KlingelnbergCycloPalloidConicalGearRating(_543.ConicalGearRating):
    """KlingelnbergCycloPalloidConicalGearRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_RATING
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearRating"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearRating:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearRating to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearRating._Cast_KlingelnbergCycloPalloidConicalGearRating",
            parent: "KlingelnbergCycloPalloidConicalGearRating",
        ):
            self._parent = parent

        @property
        def conical_gear_rating(
            self: "KlingelnbergCycloPalloidConicalGearRating._Cast_KlingelnbergCycloPalloidConicalGearRating",
        ) -> "_543.ConicalGearRating":
            return self._parent._cast(_543.ConicalGearRating)

        @property
        def gear_rating(
            self: "KlingelnbergCycloPalloidConicalGearRating._Cast_KlingelnbergCycloPalloidConicalGearRating",
        ) -> "_364.GearRating":
            from mastapy.gears.rating import _364

            return self._parent._cast(_364.GearRating)

        @property
        def abstract_gear_rating(
            self: "KlingelnbergCycloPalloidConicalGearRating._Cast_KlingelnbergCycloPalloidConicalGearRating",
        ) -> "_357.AbstractGearRating":
            from mastapy.gears.rating import _357

            return self._parent._cast(_357.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "KlingelnbergCycloPalloidConicalGearRating._Cast_KlingelnbergCycloPalloidConicalGearRating",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(
            self: "KlingelnbergCycloPalloidConicalGearRating._Cast_KlingelnbergCycloPalloidConicalGearRating",
        ) -> "_409.KlingelnbergCycloPalloidSpiralBevelGearRating":
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _409

            return self._parent._cast(
                _409.KlingelnbergCycloPalloidSpiralBevelGearRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_rating(
            self: "KlingelnbergCycloPalloidConicalGearRating._Cast_KlingelnbergCycloPalloidConicalGearRating",
        ) -> "_412.KlingelnbergCycloPalloidHypoidGearRating":
            from mastapy.gears.rating.klingelnberg_hypoid import _412

            return self._parent._cast(_412.KlingelnbergCycloPalloidHypoidGearRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_rating(
            self: "KlingelnbergCycloPalloidConicalGearRating._Cast_KlingelnbergCycloPalloidConicalGearRating",
        ) -> "KlingelnbergCycloPalloidConicalGearRating":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearRating._Cast_KlingelnbergCycloPalloidConicalGearRating",
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
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidConicalGearRating.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearRating._Cast_KlingelnbergCycloPalloidConicalGearRating":
        return self._Cast_KlingelnbergCycloPalloidConicalGearRating(self)
