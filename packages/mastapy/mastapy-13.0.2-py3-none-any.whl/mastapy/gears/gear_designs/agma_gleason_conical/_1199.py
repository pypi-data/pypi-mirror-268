"""AGMAGleasonConicalGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.gears.gear_designs.conical import _1163, _1164, _1160
from mastapy._internal.python_net import python_net_import
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_AGMA_GLEASON_CONICAL_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.AGMAGleasonConical", "AGMAGleasonConicalGearDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1170, _1159
    from mastapy.gears import _317
    from mastapy.gears.materials import _597
    from mastapy.gears.gear_designs.zerol_bevel import _956
    from mastapy.gears.gear_designs.straight_bevel import _965
    from mastapy.gears.gear_designs.straight_bevel_diff import _969
    from mastapy.gears.gear_designs.spiral_bevel import _973
    from mastapy.gears.gear_designs.hypoid import _989
    from mastapy.gears.gear_designs.bevel import _1186
    from mastapy.gears.gear_designs import _951, _952


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearDesign",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearDesign")


class AGMAGleasonConicalGearDesign(_1160.ConicalGearDesign):
    """AGMAGleasonConicalGearDesign

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearDesign")

    class _Cast_AGMAGleasonConicalGearDesign:
        """Special nested class for casting AGMAGleasonConicalGearDesign to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearDesign._Cast_AGMAGleasonConicalGearDesign",
            parent: "AGMAGleasonConicalGearDesign",
        ):
            self._parent = parent

        @property
        def conical_gear_design(
            self: "AGMAGleasonConicalGearDesign._Cast_AGMAGleasonConicalGearDesign",
        ) -> "_1160.ConicalGearDesign":
            return self._parent._cast(_1160.ConicalGearDesign)

        @property
        def gear_design(
            self: "AGMAGleasonConicalGearDesign._Cast_AGMAGleasonConicalGearDesign",
        ) -> "_951.GearDesign":
            from mastapy.gears.gear_designs import _951

            return self._parent._cast(_951.GearDesign)

        @property
        def gear_design_component(
            self: "AGMAGleasonConicalGearDesign._Cast_AGMAGleasonConicalGearDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def zerol_bevel_gear_design(
            self: "AGMAGleasonConicalGearDesign._Cast_AGMAGleasonConicalGearDesign",
        ) -> "_956.ZerolBevelGearDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _956

            return self._parent._cast(_956.ZerolBevelGearDesign)

        @property
        def straight_bevel_gear_design(
            self: "AGMAGleasonConicalGearDesign._Cast_AGMAGleasonConicalGearDesign",
        ) -> "_965.StraightBevelGearDesign":
            from mastapy.gears.gear_designs.straight_bevel import _965

            return self._parent._cast(_965.StraightBevelGearDesign)

        @property
        def straight_bevel_diff_gear_design(
            self: "AGMAGleasonConicalGearDesign._Cast_AGMAGleasonConicalGearDesign",
        ) -> "_969.StraightBevelDiffGearDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _969

            return self._parent._cast(_969.StraightBevelDiffGearDesign)

        @property
        def spiral_bevel_gear_design(
            self: "AGMAGleasonConicalGearDesign._Cast_AGMAGleasonConicalGearDesign",
        ) -> "_973.SpiralBevelGearDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _973

            return self._parent._cast(_973.SpiralBevelGearDesign)

        @property
        def hypoid_gear_design(
            self: "AGMAGleasonConicalGearDesign._Cast_AGMAGleasonConicalGearDesign",
        ) -> "_989.HypoidGearDesign":
            from mastapy.gears.gear_designs.hypoid import _989

            return self._parent._cast(_989.HypoidGearDesign)

        @property
        def bevel_gear_design(
            self: "AGMAGleasonConicalGearDesign._Cast_AGMAGleasonConicalGearDesign",
        ) -> "_1186.BevelGearDesign":
            from mastapy.gears.gear_designs.bevel import _1186

            return self._parent._cast(_1186.BevelGearDesign)

        @property
        def agma_gleason_conical_gear_design(
            self: "AGMAGleasonConicalGearDesign._Cast_AGMAGleasonConicalGearDesign",
        ) -> "AGMAGleasonConicalGearDesign":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearDesign._Cast_AGMAGleasonConicalGearDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableContactStress

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
    def front_end_type(self: Self) -> "_1170.FrontEndTypes":
        """mastapy.gears.gear_designs.conical.FrontEndTypes"""
        temp = self.wrapped.FrontEndType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Conical.FrontEndTypes"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.conical._1170", "FrontEndTypes"
        )(value)

    @front_end_type.setter
    @enforce_parameter_types
    def front_end_type(self: Self, value: "_1170.FrontEndTypes"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Conical.FrontEndTypes"
        )
        self.wrapped.FrontEndType = value

    @property
    def machine_setting_calculation_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ConicalMachineSettingCalculationMethods":
        """EnumWithSelectedValue[mastapy.gears.gear_designs.conical.ConicalMachineSettingCalculationMethods]"""
        temp = self.wrapped.MachineSettingCalculationMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ConicalMachineSettingCalculationMethods.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @machine_setting_calculation_method.setter
    @enforce_parameter_types
    def machine_setting_calculation_method(
        self: Self, value: "_1163.ConicalMachineSettingCalculationMethods"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ConicalMachineSettingCalculationMethods.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.MachineSettingCalculationMethod = value

    @property
    def manufacture_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ConicalManufactureMethods":
        """EnumWithSelectedValue[mastapy.gears.gear_designs.conical.ConicalManufactureMethods]"""
        temp = self.wrapped.ManufactureMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ConicalManufactureMethods.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @manufacture_method.setter
    @enforce_parameter_types
    def manufacture_method(self: Self, value: "_1164.ConicalManufactureMethods"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ConicalManufactureMethods.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ManufactureMethod = value

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
    def accuracy_grades(self: Self) -> "_317.AccuracyGrades":
        """mastapy.gears.AccuracyGrades

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AccuracyGrades

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gear_material(self: Self) -> "_597.GearMaterial":
        """mastapy.gears.materials.GearMaterial

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearMaterial

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cutter(self: Self) -> "_1159.ConicalGearCutter":
        """mastapy.gears.gear_designs.conical.ConicalGearCutter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Cutter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearDesign._Cast_AGMAGleasonConicalGearDesign":
        return self._Cast_AGMAGleasonConicalGearDesign(self)
