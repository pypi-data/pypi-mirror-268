"""CylindricalGearDefaults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.python_net import python_net_import
from mastapy._internal import constructor, conversion
from mastapy.utility import _1601
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_CYLINDRICAL_GEAR_DEFAULTS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalGearDefaults"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash import (
        _1096,
    )
    from mastapy.gears.gear_designs.cylindrical import _1051
    from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _745
    from mastapy.gears.manufacturing.cylindrical.cutters import _725
    from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1146
    from mastapy.utility import _1602


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearDefaults",)


Self = TypeVar("Self", bound="CylindricalGearDefaults")


class CylindricalGearDefaults(_1601.PerMachineSettings):
    """CylindricalGearDefaults

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_DEFAULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearDefaults")

    class _Cast_CylindricalGearDefaults:
        """Special nested class for casting CylindricalGearDefaults to subclasses."""

        def __init__(
            self: "CylindricalGearDefaults._Cast_CylindricalGearDefaults",
            parent: "CylindricalGearDefaults",
        ):
            self._parent = parent

        @property
        def per_machine_settings(
            self: "CylindricalGearDefaults._Cast_CylindricalGearDefaults",
        ) -> "_1601.PerMachineSettings":
            return self._parent._cast(_1601.PerMachineSettings)

        @property
        def persistent_singleton(
            self: "CylindricalGearDefaults._Cast_CylindricalGearDefaults",
        ) -> "_1602.PersistentSingleton":
            from mastapy.utility import _1602

            return self._parent._cast(_1602.PersistentSingleton)

        @property
        def cylindrical_gear_defaults(
            self: "CylindricalGearDefaults._Cast_CylindricalGearDefaults",
        ) -> "CylindricalGearDefaults":
            return self._parent

        def __getattr__(
            self: "CylindricalGearDefaults._Cast_CylindricalGearDefaults", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearDefaults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def agma_material(self: Self) -> "str":
        """str"""
        temp = self.wrapped.AGMAMaterial.SelectedItemName

        if temp is None:
            return ""

        return temp

    @agma_material.setter
    @enforce_parameter_types
    def agma_material(self: Self, value: "str"):
        self.wrapped.AGMAMaterial.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def chamfer_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ChamferAngle

        if temp is None:
            return 0.0

        return temp

    @chamfer_angle.setter
    @enforce_parameter_types
    def chamfer_angle(self: Self, value: "float"):
        self.wrapped.ChamferAngle = float(value) if value is not None else 0.0

    @property
    def diameter_chamfer_height(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DiameterChamferHeight

        if temp is None:
            return 0.0

        return temp

    @diameter_chamfer_height.setter
    @enforce_parameter_types
    def diameter_chamfer_height(self: Self, value: "float"):
        self.wrapped.DiameterChamferHeight = float(value) if value is not None else 0.0

    @property
    def fillet_roughness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FilletRoughness

        if temp is None:
            return 0.0

        return temp

    @fillet_roughness.setter
    @enforce_parameter_types
    def fillet_roughness(self: Self, value: "float"):
        self.wrapped.FilletRoughness = float(value) if value is not None else 0.0

    @property
    def finish_stock_type(self: Self) -> "_1096.FinishStockType":
        """mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash.FinishStockType"""
        temp = self.wrapped.FinishStockType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.ThicknessStockAndBacklash.FinishStockType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash._1096",
            "FinishStockType",
        )(value)

    @finish_stock_type.setter
    @enforce_parameter_types
    def finish_stock_type(self: Self, value: "_1096.FinishStockType"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.ThicknessStockAndBacklash.FinishStockType",
        )
        self.wrapped.FinishStockType = value

    @property
    def flank_roughness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FlankRoughness

        if temp is None:
            return 0.0

        return temp

    @flank_roughness.setter
    @enforce_parameter_types
    def flank_roughness(self: Self, value: "float"):
        self.wrapped.FlankRoughness = float(value) if value is not None else 0.0

    @property
    def gear_fit_system(self: Self) -> "_1051.GearFitSystems":
        """mastapy.gears.gear_designs.cylindrical.GearFitSystems"""
        temp = self.wrapped.GearFitSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.GearFitSystems"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1051", "GearFitSystems"
        )(value)

    @gear_fit_system.setter
    @enforce_parameter_types
    def gear_fit_system(self: Self, value: "_1051.GearFitSystems"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.GearFitSystems"
        )
        self.wrapped.GearFitSystem = value

    @property
    def iso_material(self: Self) -> "str":
        """str"""
        temp = self.wrapped.ISOMaterial.SelectedItemName

        if temp is None:
            return ""

        return temp

    @iso_material.setter
    @enforce_parameter_types
    def iso_material(self: Self, value: "str"):
        self.wrapped.ISOMaterial.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def iso_quality_grade(self: Self) -> "int":
        """int"""
        temp = self.wrapped.ISOQualityGrade

        if temp is None:
            return 0

        return temp

    @iso_quality_grade.setter
    @enforce_parameter_types
    def iso_quality_grade(self: Self, value: "int"):
        self.wrapped.ISOQualityGrade = int(value) if value is not None else 0

    @property
    def finish_manufacturing_process_controls(
        self: Self,
    ) -> "_745.ManufacturingProcessControls":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.ManufacturingProcessControls

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FinishManufacturingProcessControls

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rough_cutter_creation_settings(
        self: Self,
    ) -> "_725.RoughCutterCreationSettings":
        """mastapy.gears.manufacturing.cylindrical.cutters.RoughCutterCreationSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoughCutterCreationSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rough_manufacturing_process_controls(
        self: Self,
    ) -> "_745.ManufacturingProcessControls":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.ManufacturingProcessControls

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoughManufacturingProcessControls

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_of_fits_defaults(self: Self) -> "_1146.DIN3967SystemOfGearFits":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.DIN3967SystemOfGearFits

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemOfFitsDefaults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CylindricalGearDefaults._Cast_CylindricalGearDefaults":
        return self._Cast_CylindricalGearDefaults(self)
