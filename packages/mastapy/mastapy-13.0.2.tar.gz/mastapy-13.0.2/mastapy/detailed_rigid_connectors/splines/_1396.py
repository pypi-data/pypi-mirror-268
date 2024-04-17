"""CustomSplineHalfDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.detailed_rigid_connectors.splines import _1421
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_SPLINE_HALF_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "CustomSplineHalfDesign"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors import _1395


__docformat__ = "restructuredtext en"
__all__ = ("CustomSplineHalfDesign",)


Self = TypeVar("Self", bound="CustomSplineHalfDesign")


class CustomSplineHalfDesign(_1421.SplineHalfDesign):
    """CustomSplineHalfDesign

    This is a mastapy class.
    """

    TYPE = _CUSTOM_SPLINE_HALF_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomSplineHalfDesign")

    class _Cast_CustomSplineHalfDesign:
        """Special nested class for casting CustomSplineHalfDesign to subclasses."""

        def __init__(
            self: "CustomSplineHalfDesign._Cast_CustomSplineHalfDesign",
            parent: "CustomSplineHalfDesign",
        ):
            self._parent = parent

        @property
        def spline_half_design(
            self: "CustomSplineHalfDesign._Cast_CustomSplineHalfDesign",
        ) -> "_1421.SplineHalfDesign":
            return self._parent._cast(_1421.SplineHalfDesign)

        @property
        def detailed_rigid_connector_half_design(
            self: "CustomSplineHalfDesign._Cast_CustomSplineHalfDesign",
        ) -> "_1395.DetailedRigidConnectorHalfDesign":
            from mastapy.detailed_rigid_connectors import _1395

            return self._parent._cast(_1395.DetailedRigidConnectorHalfDesign)

        @property
        def custom_spline_half_design(
            self: "CustomSplineHalfDesign._Cast_CustomSplineHalfDesign",
        ) -> "CustomSplineHalfDesign":
            return self._parent

        def __getattr__(
            self: "CustomSplineHalfDesign._Cast_CustomSplineHalfDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomSplineHalfDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def actual_tooth_thickness_or_space_width_tolerance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActualToothThicknessOrSpaceWidthTolerance

        if temp is None:
            return 0.0

        return temp

    @property
    def addendum_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AddendumFactor

        if temp is None:
            return 0.0

        return temp

    @addendum_factor.setter
    @enforce_parameter_types
    def addendum_factor(self: Self, value: "float"):
        self.wrapped.AddendumFactor = float(value) if value is not None else 0.0

    @property
    def dedendum_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DedendumFactor

        if temp is None:
            return 0.0

        return temp

    @dedendum_factor.setter
    @enforce_parameter_types
    def dedendum_factor(self: Self, value: "float"):
        self.wrapped.DedendumFactor = float(value) if value is not None else 0.0

    @property
    def effective_tooth_thickness_or_space_width_tolerance(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.EffectiveToothThicknessOrSpaceWidthTolerance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @effective_tooth_thickness_or_space_width_tolerance.setter
    @enforce_parameter_types
    def effective_tooth_thickness_or_space_width_tolerance(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.EffectiveToothThicknessOrSpaceWidthTolerance = value

    @property
    def form_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def major_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MajorDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def major_diameter_specified(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MajorDiameterSpecified

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @major_diameter_specified.setter
    @enforce_parameter_types
    def major_diameter_specified(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MajorDiameterSpecified = value

    @property
    def maximum_actual_space_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumActualSpaceWidth

        if temp is None:
            return 0.0

        return temp

    @maximum_actual_space_width.setter
    @enforce_parameter_types
    def maximum_actual_space_width(self: Self, value: "float"):
        self.wrapped.MaximumActualSpaceWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_actual_tooth_thickness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumActualToothThickness

        if temp is None:
            return 0.0

        return temp

    @maximum_actual_tooth_thickness.setter
    @enforce_parameter_types
    def maximum_actual_tooth_thickness(self: Self, value: "float"):
        self.wrapped.MaximumActualToothThickness = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_chordal_span_over_teeth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumChordalSpanOverTeeth

        if temp is None:
            return 0.0

        return temp

    @maximum_chordal_span_over_teeth.setter
    @enforce_parameter_types
    def maximum_chordal_span_over_teeth(self: Self, value: "float"):
        self.wrapped.MaximumChordalSpanOverTeeth = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_dimension_over_balls(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumDimensionOverBalls

        if temp is None:
            return 0.0

        return temp

    @maximum_dimension_over_balls.setter
    @enforce_parameter_types
    def maximum_dimension_over_balls(self: Self, value: "float"):
        self.wrapped.MaximumDimensionOverBalls = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_effective_tooth_thickness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumEffectiveToothThickness

        if temp is None:
            return 0.0

        return temp

    @maximum_effective_tooth_thickness.setter
    @enforce_parameter_types
    def maximum_effective_tooth_thickness(self: Self, value: "float"):
        self.wrapped.MaximumEffectiveToothThickness = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_space_width_deviation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumSpaceWidthDeviation

        if temp is None:
            return 0.0

        return temp

    @maximum_space_width_deviation.setter
    @enforce_parameter_types
    def maximum_space_width_deviation(self: Self, value: "float"):
        self.wrapped.MaximumSpaceWidthDeviation = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_tooth_thickness_deviation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumToothThicknessDeviation

        if temp is None:
            return 0.0

        return temp

    @maximum_tooth_thickness_deviation.setter
    @enforce_parameter_types
    def maximum_tooth_thickness_deviation(self: Self, value: "float"):
        self.wrapped.MaximumToothThicknessDeviation = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_actual_space_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumActualSpaceWidth

        if temp is None:
            return 0.0

        return temp

    @minimum_actual_space_width.setter
    @enforce_parameter_types
    def minimum_actual_space_width(self: Self, value: "float"):
        self.wrapped.MinimumActualSpaceWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_actual_tooth_thickness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumActualToothThickness

        if temp is None:
            return 0.0

        return temp

    @minimum_actual_tooth_thickness.setter
    @enforce_parameter_types
    def minimum_actual_tooth_thickness(self: Self, value: "float"):
        self.wrapped.MinimumActualToothThickness = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_chordal_span_over_teeth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumChordalSpanOverTeeth

        if temp is None:
            return 0.0

        return temp

    @minimum_chordal_span_over_teeth.setter
    @enforce_parameter_types
    def minimum_chordal_span_over_teeth(self: Self, value: "float"):
        self.wrapped.MinimumChordalSpanOverTeeth = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_dimension_over_balls(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumDimensionOverBalls

        if temp is None:
            return 0.0

        return temp

    @minimum_dimension_over_balls.setter
    @enforce_parameter_types
    def minimum_dimension_over_balls(self: Self, value: "float"):
        self.wrapped.MinimumDimensionOverBalls = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_effective_space_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumEffectiveSpaceWidth

        if temp is None:
            return 0.0

        return temp

    @minimum_effective_space_width.setter
    @enforce_parameter_types
    def minimum_effective_space_width(self: Self, value: "float"):
        self.wrapped.MinimumEffectiveSpaceWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_space_width_deviation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumSpaceWidthDeviation

        if temp is None:
            return 0.0

        return temp

    @minimum_space_width_deviation.setter
    @enforce_parameter_types
    def minimum_space_width_deviation(self: Self, value: "float"):
        self.wrapped.MinimumSpaceWidthDeviation = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_tooth_thickness_deviation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumToothThicknessDeviation

        if temp is None:
            return 0.0

        return temp

    @minimum_tooth_thickness_deviation.setter
    @enforce_parameter_types
    def minimum_tooth_thickness_deviation(self: Self, value: "float"):
        self.wrapped.MinimumToothThicknessDeviation = (
            float(value) if value is not None else 0.0
        )

    @property
    def minor_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinorDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def minor_diameter_specified(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinorDiameterSpecified

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minor_diameter_specified.setter
    @enforce_parameter_types
    def minor_diameter_specified(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinorDiameterSpecified = value

    @property
    def root_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RootDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @root_diameter.setter
    @enforce_parameter_types
    def root_diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RootDiameter = value

    @property
    def root_fillet_radius_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RootFilletRadiusFactor

        if temp is None:
            return 0.0

        return temp

    @root_fillet_radius_factor.setter
    @enforce_parameter_types
    def root_fillet_radius_factor(self: Self, value: "float"):
        self.wrapped.RootFilletRadiusFactor = float(value) if value is not None else 0.0

    @property
    def tip_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TipDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tip_diameter.setter
    @enforce_parameter_types
    def tip_diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TipDiameter = value

    @property
    def total_tooth_thickness_or_space_width_tolerance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TotalToothThicknessOrSpaceWidthTolerance

        if temp is None:
            return 0.0

        return temp

    @total_tooth_thickness_or_space_width_tolerance.setter
    @enforce_parameter_types
    def total_tooth_thickness_or_space_width_tolerance(self: Self, value: "float"):
        self.wrapped.TotalToothThicknessOrSpaceWidthTolerance = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(self: Self) -> "CustomSplineHalfDesign._Cast_CustomSplineHalfDesign":
        return self._Cast_CustomSplineHalfDesign(self)
