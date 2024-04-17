"""HypoidGearMeshRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.agma_gleason_conical import _568
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Hypoid", "HypoidGearMeshRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.hypoid.standards import _446
    from mastapy.gears.gear_designs.hypoid import _990
    from mastapy.gears.rating.iso_10300 import _428, _427
    from mastapy.gears.rating.conical import _548, _542
    from mastapy.gears.rating.hypoid import _442
    from mastapy.gears.rating import _363, _356
    from mastapy.gears.analysis import _1222


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshRating",)


Self = TypeVar("Self", bound="HypoidGearMeshRating")


class HypoidGearMeshRating(_568.AGMAGleasonConicalGearMeshRating):
    """HypoidGearMeshRating

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearMeshRating")

    class _Cast_HypoidGearMeshRating:
        """Special nested class for casting HypoidGearMeshRating to subclasses."""

        def __init__(
            self: "HypoidGearMeshRating._Cast_HypoidGearMeshRating",
            parent: "HypoidGearMeshRating",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_rating(
            self: "HypoidGearMeshRating._Cast_HypoidGearMeshRating",
        ) -> "_568.AGMAGleasonConicalGearMeshRating":
            return self._parent._cast(_568.AGMAGleasonConicalGearMeshRating)

        @property
        def conical_gear_mesh_rating(
            self: "HypoidGearMeshRating._Cast_HypoidGearMeshRating",
        ) -> "_542.ConicalGearMeshRating":
            from mastapy.gears.rating.conical import _542

            return self._parent._cast(_542.ConicalGearMeshRating)

        @property
        def gear_mesh_rating(
            self: "HypoidGearMeshRating._Cast_HypoidGearMeshRating",
        ) -> "_363.GearMeshRating":
            from mastapy.gears.rating import _363

            return self._parent._cast(_363.GearMeshRating)

        @property
        def abstract_gear_mesh_rating(
            self: "HypoidGearMeshRating._Cast_HypoidGearMeshRating",
        ) -> "_356.AbstractGearMeshRating":
            from mastapy.gears.rating import _356

            return self._parent._cast(_356.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(
            self: "HypoidGearMeshRating._Cast_HypoidGearMeshRating",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def hypoid_gear_mesh_rating(
            self: "HypoidGearMeshRating._Cast_HypoidGearMeshRating",
        ) -> "HypoidGearMeshRating":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshRating._Cast_HypoidGearMeshRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearMeshRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gleason_hypoid_mesh_single_flank_rating(
        self: Self,
    ) -> "_446.GleasonHypoidMeshSingleFlankRating":
        """mastapy.gears.rating.hypoid.standards.GleasonHypoidMeshSingleFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GleasonHypoidMeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hypoid_gear_mesh(self: Self) -> "_990.HypoidGearMeshDesign":
        """mastapy.gears.gear_designs.hypoid.HypoidGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def iso10300_hypoid_mesh_single_flank_rating_method_b1(
        self: Self,
    ) -> "_428.ISO10300MeshSingleFlankRatingMethodB1":
        """mastapy.gears.rating.isoISO10300MeshSingleFlankRatingMethodB1

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO10300HypoidMeshSingleFlankRatingMethodB1

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def iso10300_hypoid_mesh_single_flank_rating_method_b2(
        self: Self,
    ) -> "_427.ISO10300MeshSingleFlankRatingHypoidMethodB2":
        """mastapy.gears.rating.isoISO10300MeshSingleFlankRatingHypoidMethodB2

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO10300HypoidMeshSingleFlankRatingMethodB2

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def meshed_gears(self: Self) -> "List[_548.ConicalMeshedGearRating]":
        """List[mastapy.gears.rating.conical.ConicalMeshedGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gears_in_mesh(self: Self) -> "List[_548.ConicalMeshedGearRating]":
        """List[mastapy.gears.rating.conical.ConicalMeshedGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsInMesh

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_gear_ratings(self: Self) -> "List[_442.HypoidGearRating]":
        """List[mastapy.gears.rating.hypoid.HypoidGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "HypoidGearMeshRating._Cast_HypoidGearMeshRating":
        return self._Cast_HypoidGearMeshRating(self)
