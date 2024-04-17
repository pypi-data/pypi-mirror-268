"""GleasonHypoidMeshSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy.gears.rating.conical import _549
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GLEASON_HYPOID_MESH_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Hypoid.Standards", "GleasonHypoidMeshSingleFlankRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _369


__docformat__ = "restructuredtext en"
__all__ = ("GleasonHypoidMeshSingleFlankRating",)


Self = TypeVar("Self", bound="GleasonHypoidMeshSingleFlankRating")


class GleasonHypoidMeshSingleFlankRating(_549.ConicalMeshSingleFlankRating):
    """GleasonHypoidMeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _GLEASON_HYPOID_MESH_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GleasonHypoidMeshSingleFlankRating")

    class _Cast_GleasonHypoidMeshSingleFlankRating:
        """Special nested class for casting GleasonHypoidMeshSingleFlankRating to subclasses."""

        def __init__(
            self: "GleasonHypoidMeshSingleFlankRating._Cast_GleasonHypoidMeshSingleFlankRating",
            parent: "GleasonHypoidMeshSingleFlankRating",
        ):
            self._parent = parent

        @property
        def conical_mesh_single_flank_rating(
            self: "GleasonHypoidMeshSingleFlankRating._Cast_GleasonHypoidMeshSingleFlankRating",
        ) -> "_549.ConicalMeshSingleFlankRating":
            return self._parent._cast(_549.ConicalMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(
            self: "GleasonHypoidMeshSingleFlankRating._Cast_GleasonHypoidMeshSingleFlankRating",
        ) -> "_369.MeshSingleFlankRating":
            from mastapy.gears.rating import _369

            return self._parent._cast(_369.MeshSingleFlankRating)

        @property
        def gleason_hypoid_mesh_single_flank_rating(
            self: "GleasonHypoidMeshSingleFlankRating._Cast_GleasonHypoidMeshSingleFlankRating",
        ) -> "GleasonHypoidMeshSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "GleasonHypoidMeshSingleFlankRating._Cast_GleasonHypoidMeshSingleFlankRating",
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
        self: Self, instance_to_wrap: "GleasonHypoidMeshSingleFlankRating.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def calculated_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculatedContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_factor_bending(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicFactorBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def dynamic_factor_contact(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicFactorContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def elastic_coefficient(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def geometry_factor_i(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryFactorI

        if temp is None:
            return 0.0

        return temp

    @property
    def load_distribution_factor_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadDistributionFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def load_distribution_factor_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadDistributionFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def overload_factor_bending(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverloadFactorBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def overload_factor_contact(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverloadFactorContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def rating_standard_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingStandardName

        if temp is None:
            return ""

        return temp

    @property
    def size_factor_bending(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SizeFactorBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def size_factor_contact(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SizeFactorContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def surface_condition_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceConditionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def temperature_factor_bending(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TemperatureFactorBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def temperature_factor_contact(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TemperatureFactorContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def transmitted_tangential_load_at_large_end(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransmittedTangentialLoadAtLargeEnd

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "GleasonHypoidMeshSingleFlankRating._Cast_GleasonHypoidMeshSingleFlankRating":
        return self._Cast_GleasonHypoidMeshSingleFlankRating(self)
