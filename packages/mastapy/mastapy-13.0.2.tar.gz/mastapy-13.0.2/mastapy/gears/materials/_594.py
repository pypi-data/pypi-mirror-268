"""CylindricalGearMaterial"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item, overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.materials import _597
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MATERIAL = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "CylindricalGearMaterial"
)

if TYPE_CHECKING:
    from mastapy.gears.materials import _605, _586, _600, _606
    from mastapy.materials import _272
    from mastapy.utility.databases import _1836


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMaterial",)


Self = TypeVar("Self", bound="CylindricalGearMaterial")


class CylindricalGearMaterial(_597.GearMaterial):
    """CylindricalGearMaterial

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MATERIAL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearMaterial")

    class _Cast_CylindricalGearMaterial:
        """Special nested class for casting CylindricalGearMaterial to subclasses."""

        def __init__(
            self: "CylindricalGearMaterial._Cast_CylindricalGearMaterial",
            parent: "CylindricalGearMaterial",
        ):
            self._parent = parent

        @property
        def gear_material(
            self: "CylindricalGearMaterial._Cast_CylindricalGearMaterial",
        ) -> "_597.GearMaterial":
            return self._parent._cast(_597.GearMaterial)

        @property
        def material(
            self: "CylindricalGearMaterial._Cast_CylindricalGearMaterial",
        ) -> "_272.Material":
            from mastapy.materials import _272

            return self._parent._cast(_272.Material)

        @property
        def named_database_item(
            self: "CylindricalGearMaterial._Cast_CylindricalGearMaterial",
        ) -> "_1836.NamedDatabaseItem":
            from mastapy.utility.databases import _1836

            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def agma_cylindrical_gear_material(
            self: "CylindricalGearMaterial._Cast_CylindricalGearMaterial",
        ) -> "_586.AGMACylindricalGearMaterial":
            from mastapy.gears.materials import _586

            return self._parent._cast(_586.AGMACylindricalGearMaterial)

        @property
        def iso_cylindrical_gear_material(
            self: "CylindricalGearMaterial._Cast_CylindricalGearMaterial",
        ) -> "_600.ISOCylindricalGearMaterial":
            from mastapy.gears.materials import _600

            return self._parent._cast(_600.ISOCylindricalGearMaterial)

        @property
        def plastic_cylindrical_gear_material(
            self: "CylindricalGearMaterial._Cast_CylindricalGearMaterial",
        ) -> "_606.PlasticCylindricalGearMaterial":
            from mastapy.gears.materials import _606

            return self._parent._cast(_606.PlasticCylindricalGearMaterial)

        @property
        def cylindrical_gear_material(
            self: "CylindricalGearMaterial._Cast_CylindricalGearMaterial",
        ) -> "CylindricalGearMaterial":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMaterial._Cast_CylindricalGearMaterial", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearMaterial.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_stress_number_bending(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AllowableStressNumberBending

        if temp is None:
            return 0.0

        return temp

    @allowable_stress_number_bending.setter
    @enforce_parameter_types
    def allowable_stress_number_bending(self: Self, value: "float"):
        self.wrapped.AllowableStressNumberBending = (
            float(value) if value is not None else 0.0
        )

    @property
    def allowable_stress_number_contact(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AllowableStressNumberContact

        if temp is None:
            return 0.0

        return temp

    @allowable_stress_number_contact.setter
    @enforce_parameter_types
    def allowable_stress_number_contact(self: Self, value: "float"):
        self.wrapped.AllowableStressNumberContact = (
            float(value) if value is not None else 0.0
        )

    @property
    def heat_treatment_distortion_control(self: Self) -> "_605.ManufactureRating":
        """mastapy.gears.materials.ManufactureRating"""
        temp = self.wrapped.HeatTreatmentDistortionControl

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Materials.ManufactureRating"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.materials._605", "ManufactureRating"
        )(value)

    @heat_treatment_distortion_control.setter
    @enforce_parameter_types
    def heat_treatment_distortion_control(self: Self, value: "_605.ManufactureRating"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Materials.ManufactureRating"
        )
        self.wrapped.HeatTreatmentDistortionControl = value

    @property
    def heat_treatment_process_development(self: Self) -> "_605.ManufactureRating":
        """mastapy.gears.materials.ManufactureRating"""
        temp = self.wrapped.HeatTreatmentProcessDevelopment

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Materials.ManufactureRating"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.materials._605", "ManufactureRating"
        )(value)

    @heat_treatment_process_development.setter
    @enforce_parameter_types
    def heat_treatment_process_development(self: Self, value: "_605.ManufactureRating"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Materials.ManufactureRating"
        )
        self.wrapped.HeatTreatmentProcessDevelopment = value

    @property
    def machine_process_development(self: Self) -> "_605.ManufactureRating":
        """mastapy.gears.materials.ManufactureRating"""
        temp = self.wrapped.MachineProcessDevelopment

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Materials.ManufactureRating"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.materials._605", "ManufactureRating"
        )(value)

    @machine_process_development.setter
    @enforce_parameter_types
    def machine_process_development(self: Self, value: "_605.ManufactureRating"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Materials.ManufactureRating"
        )
        self.wrapped.MachineProcessDevelopment = value

    @property
    def manufacturability(self: Self) -> "_605.ManufactureRating":
        """mastapy.gears.materials.ManufactureRating"""
        temp = self.wrapped.Manufacturability

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Materials.ManufactureRating"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.materials._605", "ManufactureRating"
        )(value)

    @manufacturability.setter
    @enforce_parameter_types
    def manufacturability(self: Self, value: "_605.ManufactureRating"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Materials.ManufactureRating"
        )
        self.wrapped.Manufacturability = value

    @property
    def material_type(self: Self) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.MaterialType

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @material_type.setter
    @enforce_parameter_types
    def material_type(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.MaterialType = value

    @property
    def nominal_stress_number_bending(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NominalStressNumberBending

        if temp is None:
            return 0.0

        return temp

    @nominal_stress_number_bending.setter
    @enforce_parameter_types
    def nominal_stress_number_bending(self: Self, value: "float"):
        self.wrapped.NominalStressNumberBending = (
            float(value) if value is not None else 0.0
        )

    @property
    def retained_austenite(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RetainedAustenite

        if temp is None:
            return 0.0

        return temp

    @retained_austenite.setter
    @enforce_parameter_types
    def retained_austenite(self: Self, value: "float"):
        self.wrapped.RetainedAustenite = float(value) if value is not None else 0.0

    @property
    def sn_curve_bending_allowable_stress_point_selector(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.SNCurveBendingAllowableStressPointSelector

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @sn_curve_bending_allowable_stress_point_selector.setter
    @enforce_parameter_types
    def sn_curve_bending_allowable_stress_point_selector(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.SNCurveBendingAllowableStressPointSelector = value

    @property
    def sn_curve_contact_allowable_stress_point_selector(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.SNCurveContactAllowableStressPointSelector

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @sn_curve_contact_allowable_stress_point_selector.setter
    @enforce_parameter_types
    def sn_curve_contact_allowable_stress_point_selector(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.SNCurveContactAllowableStressPointSelector = value

    @property
    def shot_peened(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShotPeened

        if temp is None:
            return False

        return temp

    @shot_peened.setter
    @enforce_parameter_types
    def shot_peened(self: Self, value: "bool"):
        self.wrapped.ShotPeened = bool(value) if value is not None else False

    @property
    def specify_allowable_stress_number_bending(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyAllowableStressNumberBending

        if temp is None:
            return False

        return temp

    @specify_allowable_stress_number_bending.setter
    @enforce_parameter_types
    def specify_allowable_stress_number_bending(self: Self, value: "bool"):
        self.wrapped.SpecifyAllowableStressNumberBending = (
            bool(value) if value is not None else False
        )

    @property
    def specify_allowable_stress_number_contact(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyAllowableStressNumberContact

        if temp is None:
            return False

        return temp

    @specify_allowable_stress_number_contact.setter
    @enforce_parameter_types
    def specify_allowable_stress_number_contact(self: Self, value: "bool"):
        self.wrapped.SpecifyAllowableStressNumberContact = (
            bool(value) if value is not None else False
        )

    @property
    def welding_structural_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.WeldingStructuralFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @welding_structural_factor.setter
    @enforce_parameter_types
    def welding_structural_factor(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.WeldingStructuralFactor = value

    @property
    def cast_to(self: Self) -> "CylindricalGearMaterial._Cast_CylindricalGearMaterial":
        return self._Cast_CylindricalGearMaterial(self)
