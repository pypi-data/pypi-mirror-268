"""InterferenceFitHalfDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.detailed_rigid_connectors import _1395
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTERFERENCE_FIT_HALF_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.InterferenceFits", "InterferenceFitHalfDesign"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.interference_fits import _1454
    from mastapy.bearings.tolerances import _1929
    from mastapy.detailed_rigid_connectors.keyed_joints import _1446


__docformat__ = "restructuredtext en"
__all__ = ("InterferenceFitHalfDesign",)


Self = TypeVar("Self", bound="InterferenceFitHalfDesign")


class InterferenceFitHalfDesign(_1395.DetailedRigidConnectorHalfDesign):
    """InterferenceFitHalfDesign

    This is a mastapy class.
    """

    TYPE = _INTERFERENCE_FIT_HALF_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InterferenceFitHalfDesign")

    class _Cast_InterferenceFitHalfDesign:
        """Special nested class for casting InterferenceFitHalfDesign to subclasses."""

        def __init__(
            self: "InterferenceFitHalfDesign._Cast_InterferenceFitHalfDesign",
            parent: "InterferenceFitHalfDesign",
        ):
            self._parent = parent

        @property
        def detailed_rigid_connector_half_design(
            self: "InterferenceFitHalfDesign._Cast_InterferenceFitHalfDesign",
        ) -> "_1395.DetailedRigidConnectorHalfDesign":
            return self._parent._cast(_1395.DetailedRigidConnectorHalfDesign)

        @property
        def keyway_joint_half_design(
            self: "InterferenceFitHalfDesign._Cast_InterferenceFitHalfDesign",
        ) -> "_1446.KeywayJointHalfDesign":
            from mastapy.detailed_rigid_connectors.keyed_joints import _1446

            return self._parent._cast(_1446.KeywayJointHalfDesign)

        @property
        def interference_fit_half_design(
            self: "InterferenceFitHalfDesign._Cast_InterferenceFitHalfDesign",
        ) -> "InterferenceFitHalfDesign":
            return self._parent

        def __getattr__(
            self: "InterferenceFitHalfDesign._Cast_InterferenceFitHalfDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InterferenceFitHalfDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_joint_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageJointDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def average_surface_roughness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AverageSurfaceRoughness

        if temp is None:
            return 0.0

        return temp

    @average_surface_roughness.setter
    @enforce_parameter_types
    def average_surface_roughness(self: Self, value: "float"):
        self.wrapped.AverageSurfaceRoughness = (
            float(value) if value is not None else 0.0
        )

    @property
    def designation(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Designation

        if temp is None:
            return ""

        return temp

    @property
    def diameter_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DiameterRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def joint_pressure_for_fully_plastic_part(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.JointPressureForFullyPlasticPart

        if temp is None:
            return 0.0

        return temp

    @property
    def lower_deviation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LowerDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def nominal_joint_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NominalJointDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @nominal_joint_diameter.setter
    @enforce_parameter_types
    def nominal_joint_diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NominalJointDiameter = value

    @property
    def permissible_joint_pressure_for_fully_elastic_part(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleJointPressureForFullyElasticPart

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_relative_interference_for_fully_elastic_part(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleRelativeInterferenceForFullyElasticPart

        if temp is None:
            return 0.0

        return temp

    @property
    def required_safety_against_plastic_strain(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RequiredSafetyAgainstPlasticStrain

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @required_safety_against_plastic_strain.setter
    @enforce_parameter_types
    def required_safety_against_plastic_strain(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RequiredSafetyAgainstPlasticStrain = value

    @property
    def stress_region(self: Self) -> "_1454.StressRegions":
        """mastapy.detailed_rigid_connectors.interference_fits.StressRegions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressRegion

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.DetailedRigidConnectors.InterferenceFits.StressRegions"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.detailed_rigid_connectors.interference_fits._1454", "StressRegions"
        )(value)

    @property
    def upper_deviation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UpperDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def tolerance(self: Self) -> "_1929.SupportTolerance":
        """mastapy.bearings.tolerances.SupportTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Tolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "InterferenceFitHalfDesign._Cast_InterferenceFitHalfDesign":
        return self._Cast_InterferenceFitHalfDesign(self)
