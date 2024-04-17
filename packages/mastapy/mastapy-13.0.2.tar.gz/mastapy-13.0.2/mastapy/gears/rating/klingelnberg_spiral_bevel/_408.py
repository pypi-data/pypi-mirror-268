"""KlingelnbergCycloPalloidSpiralBevelGearMeshRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.klingelnberg_conical import _414
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.KlingelnbergSpiralBevel",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshRating",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.klingelnberg_conical.kn3030 import _422
    from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _978
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _409
    from mastapy.gears.rating.conical import _542
    from mastapy.gears.rating import _363, _356
    from mastapy.gears.analysis import _1222


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearMeshRating",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelGearMeshRating")


class KlingelnbergCycloPalloidSpiralBevelGearMeshRating(
    _414.KlingelnbergCycloPalloidConicalGearMeshRating
):
    """KlingelnbergCycloPalloidSpiralBevelGearMeshRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_RATING
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshRating"
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshRating:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearMeshRating to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshRating",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearMeshRating",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_rating(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshRating",
        ) -> "_414.KlingelnbergCycloPalloidConicalGearMeshRating":
            return self._parent._cast(
                _414.KlingelnbergCycloPalloidConicalGearMeshRating
            )

        @property
        def conical_gear_mesh_rating(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshRating",
        ) -> "_542.ConicalGearMeshRating":
            from mastapy.gears.rating.conical import _542

            return self._parent._cast(_542.ConicalGearMeshRating)

        @property
        def gear_mesh_rating(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshRating",
        ) -> "_363.GearMeshRating":
            from mastapy.gears.rating import _363

            return self._parent._cast(_363.GearMeshRating)

        @property
        def abstract_gear_mesh_rating(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshRating",
        ) -> "_356.AbstractGearMeshRating":
            from mastapy.gears.rating import _356

            return self._parent._cast(_356.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshRating",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_rating(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshRating",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshRating":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshRating",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearMeshRating.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def kn3030_klingelnberg_mesh_single_flank_rating(
        self: Self,
    ) -> "_422.KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating":
        """mastapy.gears.rating.klingelnberg_conical.kn3030.KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KN3030KlingelnbergMeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
        self: Self,
    ) -> "_978.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign":
        """mastapy.gears.gear_designs.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_ratings(
        self: Self,
    ) -> "List[_409.KlingelnbergCycloPalloidSpiralBevelGearRating]":
        """List[mastapy.gears.rating.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshRating":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshRating(self)
