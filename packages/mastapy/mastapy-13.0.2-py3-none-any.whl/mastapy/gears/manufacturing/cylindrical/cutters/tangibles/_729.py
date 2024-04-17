"""CylindricalGearShaperTangible"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _726
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SHAPER_TANGIBLE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters.Tangibles",
    "CylindricalGearShaperTangible",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters import _717


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearShaperTangible",)


Self = TypeVar("Self", bound="CylindricalGearShaperTangible")


class CylindricalGearShaperTangible(_726.CutterShapeDefinition):
    """CylindricalGearShaperTangible

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SHAPER_TANGIBLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearShaperTangible")

    class _Cast_CylindricalGearShaperTangible:
        """Special nested class for casting CylindricalGearShaperTangible to subclasses."""

        def __init__(
            self: "CylindricalGearShaperTangible._Cast_CylindricalGearShaperTangible",
            parent: "CylindricalGearShaperTangible",
        ):
            self._parent = parent

        @property
        def cutter_shape_definition(
            self: "CylindricalGearShaperTangible._Cast_CylindricalGearShaperTangible",
        ) -> "_726.CutterShapeDefinition":
            return self._parent._cast(_726.CutterShapeDefinition)

        @property
        def cylindrical_gear_shaper_tangible(
            self: "CylindricalGearShaperTangible._Cast_CylindricalGearShaperTangible",
        ) -> "CylindricalGearShaperTangible":
            return self._parent

        def __getattr__(
            self: "CylindricalGearShaperTangible._Cast_CylindricalGearShaperTangible",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearShaperTangible.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def actual_protuberance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActualProtuberance

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
    def edge_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EdgeRadius

        if temp is None:
            return 0.0

        return temp

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
    def maximum_blade_control_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumBladeControlDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_protuberance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumProtuberance

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_protuberance_height_for_single_circle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumProtuberanceHeightForSingleCircle

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_tip_control_distance_for_zero_protuberance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumTipControlDistanceForZeroProtuberance

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_tip_diameter_to_avoid_pointed_teeth_no_protuberance(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumTipDiameterToAvoidPointedTeethNoProtuberance

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_protuberance_having_pointed_teeth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumProtuberanceHavingPointedTeeth

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_protuberance_height_for_single_circle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumProtuberanceHeightForSingleCircle

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_tooth_thickness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalToothThickness

        if temp is None:
            return 0.0

        return temp

    @normal_tooth_thickness.setter
    @enforce_parameter_types
    def normal_tooth_thickness(self: Self, value: "float"):
        self.wrapped.NormalToothThickness = float(value) if value is not None else 0.0

    @property
    def protuberance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Protuberance

        if temp is None:
            return 0.0

        return temp

    @protuberance.setter
    @enforce_parameter_types
    def protuberance(self: Self, value: "float"):
        self.wrapped.Protuberance = float(value) if value is not None else 0.0

    @property
    def protuberance_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProtuberanceAngle

        if temp is None:
            return 0.0

        return temp

    @protuberance_angle.setter
    @enforce_parameter_types
    def protuberance_angle(self: Self, value: "float"):
        self.wrapped.ProtuberanceAngle = float(value) if value is not None else 0.0

    @property
    def protuberance_height(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProtuberanceHeight

        if temp is None:
            return 0.0

        return temp

    @protuberance_height.setter
    @enforce_parameter_types
    def protuberance_height(self: Self, value: "float"):
        self.wrapped.ProtuberanceHeight = float(value) if value is not None else 0.0

    @property
    def root_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RootDiameter

        if temp is None:
            return 0.0

        return temp

    @root_diameter.setter
    @enforce_parameter_types
    def root_diameter(self: Self, value: "float"):
        self.wrapped.RootDiameter = float(value) if value is not None else 0.0

    @property
    def semi_topping_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SemiToppingDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def semi_topping_pressure_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SemiToppingPressureAngle

        if temp is None:
            return 0.0

        return temp

    @semi_topping_pressure_angle.setter
    @enforce_parameter_types
    def semi_topping_pressure_angle(self: Self, value: "float"):
        self.wrapped.SemiToppingPressureAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def single_circle_maximum_edge_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SingleCircleMaximumEdgeRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TipDiameter

        if temp is None:
            return 0.0

        return temp

    @tip_diameter.setter
    @enforce_parameter_types
    def tip_diameter(self: Self, value: "float"):
        self.wrapped.TipDiameter = float(value) if value is not None else 0.0

    @property
    def tip_thickness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TipThickness

        if temp is None:
            return 0.0

        return temp

    @tip_thickness.setter
    @enforce_parameter_types
    def tip_thickness(self: Self, value: "float"):
        self.wrapped.TipThickness = float(value) if value is not None else 0.0

    @property
    def design(self: Self) -> "_717.CylindricalGearShaper":
        """mastapy.gears.manufacturing.cylindrical.cutters.CylindricalGearShaper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Design

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearShaperTangible._Cast_CylindricalGearShaperTangible":
        return self._Cast_CylindricalGearShaperTangible(self)
