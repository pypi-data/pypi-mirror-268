"""FlexiblePinAssembly"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.part_model import _2483
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_FLEXIBLE_PIN_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "FlexiblePinAssembly"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2532
    from mastapy.system_model.part_model import _2441, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssembly",)


Self = TypeVar("Self", bound="FlexiblePinAssembly")


class FlexiblePinAssembly(_2483.SpecialisedAssembly):
    """FlexiblePinAssembly

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FlexiblePinAssembly")

    class _Cast_FlexiblePinAssembly:
        """Special nested class for casting FlexiblePinAssembly to subclasses."""

        def __init__(
            self: "FlexiblePinAssembly._Cast_FlexiblePinAssembly",
            parent: "FlexiblePinAssembly",
        ):
            self._parent = parent

        @property
        def specialised_assembly(
            self: "FlexiblePinAssembly._Cast_FlexiblePinAssembly",
        ) -> "_2483.SpecialisedAssembly":
            return self._parent._cast(_2483.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "FlexiblePinAssembly._Cast_FlexiblePinAssembly",
        ) -> "_2441.AbstractAssembly":
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.AbstractAssembly)

        @property
        def part(self: "FlexiblePinAssembly._Cast_FlexiblePinAssembly") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "FlexiblePinAssembly._Cast_FlexiblePinAssembly",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def flexible_pin_assembly(
            self: "FlexiblePinAssembly._Cast_FlexiblePinAssembly",
        ) -> "FlexiblePinAssembly":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssembly._Cast_FlexiblePinAssembly", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FlexiblePinAssembly.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length_to_diameter_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthToDiameterRatio

        if temp is None:
            return 0.0

        return temp

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
    def maximum_pin_diameter_from_planet_bore(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPinDiameterFromPlanetBore

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_fatigue_safety_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumFatigueSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @minimum_fatigue_safety_factor.setter
    @enforce_parameter_types
    def minimum_fatigue_safety_factor(self: Self, value: "float"):
        self.wrapped.MinimumFatigueSafetyFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def pin_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PinDiameter

        if temp is None:
            return 0.0

        return temp

    @pin_diameter.setter
    @enforce_parameter_types
    def pin_diameter(self: Self, value: "float"):
        self.wrapped.PinDiameter = float(value) if value is not None else 0.0

    @property
    def pin_position_tolerance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PinPositionTolerance

        if temp is None:
            return 0.0

        return temp

    @pin_position_tolerance.setter
    @enforce_parameter_types
    def pin_position_tolerance(self: Self, value: "float"):
        self.wrapped.PinPositionTolerance = float(value) if value is not None else 0.0

    @property
    def pitch_iso_quality_grade(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_int":
        """ListWithSelectedItem[int]"""
        temp = self.wrapped.PitchISOQualityGrade

        if temp is None:
            return 0

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_int",
        )(temp)

    @pitch_iso_quality_grade.setter
    @enforce_parameter_types
    def pitch_iso_quality_grade(self: Self, value: "int"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_int.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_int.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0
        )
        self.wrapped.PitchISOQualityGrade = value

    @property
    def planet_gear_bore_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetGearBoreDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def spindle_outer_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpindleOuterDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def total_pin_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalPinLength

        if temp is None:
            return 0.0

        return temp

    @property
    def unsupported_pin_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UnsupportedPinLength

        if temp is None:
            return 0.0

        return temp

    @property
    def planet_gear(self: Self) -> "_2532.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "FlexiblePinAssembly._Cast_FlexiblePinAssembly":
        return self._Cast_FlexiblePinAssembly(self)
