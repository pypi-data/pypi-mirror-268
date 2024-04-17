"""SAESplineHalfDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.detailed_rigid_connectors.splines import _1426
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAE_SPLINE_HALF_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "SAESplineHalfDesign"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.splines.tolerances_and_deviations import (
        _1429,
    )
    from mastapy.detailed_rigid_connectors.splines import _1421
    from mastapy.detailed_rigid_connectors import _1395


__docformat__ = "restructuredtext en"
__all__ = ("SAESplineHalfDesign",)


Self = TypeVar("Self", bound="SAESplineHalfDesign")


class SAESplineHalfDesign(_1426.StandardSplineHalfDesign):
    """SAESplineHalfDesign

    This is a mastapy class.
    """

    TYPE = _SAE_SPLINE_HALF_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SAESplineHalfDesign")

    class _Cast_SAESplineHalfDesign:
        """Special nested class for casting SAESplineHalfDesign to subclasses."""

        def __init__(
            self: "SAESplineHalfDesign._Cast_SAESplineHalfDesign",
            parent: "SAESplineHalfDesign",
        ):
            self._parent = parent

        @property
        def standard_spline_half_design(
            self: "SAESplineHalfDesign._Cast_SAESplineHalfDesign",
        ) -> "_1426.StandardSplineHalfDesign":
            return self._parent._cast(_1426.StandardSplineHalfDesign)

        @property
        def spline_half_design(
            self: "SAESplineHalfDesign._Cast_SAESplineHalfDesign",
        ) -> "_1421.SplineHalfDesign":
            from mastapy.detailed_rigid_connectors.splines import _1421

            return self._parent._cast(_1421.SplineHalfDesign)

        @property
        def detailed_rigid_connector_half_design(
            self: "SAESplineHalfDesign._Cast_SAESplineHalfDesign",
        ) -> "_1395.DetailedRigidConnectorHalfDesign":
            from mastapy.detailed_rigid_connectors import _1395

            return self._parent._cast(_1395.DetailedRigidConnectorHalfDesign)

        @property
        def sae_spline_half_design(
            self: "SAESplineHalfDesign._Cast_SAESplineHalfDesign",
        ) -> "SAESplineHalfDesign":
            return self._parent

        def __getattr__(
            self: "SAESplineHalfDesign._Cast_SAESplineHalfDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SAESplineHalfDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def change_in_root_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ChangeInRootDiameter

        if temp is None:
            return 0.0

        return temp

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
    def maximum_effective_space_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumEffectiveSpaceWidth

        if temp is None:
            return 0.0

        return temp

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
    def maximum_major_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumMajorDiameter

        if temp is None:
            return 0.0

        return temp

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
    def minimum_effective_tooth_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumEffectiveToothThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_major_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumMajorDiameter

        if temp is None:
            return 0.0

        return temp

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
    def sae_accuracy_and_tolerance(self: Self) -> "_1429.SAESplineTolerances":
        """mastapy.detailed_rigid_connectors.splines.tolerances_and_deviations.SAESplineTolerances

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SAEAccuracyAndTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "SAESplineHalfDesign._Cast_SAESplineHalfDesign":
        return self._Cast_SAESplineHalfDesign(self)
