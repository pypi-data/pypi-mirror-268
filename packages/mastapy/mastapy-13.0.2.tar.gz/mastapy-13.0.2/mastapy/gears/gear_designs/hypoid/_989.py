"""HypoidGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.gear_designs.agma_gleason_conical import _1199
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Hypoid", "HypoidGearDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1160
    from mastapy.gears.gear_designs import _951, _952


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearDesign",)


Self = TypeVar("Self", bound="HypoidGearDesign")


class HypoidGearDesign(_1199.AGMAGleasonConicalGearDesign):
    """HypoidGearDesign

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearDesign")

    class _Cast_HypoidGearDesign:
        """Special nested class for casting HypoidGearDesign to subclasses."""

        def __init__(
            self: "HypoidGearDesign._Cast_HypoidGearDesign", parent: "HypoidGearDesign"
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_design(
            self: "HypoidGearDesign._Cast_HypoidGearDesign",
        ) -> "_1199.AGMAGleasonConicalGearDesign":
            return self._parent._cast(_1199.AGMAGleasonConicalGearDesign)

        @property
        def conical_gear_design(
            self: "HypoidGearDesign._Cast_HypoidGearDesign",
        ) -> "_1160.ConicalGearDesign":
            from mastapy.gears.gear_designs.conical import _1160

            return self._parent._cast(_1160.ConicalGearDesign)

        @property
        def gear_design(
            self: "HypoidGearDesign._Cast_HypoidGearDesign",
        ) -> "_951.GearDesign":
            from mastapy.gears.gear_designs import _951

            return self._parent._cast(_951.GearDesign)

        @property
        def gear_design_component(
            self: "HypoidGearDesign._Cast_HypoidGearDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def hypoid_gear_design(
            self: "HypoidGearDesign._Cast_HypoidGearDesign",
        ) -> "HypoidGearDesign":
            return self._parent

        def __getattr__(self: "HypoidGearDesign._Cast_HypoidGearDesign", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def addendum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Addendum

        if temp is None:
            return 0.0

        return temp

    @property
    def addendum_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AddendumAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def crown_to_crossing_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CrownToCrossingPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def dedendum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Dedendum

        if temp is None:
            return 0.0

        return temp

    @property
    def dedendum_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DedendumAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def face_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def face_apex_to_crossing_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceApexToCrossingPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @face_width.setter
    @enforce_parameter_types
    def face_width(self: Self, value: "float"):
        self.wrapped.FaceWidth = float(value) if value is not None else 0.0

    @property
    def front_crown_to_crossing_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrontCrownToCrossingPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def geometry_factor_j(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryFactorJ

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_cone_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerConeDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_addendum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanAddendum

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_cone_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanConeDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_dedendum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanDedendum

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_normal_circular_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanNormalCircularThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_normal_topland(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanNormalTopland

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_pitch_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_point_to_crossing_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanPointToCrossingPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_root_spiral_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanRootSpiralAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_spiral_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanSpiralAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def offset_angle_in_axial_plane(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OffsetAngleInAxialPlane

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_cone_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterConeDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_tip_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterTipDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_whole_depth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterWholeDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_working_depth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterWorkingDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_apex_to_crossing_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchApexToCrossingPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_apex_to_crown(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchApexToCrown

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def root_apex_to_crossing_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootApexToCrossingPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def strength_factor_q(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StrengthFactorQ

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "HypoidGearDesign._Cast_HypoidGearDesign":
        return self._Cast_HypoidGearDesign(self)
