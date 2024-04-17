"""KlingelnbergCycloPalloidSpiralBevelGearRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating.klingelnberg_conical import _415
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.KlingelnbergSpiralBevel",
    "KlingelnbergCycloPalloidSpiralBevelGearRating",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _977
    from mastapy.gears.rating.conical import _543
    from mastapy.gears.rating import _364, _357
    from mastapy.gears.analysis import _1221


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearRating",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelGearRating")


class KlingelnbergCycloPalloidSpiralBevelGearRating(
    _415.KlingelnbergCycloPalloidConicalGearRating
):
    """KlingelnbergCycloPalloidSpiralBevelGearRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_RATING
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearRating"
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearRating:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearRating to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearRating",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearRating",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_rating(
            self: "KlingelnbergCycloPalloidSpiralBevelGearRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearRating",
        ) -> "_415.KlingelnbergCycloPalloidConicalGearRating":
            return self._parent._cast(_415.KlingelnbergCycloPalloidConicalGearRating)

        @property
        def conical_gear_rating(
            self: "KlingelnbergCycloPalloidSpiralBevelGearRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearRating",
        ) -> "_543.ConicalGearRating":
            from mastapy.gears.rating.conical import _543

            return self._parent._cast(_543.ConicalGearRating)

        @property
        def gear_rating(
            self: "KlingelnbergCycloPalloidSpiralBevelGearRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearRating",
        ) -> "_364.GearRating":
            from mastapy.gears.rating import _364

            return self._parent._cast(_364.GearRating)

        @property
        def abstract_gear_rating(
            self: "KlingelnbergCycloPalloidSpiralBevelGearRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearRating",
        ) -> "_357.AbstractGearRating":
            from mastapy.gears.rating import _357

            return self._parent._cast(_357.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearRating",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(
            self: "KlingelnbergCycloPalloidSpiralBevelGearRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearRating",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearRating":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearRating",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearRating.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear(
        self: Self,
    ) -> "_977.KlingelnbergCycloPalloidSpiralBevelGearDesign":
        """mastapy.gears.gear_designs.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearRating":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearRating(self)
