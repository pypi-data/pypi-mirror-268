"""FESubstructure"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List, Optional

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.implicit import (
    list_with_selected_item,
    overridable,
    enum_with_selected_value,
)
from mastapy.system_model.part_model import _2451, _2455
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.utility.units_and_measurements import _1617
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.fe import _2418, _2395
from mastapy.nodal_analysis import _66
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_STRING = python_net_import("System", "String")
_TASK_PROGRESS = python_net_import("SMT.MastaAPIUtility", "TaskProgress")
_FE_SUBSTRUCTURE = python_net_import("SMT.MastaAPI.SystemModel.FE", "FESubstructure")

if TYPE_CHECKING:
    from mastapy.system_model.fe import (
        _2363,
        _2369,
        _2365,
        _2391,
        _2402,
        _2388,
        _2403,
        _2392,
        _2416,
        _2398,
        _2399,
        _2400,
        _2401,
    )
    from mastapy.nodal_analysis import _70, _88, _60
    from mastapy.nodal_analysis.component_mode_synthesis import _236, _229
    from mastapy.materials import _240, _286
    from mastapy.system_model import _2227
    from mastapy.math_utility import _1506
    from mastapy.system_model.part_model import _2460
    from mastapy.nodal_analysis.geometry_modeller_link import _158, _160
    from mastapy.system_model.fe.links import _2425
    from mastapy.system_model.part_model.shaft_model import _2489
    from mastapy.math_utility.measured_vectors import _1571
    from mastapy.nodal_analysis.fe_export_utility import _169
    from mastapy import _7567


__docformat__ = "restructuredtext en"
__all__ = ("FESubstructure",)


Self = TypeVar("Self", bound="FESubstructure")


class FESubstructure(_66.FEStiffness):
    """FESubstructure

    This is a mastapy class.
    """

    TYPE = _FE_SUBSTRUCTURE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FESubstructure")

    class _Cast_FESubstructure:
        """Special nested class for casting FESubstructure to subclasses."""

        def __init__(
            self: "FESubstructure._Cast_FESubstructure", parent: "FESubstructure"
        ):
            self._parent = parent

        @property
        def fe_stiffness(
            self: "FESubstructure._Cast_FESubstructure",
        ) -> "_66.FEStiffness":
            return self._parent._cast(_66.FEStiffness)

        @property
        def fe_substructure(
            self: "FESubstructure._Cast_FESubstructure",
        ) -> "FESubstructure":
            return self._parent

        def __getattr__(self: "FESubstructure._Cast_FESubstructure", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FESubstructure.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def actual_number_of_rigid_body_modes(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActualNumberOfRigidBodyModes

        if temp is None:
            return 0

        return temp

    @property
    def alignment_method(self: Self) -> "_2363.AlignmentMethod":
        """mastapy.system_model.fe.AlignmentMethod"""
        temp = self.wrapped.AlignmentMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.FE.AlignmentMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.fe._2363", "AlignmentMethod"
        )(value)

    @alignment_method.setter
    @enforce_parameter_types
    def alignment_method(self: Self, value: "_2363.AlignmentMethod"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.FE.AlignmentMethod"
        )
        self.wrapped.AlignmentMethod = value

    @property
    def angle_span(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AngleSpan

        if temp is None:
            return 0.0

        return temp

    @angle_span.setter
    @enforce_parameter_types
    def angle_span(self: Self, value: "float"):
        self.wrapped.AngleSpan = float(value) if value is not None else 0.0

    @property
    def angular_alignment_tolerance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AngularAlignmentTolerance

        if temp is None:
            return 0.0

        return temp

    @angular_alignment_tolerance.setter
    @enforce_parameter_types
    def angular_alignment_tolerance(self: Self, value: "float"):
        self.wrapped.AngularAlignmentTolerance = (
            float(value) if value is not None else 0.0
        )

    @property
    def apply_translation_and_rotation_for_planetary_duplicates(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ApplyTranslationAndRotationForPlanetaryDuplicates

        if temp is None:
            return False

        return temp

    @apply_translation_and_rotation_for_planetary_duplicates.setter
    @enforce_parameter_types
    def apply_translation_and_rotation_for_planetary_duplicates(
        self: Self, value: "bool"
    ):
        self.wrapped.ApplyTranslationAndRotationForPlanetaryDuplicates = (
            bool(value) if value is not None else False
        )

    @property
    def are_vectors_loaded(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AreVectorsLoaded

        if temp is None:
            return False

        return temp

    @property
    def bearing_node_alignment(self: Self) -> "_2369.BearingNodeAlignmentOption":
        """mastapy.system_model.fe.BearingNodeAlignmentOption"""
        temp = self.wrapped.BearingNodeAlignment

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.FE.BearingNodeAlignmentOption"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.fe._2369", "BearingNodeAlignmentOption"
        )(value)

    @bearing_node_alignment.setter
    @enforce_parameter_types
    def bearing_node_alignment(self: Self, value: "_2369.BearingNodeAlignmentOption"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.FE.BearingNodeAlignmentOption"
        )
        self.wrapped.BearingNodeAlignment = value

    @property
    def bearing_races_in_fe(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.BearingRacesInFE

        if temp is None:
            return False

        return temp

    @bearing_races_in_fe.setter
    @enforce_parameter_types
    def bearing_races_in_fe(self: Self, value: "bool"):
        self.wrapped.BearingRacesInFE = bool(value) if value is not None else False

    @property
    def check_fe_has_internal_modes_before_nvh_analysis(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CheckFEHasInternalModesBeforeNVHAnalysis

        if temp is None:
            return False

        return temp

    @check_fe_has_internal_modes_before_nvh_analysis.setter
    @enforce_parameter_types
    def check_fe_has_internal_modes_before_nvh_analysis(self: Self, value: "bool"):
        self.wrapped.CheckFEHasInternalModesBeforeNVHAnalysis = (
            bool(value) if value is not None else False
        )

    @property
    def comment(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Comment

        if temp is None:
            return ""

        return temp

    @comment.setter
    @enforce_parameter_types
    def comment(self: Self, value: "str"):
        self.wrapped.Comment = str(value) if value is not None else ""

    @property
    def component_to_align_to(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_Component":
        """ListWithSelectedItem[mastapy.system_model.part_model.Component]"""
        temp = self.wrapped.ComponentToAlignTo

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Component",
        )(temp)

    @component_to_align_to.setter
    @enforce_parameter_types
    def component_to_align_to(self: Self, value: "_2451.Component"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_Component.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Component.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.ComponentToAlignTo = value

    @property
    def condensation_node_size(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CondensationNodeSize

        if temp is None:
            return 0.0

        return temp

    @condensation_node_size.setter
    @enforce_parameter_types
    def condensation_node_size(self: Self, value: "float"):
        self.wrapped.CondensationNodeSize = float(value) if value is not None else 0.0

    @property
    def datum(self: Self) -> "list_with_selected_item.ListWithSelectedItem_Datum":
        """ListWithSelectedItem[mastapy.system_model.part_model.Datum]"""
        temp = self.wrapped.Datum

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Datum",
        )(temp)

    @datum.setter
    @enforce_parameter_types
    def datum(self: Self, value: "_2455.Datum"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Datum.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Datum.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.Datum = value

    @property
    def distance_display_unit(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_Unit":
        """ListWithSelectedItem[mastapy.utility.units_and_measurements.Unit]"""
        temp = self.wrapped.DistanceDisplayUnit

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Unit",
        )(temp)

    @distance_display_unit.setter
    @enforce_parameter_types
    def distance_display_unit(self: Self, value: "_1617.Unit"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.DistanceDisplayUnit = value

    @property
    def expected_number_of_rigid_body_modes(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.ExpectedNumberOfRigidBodyModes

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @expected_number_of_rigid_body_modes.setter
    @enforce_parameter_types
    def expected_number_of_rigid_body_modes(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.ExpectedNumberOfRigidBodyModes = value

    @property
    def external_fe_forces_are_from_gravity_only(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ExternalFEForcesAreFromGravityOnly

        if temp is None:
            return False

        return temp

    @external_fe_forces_are_from_gravity_only.setter
    @enforce_parameter_types
    def external_fe_forces_are_from_gravity_only(self: Self, value: "bool"):
        self.wrapped.ExternalFEForcesAreFromGravityOnly = (
            bool(value) if value is not None else False
        )

    @property
    def force_display_unit(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_Unit":
        """ListWithSelectedItem[mastapy.utility.units_and_measurements.Unit]"""
        temp = self.wrapped.ForceDisplayUnit

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Unit",
        )(temp)

    @force_display_unit.setter
    @enforce_parameter_types
    def force_display_unit(self: Self, value: "_1617.Unit"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.ForceDisplayUnit = value

    @property
    def full_fe_model_mesh_path(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FullFEModelMeshPath

        if temp is None:
            return ""

        return temp

    @property
    def full_fe_model_mesh_size(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FullFEModelMeshSize

        if temp is None:
            return ""

        return temp

    @property
    def full_fe_model_vectors_path(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FullFEModelVectorsPath

        if temp is None:
            return ""

        return temp

    @property
    def full_fe_model_vectors_size(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FullFEModelVectorsSize

        if temp is None:
            return ""

        return temp

    @property
    def geometry_meshing_material(self: Self) -> "str":
        """str"""
        temp = self.wrapped.GeometryMeshingMaterial.SelectedItemName

        if temp is None:
            return ""

        return temp

    @geometry_meshing_material.setter
    @enforce_parameter_types
    def geometry_meshing_material(self: Self, value: "str"):
        self.wrapped.GeometryMeshingMaterial.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def gravity_force_can_be_rotated(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GravityForceCanBeRotated

        if temp is None:
            return False

        return temp

    @property
    def gravity_force_source(self: Self) -> "_70.GravityForceSource":
        """mastapy.nodal_analysis.GravityForceSource

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GravityForceSource

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.GravityForceSource"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis._70", "GravityForceSource"
        )(value)

    @property
    def gravity_magnitude_used_for_reduced_forces(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GravityMagnitudeUsedForReducedForces

        if temp is None:
            return 0.0

        return temp

    @gravity_magnitude_used_for_reduced_forces.setter
    @enforce_parameter_types
    def gravity_magnitude_used_for_reduced_forces(self: Self, value: "float"):
        self.wrapped.GravityMagnitudeUsedForReducedForces = (
            float(value) if value is not None else 0.0
        )

    @property
    def housing_is_grounded(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.HousingIsGrounded

        if temp is None:
            return False

        return temp

    @housing_is_grounded.setter
    @enforce_parameter_types
    def housing_is_grounded(self: Self, value: "bool"):
        self.wrapped.HousingIsGrounded = bool(value) if value is not None else False

    @property
    def is_housing(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsHousing

        if temp is None:
            return False

        return temp

    @is_housing.setter
    @enforce_parameter_types
    def is_housing(self: Self, value: "bool"):
        self.wrapped.IsHousing = bool(value) if value is not None else False

    @property
    def is_mesh_loaded(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsMeshLoaded

        if temp is None:
            return False

        return temp

    @property
    def material(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Material.SelectedItemName

        if temp is None:
            return ""

        return temp

    @material.setter
    @enforce_parameter_types
    def material(self: Self, value: "str"):
        self.wrapped.Material.SetSelectedItem(str(value) if value is not None else "")

    @property
    def non_condensation_node_size(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NonCondensationNodeSize

        if temp is None:
            return 0

        return temp

    @non_condensation_node_size.setter
    @enforce_parameter_types
    def non_condensation_node_size(self: Self, value: "int"):
        self.wrapped.NonCondensationNodeSize = int(value) if value is not None else 0

    @property
    def number_of_angles(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfAngles

        if temp is None:
            return 0

        return temp

    @number_of_angles.setter
    @enforce_parameter_types
    def number_of_angles(self: Self, value: "int"):
        self.wrapped.NumberOfAngles = int(value) if value is not None else 0

    @property
    def number_of_condensation_nodes(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfCondensationNodes

        if temp is None:
            return 0

        return temp

    @property
    def number_of_condensation_nodes_in_reduced_model(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfCondensationNodesInReducedModel

        if temp is None:
            return 0

        return temp

    @property
    def polar_inertia(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PolarInertia

        if temp is None:
            return 0.0

        return temp

    @property
    def reduced_stiffness_file(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReducedStiffnessFile

        if temp is None:
            return ""

        return temp

    @property
    def reduced_stiffness_file_editable(self: Self) -> "str":
        """str"""
        temp = self.wrapped.ReducedStiffnessFileEditable

        if temp is None:
            return ""

        return temp

    @reduced_stiffness_file_editable.setter
    @enforce_parameter_types
    def reduced_stiffness_file_editable(self: Self, value: "str"):
        self.wrapped.ReducedStiffnessFileEditable = (
            str(value) if value is not None else ""
        )

    @property
    def reduction_mode_type(self: Self) -> "_236.ReductionModeType":
        """mastapy.nodal_analysis.component_mode_synthesis.ReductionModeType"""
        temp = self.wrapped.ReductionModeType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis.ReductionModeType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis.component_mode_synthesis._236", "ReductionModeType"
        )(value)

    @reduction_mode_type.setter
    @enforce_parameter_types
    def reduction_mode_type(self: Self, value: "_236.ReductionModeType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis.ReductionModeType"
        )
        self.wrapped.ReductionModeType = value

    @property
    def thermal_expansion_option(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ThermalExpansionOption":
        """EnumWithSelectedValue[mastapy.system_model.fe.ThermalExpansionOption]"""
        temp = self.wrapped.ThermalExpansionOption

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ThermalExpansionOption.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @thermal_expansion_option.setter
    @enforce_parameter_types
    def thermal_expansion_option(self: Self, value: "_2418.ThermalExpansionOption"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ThermalExpansionOption.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ThermalExpansionOption = value

    @property
    def torque_transmission_relative_tolerance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TorqueTransmissionRelativeTolerance

        if temp is None:
            return 0.0

        return temp

    @torque_transmission_relative_tolerance.setter
    @enforce_parameter_types
    def torque_transmission_relative_tolerance(self: Self, value: "float"):
        self.wrapped.TorqueTransmissionRelativeTolerance = (
            float(value) if value is not None else 0.0
        )

    @property
    def type_(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_FESubstructureType":
        """EnumWithSelectedValue[mastapy.system_model.fe.FESubstructureType]"""
        temp = self.wrapped.Type

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_FESubstructureType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @type_.setter
    @enforce_parameter_types
    def type_(self: Self, value: "_2395.FESubstructureType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_FESubstructureType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.Type = value

    @property
    def acoustic_radiation_efficiency(self: Self) -> "_240.AcousticRadiationEfficiency":
        """mastapy.materials.AcousticRadiationEfficiency

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AcousticRadiationEfficiency

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def alignment_using_axial_node_positions(
        self: Self,
    ) -> "_2365.AlignmentUsingAxialNodePositions":
        """mastapy.system_model.fe.AlignmentUsingAxialNodePositions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AlignmentUsingAxialNodePositions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def alignment_to_component(
        self: Self,
    ) -> "_2227.RelativeComponentAlignment[_2451.Component]":
        """mastapy.system_model.RelativeComponentAlignment[mastapy.system_model.part_model.Component]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AlignmentToComponent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_2451.Component](temp)

    @property
    def cms_model(self: Self) -> "_229.CMSModel":
        """mastapy.nodal_analysis.component_mode_synthesis.CMSModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CMSModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def coordinate_system(self: Self) -> "_1506.CoordinateSystem3D":
        """mastapy.math_utility.CoordinateSystem3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def export(self: Self) -> "_2391.FESubstructureExportOptions":
        """mastapy.system_model.fe.FESubstructureExportOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Export

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def fe_meshing_options(self: Self) -> "_88.ShaftFEMeshingOptions":
        """mastapy.nodal_analysis.ShaftFEMeshingOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEMeshingOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def fe_part(self: Self) -> "_2460.FEPart":
        """mastapy.system_model.part_model.FEPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEPart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def geometry_modeller_design_information(
        self: Self,
    ) -> "_158.GeometryModellerDesignInformation":
        """mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDesignInformation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryModellerDesignInformation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def geometry_modeller_dimensions(self: Self) -> "_160.GeometryModellerDimensions":
        """mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDimensions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryModellerDimensions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def sound_pressure_enclosure(self: Self) -> "_286.SoundPressureEnclosure":
        """mastapy.materials.SoundPressureEnclosure

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SoundPressureEnclosure

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_meshing_options(self: Self) -> "List[_2402.GearMeshingOptions]":
        """List[mastapy.system_model.fe.GearMeshingOptions]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshingOptions

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def geometries(self: Self) -> "List[_2388.FEStiffnessGeometry]":
        """List[mastapy.system_model.fe.FEStiffnessGeometry]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Geometries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def independent_masta_created_condensation_nodes(
        self: Self,
    ) -> "List[_2403.IndependentMASTACreatedCondensationNode]":
        """List[mastapy.system_model.fe.IndependentMASTACreatedCondensationNode]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IndependentMastaCreatedCondensationNodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def links(self: Self) -> "List[_2425.FELink]":
        """List[mastapy.system_model.fe.links.FELink]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Links

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def nodes(self: Self) -> "List[_2392.FESubstructureNode]":
        """List[mastapy.system_model.fe.FESubstructureNode]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Nodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def replaced_shafts(self: Self) -> "List[_2489.Shaft]":
        """List[mastapy.system_model.part_model.shaft_model.Shaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReplacedShafts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def shafts_that_can_be_replaced(
        self: Self,
    ) -> "List[_2416.ReplacedShaftSelectionHelper]":
        """List[mastapy.system_model.fe.ReplacedShaftSelectionHelper]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftsThatCanBeReplaced

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def thermal_expansion_displacements(
        self: Self,
    ) -> "List[_1571.VectorWithLinearAndAngularComponents]":
        """List[mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThermalExpansionDisplacements

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def thermal_expansion_forces(
        self: Self,
    ) -> "List[_1571.VectorWithLinearAndAngularComponents]":
        """List[mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThermalExpansionForces

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    def add_geometry(self: Self):
        """Method does not return."""
        self.wrapped.AddGeometry()

    def auto_connect_external_nodes(self: Self):
        """Method does not return."""
        self.wrapped.AutoConnectExternalNodes()

    def copy_datum_to_manual(self: Self):
        """Method does not return."""
        self.wrapped.CopyDatumToManual()

    def create_datum_from_manual_alignment(self: Self):
        """Method does not return."""
        self.wrapped.CreateDatumFromManualAlignment()

    def create_fe_volume_mesh(self: Self):
        """Method does not return."""
        self.wrapped.CreateFEVolumeMesh()

    def default_node_creation_options(self: Self):
        """Method does not return."""
        self.wrapped.DefaultNodeCreationOptions()

    def delete_all_links(self: Self):
        """Method does not return."""
        self.wrapped.DeleteAllLinks()

    def embed_fe_model_mesh_in_masta_file(self: Self):
        """Method does not return."""
        self.wrapped.EmbedFEModelMeshInMASTAFile()

    def embed_fe_model_vectors_in_masta_file(self: Self):
        """Method does not return."""
        self.wrapped.EmbedFEModelVectorsInMASTAFile()

    def perform_reduction(self: Self):
        """Method does not return."""
        self.wrapped.PerformReduction()

    def re_import_external_fe_mesh(self: Self):
        """Method does not return."""
        self.wrapped.ReImportExternalFEMesh()

    def remove_full_fe_mesh(self: Self):
        """Method does not return."""
        self.wrapped.RemoveFullFEMesh()

    def reread_mesh_from_geometry_modeller(self: Self):
        """Method does not return."""
        self.wrapped.RereadMeshFromGeometryModeller()

    def unload_external_mesh_file(self: Self):
        """Method does not return."""
        self.wrapped.UnloadExternalMeshFile()

    def unload_external_vectors_file(self: Self):
        """Method does not return."""
        self.wrapped.UnloadExternalVectorsFile()

    def update_gear_teeth_mesh(self: Self):
        """Method does not return."""
        self.wrapped.UpdateGearTeethMesh()

    @enforce_parameter_types
    def convert_shafts_to_fe(
        self: Self, operation: "_60.FEMeshingOperation", export_file_name: "str"
    ):
        """Method does not return.

        Args:
            operation (mastapy.nodal_analysis.FEMeshingOperation)
            export_file_name (str)
        """
        operation = conversion.mp_to_pn_enum(
            operation, "SMT.MastaAPI.NodalAnalysis.FEMeshingOperation"
        )
        export_file_name = str(export_file_name)
        self.wrapped.ConvertShaftsToFE(
            operation, export_file_name if export_file_name else ""
        )

    def create_fe_substructure_with_selection_components(
        self: Self,
    ) -> "_2398.FESubstructureWithSelectionComponents":
        """mastapy.system_model.fe.FESubstructureWithSelectionComponents"""
        method_result = self.wrapped.CreateFESubstructureWithSelectionComponents()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def create_fe_substructure_with_selection_for_harmonic_analysis(
        self: Self,
    ) -> "_2399.FESubstructureWithSelectionForHarmonicAnalysis":
        """mastapy.system_model.fe.FESubstructureWithSelectionForHarmonicAnalysis"""
        method_result = (
            self.wrapped.CreateFESubstructureWithSelectionForHarmonicAnalysis()
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def create_fe_substructure_with_selection_for_modal_analysis(
        self: Self,
    ) -> "_2400.FESubstructureWithSelectionForModalAnalysis":
        """mastapy.system_model.fe.FESubstructureWithSelectionForModalAnalysis"""
        method_result = self.wrapped.CreateFESubstructureWithSelectionForModalAnalysis()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def create_fe_substructure_with_selection_for_static_analysis(
        self: Self,
    ) -> "_2401.FESubstructureWithSelectionForStaticAnalysis":
        """mastapy.system_model.fe.FESubstructureWithSelectionForStaticAnalysis"""
        method_result = (
            self.wrapped.CreateFESubstructureWithSelectionForStaticAnalysis()
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def duplicate(self: Self, name: "str") -> "FESubstructure":
        """mastapy.system_model.fe.FESubstructure

        Args:
            name (str)
        """
        name = str(name)
        method_result = self.wrapped.Duplicate(name if name else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def import_fe_mesh(
        self: Self,
        file_path: "str",
        format_: "_169.FEExportFormat",
        length_scale: "float" = 1.0,
        force_scale: "float" = 1.0,
        progress: Optional["_7567.TaskProgress"] = None,
    ):
        """Method does not return.

        Args:
            file_path (str)
            format_ (mastapy.nodal_analysis.fe_export_utility.FEExportFormat)
            length_scale (float, optional)
            force_scale (float, optional)
            progress (mastapy.TaskProgress, optional)
        """
        file_path = str(file_path)
        format_ = conversion.mp_to_pn_enum(
            format_, "SMT.MastaAPI.NodalAnalysis.FeExportUtility.FEExportFormat"
        )
        length_scale = float(length_scale)
        force_scale = float(force_scale)
        self.wrapped.ImportFEMesh(
            file_path if file_path else "",
            format_,
            length_scale if length_scale else 0.0,
            force_scale if force_scale else 0.0,
            progress.wrapped if progress else None,
        )

    @enforce_parameter_types
    def import_node_positions(
        self: Self, file_name: "str", distance_unit: "_1617.Unit"
    ):
        """Method does not return.

        Args:
            file_name (str)
            distance_unit (mastapy.utility.units_and_measurements.Unit)
        """
        file_name = str(file_name)
        self.wrapped.ImportNodePositions(
            file_name if file_name else "",
            distance_unit.wrapped if distance_unit else None,
        )

    @enforce_parameter_types
    def import_reduced_stiffness(
        self: Self,
        file_name: "str",
        distance_unit: "_1617.Unit",
        force_unit: "_1617.Unit",
    ):
        """Method does not return.

        Args:
            file_name (str)
            distance_unit (mastapy.utility.units_and_measurements.Unit)
            force_unit (mastapy.utility.units_and_measurements.Unit)
        """
        file_name = str(file_name)
        self.wrapped.ImportReducedStiffness(
            file_name if file_name else "",
            distance_unit.wrapped if distance_unit else None,
            force_unit.wrapped if force_unit else None,
        )

    @enforce_parameter_types
    def links_for(self: Self, node: "_2392.FESubstructureNode") -> "List[_2425.FELink]":
        """List[mastapy.system_model.fe.links.FELink]

        Args:
            node (mastapy.system_model.fe.FESubstructureNode)
        """
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.LinksFor(node.wrapped if node else None)
        )

    @enforce_parameter_types
    def load_existing_masta_fe_file(self: Self, file_name: "str"):
        """Method does not return.

        Args:
            file_name (str)
        """
        file_name = str(file_name)
        self.wrapped.LoadExistingMastaFEFile.Overloads[_STRING](
            file_name if file_name else ""
        )

    @enforce_parameter_types
    def load_existing_masta_fe_file_with_progress(
        self: Self, file_name: "str", progress: "_7567.TaskProgress"
    ):
        """Method does not return.

        Args:
            file_name (str)
            progress (mastapy.TaskProgress)
        """
        file_name = str(file_name)
        self.wrapped.LoadExistingMastaFEFile.Overloads[_STRING, _TASK_PROGRESS](
            file_name if file_name else "", progress.wrapped if progress else None
        )

    @enforce_parameter_types
    def load_external_mesh(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.LoadExternalMesh(file_path if file_path else "")

    @enforce_parameter_types
    def load_external_vectors(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.LoadExternalVectors(file_path if file_path else "")

    @enforce_parameter_types
    def load_stl_geometry(self: Self, length_unit: "_1617.Unit", file_name: "str"):
        """Method does not return.

        Args:
            length_unit (mastapy.utility.units_and_measurements.Unit)
            file_name (str)
        """
        file_name = str(file_name)
        self.wrapped.LoadStlGeometry(
            length_unit.wrapped if length_unit else None, file_name if file_name else ""
        )

    @enforce_parameter_types
    def store_full_fe_mesh_in_external_file(self: Self, external_fe_path: "str"):
        """Method does not return.

        Args:
            external_fe_path (str)
        """
        external_fe_path = str(external_fe_path)
        self.wrapped.StoreFullFeMeshInExternalFile(
            external_fe_path if external_fe_path else ""
        )

    @enforce_parameter_types
    def store_full_fe_model_vectors_in_external_file(
        self: Self, external_fe_path: "str"
    ):
        """Method does not return.

        Args:
            external_fe_path (str)
        """
        external_fe_path = str(external_fe_path)
        self.wrapped.StoreFullFeModelVectorsInExternalFile(
            external_fe_path if external_fe_path else ""
        )

    @property
    def cast_to(self: Self) -> "FESubstructure._Cast_FESubstructure":
        return self._Cast_FESubstructure(self)
