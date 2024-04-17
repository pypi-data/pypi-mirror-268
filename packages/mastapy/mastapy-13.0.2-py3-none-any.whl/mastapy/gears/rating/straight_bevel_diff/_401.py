"""StraightBevelDiffGearMeshRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.conical import _542
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.StraightBevelDiff", "StraightBevelDiffGearMeshRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel_diff import _970
    from mastapy.gears.rating.straight_bevel_diff import _404, _402
    from mastapy.gears.rating import _363, _356
    from mastapy.gears.analysis import _1222


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshRating",)


Self = TypeVar("Self", bound="StraightBevelDiffGearMeshRating")


class StraightBevelDiffGearMeshRating(_542.ConicalGearMeshRating):
    """StraightBevelDiffGearMeshRating

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffGearMeshRating")

    class _Cast_StraightBevelDiffGearMeshRating:
        """Special nested class for casting StraightBevelDiffGearMeshRating to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshRating._Cast_StraightBevelDiffGearMeshRating",
            parent: "StraightBevelDiffGearMeshRating",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_rating(
            self: "StraightBevelDiffGearMeshRating._Cast_StraightBevelDiffGearMeshRating",
        ) -> "_542.ConicalGearMeshRating":
            return self._parent._cast(_542.ConicalGearMeshRating)

        @property
        def gear_mesh_rating(
            self: "StraightBevelDiffGearMeshRating._Cast_StraightBevelDiffGearMeshRating",
        ) -> "_363.GearMeshRating":
            from mastapy.gears.rating import _363

            return self._parent._cast(_363.GearMeshRating)

        @property
        def abstract_gear_mesh_rating(
            self: "StraightBevelDiffGearMeshRating._Cast_StraightBevelDiffGearMeshRating",
        ) -> "_356.AbstractGearMeshRating":
            from mastapy.gears.rating import _356

            return self._parent._cast(_356.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(
            self: "StraightBevelDiffGearMeshRating._Cast_StraightBevelDiffGearMeshRating",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_rating(
            self: "StraightBevelDiffGearMeshRating._Cast_StraightBevelDiffGearMeshRating",
        ) -> "StraightBevelDiffGearMeshRating":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshRating._Cast_StraightBevelDiffGearMeshRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelDiffGearMeshRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def derating_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DeratingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def inertia_factor_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InertiaFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def load_distribution_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadDistributionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def rating_result(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingResult

        if temp is None:
            return ""

        return temp

    @property
    def straight_bevel_diff_gear_mesh(
        self: Self,
    ) -> "_970.StraightBevelDiffGearMeshDesign":
        """mastapy.gears.gear_designs.straight_bevel_diff.StraightBevelDiffGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def meshed_gears(self: Self) -> "List[_404.StraightBevelDiffMeshedGearRating]":
        """List[mastapy.gears.rating.straight_bevel_diff.StraightBevelDiffMeshedGearRating]

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
    def gears_in_mesh(self: Self) -> "List[_404.StraightBevelDiffMeshedGearRating]":
        """List[mastapy.gears.rating.straight_bevel_diff.StraightBevelDiffMeshedGearRating]

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
    def straight_bevel_diff_gear_ratings(
        self: Self,
    ) -> "List[_402.StraightBevelDiffGearRating]":
        """List[mastapy.gears.rating.straight_bevel_diff.StraightBevelDiffGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearMeshRating._Cast_StraightBevelDiffGearMeshRating":
        return self._Cast_StraightBevelDiffGearMeshRating(self)
