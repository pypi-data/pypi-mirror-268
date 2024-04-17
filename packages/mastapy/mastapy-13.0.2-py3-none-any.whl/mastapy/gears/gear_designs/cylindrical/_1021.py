"""CylindricalGearFlankDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FLANK_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalGearFlankDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1029


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearFlankDesign",)


Self = TypeVar("Self", bound="CylindricalGearFlankDesign")


class CylindricalGearFlankDesign(_0.APIBase):
    """CylindricalGearFlankDesign

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_FLANK_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearFlankDesign")

    class _Cast_CylindricalGearFlankDesign:
        """Special nested class for casting CylindricalGearFlankDesign to subclasses."""

        def __init__(
            self: "CylindricalGearFlankDesign._Cast_CylindricalGearFlankDesign",
            parent: "CylindricalGearFlankDesign",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_flank_design(
            self: "CylindricalGearFlankDesign._Cast_CylindricalGearFlankDesign",
        ) -> "CylindricalGearFlankDesign":
            return self._parent

        def __getattr__(
            self: "CylindricalGearFlankDesign._Cast_CylindricalGearFlankDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearFlankDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def absolute_base_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AbsoluteBaseDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def absolute_form_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AbsoluteFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def absolute_form_to_sap_diameter_clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AbsoluteFormToSAPDiameterClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def absolute_tip_form_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AbsoluteTipFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def base_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BaseDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def base_thickness_half_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BaseThicknessHalfAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def base_to_form_diameter_clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BaseToFormDiameterClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def base_to_form_diameter_clearance_as_normal_module_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BaseToFormDiameterClearanceAsNormalModuleRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def chamfer_angle_in_normal_plane(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ChamferAngleInNormalPlane

        if temp is None:
            return 0.0

        return temp

    @property
    def effective_tip_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveTipRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def flank_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlankName

        if temp is None:
            return ""

        return temp

    @property
    def form_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FormRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def form_to_sap_diameter_absolute_clearance_as_normal_module_ratio(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FormToSAPDiameterAbsoluteClearanceAsNormalModuleRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def has_chamfer(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasChamfer

        if temp is None:
            return False

        return temp

    @property
    def is_under_cut_by_cutter(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsUnderCutByCutter

        if temp is None:
            return False

        return temp

    @property
    def lowest_sap_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LowestSAPDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_normal_thickness_at_root_form_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanNormalThicknessAtRootFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_normal_thickness_at_tip_form_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanNormalThicknessAtTipFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_base_pitch(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalBasePitch

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def radii_of_curvature_at_tip(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RadiiOfCurvatureAtTip

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @radii_of_curvature_at_tip.setter
    @enforce_parameter_types
    def radii_of_curvature_at_tip(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RadiiOfCurvatureAtTip = value

    @property
    def root_form_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def root_form_roll_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootFormRollAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def root_form_roll_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootFormRollDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def signed_root_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SignedRootDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_form_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_form_roll_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipFormRollAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_form_roll_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipFormRollDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_thickness_half_angle_at_reference_circle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothThicknessHalfAngleAtReferenceCircle

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_base_pitch(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseBasePitch

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_chamfer_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseChamferAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransversePressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def highest_point_of_fewest_tooth_contacts(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HighestPointOfFewestToothContacts

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def lowest_point_of_fewest_tooth_contacts(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LowestPointOfFewestToothContacts

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def lowest_start_of_active_profile(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LowestStartOfActiveProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def root_diameter_reporting(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootDiameterReporting

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def root_form(self: Self) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootForm

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def tip_diameter_reporting(self: Self) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipDiameterReporting

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def tip_form(self: Self) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipForm

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearFlankDesign._Cast_CylindricalGearFlankDesign":
        return self._Cast_CylindricalGearFlankDesign(self)
