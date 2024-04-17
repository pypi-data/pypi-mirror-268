"""KlingelnbergCycloPalloidConicalGearMeshRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.conical import _542
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.KlingelnbergConical",
    "KlingelnbergCycloPalloidConicalGearMeshRating",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _408
    from mastapy.gears.rating.klingelnberg_hypoid import _411
    from mastapy.gears.rating import _363, _356
    from mastapy.gears.analysis import _1222


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshRating",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearMeshRating")


class KlingelnbergCycloPalloidConicalGearMeshRating(_542.ConicalGearMeshRating):
    """KlingelnbergCycloPalloidConicalGearMeshRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_RATING
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshRating"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshRating:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshRating to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshRating._Cast_KlingelnbergCycloPalloidConicalGearMeshRating",
            parent: "KlingelnbergCycloPalloidConicalGearMeshRating",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_rating(
            self: "KlingelnbergCycloPalloidConicalGearMeshRating._Cast_KlingelnbergCycloPalloidConicalGearMeshRating",
        ) -> "_542.ConicalGearMeshRating":
            return self._parent._cast(_542.ConicalGearMeshRating)

        @property
        def gear_mesh_rating(
            self: "KlingelnbergCycloPalloidConicalGearMeshRating._Cast_KlingelnbergCycloPalloidConicalGearMeshRating",
        ) -> "_363.GearMeshRating":
            from mastapy.gears.rating import _363

            return self._parent._cast(_363.GearMeshRating)

        @property
        def abstract_gear_mesh_rating(
            self: "KlingelnbergCycloPalloidConicalGearMeshRating._Cast_KlingelnbergCycloPalloidConicalGearMeshRating",
        ) -> "_356.AbstractGearMeshRating":
            from mastapy.gears.rating import _356

            return self._parent._cast(_356.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshRating._Cast_KlingelnbergCycloPalloidConicalGearMeshRating",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_rating(
            self: "KlingelnbergCycloPalloidConicalGearMeshRating._Cast_KlingelnbergCycloPalloidConicalGearMeshRating",
        ) -> "_408.KlingelnbergCycloPalloidSpiralBevelGearMeshRating":
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _408

            return self._parent._cast(
                _408.KlingelnbergCycloPalloidSpiralBevelGearMeshRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_rating(
            self: "KlingelnbergCycloPalloidConicalGearMeshRating._Cast_KlingelnbergCycloPalloidConicalGearMeshRating",
        ) -> "_411.KlingelnbergCycloPalloidHypoidGearMeshRating":
            from mastapy.gears.rating.klingelnberg_hypoid import _411

            return self._parent._cast(_411.KlingelnbergCycloPalloidHypoidGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_rating(
            self: "KlingelnbergCycloPalloidConicalGearMeshRating._Cast_KlingelnbergCycloPalloidConicalGearMeshRating",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshRating":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshRating._Cast_KlingelnbergCycloPalloidConicalGearMeshRating",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshRating.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearMeshRating._Cast_KlingelnbergCycloPalloidConicalGearMeshRating":
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshRating(self)
