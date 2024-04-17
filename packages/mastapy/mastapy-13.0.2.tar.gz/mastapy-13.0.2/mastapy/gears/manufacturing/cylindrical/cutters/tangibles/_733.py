"""RackShape"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _726
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RACK_SHAPE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters.Tangibles", "RackShape"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters import _715
    from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _728, _731


__docformat__ = "restructuredtext en"
__all__ = ("RackShape",)


Self = TypeVar("Self", bound="RackShape")


class RackShape(_726.CutterShapeDefinition):
    """RackShape

    This is a mastapy class.
    """

    TYPE = _RACK_SHAPE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RackShape")

    class _Cast_RackShape:
        """Special nested class for casting RackShape to subclasses."""

        def __init__(self: "RackShape._Cast_RackShape", parent: "RackShape"):
            self._parent = parent

        @property
        def cutter_shape_definition(
            self: "RackShape._Cast_RackShape",
        ) -> "_726.CutterShapeDefinition":
            return self._parent._cast(_726.CutterShapeDefinition)

        @property
        def cylindrical_gear_hob_shape(
            self: "RackShape._Cast_RackShape",
        ) -> "_728.CylindricalGearHobShape":
            from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _728

            return self._parent._cast(_728.CylindricalGearHobShape)

        @property
        def cylindrical_gear_worm_grinder_shape(
            self: "RackShape._Cast_RackShape",
        ) -> "_731.CylindricalGearWormGrinderShape":
            from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _731

            return self._parent._cast(_731.CylindricalGearWormGrinderShape)

        @property
        def rack_shape(self: "RackShape._Cast_RackShape") -> "RackShape":
            return self._parent

        def __getattr__(self: "RackShape._Cast_RackShape", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RackShape.TYPE"):
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
    def addendum(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Addendum

        if temp is None:
            return 0.0

        return temp

    @addendum.setter
    @enforce_parameter_types
    def addendum(self: Self, value: "float"):
        self.wrapped.Addendum = float(value) if value is not None else 0.0

    @property
    def addendum_form(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AddendumForm

        if temp is None:
            return 0.0

        return temp

    @property
    def dedendum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Dedendum

        if temp is None:
            return 0.0

        return temp

    @property
    def edge_height(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EdgeHeight

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
    def flat_root_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlatRootWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def flat_tip_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlatTipWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def has_semi_topping_blade(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasSemiToppingBlade

        if temp is None:
            return False

        return temp

    @property
    def hob_whole_depth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HobWholeDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def main_blade_pressure_angle_nearest_hob_root(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MainBladePressureAngleNearestHobRoot

        if temp is None:
            return 0.0

        return temp

    @property
    def main_blade_pressure_angle_nearest_hob_tip(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MainBladePressureAngleNearestHobTip

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_edge_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumEdgeRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_protuberance_blade_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumProtuberanceBladePressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_protuberance_blade_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumProtuberanceBladePressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_protuberance_height(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumProtuberanceHeight

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_thickness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalThickness

        if temp is None:
            return 0.0

        return temp

    @normal_thickness.setter
    @enforce_parameter_types
    def normal_thickness(self: Self, value: "float"):
        self.wrapped.NormalThickness = float(value) if value is not None else 0.0

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
    def protuberance_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProtuberanceLength

        if temp is None:
            return 0.0

        return temp

    @property
    def protuberance_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProtuberancePressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def protuberance_relative_to_main_blade_pressure_angle_nearest_hob_tip(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProtuberanceRelativeToMainBladePressureAngleNearestHobTip

        if temp is None:
            return 0.0

        return temp

    @property
    def semi_topping_height(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SemiToppingHeight

        if temp is None:
            return 0.0

        return temp

    @semi_topping_height.setter
    @enforce_parameter_types
    def semi_topping_height(self: Self, value: "float"):
        self.wrapped.SemiToppingHeight = float(value) if value is not None else 0.0

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
    def semi_topping_start(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SemiToppingStart

        if temp is None:
            return 0.0

        return temp

    @semi_topping_start.setter
    @enforce_parameter_types
    def semi_topping_start(self: Self, value: "float"):
        self.wrapped.SemiToppingStart = float(value) if value is not None else 0.0

    @property
    def design(self: Self) -> "_715.CylindricalGearRackDesign":
        """mastapy.gears.manufacturing.cylindrical.cutters.CylindricalGearRackDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Design

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "RackShape._Cast_RackShape":
        return self._Cast_RackShape(self)
