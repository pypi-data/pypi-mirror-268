"""CylindricalGearBasicRack"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.gears.gear_designs.cylindrical import _1010
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_BASIC_RACK = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalGearBasicRack"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1004, _1087, _1027, _1082


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearBasicRack",)


Self = TypeVar("Self", bound="CylindricalGearBasicRack")


class CylindricalGearBasicRack(_1010.CylindricalGearAbstractRack):
    """CylindricalGearBasicRack

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_BASIC_RACK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearBasicRack")

    class _Cast_CylindricalGearBasicRack:
        """Special nested class for casting CylindricalGearBasicRack to subclasses."""

        def __init__(
            self: "CylindricalGearBasicRack._Cast_CylindricalGearBasicRack",
            parent: "CylindricalGearBasicRack",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_abstract_rack(
            self: "CylindricalGearBasicRack._Cast_CylindricalGearBasicRack",
        ) -> "_1010.CylindricalGearAbstractRack":
            return self._parent._cast(_1010.CylindricalGearAbstractRack)

        @property
        def standard_rack(
            self: "CylindricalGearBasicRack._Cast_CylindricalGearBasicRack",
        ) -> "_1082.StandardRack":
            from mastapy.gears.gear_designs.cylindrical import _1082

            return self._parent._cast(_1082.StandardRack)

        @property
        def cylindrical_gear_basic_rack(
            self: "CylindricalGearBasicRack._Cast_CylindricalGearBasicRack",
        ) -> "CylindricalGearBasicRack":
            return self._parent

        def __getattr__(
            self: "CylindricalGearBasicRack._Cast_CylindricalGearBasicRack", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearBasicRack.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def basic_rack_clearance_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicRackClearanceFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rack_profile(self: Self) -> "_1004.BasicRackProfiles":
        """mastapy.gears.gear_designs.cylindrical.BasicRackProfiles"""
        temp = self.wrapped.BasicRackProfile

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.BasicRackProfiles"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1004", "BasicRackProfiles"
        )(value)

    @basic_rack_profile.setter
    @enforce_parameter_types
    def basic_rack_profile(self: Self, value: "_1004.BasicRackProfiles"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.BasicRackProfiles"
        )
        self.wrapped.BasicRackProfile = value

    @property
    def proportional_method_for_tip_clearance(
        self: Self,
    ) -> "_1087.TipAlterationCoefficientMethod":
        """mastapy.gears.gear_designs.cylindrical.TipAlterationCoefficientMethod"""
        temp = self.wrapped.ProportionalMethodForTipClearance

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.TipAlterationCoefficientMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1087",
            "TipAlterationCoefficientMethod",
        )(value)

    @proportional_method_for_tip_clearance.setter
    @enforce_parameter_types
    def proportional_method_for_tip_clearance(
        self: Self, value: "_1087.TipAlterationCoefficientMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.TipAlterationCoefficientMethod",
        )
        self.wrapped.ProportionalMethodForTipClearance = value

    @property
    def tip_alteration_proportional_method_mesh(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.TipAlterationProportionalMethodMesh

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @tip_alteration_proportional_method_mesh.setter
    @enforce_parameter_types
    def tip_alteration_proportional_method_mesh(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.TipAlterationProportionalMethodMesh = value

    @property
    def pinion_type_cutter_for_rating(
        self: Self,
    ) -> "_1027.CylindricalGearPinionTypeCutter":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearPinionTypeCutter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionTypeCutterForRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearBasicRack._Cast_CylindricalGearBasicRack":
        return self._Cast_CylindricalGearBasicRack(self)
