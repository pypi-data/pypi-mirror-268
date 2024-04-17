"""InvoluteCutterDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.cylindrical.cutters import _716
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INVOLUTE_CUTTER_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters", "InvoluteCutterDesign"
)

if TYPE_CHECKING:
    from mastapy.gears import _336
    from mastapy.gears.gear_designs.cylindrical import _1092
    from mastapy.gears.manufacturing.cylindrical.cutters import _713, _717, _718, _709
    from mastapy.utility.databases import _1836


__docformat__ = "restructuredtext en"
__all__ = ("InvoluteCutterDesign",)


Self = TypeVar("Self", bound="InvoluteCutterDesign")


class InvoluteCutterDesign(_716.CylindricalGearRealCutterDesign):
    """InvoluteCutterDesign

    This is a mastapy class.
    """

    TYPE = _INVOLUTE_CUTTER_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InvoluteCutterDesign")

    class _Cast_InvoluteCutterDesign:
        """Special nested class for casting InvoluteCutterDesign to subclasses."""

        def __init__(
            self: "InvoluteCutterDesign._Cast_InvoluteCutterDesign",
            parent: "InvoluteCutterDesign",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_real_cutter_design(
            self: "InvoluteCutterDesign._Cast_InvoluteCutterDesign",
        ) -> "_716.CylindricalGearRealCutterDesign":
            return self._parent._cast(_716.CylindricalGearRealCutterDesign)

        @property
        def cylindrical_gear_abstract_cutter_design(
            self: "InvoluteCutterDesign._Cast_InvoluteCutterDesign",
        ) -> "_709.CylindricalGearAbstractCutterDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _709

            return self._parent._cast(_709.CylindricalGearAbstractCutterDesign)

        @property
        def named_database_item(
            self: "InvoluteCutterDesign._Cast_InvoluteCutterDesign",
        ) -> "_1836.NamedDatabaseItem":
            from mastapy.utility.databases import _1836

            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def cylindrical_gear_plunge_shaver(
            self: "InvoluteCutterDesign._Cast_InvoluteCutterDesign",
        ) -> "_713.CylindricalGearPlungeShaver":
            from mastapy.gears.manufacturing.cylindrical.cutters import _713

            return self._parent._cast(_713.CylindricalGearPlungeShaver)

        @property
        def cylindrical_gear_shaper(
            self: "InvoluteCutterDesign._Cast_InvoluteCutterDesign",
        ) -> "_717.CylindricalGearShaper":
            from mastapy.gears.manufacturing.cylindrical.cutters import _717

            return self._parent._cast(_717.CylindricalGearShaper)

        @property
        def cylindrical_gear_shaver(
            self: "InvoluteCutterDesign._Cast_InvoluteCutterDesign",
        ) -> "_718.CylindricalGearShaver":
            from mastapy.gears.manufacturing.cylindrical.cutters import _718

            return self._parent._cast(_718.CylindricalGearShaver)

        @property
        def involute_cutter_design(
            self: "InvoluteCutterDesign._Cast_InvoluteCutterDesign",
        ) -> "InvoluteCutterDesign":
            return self._parent

        def __getattr__(
            self: "InvoluteCutterDesign._Cast_InvoluteCutterDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InvoluteCutterDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hand(self: Self) -> "_336.Hand":
        """mastapy.gears.Hand"""
        temp = self.wrapped.Hand

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.Hand")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.gears._336", "Hand")(value)

    @hand.setter
    @enforce_parameter_types
    def hand(self: Self, value: "_336.Hand"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Gears.Hand")
        self.wrapped.Hand = value

    @property
    def helix_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HelixAngle

        if temp is None:
            return 0.0

        return temp

    @helix_angle.setter
    @enforce_parameter_types
    def helix_angle(self: Self, value: "float"):
        self.wrapped.HelixAngle = float(value) if value is not None else 0.0

    @property
    def number_of_teeth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NumberOfTeeth

        if temp is None:
            return 0.0

        return temp

    @number_of_teeth.setter
    @enforce_parameter_types
    def number_of_teeth(self: Self, value: "float"):
        self.wrapped.NumberOfTeeth = float(value) if value is not None else 0.0

    @property
    def tooth_thickness(self: Self) -> "_1092.ToothThicknessSpecificationBase":
        """mastapy.gears.gear_designs.cylindrical.ToothThicknessSpecificationBase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothThickness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "InvoluteCutterDesign._Cast_InvoluteCutterDesign":
        return self._Cast_InvoluteCutterDesign(self)
