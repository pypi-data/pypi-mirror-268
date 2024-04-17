"""InterferenceFitDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.detailed_rigid_connectors.interference_fits import _1455
from mastapy.detailed_rigid_connectors import _1394
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTERFERENCE_FIT_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.InterferenceFits", "InterferenceFitDesign"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.interference_fits import _1450, _1451
    from mastapy.detailed_rigid_connectors.keyed_joints import _1444


__docformat__ = "restructuredtext en"
__all__ = ("InterferenceFitDesign",)


Self = TypeVar("Self", bound="InterferenceFitDesign")


class InterferenceFitDesign(_1394.DetailedRigidConnectorDesign):
    """InterferenceFitDesign

    This is a mastapy class.
    """

    TYPE = _INTERFERENCE_FIT_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InterferenceFitDesign")

    class _Cast_InterferenceFitDesign:
        """Special nested class for casting InterferenceFitDesign to subclasses."""

        def __init__(
            self: "InterferenceFitDesign._Cast_InterferenceFitDesign",
            parent: "InterferenceFitDesign",
        ):
            self._parent = parent

        @property
        def detailed_rigid_connector_design(
            self: "InterferenceFitDesign._Cast_InterferenceFitDesign",
        ) -> "_1394.DetailedRigidConnectorDesign":
            return self._parent._cast(_1394.DetailedRigidConnectorDesign)

        @property
        def keyed_joint_design(
            self: "InterferenceFitDesign._Cast_InterferenceFitDesign",
        ) -> "_1444.KeyedJointDesign":
            from mastapy.detailed_rigid_connectors.keyed_joints import _1444

            return self._parent._cast(_1444.KeyedJointDesign)

        @property
        def interference_fit_design(
            self: "InterferenceFitDesign._Cast_InterferenceFitDesign",
        ) -> "InterferenceFitDesign":
            return self._parent

        def __getattr__(
            self: "InterferenceFitDesign._Cast_InterferenceFitDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InterferenceFitDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_interference(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyInterference

        if temp is None:
            return 0.0

        return temp

    @property
    def assembly_method(self: Self) -> "_1450.AssemblyMethods":
        """mastapy.detailed_rigid_connectors.interference_fits.AssemblyMethods"""
        temp = self.wrapped.AssemblyMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.DetailedRigidConnectors.InterferenceFits.AssemblyMethods",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.detailed_rigid_connectors.interference_fits._1450",
            "AssemblyMethods",
        )(value)

    @assembly_method.setter
    @enforce_parameter_types
    def assembly_method(self: Self, value: "_1450.AssemblyMethods"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.DetailedRigidConnectors.InterferenceFits.AssemblyMethods",
        )
        self.wrapped.AssemblyMethod = value

    @property
    def auxiliary_elasticity_parameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuxiliaryElasticityParameter

        if temp is None:
            return 0.0

        return temp

    @property
    def average_allowable_axial_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageAllowableAxialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def average_allowable_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageAllowableTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def average_effective_interference(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageEffectiveInterference

        if temp is None:
            return 0.0

        return temp

    @property
    def average_interference(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageInterference

        if temp is None:
            return 0.0

        return temp

    @property
    def average_joint_pressure(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageJointPressure

        if temp is None:
            return 0.0

        return temp

    @property
    def average_permissible_axial_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AveragePermissibleAxialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def average_permissible_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AveragePermissibleTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def average_relative_interference(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageRelativeInterference

        if temp is None:
            return 0.0

        return temp

    @property
    def calculation_method(self: Self) -> "_1451.CalculationMethods":
        """mastapy.detailed_rigid_connectors.interference_fits.CalculationMethods"""
        temp = self.wrapped.CalculationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.DetailedRigidConnectors.InterferenceFits.CalculationMethods",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.detailed_rigid_connectors.interference_fits._1451",
            "CalculationMethods",
        )(value)

    @calculation_method.setter
    @enforce_parameter_types
    def calculation_method(self: Self, value: "_1451.CalculationMethods"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.DetailedRigidConnectors.InterferenceFits.CalculationMethods",
        )
        self.wrapped.CalculationMethod = value

    @property
    def coefficient_of_friction_assembly(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CoefficientOfFrictionAssembly

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @coefficient_of_friction_assembly.setter
    @enforce_parameter_types
    def coefficient_of_friction_assembly(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CoefficientOfFrictionAssembly = value

    @property
    def coefficient_of_friction_circumferential(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CoefficientOfFrictionCircumferential

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @coefficient_of_friction_circumferential.setter
    @enforce_parameter_types
    def coefficient_of_friction_circumferential(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CoefficientOfFrictionCircumferential = value

    @property
    def coefficient_of_friction_longitudinal(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CoefficientOfFrictionLongitudinal

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @coefficient_of_friction_longitudinal.setter
    @enforce_parameter_types
    def coefficient_of_friction_longitudinal(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CoefficientOfFrictionLongitudinal = value

    @property
    def diameter_of_joint(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DiameterOfJoint

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @diameter_of_joint.setter
    @enforce_parameter_types
    def diameter_of_joint(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DiameterOfJoint = value

    @property
    def dimensionless_plasticity_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DimensionlessPlasticityDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def insertion_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InsertionForce

        if temp is None:
            return 0.0

        return temp

    @property
    def joining_play(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.JoiningPlay

        if temp is None:
            return 0.0

        return temp

    @property
    def joint_interface_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_Table4JointInterfaceTypes":
        """EnumWithSelectedValue[mastapy.detailed_rigid_connectors.interference_fits.Table4JointInterfaceTypes]"""
        temp = self.wrapped.JointInterfaceType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_Table4JointInterfaceTypes.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @joint_interface_type.setter
    @enforce_parameter_types
    def joint_interface_type(self: Self, value: "_1455.Table4JointInterfaceTypes"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_Table4JointInterfaceTypes.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.JointInterfaceType = value

    @property
    def maximum_allowable_axial_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumAllowableAxialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_allowable_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumAllowableTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_assembly_interference(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumAssemblyInterference

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_effective_interference(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumEffectiveInterference

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_interference(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumInterference

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_joint_pressure(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumJointPressure

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_permissible_axial_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPermissibleAxialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_permissible_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPermissibleTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_relative_interference(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumRelativeInterference

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_allowable_axial_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumAllowableAxialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_allowable_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumAllowableTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_effective_interference(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumEffectiveInterference

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_interference(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumInterference

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_joint_pressure(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumJointPressure

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_permissible_axial_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumPermissibleAxialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_permissible_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumPermissibleTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_relative_interference(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumRelativeInterference

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_dimensionless_plasticity_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleDimensionlessPlasticityDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def proportion_of_outer_plastically_stressed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProportionOfOuterPlasticallyStressed

        if temp is None:
            return 0.0

        return temp

    @property
    def ratio_of_joint_length_to_joint_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatioOfJointLengthToJointDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def required_assembly_temperature_of_the_outer_part(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RequiredAssemblyTemperatureOfTheOuterPart

        if temp is None:
            return 0.0

        return temp

    @property
    def room_temperature_during_assembly(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RoomTemperatureDuringAssembly

        if temp is None:
            return 0.0

        return temp

    @room_temperature_during_assembly.setter
    @enforce_parameter_types
    def room_temperature_during_assembly(self: Self, value: "float"):
        self.wrapped.RoomTemperatureDuringAssembly = (
            float(value) if value is not None else 0.0
        )

    @property
    def specified_joint_pressure(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpecifiedJointPressure

        if temp is None:
            return 0.0

        return temp

    @specified_joint_pressure.setter
    @enforce_parameter_types
    def specified_joint_pressure(self: Self, value: "float"):
        self.wrapped.SpecifiedJointPressure = float(value) if value is not None else 0.0

    @property
    def temperature_of_inner_part_during_assembly(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TemperatureOfInnerPartDuringAssembly

        if temp is None:
            return 0.0

        return temp

    @temperature_of_inner_part_during_assembly.setter
    @enforce_parameter_types
    def temperature_of_inner_part_during_assembly(self: Self, value: "float"):
        self.wrapped.TemperatureOfInnerPartDuringAssembly = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(self: Self) -> "InterferenceFitDesign._Cast_InterferenceFitDesign":
        return self._Cast_InterferenceFitDesign(self)
