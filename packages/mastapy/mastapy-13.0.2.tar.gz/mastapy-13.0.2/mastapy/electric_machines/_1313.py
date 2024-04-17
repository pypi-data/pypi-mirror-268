"""ToothAndSlot"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.electric_machines import _1250
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOOTH_AND_SLOT = python_net_import("SMT.MastaAPI.ElectricMachines", "ToothAndSlot")

if TYPE_CHECKING:
    from mastapy.electric_machines import _1315, _1314


__docformat__ = "restructuredtext en"
__all__ = ("ToothAndSlot",)


Self = TypeVar("Self", bound="ToothAndSlot")


class ToothAndSlot(_1250.AbstractToothAndSlot):
    """ToothAndSlot

    This is a mastapy class.
    """

    TYPE = _TOOTH_AND_SLOT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ToothAndSlot")

    class _Cast_ToothAndSlot:
        """Special nested class for casting ToothAndSlot to subclasses."""

        def __init__(self: "ToothAndSlot._Cast_ToothAndSlot", parent: "ToothAndSlot"):
            self._parent = parent

        @property
        def abstract_tooth_and_slot(
            self: "ToothAndSlot._Cast_ToothAndSlot",
        ) -> "_1250.AbstractToothAndSlot":
            return self._parent._cast(_1250.AbstractToothAndSlot)

        @property
        def tooth_and_slot(self: "ToothAndSlot._Cast_ToothAndSlot") -> "ToothAndSlot":
            return self._parent

        def __getattr__(self: "ToothAndSlot._Cast_ToothAndSlot", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ToothAndSlot.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def full_round_at_slot_bottom(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.FullRoundAtSlotBottom

        if temp is None:
            return False

        return temp

    @full_round_at_slot_bottom.setter
    @enforce_parameter_types
    def full_round_at_slot_bottom(self: Self, value: "bool"):
        self.wrapped.FullRoundAtSlotBottom = bool(value) if value is not None else False

    @property
    def has_wedges(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.HasWedges

        if temp is None:
            return False

        return temp

    @has_wedges.setter
    @enforce_parameter_types
    def has_wedges(self: Self, value: "bool"):
        self.wrapped.HasWedges = bool(value) if value is not None else False

    @property
    def radius_of_curvature_at_slot_bottom(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadiusOfCurvatureAtSlotBottom

        if temp is None:
            return 0.0

        return temp

    @radius_of_curvature_at_slot_bottom.setter
    @enforce_parameter_types
    def radius_of_curvature_at_slot_bottom(self: Self, value: "float"):
        self.wrapped.RadiusOfCurvatureAtSlotBottom = (
            float(value) if value is not None else 0.0
        )

    @property
    def slot_depth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SlotDepth

        if temp is None:
            return 0.0

        return temp

    @slot_depth.setter
    @enforce_parameter_types
    def slot_depth(self: Self, value: "float"):
        self.wrapped.SlotDepth = float(value) if value is not None else 0.0

    @property
    def slot_opening_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SlotOpeningLength

        if temp is None:
            return 0.0

        return temp

    @slot_opening_length.setter
    @enforce_parameter_types
    def slot_opening_length(self: Self, value: "float"):
        self.wrapped.SlotOpeningLength = float(value) if value is not None else 0.0

    @property
    def slot_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SlotWidth

        if temp is None:
            return 0.0

        return temp

    @slot_width.setter
    @enforce_parameter_types
    def slot_width(self: Self, value: "float"):
        self.wrapped.SlotWidth = float(value) if value is not None else 0.0

    @property
    def tooth_asymmetric_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ToothAsymmetricLength

        if temp is None:
            return 0.0

        return temp

    @tooth_asymmetric_length.setter
    @enforce_parameter_types
    def tooth_asymmetric_length(self: Self, value: "float"):
        self.wrapped.ToothAsymmetricLength = float(value) if value is not None else 0.0

    @property
    def tooth_taper_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ToothTaperAngle

        if temp is None:
            return 0.0

        return temp

    @tooth_taper_angle.setter
    @enforce_parameter_types
    def tooth_taper_angle(self: Self, value: "float"):
        self.wrapped.ToothTaperAngle = float(value) if value is not None else 0.0

    @property
    def tooth_taper_depth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ToothTaperDepth

        if temp is None:
            return 0.0

        return temp

    @tooth_taper_depth.setter
    @enforce_parameter_types
    def tooth_taper_depth(self: Self, value: "float"):
        self.wrapped.ToothTaperDepth = float(value) if value is not None else 0.0

    @property
    def tooth_taper_specification(self: Self) -> "_1315.ToothTaperSpecification":
        """mastapy.electric_machines.ToothTaperSpecification"""
        temp = self.wrapped.ToothTaperSpecification

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.ElectricMachines.ToothTaperSpecification"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines._1315", "ToothTaperSpecification"
        )(value)

    @tooth_taper_specification.setter
    @enforce_parameter_types
    def tooth_taper_specification(self: Self, value: "_1315.ToothTaperSpecification"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.ElectricMachines.ToothTaperSpecification"
        )
        self.wrapped.ToothTaperSpecification = value

    @property
    def tooth_tip_depth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ToothTipDepth

        if temp is None:
            return 0.0

        return temp

    @tooth_tip_depth.setter
    @enforce_parameter_types
    def tooth_tip_depth(self: Self, value: "float"):
        self.wrapped.ToothTipDepth = float(value) if value is not None else 0.0

    @property
    def tooth_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ToothWidth

        if temp is None:
            return 0.0

        return temp

    @tooth_width.setter
    @enforce_parameter_types
    def tooth_width(self: Self, value: "float"):
        self.wrapped.ToothWidth = float(value) if value is not None else 0.0

    @property
    def tooth_width_at_slot_bottom(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ToothWidthAtSlotBottom

        if temp is None:
            return 0.0

        return temp

    @tooth_width_at_slot_bottom.setter
    @enforce_parameter_types
    def tooth_width_at_slot_bottom(self: Self, value: "float"):
        self.wrapped.ToothWidthAtSlotBottom = float(value) if value is not None else 0.0

    @property
    def tooth_width_at_slot_top(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ToothWidthAtSlotTop

        if temp is None:
            return 0.0

        return temp

    @tooth_width_at_slot_top.setter
    @enforce_parameter_types
    def tooth_width_at_slot_top(self: Self, value: "float"):
        self.wrapped.ToothWidthAtSlotTop = float(value) if value is not None else 0.0

    @property
    def tooth_slot_style(self: Self) -> "_1314.ToothSlotStyle":
        """mastapy.electric_machines.ToothSlotStyle"""
        temp = self.wrapped.ToothSlotStyle

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.ElectricMachines.ToothSlotStyle"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines._1314", "ToothSlotStyle"
        )(value)

    @tooth_slot_style.setter
    @enforce_parameter_types
    def tooth_slot_style(self: Self, value: "_1314.ToothSlotStyle"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.ElectricMachines.ToothSlotStyle"
        )
        self.wrapped.ToothSlotStyle = value

    @property
    def wedge_thickness(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.WedgeThickness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @wedge_thickness.setter
    @enforce_parameter_types
    def wedge_thickness(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.WedgeThickness = value

    @property
    def cast_to(self: Self) -> "ToothAndSlot._Cast_ToothAndSlot":
        return self._Cast_ToothAndSlot(self)
