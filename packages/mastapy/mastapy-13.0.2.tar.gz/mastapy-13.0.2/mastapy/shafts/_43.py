"""SimpleShaftDefinition"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.utility.databases import _1836
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_SIMPLE_SHAFT_DEFINITION = python_net_import(
    "SMT.MastaAPI.Shafts", "SimpleShaftDefinition"
)

if TYPE_CHECKING:
    from mastapy.shafts import _42, _30, _26, _9, _14, _22, _33, _41


__docformat__ = "restructuredtext en"
__all__ = ("SimpleShaftDefinition",)


Self = TypeVar("Self", bound="SimpleShaftDefinition")


class SimpleShaftDefinition(_1836.NamedDatabaseItem):
    """SimpleShaftDefinition

    This is a mastapy class.
    """

    TYPE = _SIMPLE_SHAFT_DEFINITION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SimpleShaftDefinition")

    class _Cast_SimpleShaftDefinition:
        """Special nested class for casting SimpleShaftDefinition to subclasses."""

        def __init__(
            self: "SimpleShaftDefinition._Cast_SimpleShaftDefinition",
            parent: "SimpleShaftDefinition",
        ):
            self._parent = parent

        @property
        def named_database_item(
            self: "SimpleShaftDefinition._Cast_SimpleShaftDefinition",
        ) -> "_1836.NamedDatabaseItem":
            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def simple_shaft_definition(
            self: "SimpleShaftDefinition._Cast_SimpleShaftDefinition",
        ) -> "SimpleShaftDefinition":
            return self._parent

        def __getattr__(
            self: "SimpleShaftDefinition._Cast_SimpleShaftDefinition", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SimpleShaftDefinition.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def default_fillet_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DefaultFilletRadius

        if temp is None:
            return 0.0

        return temp

    @default_fillet_radius.setter
    @enforce_parameter_types
    def default_fillet_radius(self: Self, value: "float"):
        self.wrapped.DefaultFilletRadius = float(value) if value is not None else 0.0

    @property
    def design_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignName

        if temp is None:
            return ""

        return temp

    @property
    def factor_for_gjl_material(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FactorForGJLMaterial

        if temp is None:
            return 0.0

        return temp

    @factor_for_gjl_material.setter
    @enforce_parameter_types
    def factor_for_gjl_material(self: Self, value: "float"):
        self.wrapped.FactorForGJLMaterial = float(value) if value is not None else 0.0

    @property
    def material(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Material.SelectedItemName

        if temp is None:
            return ""

        return temp

    @material.setter
    @enforce_parameter_types
    def material(self: Self, value: "str"):
        self.wrapped.Material.SetSelectedItem(str(value) if value is not None else "")

    @property
    def report_shaft_fatigue_warnings(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ReportShaftFatigueWarnings

        if temp is None:
            return False

        return temp

    @report_shaft_fatigue_warnings.setter
    @enforce_parameter_types
    def report_shaft_fatigue_warnings(self: Self, value: "bool"):
        self.wrapped.ReportShaftFatigueWarnings = (
            bool(value) if value is not None else False
        )

    @property
    def surface_treatment_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SurfaceTreatmentFactor

        if temp is None:
            return 0.0

        return temp

    @surface_treatment_factor.setter
    @enforce_parameter_types
    def surface_treatment_factor(self: Self, value: "float"):
        self.wrapped.SurfaceTreatmentFactor = float(value) if value is not None else 0.0

    @property
    def default_surface_roughness(self: Self) -> "_42.ShaftSurfaceRoughness":
        """mastapy.shafts.ShaftSurfaceRoughness

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DefaultSurfaceRoughness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_profile(self: Self) -> "_30.ShaftProfile":
        """mastapy.shafts.ShaftProfile

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def outer_profile(self: Self) -> "_30.ShaftProfile":
        """mastapy.shafts.ShaftProfile

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaft_material(self: Self) -> "_26.ShaftMaterialForReports":
        """mastapy.shafts.ShaftMaterialForReports

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftMaterial

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def design_shaft_sections(self: Self) -> "List[_9.DesignShaftSection]":
        """List[mastapy.shafts.DesignShaftSection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignShaftSections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def generic_stress_concentration_factors(
        self: Self,
    ) -> "List[_14.GenericStressConcentrationFactor]":
        """List[mastapy.shafts.GenericStressConcentrationFactor]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GenericStressConcentrationFactors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def grooves(self: Self) -> "List[_22.ShaftGroove]":
        """List[mastapy.shafts.ShaftGroove]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Grooves

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def radial_holes(self: Self) -> "List[_33.ShaftRadialHole]":
        """List[mastapy.shafts.ShaftRadialHole]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialHoles

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def surface_finish_sections(self: Self) -> "List[_41.ShaftSurfaceFinishSection]":
        """List[mastapy.shafts.ShaftSurfaceFinishSection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceFinishSections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def add_generic_stress_concentration_factor(self: Self):
        """Method does not return."""
        self.wrapped.AddGenericStressConcentrationFactor()

    def add_generic_stress_concentration_factor_for_context_menu(self: Self):
        """Method does not return."""
        self.wrapped.AddGenericStressConcentrationFactorForContextMenu()

    def add_groove(self: Self):
        """Method does not return."""
        self.wrapped.AddGroove()

    def add_groove_for_context_menu(self: Self):
        """Method does not return."""
        self.wrapped.AddGrooveForContextMenu()

    def add_radial_hole(self: Self):
        """Method does not return."""
        self.wrapped.AddRadialHole()

    def add_radial_hole_for_context_menu(self: Self):
        """Method does not return."""
        self.wrapped.AddRadialHoleForContextMenu()

    def add_surface_finish_section(self: Self):
        """Method does not return."""
        self.wrapped.AddSurfaceFinishSection()

    def add_surface_finish_section_for_context_menu(self: Self):
        """Method does not return."""
        self.wrapped.AddSurfaceFinishSectionForContextMenu()

    @property
    def cast_to(self: Self) -> "SimpleShaftDefinition._Cast_SimpleShaftDefinition":
        return self._Cast_SimpleShaftDefinition(self)
