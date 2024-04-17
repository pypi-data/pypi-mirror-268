"""GleasonSpiralBevelMeshSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.gears.rating.bevel.standards import _565
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GLEASON_SPIRAL_BEVEL_MESH_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Bevel.Standards",
    "GleasonSpiralBevelMeshSingleFlankRating",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.bevel.standards import _562
    from mastapy.gears.rating.conical import _549
    from mastapy.gears.rating import _369


__docformat__ = "restructuredtext en"
__all__ = ("GleasonSpiralBevelMeshSingleFlankRating",)


Self = TypeVar("Self", bound="GleasonSpiralBevelMeshSingleFlankRating")


class GleasonSpiralBevelMeshSingleFlankRating(_565.SpiralBevelMeshSingleFlankRating):
    """GleasonSpiralBevelMeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _GLEASON_SPIRAL_BEVEL_MESH_SINGLE_FLANK_RATING
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GleasonSpiralBevelMeshSingleFlankRating"
    )

    class _Cast_GleasonSpiralBevelMeshSingleFlankRating:
        """Special nested class for casting GleasonSpiralBevelMeshSingleFlankRating to subclasses."""

        def __init__(
            self: "GleasonSpiralBevelMeshSingleFlankRating._Cast_GleasonSpiralBevelMeshSingleFlankRating",
            parent: "GleasonSpiralBevelMeshSingleFlankRating",
        ):
            self._parent = parent

        @property
        def spiral_bevel_mesh_single_flank_rating(
            self: "GleasonSpiralBevelMeshSingleFlankRating._Cast_GleasonSpiralBevelMeshSingleFlankRating",
        ) -> "_565.SpiralBevelMeshSingleFlankRating":
            return self._parent._cast(_565.SpiralBevelMeshSingleFlankRating)

        @property
        def conical_mesh_single_flank_rating(
            self: "GleasonSpiralBevelMeshSingleFlankRating._Cast_GleasonSpiralBevelMeshSingleFlankRating",
        ) -> "_549.ConicalMeshSingleFlankRating":
            from mastapy.gears.rating.conical import _549

            return self._parent._cast(_549.ConicalMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(
            self: "GleasonSpiralBevelMeshSingleFlankRating._Cast_GleasonSpiralBevelMeshSingleFlankRating",
        ) -> "_369.MeshSingleFlankRating":
            from mastapy.gears.rating import _369

            return self._parent._cast(_369.MeshSingleFlankRating)

        @property
        def gleason_spiral_bevel_mesh_single_flank_rating(
            self: "GleasonSpiralBevelMeshSingleFlankRating._Cast_GleasonSpiralBevelMeshSingleFlankRating",
        ) -> "GleasonSpiralBevelMeshSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "GleasonSpiralBevelMeshSingleFlankRating._Cast_GleasonSpiralBevelMeshSingleFlankRating",
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
        self: Self, instance_to_wrap: "GleasonSpiralBevelMeshSingleFlankRating.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_scoring_index(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableScoringIndex

        if temp is None:
            return 0.0

        return temp

    @property
    def assumed_maximum_pinion_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssumedMaximumPinionTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_ellipse_width_instantaneous(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactEllipseWidthInstantaneous

        if temp is None:
            return 0.0

        return temp

    @property
    def geometry_factor_g(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryFactorG

        if temp is None:
            return 0.0

        return temp

    @property
    def load_factor_scoring(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadFactorScoring

        if temp is None:
            return 0.0

        return temp

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
    def safety_factor_scoring(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorScoring

        if temp is None:
            return 0.0

        return temp

    @property
    def scoring_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScoringFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def temperature_rise_at_critical_point_of_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TemperatureRiseAtCriticalPointOfContact

        if temp is None:
            return 0.0

        return temp

    @property
    def thermal_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThermalFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_single_flank_ratings(
        self: Self,
    ) -> "List[_562.GleasonSpiralBevelGearSingleFlankRating]":
        """List[mastapy.gears.rating.bevel.standards.GleasonSpiralBevelGearSingleFlankRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gleason_bevel_gear_single_flank_ratings(
        self: Self,
    ) -> "List[_562.GleasonSpiralBevelGearSingleFlankRating]":
        """List[mastapy.gears.rating.bevel.standards.GleasonSpiralBevelGearSingleFlankRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GleasonBevelGearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GleasonSpiralBevelMeshSingleFlankRating._Cast_GleasonSpiralBevelMeshSingleFlankRating":
        return self._Cast_GleasonSpiralBevelMeshSingleFlankRating(self)
