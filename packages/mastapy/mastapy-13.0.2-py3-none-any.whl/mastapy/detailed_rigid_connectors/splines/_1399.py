"""DIN5480SplineHalfDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.detailed_rigid_connectors.splines import _1426
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DIN5480_SPLINE_HALF_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "DIN5480SplineHalfDesign"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.splines import _1418, _1409, _1421
    from mastapy.detailed_rigid_connectors import _1395


__docformat__ = "restructuredtext en"
__all__ = ("DIN5480SplineHalfDesign",)


Self = TypeVar("Self", bound="DIN5480SplineHalfDesign")


class DIN5480SplineHalfDesign(_1426.StandardSplineHalfDesign):
    """DIN5480SplineHalfDesign

    This is a mastapy class.
    """

    TYPE = _DIN5480_SPLINE_HALF_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DIN5480SplineHalfDesign")

    class _Cast_DIN5480SplineHalfDesign:
        """Special nested class for casting DIN5480SplineHalfDesign to subclasses."""

        def __init__(
            self: "DIN5480SplineHalfDesign._Cast_DIN5480SplineHalfDesign",
            parent: "DIN5480SplineHalfDesign",
        ):
            self._parent = parent

        @property
        def standard_spline_half_design(
            self: "DIN5480SplineHalfDesign._Cast_DIN5480SplineHalfDesign",
        ) -> "_1426.StandardSplineHalfDesign":
            return self._parent._cast(_1426.StandardSplineHalfDesign)

        @property
        def spline_half_design(
            self: "DIN5480SplineHalfDesign._Cast_DIN5480SplineHalfDesign",
        ) -> "_1421.SplineHalfDesign":
            from mastapy.detailed_rigid_connectors.splines import _1421

            return self._parent._cast(_1421.SplineHalfDesign)

        @property
        def detailed_rigid_connector_half_design(
            self: "DIN5480SplineHalfDesign._Cast_DIN5480SplineHalfDesign",
        ) -> "_1395.DetailedRigidConnectorHalfDesign":
            from mastapy.detailed_rigid_connectors import _1395

            return self._parent._cast(_1395.DetailedRigidConnectorHalfDesign)

        @property
        def din5480_spline_half_design(
            self: "DIN5480SplineHalfDesign._Cast_DIN5480SplineHalfDesign",
        ) -> "DIN5480SplineHalfDesign":
            return self._parent

        def __getattr__(
            self: "DIN5480SplineHalfDesign._Cast_DIN5480SplineHalfDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DIN5480SplineHalfDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def addendum_modification(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AddendumModification

        if temp is None:
            return 0.0

        return temp

    @property
    def addendum_of_basic_rack(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AddendumOfBasicRack

        if temp is None:
            return 0.0

        return temp

    @property
    def base_form_circle_diameter_limit(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BaseFormCircleDiameterLimit

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rack_addendum_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicRackAddendumFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rack_dedendum_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicRackDedendumFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def bottom_clearance_of_basic_rack(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BottomClearanceOfBasicRack

        if temp is None:
            return 0.0

        return temp

    @property
    def dedendum_of_basic_rack(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DedendumOfBasicRack

        if temp is None:
            return 0.0

        return temp

    @property
    def finishing_method(self: Self) -> "_1418.FinishingMethods":
        """mastapy.detailed_rigid_connectors.splines.FinishingMethods"""
        temp = self.wrapped.FinishingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.DetailedRigidConnectors.Splines.FinishingMethods"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.detailed_rigid_connectors.splines._1418", "FinishingMethods"
        )(value)

    @finishing_method.setter
    @enforce_parameter_types
    def finishing_method(self: Self, value: "_1418.FinishingMethods"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.DetailedRigidConnectors.Splines.FinishingMethods"
        )
        self.wrapped.FinishingMethod = value

    @property
    def form_clearance_of_basic_rack(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FormClearanceOfBasicRack

        if temp is None:
            return 0.0

        return temp

    @property
    def manufacturing_type(self: Self) -> "_1409.ManufacturingTypes":
        """mastapy.detailed_rigid_connectors.splines.ManufacturingTypes"""
        temp = self.wrapped.ManufacturingType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.DetailedRigidConnectors.Splines.ManufacturingTypes"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.detailed_rigid_connectors.splines._1409", "ManufacturingTypes"
        )(value)

    @manufacturing_type.setter
    @enforce_parameter_types
    def manufacturing_type(self: Self, value: "_1409.ManufacturingTypes"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.DetailedRigidConnectors.Splines.ManufacturingTypes"
        )
        self.wrapped.ManufacturingType = value

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
    def maximum_effective_root_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumEffectiveRootDiameter

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
    def minimum_effective_root_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumEffectiveRootDiameter

        if temp is None:
            return 0.0

        return temp

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
    def root_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def root_fillet_radius_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootFilletRadiusFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_height_of_basic_rack(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothHeightOfBasicRack

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "DIN5480SplineHalfDesign._Cast_DIN5480SplineHalfDesign":
        return self._Cast_DIN5480SplineHalfDesign(self)
