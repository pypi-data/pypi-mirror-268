"""BevelGearMeshDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.gear_designs.agma_gleason_conical import _1200
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Bevel", "BevelGearMeshDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.zerol_bevel import _957
    from mastapy.gears.gear_designs.straight_bevel import _966
    from mastapy.gears.gear_designs.straight_bevel_diff import _970
    from mastapy.gears.gear_designs.spiral_bevel import _974
    from mastapy.gears.gear_designs.conical import _1161
    from mastapy.gears.gear_designs import _953, _952


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshDesign",)


Self = TypeVar("Self", bound="BevelGearMeshDesign")


class BevelGearMeshDesign(_1200.AGMAGleasonConicalGearMeshDesign):
    """BevelGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMeshDesign")

    class _Cast_BevelGearMeshDesign:
        """Special nested class for casting BevelGearMeshDesign to subclasses."""

        def __init__(
            self: "BevelGearMeshDesign._Cast_BevelGearMeshDesign",
            parent: "BevelGearMeshDesign",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_design(
            self: "BevelGearMeshDesign._Cast_BevelGearMeshDesign",
        ) -> "_1200.AGMAGleasonConicalGearMeshDesign":
            return self._parent._cast(_1200.AGMAGleasonConicalGearMeshDesign)

        @property
        def conical_gear_mesh_design(
            self: "BevelGearMeshDesign._Cast_BevelGearMeshDesign",
        ) -> "_1161.ConicalGearMeshDesign":
            from mastapy.gears.gear_designs.conical import _1161

            return self._parent._cast(_1161.ConicalGearMeshDesign)

        @property
        def gear_mesh_design(
            self: "BevelGearMeshDesign._Cast_BevelGearMeshDesign",
        ) -> "_953.GearMeshDesign":
            from mastapy.gears.gear_designs import _953

            return self._parent._cast(_953.GearMeshDesign)

        @property
        def gear_design_component(
            self: "BevelGearMeshDesign._Cast_BevelGearMeshDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def zerol_bevel_gear_mesh_design(
            self: "BevelGearMeshDesign._Cast_BevelGearMeshDesign",
        ) -> "_957.ZerolBevelGearMeshDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _957

            return self._parent._cast(_957.ZerolBevelGearMeshDesign)

        @property
        def straight_bevel_gear_mesh_design(
            self: "BevelGearMeshDesign._Cast_BevelGearMeshDesign",
        ) -> "_966.StraightBevelGearMeshDesign":
            from mastapy.gears.gear_designs.straight_bevel import _966

            return self._parent._cast(_966.StraightBevelGearMeshDesign)

        @property
        def straight_bevel_diff_gear_mesh_design(
            self: "BevelGearMeshDesign._Cast_BevelGearMeshDesign",
        ) -> "_970.StraightBevelDiffGearMeshDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _970

            return self._parent._cast(_970.StraightBevelDiffGearMeshDesign)

        @property
        def spiral_bevel_gear_mesh_design(
            self: "BevelGearMeshDesign._Cast_BevelGearMeshDesign",
        ) -> "_974.SpiralBevelGearMeshDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _974

            return self._parent._cast(_974.SpiralBevelGearMeshDesign)

        @property
        def bevel_gear_mesh_design(
            self: "BevelGearMeshDesign._Cast_BevelGearMeshDesign",
        ) -> "BevelGearMeshDesign":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshDesign._Cast_BevelGearMeshDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearMeshDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_effective_face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactEffectiveFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_wheel_inner_cone_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactWheelInnerConeDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_wheel_mean_cone_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactWheelMeanConeDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_wheel_outer_cone_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactWheelOuterConeDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def face_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceContactRatio

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
    def ideal_pinion_pitch_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IdealPinionPitchAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def ideal_wheel_pitch_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IdealWheelPitchAngle

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
    def is_topland_balanced(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsToplandBalanced

        if temp is None:
            return False

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
    def load_sharing_ratio_scoring(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadSharingRatioScoring

        if temp is None:
            return 0.0

        return temp

    @property
    def modified_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModifiedContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_face_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionFaceAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_inner_dedendum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionInnerDedendum

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_inner_dedendum_limit(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionInnerDedendumLimit

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_passed_undercut_check(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionPassedUndercutCheck

        if temp is None:
            return False

        return temp

    @property
    def pinion_pitch_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionPitchAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_pitch_angle_modification(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PinionPitchAngleModification

        if temp is None:
            return 0.0

        return temp

    @pinion_pitch_angle_modification.setter
    @enforce_parameter_types
    def pinion_pitch_angle_modification(self: Self, value: "float"):
        self.wrapped.PinionPitchAngleModification = (
            float(value) if value is not None else 0.0
        )

    @property
    def pinion_root_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionRootAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_thickness_modification_coefficient_backlash_included(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionThicknessModificationCoefficientBacklashIncluded

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
    def strength_balance_agma_coast(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StrengthBalanceAGMACoast

        if temp is None:
            return 0.0

        return temp

    @property
    def strength_balance_agma_drive(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StrengthBalanceAGMADrive

        if temp is None:
            return 0.0

        return temp

    @property
    def strength_balance_gleason_coast(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StrengthBalanceGleasonCoast

        if temp is None:
            return 0.0

        return temp

    @property
    def strength_balance_gleason_drive(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StrengthBalanceGleasonDrive

        if temp is None:
            return 0.0

        return temp

    @property
    def strength_balance_obtained_coast(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StrengthBalanceObtainedCoast

        if temp is None:
            return 0.0

        return temp

    @property
    def strength_balance_obtained_drive(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StrengthBalanceObtainedDrive

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
    def wheel_face_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelFaceAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_pitch_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelPitchAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_pitch_angle_modification(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelPitchAngleModification

        if temp is None:
            return 0.0

        return temp

    @wheel_pitch_angle_modification.setter
    @enforce_parameter_types
    def wheel_pitch_angle_modification(self: Self, value: "float"):
        self.wrapped.WheelPitchAngleModification = (
            float(value) if value is not None else 0.0
        )

    @property
    def wheel_root_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelRootAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_spiral_angle_at_contact_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelSpiralAngleAtContactOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_thickness_modification_coefficient_backlash_included(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelThicknessModificationCoefficientBacklashIncluded

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "BevelGearMeshDesign._Cast_BevelGearMeshDesign":
        return self._Cast_BevelGearMeshDesign(self)
