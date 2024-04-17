"""Shaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.python_net import python_net_import
from mastapy._internal import constructor
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.part_model import _2462, _2442
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_SHAFT = python_net_import("SMT.MastaAPI.SystemModel.PartModel.ShaftModel", "Shaft")

if TYPE_CHECKING:
    from mastapy.shafts import _43
    from mastapy.system_model.part_model import _2463, _2471, _2443, _2451, _2475
    from mastapy.system_model.fe import _2390
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("Shaft",)


Self = TypeVar("Self", bound="Shaft")


class Shaft(_2442.AbstractShaft):
    """Shaft

    This is a mastapy class.
    """

    TYPE = _SHAFT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Shaft")

    class _Cast_Shaft:
        """Special nested class for casting Shaft to subclasses."""

        def __init__(self: "Shaft._Cast_Shaft", parent: "Shaft"):
            self._parent = parent

        @property
        def abstract_shaft(self: "Shaft._Cast_Shaft") -> "_2442.AbstractShaft":
            return self._parent._cast(_2442.AbstractShaft)

        @property
        def abstract_shaft_or_housing(
            self: "Shaft._Cast_Shaft",
        ) -> "_2443.AbstractShaftOrHousing":
            from mastapy.system_model.part_model import _2443

            return self._parent._cast(_2443.AbstractShaftOrHousing)

        @property
        def component(self: "Shaft._Cast_Shaft") -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(self: "Shaft._Cast_Shaft") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(self: "Shaft._Cast_Shaft") -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def shaft(self: "Shaft._Cast_Shaft") -> "Shaft":
            return self._parent

        def __getattr__(self: "Shaft._Cast_Shaft", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Shaft.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_design(self: Self) -> "str":
        """str"""
        temp = self.wrapped.ActiveDesign.SelectedItemName

        if temp is None:
            return ""

        return temp

    @active_design.setter
    @enforce_parameter_types
    def active_design(self: Self, value: "str"):
        self.wrapped.ActiveDesign.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def cad_model(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_GuideDxfModel":
        """ListWithSelectedItem[mastapy.system_model.part_model.GuideDxfModel]"""
        temp = self.wrapped.CADModel

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_GuideDxfModel",
        )(temp)

    @cad_model.setter
    @enforce_parameter_types
    def cad_model(self: Self, value: "_2462.GuideDxfModel"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_GuideDxfModel.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_GuideDxfModel.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.CADModel = value

    @property
    def has_guide_image(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.HasGuideImage

        if temp is None:
            return False

        return temp

    @has_guide_image.setter
    @enforce_parameter_types
    def has_guide_image(self: Self, value: "bool"):
        self.wrapped.HasGuideImage = bool(value) if value is not None else False

    @property
    def is_replaced_by_fe(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsReplacedByFE

        if temp is None:
            return False

        return temp

    @property
    def left_side_offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LeftSideOffset

        if temp is None:
            return 0.0

        return temp

    @left_side_offset.setter
    @enforce_parameter_types
    def left_side_offset(self: Self, value: "float"):
        self.wrapped.LeftSideOffset = float(value) if value is not None else 0.0

    @property
    def length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    @enforce_parameter_types
    def length(self: Self, value: "float"):
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def mass_of_shaft_body(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassOfShaftBody

        if temp is None:
            return 0.0

        return temp

    @property
    def polar_inertia_of_shaft_body(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PolarInertiaOfShaftBody

        if temp is None:
            return 0.0

        return temp

    @property
    def position_fixed(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.PositionFixed

        if temp is None:
            return False

        return temp

    @position_fixed.setter
    @enforce_parameter_types
    def position_fixed(self: Self, value: "bool"):
        self.wrapped.PositionFixed = bool(value) if value is not None else False

    @property
    def rotation_about_axis_for_all_mounted_components(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotationAboutAxisForAllMountedComponents

        if temp is None:
            return 0.0

        return temp

    @rotation_about_axis_for_all_mounted_components.setter
    @enforce_parameter_types
    def rotation_about_axis_for_all_mounted_components(self: Self, value: "float"):
        self.wrapped.RotationAboutAxisForAllMountedComponents = (
            float(value) if value is not None else 0.0
        )

    @property
    def stress_to_yield_strength_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StressToYieldStrengthFactor

        if temp is None:
            return 0.0

        return temp

    @stress_to_yield_strength_factor.setter
    @enforce_parameter_types
    def stress_to_yield_strength_factor(self: Self, value: "float"):
        self.wrapped.StressToYieldStrengthFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def uses_cad_guide(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UsesCADGuide

        if temp is None:
            return False

        return temp

    @uses_cad_guide.setter
    @enforce_parameter_types
    def uses_cad_guide(self: Self, value: "bool"):
        self.wrapped.UsesCADGuide = bool(value) if value is not None else False

    @property
    def active_definition(self: Self) -> "_43.SimpleShaftDefinition":
        """mastapy.shafts.SimpleShaftDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveDefinition

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def guide_image(self: Self) -> "_2463.GuideImage":
        """mastapy.system_model.part_model.GuideImage

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GuideImage

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def fe_substructure_replacing_this(self: Self) -> "_2390.FESubstructure":
        """mastapy.system_model.fe.FESubstructure

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FESubstructureReplacingThis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def import_shaft(self: Self):
        """Method does not return."""
        self.wrapped.ImportShaft()

    @enforce_parameter_types
    def add_section(
        self: Self,
        start_offset: "float",
        end_offset: "float",
        start_outer: "float",
        start_inner: "float",
        end_outer: "float",
        end_inner: "float",
    ):
        """Method does not return.

        Args:
            start_offset (float)
            end_offset (float)
            start_outer (float)
            start_inner (float)
            end_outer (float)
            end_inner (float)
        """
        start_offset = float(start_offset)
        end_offset = float(end_offset)
        start_outer = float(start_outer)
        start_inner = float(start_inner)
        end_outer = float(end_outer)
        end_inner = float(end_inner)
        self.wrapped.AddSection(
            start_offset if start_offset else 0.0,
            end_offset if end_offset else 0.0,
            start_outer if start_outer else 0.0,
            start_inner if start_inner else 0.0,
            end_outer if end_outer else 0.0,
            end_inner if end_inner else 0.0,
        )

    @enforce_parameter_types
    def mount_component(
        self: Self, component: "_2471.MountableComponent", offset: "float"
    ):
        """Method does not return.

        Args:
            component (mastapy.system_model.part_model.MountableComponent)
            offset (float)
        """
        offset = float(offset)
        self.wrapped.MountComponent(
            component.wrapped if component else None, offset if offset else 0.0
        )

    def remove_all_sections(self: Self):
        """Method does not return."""
        self.wrapped.RemoveAllSections()

    def remove_duplications(self: Self):
        """Method does not return."""
        self.wrapped.RemoveDuplications()

    @property
    def cast_to(self: Self) -> "Shaft._Cast_Shaft":
        return self._Cast_Shaft(self)
