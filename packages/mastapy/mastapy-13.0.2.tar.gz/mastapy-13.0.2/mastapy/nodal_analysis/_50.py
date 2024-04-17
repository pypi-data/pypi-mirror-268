"""AnalysisSettingsItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.utility.databases import _1836
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANALYSIS_SETTINGS_ITEM = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "AnalysisSettingsItem"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _84, _85


__docformat__ = "restructuredtext en"
__all__ = ("AnalysisSettingsItem",)


Self = TypeVar("Self", bound="AnalysisSettingsItem")


class AnalysisSettingsItem(_1836.NamedDatabaseItem):
    """AnalysisSettingsItem

    This is a mastapy class.
    """

    TYPE = _ANALYSIS_SETTINGS_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AnalysisSettingsItem")

    class _Cast_AnalysisSettingsItem:
        """Special nested class for casting AnalysisSettingsItem to subclasses."""

        def __init__(
            self: "AnalysisSettingsItem._Cast_AnalysisSettingsItem",
            parent: "AnalysisSettingsItem",
        ):
            self._parent = parent

        @property
        def named_database_item(
            self: "AnalysisSettingsItem._Cast_AnalysisSettingsItem",
        ) -> "_1836.NamedDatabaseItem":
            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def analysis_settings_item(
            self: "AnalysisSettingsItem._Cast_AnalysisSettingsItem",
        ) -> "AnalysisSettingsItem":
            return self._parent

        def __getattr__(
            self: "AnalysisSettingsItem._Cast_AnalysisSettingsItem", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AnalysisSettingsItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_mesh_nodes_per_unit_length_to_diameter_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GearMeshNodesPerUnitLengthToDiameterRatio

        if temp is None:
            return 0.0

        return temp

    @gear_mesh_nodes_per_unit_length_to_diameter_ratio.setter
    @enforce_parameter_types
    def gear_mesh_nodes_per_unit_length_to_diameter_ratio(self: Self, value: "float"):
        self.wrapped.GearMeshNodesPerUnitLengthToDiameterRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_section_length_to_diameter_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumSectionLengthToDiameterRatio

        if temp is None:
            return 0.0

        return temp

    @maximum_section_length_to_diameter_ratio.setter
    @enforce_parameter_types
    def maximum_section_length_to_diameter_ratio(self: Self, value: "float"):
        self.wrapped.MaximumSectionLengthToDiameterRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_number_of_gear_mesh_nodes(self: Self) -> "int":
        """int"""
        temp = self.wrapped.MinimumNumberOfGearMeshNodes

        if temp is None:
            return 0

        return temp

    @minimum_number_of_gear_mesh_nodes.setter
    @enforce_parameter_types
    def minimum_number_of_gear_mesh_nodes(self: Self, value: "int"):
        self.wrapped.MinimumNumberOfGearMeshNodes = (
            int(value) if value is not None else 0
        )

    @property
    def overwrite_advanced_system_deflection_load_cases_created_for_harmonic_excitations(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.OverwriteAdvancedSystemDeflectionLoadCasesCreatedForHarmonicExcitations
        )

        if temp is None:
            return False

        return temp

    @overwrite_advanced_system_deflection_load_cases_created_for_harmonic_excitations.setter
    @enforce_parameter_types
    def overwrite_advanced_system_deflection_load_cases_created_for_harmonic_excitations(
        self: Self, value: "bool"
    ):
        self.wrapped.OverwriteAdvancedSystemDeflectionLoadCasesCreatedForHarmonicExcitations = (
            bool(value) if value is not None else False
        )

    @property
    def rating_type_for_bearing_reliability(
        self: Self,
    ) -> "_84.RatingTypeForBearingReliability":
        """mastapy.nodal_analysis.RatingTypeForBearingReliability"""
        temp = self.wrapped.RatingTypeForBearingReliability

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.RatingTypeForBearingReliability"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis._84", "RatingTypeForBearingReliability"
        )(value)

    @rating_type_for_bearing_reliability.setter
    @enforce_parameter_types
    def rating_type_for_bearing_reliability(
        self: Self, value: "_84.RatingTypeForBearingReliability"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.NodalAnalysis.RatingTypeForBearingReliability"
        )
        self.wrapped.RatingTypeForBearingReliability = value

    @property
    def rating_type_for_shaft_reliability(
        self: Self,
    ) -> "_85.RatingTypeForShaftReliability":
        """mastapy.nodal_analysis.RatingTypeForShaftReliability"""
        temp = self.wrapped.RatingTypeForShaftReliability

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.RatingTypeForShaftReliability"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis._85", "RatingTypeForShaftReliability"
        )(value)

    @rating_type_for_shaft_reliability.setter
    @enforce_parameter_types
    def rating_type_for_shaft_reliability(
        self: Self, value: "_85.RatingTypeForShaftReliability"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.NodalAnalysis.RatingTypeForShaftReliability"
        )
        self.wrapped.RatingTypeForShaftReliability = value

    @property
    def remove_rigid_body_rotation_theta_z_twist_from_shaft_reporting(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = self.wrapped.RemoveRigidBodyRotationThetaZTwistFromShaftReporting

        if temp is None:
            return False

        return temp

    @remove_rigid_body_rotation_theta_z_twist_from_shaft_reporting.setter
    @enforce_parameter_types
    def remove_rigid_body_rotation_theta_z_twist_from_shaft_reporting(
        self: Self, value: "bool"
    ):
        self.wrapped.RemoveRigidBodyRotationThetaZTwistFromShaftReporting = (
            bool(value) if value is not None else False
        )

    @property
    def spline_nodes_per_unit_length_to_diameter_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SplineNodesPerUnitLengthToDiameterRatio

        if temp is None:
            return 0.0

        return temp

    @spline_nodes_per_unit_length_to_diameter_ratio.setter
    @enforce_parameter_types
    def spline_nodes_per_unit_length_to_diameter_ratio(self: Self, value: "float"):
        self.wrapped.SplineNodesPerUnitLengthToDiameterRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def system_deflection_maximum_iterations(self: Self) -> "int":
        """int"""
        temp = self.wrapped.SystemDeflectionMaximumIterations

        if temp is None:
            return 0

        return temp

    @system_deflection_maximum_iterations.setter
    @enforce_parameter_types
    def system_deflection_maximum_iterations(self: Self, value: "int"):
        self.wrapped.SystemDeflectionMaximumIterations = (
            int(value) if value is not None else 0
        )

    @property
    def use_mean_load_and_load_sharing_factor_for_planet_bearing_reliability(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = self.wrapped.UseMeanLoadAndLoadSharingFactorForPlanetBearingReliability

        if temp is None:
            return False

        return temp

    @use_mean_load_and_load_sharing_factor_for_planet_bearing_reliability.setter
    @enforce_parameter_types
    def use_mean_load_and_load_sharing_factor_for_planet_bearing_reliability(
        self: Self, value: "bool"
    ):
        self.wrapped.UseMeanLoadAndLoadSharingFactorForPlanetBearingReliability = (
            bool(value) if value is not None else False
        )

    @property
    def use_single_node_for_cylindrical_gear_meshes(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseSingleNodeForCylindricalGearMeshes

        if temp is None:
            return False

        return temp

    @use_single_node_for_cylindrical_gear_meshes.setter
    @enforce_parameter_types
    def use_single_node_for_cylindrical_gear_meshes(self: Self, value: "bool"):
        self.wrapped.UseSingleNodeForCylindricalGearMeshes = (
            bool(value) if value is not None else False
        )

    @property
    def use_single_node_for_spline_connections(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseSingleNodeForSplineConnections

        if temp is None:
            return False

        return temp

    @use_single_node_for_spline_connections.setter
    @enforce_parameter_types
    def use_single_node_for_spline_connections(self: Self, value: "bool"):
        self.wrapped.UseSingleNodeForSplineConnections = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(self: Self) -> "AnalysisSettingsItem._Cast_AnalysisSettingsItem":
        return self._Cast_AnalysisSettingsItem(self)
