"""SpiralBevelMeshSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.implicit import overridable
from mastapy._internal import constructor
from mastapy.gears.rating.conical import _549
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_MESH_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Bevel.Standards", "SpiralBevelMeshSingleFlankRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.bevel.standards import _561, _563
    from mastapy.gears.rating import _369


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelMeshSingleFlankRating",)


Self = TypeVar("Self", bound="SpiralBevelMeshSingleFlankRating")


class SpiralBevelMeshSingleFlankRating(_549.ConicalMeshSingleFlankRating):
    """SpiralBevelMeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_MESH_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelMeshSingleFlankRating")

    class _Cast_SpiralBevelMeshSingleFlankRating:
        """Special nested class for casting SpiralBevelMeshSingleFlankRating to subclasses."""

        def __init__(
            self: "SpiralBevelMeshSingleFlankRating._Cast_SpiralBevelMeshSingleFlankRating",
            parent: "SpiralBevelMeshSingleFlankRating",
        ):
            self._parent = parent

        @property
        def conical_mesh_single_flank_rating(
            self: "SpiralBevelMeshSingleFlankRating._Cast_SpiralBevelMeshSingleFlankRating",
        ) -> "_549.ConicalMeshSingleFlankRating":
            return self._parent._cast(_549.ConicalMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(
            self: "SpiralBevelMeshSingleFlankRating._Cast_SpiralBevelMeshSingleFlankRating",
        ) -> "_369.MeshSingleFlankRating":
            from mastapy.gears.rating import _369

            return self._parent._cast(_369.MeshSingleFlankRating)

        @property
        def agma_spiral_bevel_mesh_single_flank_rating(
            self: "SpiralBevelMeshSingleFlankRating._Cast_SpiralBevelMeshSingleFlankRating",
        ) -> "_561.AGMASpiralBevelMeshSingleFlankRating":
            from mastapy.gears.rating.bevel.standards import _561

            return self._parent._cast(_561.AGMASpiralBevelMeshSingleFlankRating)

        @property
        def gleason_spiral_bevel_mesh_single_flank_rating(
            self: "SpiralBevelMeshSingleFlankRating._Cast_SpiralBevelMeshSingleFlankRating",
        ) -> "_563.GleasonSpiralBevelMeshSingleFlankRating":
            from mastapy.gears.rating.bevel.standards import _563

            return self._parent._cast(_563.GleasonSpiralBevelMeshSingleFlankRating)

        @property
        def spiral_bevel_mesh_single_flank_rating(
            self: "SpiralBevelMeshSingleFlankRating._Cast_SpiralBevelMeshSingleFlankRating",
        ) -> "SpiralBevelMeshSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "SpiralBevelMeshSingleFlankRating._Cast_SpiralBevelMeshSingleFlankRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelMeshSingleFlankRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def inertia_factor_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InertiaFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def length_of_line_of_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthOfLineOfContact

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
    def load_sharing_ratio_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadSharingRatioContact

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
    def pitch_line_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchLineVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def pitting_resistance_geometry_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PittingResistanceGeometryFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def reliability_factor_bending(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReliabilityFactorBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def reliability_factor_contact(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReliabilityFactorContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

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
    def transverse_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelMeshSingleFlankRating._Cast_SpiralBevelMeshSingleFlankRating":
        return self._Cast_SpiralBevelMeshSingleFlankRating(self)
