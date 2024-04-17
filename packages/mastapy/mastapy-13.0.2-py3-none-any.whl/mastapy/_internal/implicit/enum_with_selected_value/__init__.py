"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from .shaft_rating_method import EnumWithSelectedValue_ShaftRatingMethod
    from .surface_finishes import EnumWithSelectedValue_SurfaceFinishes
    from .integration_method import EnumWithSelectedValue_IntegrationMethod
    from .value_input_option import EnumWithSelectedValue_ValueInputOption
    from .single_point_selection_method import (
        EnumWithSelectedValue_SinglePointSelectionMethod,
    )
    from .result_options_for_3d_vector import (
        EnumWithSelectedValue_ResultOptionsFor3DVector,
    )
    from .elmer_result_type import EnumWithSelectedValue_ElmerResultType
    from .mode_input_type import EnumWithSelectedValue_ModeInputType
    from .material_property_class import EnumWithSelectedValue_MaterialPropertyClass
    from .lubricant_definition import EnumWithSelectedValue_LubricantDefinition
    from .lubricant_viscosity_class_iso import (
        EnumWithSelectedValue_LubricantViscosityClassISO,
    )
    from .micro_geometry_model import EnumWithSelectedValue_MicroGeometryModel
    from .extrapolation_options import EnumWithSelectedValue_ExtrapolationOptions
    from .cylindrical_gear_rating_methods import (
        EnumWithSelectedValue_CylindricalGearRatingMethods,
    )
    from .scuffing_flash_temperature_rating_method import (
        EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod,
    )
    from .scuffing_integral_temperature_rating_method import (
        EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod,
    )
    from .location_of_evaluation_lower_limit import (
        EnumWithSelectedValue_LocationOfEvaluationLowerLimit,
    )
    from .location_of_evaluation_upper_limit import (
        EnumWithSelectedValue_LocationOfEvaluationUpperLimit,
    )
    from .location_of_root_relief_evaluation import (
        EnumWithSelectedValue_LocationOfRootReliefEvaluation,
    )
    from .location_of_tip_relief_evaluation import (
        EnumWithSelectedValue_LocationOfTipReliefEvaluation,
    )
    from .cylindrical_mft_finishing_methods import (
        EnumWithSelectedValue_CylindricalMftFinishingMethods,
    )
    from .cylindrical_mft_roughing_methods import (
        EnumWithSelectedValue_CylindricalMftRoughingMethods,
    )
    from .micro_geometry_definition_method import (
        EnumWithSelectedValue_MicroGeometryDefinitionMethod,
    )
    from .micro_geometry_definition_type import (
        EnumWithSelectedValue_MicroGeometryDefinitionType,
    )
    from .chart_type import EnumWithSelectedValue_ChartType
    from .flank import EnumWithSelectedValue_Flank
    from .active_process_method import EnumWithSelectedValue_ActiveProcessMethod
    from .cutter_flank_sections import EnumWithSelectedValue_CutterFlankSections
    from .basic_curve_types import EnumWithSelectedValue_BasicCurveTypes
    from .thickness_type import EnumWithSelectedValue_ThicknessType
    from .conical_machine_setting_calculation_methods import (
        EnumWithSelectedValue_ConicalMachineSettingCalculationMethods,
    )
    from .conical_manufacture_methods import (
        EnumWithSelectedValue_ConicalManufactureMethods,
    )
    from .candidate_display_choice import EnumWithSelectedValue_CandidateDisplayChoice
    from .severity import EnumWithSelectedValue_Severity
    from .geometry_specification_type import (
        EnumWithSelectedValue_GeometrySpecificationType,
    )
    from .status_item_severity import EnumWithSelectedValue_StatusItemSeverity
    from .lubrication_methods import EnumWithSelectedValue_LubricationMethods
    from .micropitting_coefficient_of_friction_calculation_method import (
        EnumWithSelectedValue_MicropittingCoefficientOfFrictionCalculationMethod,
    )
    from .scuffing_coefficient_of_friction_methods import (
        EnumWithSelectedValue_ScuffingCoefficientOfFrictionMethods,
    )
    from .residual_stress_calculation_method import (
        EnumWithSelectedValue_ResidualStressCalculationMethod,
    )
    from .contact_result_type import EnumWithSelectedValue_ContactResultType
    from .stress_results_type import EnumWithSelectedValue_StressResultsType
    from .derived_parameter_option import (
        EnumWithSelectedValue_CylindricalGearPairCreationOptions_DerivedParameterOption,
    )
    from .tooth_thickness_specification_method import (
        EnumWithSelectedValue_ToothThicknessSpecificationMethod,
    )
    from .load_distribution_factor_methods import (
        EnumWithSelectedValue_LoadDistributionFactorMethods,
    )
    from .agma_gleason_conical_gear_geometry_methods import (
        EnumWithSelectedValue_AGMAGleasonConicalGearGeometryMethods,
    )
    from .pro_solve_mpc_type import EnumWithSelectedValue_ProSolveMpcType
    from .pro_solve_solver_type import EnumWithSelectedValue_ProSolveSolverType
    from .coil_position_in_slot import EnumWithSelectedValue_CoilPositionInSlot
    from .electric_machine_analysis_period import (
        EnumWithSelectedValue_ElectricMachineAnalysisPeriod,
    )
    from .specify_torque_or_current import EnumWithSelectedValue_SpecifyTorqueOrCurrent
    from .load_case_type import EnumWithSelectedValue_LoadCaseType
    from .harmonic_load_data_type import EnumWithSelectedValue_HarmonicLoadDataType
    from .force_display_option import EnumWithSelectedValue_ForceDisplayOption
    from .it_designation import EnumWithSelectedValue_ITDesignation
    from .dudley_effective_length_approximation_option import (
        EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption,
    )
    from .spline_rating_types import EnumWithSelectedValue_SplineRatingTypes
    from .modules import EnumWithSelectedValue_Modules
    from .pressure_angle_types import EnumWithSelectedValue_PressureAngleTypes
    from .spline_fit_class_type import EnumWithSelectedValue_SplineFitClassType
    from .spline_tolerance_class_types import (
        EnumWithSelectedValue_SplineToleranceClassTypes,
    )
    from .table_4_joint_interface_types import (
        EnumWithSelectedValue_Table4JointInterfaceTypes,
    )
    from .dynamics_response_scaling import EnumWithSelectedValue_DynamicsResponseScaling
    from .cad_page_orientation import EnumWithSelectedValue_CadPageOrientation
    from .fluid_film_temperature_options import (
        EnumWithSelectedValue_FluidFilmTemperatureOptions,
    )
    from .support_tolerance_location_designation import (
        EnumWithSelectedValue_SupportToleranceLocationDesignation,
    )
    from .loaded_ball_element_property_type import (
        EnumWithSelectedValue_LoadedBallElementPropertyType,
    )
    from .roller_bearing_profile_types import (
        EnumWithSelectedValue_RollerBearingProfileTypes,
    )
    from .rolling_bearing_arrangement import (
        EnumWithSelectedValue_RollingBearingArrangement,
    )
    from .basic_dynamic_load_rating_calculation_method import (
        EnumWithSelectedValue_BasicDynamicLoadRatingCalculationMethod,
    )
    from .basic_static_load_rating_calculation_method import (
        EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod,
    )
    from .fatigue_load_limit_calculation_method_enum import (
        EnumWithSelectedValue_FatigueLoadLimitCalculationMethodEnum,
    )
    from .rolling_bearing_race_type import EnumWithSelectedValue_RollingBearingRaceType
    from .rotational_directions import EnumWithSelectedValue_RotationalDirections
    from .bearing_efficiency_rating_method import (
        EnumWithSelectedValue_BearingEfficiencyRatingMethod,
    )
    from .shaft_diameter_modification_due_to_rolling_bearing_ring import (
        EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing,
    )
    from .excitation_analysis_view_option import (
        EnumWithSelectedValue_ExcitationAnalysisViewOption,
    )
    from .three_d_view_contour_option_first_selection import (
        EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection,
    )
    from .three_d_view_contour_option_second_selection import (
        EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection,
    )
    from .component_orientation_option import (
        EnumWithSelectedValue_ComponentOrientationOption,
    )
    from .axis import EnumWithSelectedValue_Axis
    from .alignment_axis import EnumWithSelectedValue_AlignmentAxis
    from .design_entity_id import EnumWithSelectedValue_DesignEntityId
    from .thermal_expansion_option import EnumWithSelectedValue_ThermalExpansionOption
    from .fe_substructure_type import EnumWithSelectedValue_FESubstructureType
    from .fe_substructuring_file_format import (
        EnumWithSelectedValue_FESubstructuringFileFormat,
    )
    from .three_d_view_contour_option import (
        EnumWithSelectedValue_ThreeDViewContourOption,
    )
    from .boundary_condition_type import EnumWithSelectedValue_BoundaryConditionType
    from .fe_export_format import EnumWithSelectedValue_FEExportFormat
    from .bearing_node_option import EnumWithSelectedValue_BearingNodeOption
    from .link_node_source import EnumWithSelectedValue_LinkNodeSource
    from .bearing_tolerance_class import EnumWithSelectedValue_BearingToleranceClass
    from .bearing_model import EnumWithSelectedValue_BearingModel
    from .preload_type import EnumWithSelectedValue_PreloadType
    from .race_axial_mounting_type import EnumWithSelectedValue_RaceAxialMountingType
    from .race_radial_mounting_type import EnumWithSelectedValue_RaceRadialMountingType
    from .internal_clearance_class import EnumWithSelectedValue_InternalClearanceClass
    from .bearing_tolerance_definition_options import (
        EnumWithSelectedValue_BearingToleranceDefinitionOptions,
    )
    from .oil_seal_loss_calculation_method import (
        EnumWithSelectedValue_OilSealLossCalculationMethod,
    )
    from .power_load_type import EnumWithSelectedValue_PowerLoadType
    from .rigid_connector_stiffness_type import (
        EnumWithSelectedValue_RigidConnectorStiffnessType,
    )
    from .rigid_connector_tooth_spacing_type import (
        EnumWithSelectedValue_RigidConnectorToothSpacingType,
    )
    from .rigid_connector_types import EnumWithSelectedValue_RigidConnectorTypes
    from .fit_types import EnumWithSelectedValue_FitTypes
    from .doe_value_specification_option import (
        EnumWithSelectedValue_DoeValueSpecificationOption,
    )
    from .analysis_type import EnumWithSelectedValue_AnalysisType
    from .bar_model_export_type import EnumWithSelectedValue_BarModelExportType
    from .dynamics_response_3d_chart_type import (
        EnumWithSelectedValue_DynamicsResponse3DChartType,
    )
    from .complex_part_display_option import (
        EnumWithSelectedValue_ComplexPartDisplayOption,
    )
    from .dynamics_response_type import EnumWithSelectedValue_DynamicsResponseType
    from .bearing_stiffness_model import EnumWithSelectedValue_BearingStiffnessModel
    from .gear_mesh_stiffness_model import EnumWithSelectedValue_GearMeshStiffnessModel
    from .shaft_and_housing_flexibility_option import (
        EnumWithSelectedValue_ShaftAndHousingFlexibilityOption,
    )
    from .export_output_type import EnumWithSelectedValue_ExportOutputType
    from .complex_number_output import (
        EnumWithSelectedValue_HarmonicAnalysisFEExportOptions_ComplexNumberOutput,
    )
    from .step_creation import (
        EnumWithSelectedValue_StiffnessOptionsForHarmonicAnalysis_StepCreation,
    )
    from .harmonic_analysis_torque_input_type import (
        EnumWithSelectedValue_HarmonicAnalysisTorqueInputType,
    )
    from .friction_model_for_gyroscopic_moment import (
        EnumWithSelectedValue_FrictionModelForGyroscopicMoment,
    )
    from .mesh_stiffness_model import EnumWithSelectedValue_MeshStiffnessModel
    from .shear_area_factor_method import EnumWithSelectedValue_ShearAreaFactorMethod
    from .stress_concentration_method import (
        EnumWithSelectedValue_StressConcentrationMethod,
    )
    from .ball_bearing_analysis_method import (
        EnumWithSelectedValue_BallBearingAnalysisMethod,
    )
    from .hertzian_contact_deflection_calculation_method import (
        EnumWithSelectedValue_HertzianContactDeflectionCalculationMethod,
    )
    from .torque_ripple_input_type import EnumWithSelectedValue_TorqueRippleInputType
    from .harmonic_excitation_type import EnumWithSelectedValue_HarmonicExcitationType
    from .force_specification import (
        EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification,
    )
    from .torque_specification_for_system_deflection import (
        EnumWithSelectedValue_TorqueSpecificationForSystemDeflection,
    )
    from .power_load_input_torque_specification_method import (
        EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod,
    )
    from .torque_converter_lockup_rule import (
        EnumWithSelectedValue_TorqueConverterLockupRule,
    )
    from .degree_of_freedom import EnumWithSelectedValue_DegreeOfFreedom
    from .destination_design_state import EnumWithSelectedValue_DestinationDesignState
else:
    import_structure = {
        "shaft_rating_method": ["EnumWithSelectedValue_ShaftRatingMethod"],
        "surface_finishes": ["EnumWithSelectedValue_SurfaceFinishes"],
        "integration_method": ["EnumWithSelectedValue_IntegrationMethod"],
        "value_input_option": ["EnumWithSelectedValue_ValueInputOption"],
        "single_point_selection_method": [
            "EnumWithSelectedValue_SinglePointSelectionMethod"
        ],
        "result_options_for_3d_vector": [
            "EnumWithSelectedValue_ResultOptionsFor3DVector"
        ],
        "elmer_result_type": ["EnumWithSelectedValue_ElmerResultType"],
        "mode_input_type": ["EnumWithSelectedValue_ModeInputType"],
        "material_property_class": ["EnumWithSelectedValue_MaterialPropertyClass"],
        "lubricant_definition": ["EnumWithSelectedValue_LubricantDefinition"],
        "lubricant_viscosity_class_iso": [
            "EnumWithSelectedValue_LubricantViscosityClassISO"
        ],
        "micro_geometry_model": ["EnumWithSelectedValue_MicroGeometryModel"],
        "extrapolation_options": ["EnumWithSelectedValue_ExtrapolationOptions"],
        "cylindrical_gear_rating_methods": [
            "EnumWithSelectedValue_CylindricalGearRatingMethods"
        ],
        "scuffing_flash_temperature_rating_method": [
            "EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod"
        ],
        "scuffing_integral_temperature_rating_method": [
            "EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod"
        ],
        "location_of_evaluation_lower_limit": [
            "EnumWithSelectedValue_LocationOfEvaluationLowerLimit"
        ],
        "location_of_evaluation_upper_limit": [
            "EnumWithSelectedValue_LocationOfEvaluationUpperLimit"
        ],
        "location_of_root_relief_evaluation": [
            "EnumWithSelectedValue_LocationOfRootReliefEvaluation"
        ],
        "location_of_tip_relief_evaluation": [
            "EnumWithSelectedValue_LocationOfTipReliefEvaluation"
        ],
        "cylindrical_mft_finishing_methods": [
            "EnumWithSelectedValue_CylindricalMftFinishingMethods"
        ],
        "cylindrical_mft_roughing_methods": [
            "EnumWithSelectedValue_CylindricalMftRoughingMethods"
        ],
        "micro_geometry_definition_method": [
            "EnumWithSelectedValue_MicroGeometryDefinitionMethod"
        ],
        "micro_geometry_definition_type": [
            "EnumWithSelectedValue_MicroGeometryDefinitionType"
        ],
        "chart_type": ["EnumWithSelectedValue_ChartType"],
        "flank": ["EnumWithSelectedValue_Flank"],
        "active_process_method": ["EnumWithSelectedValue_ActiveProcessMethod"],
        "cutter_flank_sections": ["EnumWithSelectedValue_CutterFlankSections"],
        "basic_curve_types": ["EnumWithSelectedValue_BasicCurveTypes"],
        "thickness_type": ["EnumWithSelectedValue_ThicknessType"],
        "conical_machine_setting_calculation_methods": [
            "EnumWithSelectedValue_ConicalMachineSettingCalculationMethods"
        ],
        "conical_manufacture_methods": [
            "EnumWithSelectedValue_ConicalManufactureMethods"
        ],
        "candidate_display_choice": ["EnumWithSelectedValue_CandidateDisplayChoice"],
        "severity": ["EnumWithSelectedValue_Severity"],
        "geometry_specification_type": [
            "EnumWithSelectedValue_GeometrySpecificationType"
        ],
        "status_item_severity": ["EnumWithSelectedValue_StatusItemSeverity"],
        "lubrication_methods": ["EnumWithSelectedValue_LubricationMethods"],
        "micropitting_coefficient_of_friction_calculation_method": [
            "EnumWithSelectedValue_MicropittingCoefficientOfFrictionCalculationMethod"
        ],
        "scuffing_coefficient_of_friction_methods": [
            "EnumWithSelectedValue_ScuffingCoefficientOfFrictionMethods"
        ],
        "residual_stress_calculation_method": [
            "EnumWithSelectedValue_ResidualStressCalculationMethod"
        ],
        "contact_result_type": ["EnumWithSelectedValue_ContactResultType"],
        "stress_results_type": ["EnumWithSelectedValue_StressResultsType"],
        "derived_parameter_option": [
            "EnumWithSelectedValue_CylindricalGearPairCreationOptions_DerivedParameterOption"
        ],
        "tooth_thickness_specification_method": [
            "EnumWithSelectedValue_ToothThicknessSpecificationMethod"
        ],
        "load_distribution_factor_methods": [
            "EnumWithSelectedValue_LoadDistributionFactorMethods"
        ],
        "agma_gleason_conical_gear_geometry_methods": [
            "EnumWithSelectedValue_AGMAGleasonConicalGearGeometryMethods"
        ],
        "pro_solve_mpc_type": ["EnumWithSelectedValue_ProSolveMpcType"],
        "pro_solve_solver_type": ["EnumWithSelectedValue_ProSolveSolverType"],
        "coil_position_in_slot": ["EnumWithSelectedValue_CoilPositionInSlot"],
        "electric_machine_analysis_period": [
            "EnumWithSelectedValue_ElectricMachineAnalysisPeriod"
        ],
        "specify_torque_or_current": ["EnumWithSelectedValue_SpecifyTorqueOrCurrent"],
        "load_case_type": ["EnumWithSelectedValue_LoadCaseType"],
        "harmonic_load_data_type": ["EnumWithSelectedValue_HarmonicLoadDataType"],
        "force_display_option": ["EnumWithSelectedValue_ForceDisplayOption"],
        "it_designation": ["EnumWithSelectedValue_ITDesignation"],
        "dudley_effective_length_approximation_option": [
            "EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption"
        ],
        "spline_rating_types": ["EnumWithSelectedValue_SplineRatingTypes"],
        "modules": ["EnumWithSelectedValue_Modules"],
        "pressure_angle_types": ["EnumWithSelectedValue_PressureAngleTypes"],
        "spline_fit_class_type": ["EnumWithSelectedValue_SplineFitClassType"],
        "spline_tolerance_class_types": [
            "EnumWithSelectedValue_SplineToleranceClassTypes"
        ],
        "table_4_joint_interface_types": [
            "EnumWithSelectedValue_Table4JointInterfaceTypes"
        ],
        "dynamics_response_scaling": ["EnumWithSelectedValue_DynamicsResponseScaling"],
        "cad_page_orientation": ["EnumWithSelectedValue_CadPageOrientation"],
        "fluid_film_temperature_options": [
            "EnumWithSelectedValue_FluidFilmTemperatureOptions"
        ],
        "support_tolerance_location_designation": [
            "EnumWithSelectedValue_SupportToleranceLocationDesignation"
        ],
        "loaded_ball_element_property_type": [
            "EnumWithSelectedValue_LoadedBallElementPropertyType"
        ],
        "roller_bearing_profile_types": [
            "EnumWithSelectedValue_RollerBearingProfileTypes"
        ],
        "rolling_bearing_arrangement": [
            "EnumWithSelectedValue_RollingBearingArrangement"
        ],
        "basic_dynamic_load_rating_calculation_method": [
            "EnumWithSelectedValue_BasicDynamicLoadRatingCalculationMethod"
        ],
        "basic_static_load_rating_calculation_method": [
            "EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod"
        ],
        "fatigue_load_limit_calculation_method_enum": [
            "EnumWithSelectedValue_FatigueLoadLimitCalculationMethodEnum"
        ],
        "rolling_bearing_race_type": ["EnumWithSelectedValue_RollingBearingRaceType"],
        "rotational_directions": ["EnumWithSelectedValue_RotationalDirections"],
        "bearing_efficiency_rating_method": [
            "EnumWithSelectedValue_BearingEfficiencyRatingMethod"
        ],
        "shaft_diameter_modification_due_to_rolling_bearing_ring": [
            "EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing"
        ],
        "excitation_analysis_view_option": [
            "EnumWithSelectedValue_ExcitationAnalysisViewOption"
        ],
        "three_d_view_contour_option_first_selection": [
            "EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection"
        ],
        "three_d_view_contour_option_second_selection": [
            "EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection"
        ],
        "component_orientation_option": [
            "EnumWithSelectedValue_ComponentOrientationOption"
        ],
        "axis": ["EnumWithSelectedValue_Axis"],
        "alignment_axis": ["EnumWithSelectedValue_AlignmentAxis"],
        "design_entity_id": ["EnumWithSelectedValue_DesignEntityId"],
        "thermal_expansion_option": ["EnumWithSelectedValue_ThermalExpansionOption"],
        "fe_substructure_type": ["EnumWithSelectedValue_FESubstructureType"],
        "fe_substructuring_file_format": [
            "EnumWithSelectedValue_FESubstructuringFileFormat"
        ],
        "three_d_view_contour_option": [
            "EnumWithSelectedValue_ThreeDViewContourOption"
        ],
        "boundary_condition_type": ["EnumWithSelectedValue_BoundaryConditionType"],
        "fe_export_format": ["EnumWithSelectedValue_FEExportFormat"],
        "bearing_node_option": ["EnumWithSelectedValue_BearingNodeOption"],
        "link_node_source": ["EnumWithSelectedValue_LinkNodeSource"],
        "bearing_tolerance_class": ["EnumWithSelectedValue_BearingToleranceClass"],
        "bearing_model": ["EnumWithSelectedValue_BearingModel"],
        "preload_type": ["EnumWithSelectedValue_PreloadType"],
        "race_axial_mounting_type": ["EnumWithSelectedValue_RaceAxialMountingType"],
        "race_radial_mounting_type": ["EnumWithSelectedValue_RaceRadialMountingType"],
        "internal_clearance_class": ["EnumWithSelectedValue_InternalClearanceClass"],
        "bearing_tolerance_definition_options": [
            "EnumWithSelectedValue_BearingToleranceDefinitionOptions"
        ],
        "oil_seal_loss_calculation_method": [
            "EnumWithSelectedValue_OilSealLossCalculationMethod"
        ],
        "power_load_type": ["EnumWithSelectedValue_PowerLoadType"],
        "rigid_connector_stiffness_type": [
            "EnumWithSelectedValue_RigidConnectorStiffnessType"
        ],
        "rigid_connector_tooth_spacing_type": [
            "EnumWithSelectedValue_RigidConnectorToothSpacingType"
        ],
        "rigid_connector_types": ["EnumWithSelectedValue_RigidConnectorTypes"],
        "fit_types": ["EnumWithSelectedValue_FitTypes"],
        "doe_value_specification_option": [
            "EnumWithSelectedValue_DoeValueSpecificationOption"
        ],
        "analysis_type": ["EnumWithSelectedValue_AnalysisType"],
        "bar_model_export_type": ["EnumWithSelectedValue_BarModelExportType"],
        "dynamics_response_3d_chart_type": [
            "EnumWithSelectedValue_DynamicsResponse3DChartType"
        ],
        "complex_part_display_option": [
            "EnumWithSelectedValue_ComplexPartDisplayOption"
        ],
        "dynamics_response_type": ["EnumWithSelectedValue_DynamicsResponseType"],
        "bearing_stiffness_model": ["EnumWithSelectedValue_BearingStiffnessModel"],
        "gear_mesh_stiffness_model": ["EnumWithSelectedValue_GearMeshStiffnessModel"],
        "shaft_and_housing_flexibility_option": [
            "EnumWithSelectedValue_ShaftAndHousingFlexibilityOption"
        ],
        "export_output_type": ["EnumWithSelectedValue_ExportOutputType"],
        "complex_number_output": [
            "EnumWithSelectedValue_HarmonicAnalysisFEExportOptions_ComplexNumberOutput"
        ],
        "step_creation": [
            "EnumWithSelectedValue_StiffnessOptionsForHarmonicAnalysis_StepCreation"
        ],
        "harmonic_analysis_torque_input_type": [
            "EnumWithSelectedValue_HarmonicAnalysisTorqueInputType"
        ],
        "friction_model_for_gyroscopic_moment": [
            "EnumWithSelectedValue_FrictionModelForGyroscopicMoment"
        ],
        "mesh_stiffness_model": ["EnumWithSelectedValue_MeshStiffnessModel"],
        "shear_area_factor_method": ["EnumWithSelectedValue_ShearAreaFactorMethod"],
        "stress_concentration_method": [
            "EnumWithSelectedValue_StressConcentrationMethod"
        ],
        "ball_bearing_analysis_method": [
            "EnumWithSelectedValue_BallBearingAnalysisMethod"
        ],
        "hertzian_contact_deflection_calculation_method": [
            "EnumWithSelectedValue_HertzianContactDeflectionCalculationMethod"
        ],
        "torque_ripple_input_type": ["EnumWithSelectedValue_TorqueRippleInputType"],
        "harmonic_excitation_type": ["EnumWithSelectedValue_HarmonicExcitationType"],
        "force_specification": [
            "EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification"
        ],
        "torque_specification_for_system_deflection": [
            "EnumWithSelectedValue_TorqueSpecificationForSystemDeflection"
        ],
        "power_load_input_torque_specification_method": [
            "EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod"
        ],
        "torque_converter_lockup_rule": [
            "EnumWithSelectedValue_TorqueConverterLockupRule"
        ],
        "degree_of_freedom": ["EnumWithSelectedValue_DegreeOfFreedom"],
        "destination_design_state": ["EnumWithSelectedValue_DestinationDesignState"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "EnumWithSelectedValue_ShaftRatingMethod",
    "EnumWithSelectedValue_SurfaceFinishes",
    "EnumWithSelectedValue_IntegrationMethod",
    "EnumWithSelectedValue_ValueInputOption",
    "EnumWithSelectedValue_SinglePointSelectionMethod",
    "EnumWithSelectedValue_ResultOptionsFor3DVector",
    "EnumWithSelectedValue_ElmerResultType",
    "EnumWithSelectedValue_ModeInputType",
    "EnumWithSelectedValue_MaterialPropertyClass",
    "EnumWithSelectedValue_LubricantDefinition",
    "EnumWithSelectedValue_LubricantViscosityClassISO",
    "EnumWithSelectedValue_MicroGeometryModel",
    "EnumWithSelectedValue_ExtrapolationOptions",
    "EnumWithSelectedValue_CylindricalGearRatingMethods",
    "EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod",
    "EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod",
    "EnumWithSelectedValue_LocationOfEvaluationLowerLimit",
    "EnumWithSelectedValue_LocationOfEvaluationUpperLimit",
    "EnumWithSelectedValue_LocationOfRootReliefEvaluation",
    "EnumWithSelectedValue_LocationOfTipReliefEvaluation",
    "EnumWithSelectedValue_CylindricalMftFinishingMethods",
    "EnumWithSelectedValue_CylindricalMftRoughingMethods",
    "EnumWithSelectedValue_MicroGeometryDefinitionMethod",
    "EnumWithSelectedValue_MicroGeometryDefinitionType",
    "EnumWithSelectedValue_ChartType",
    "EnumWithSelectedValue_Flank",
    "EnumWithSelectedValue_ActiveProcessMethod",
    "EnumWithSelectedValue_CutterFlankSections",
    "EnumWithSelectedValue_BasicCurveTypes",
    "EnumWithSelectedValue_ThicknessType",
    "EnumWithSelectedValue_ConicalMachineSettingCalculationMethods",
    "EnumWithSelectedValue_ConicalManufactureMethods",
    "EnumWithSelectedValue_CandidateDisplayChoice",
    "EnumWithSelectedValue_Severity",
    "EnumWithSelectedValue_GeometrySpecificationType",
    "EnumWithSelectedValue_StatusItemSeverity",
    "EnumWithSelectedValue_LubricationMethods",
    "EnumWithSelectedValue_MicropittingCoefficientOfFrictionCalculationMethod",
    "EnumWithSelectedValue_ScuffingCoefficientOfFrictionMethods",
    "EnumWithSelectedValue_ResidualStressCalculationMethod",
    "EnumWithSelectedValue_ContactResultType",
    "EnumWithSelectedValue_StressResultsType",
    "EnumWithSelectedValue_CylindricalGearPairCreationOptions_DerivedParameterOption",
    "EnumWithSelectedValue_ToothThicknessSpecificationMethod",
    "EnumWithSelectedValue_LoadDistributionFactorMethods",
    "EnumWithSelectedValue_AGMAGleasonConicalGearGeometryMethods",
    "EnumWithSelectedValue_ProSolveMpcType",
    "EnumWithSelectedValue_ProSolveSolverType",
    "EnumWithSelectedValue_CoilPositionInSlot",
    "EnumWithSelectedValue_ElectricMachineAnalysisPeriod",
    "EnumWithSelectedValue_SpecifyTorqueOrCurrent",
    "EnumWithSelectedValue_LoadCaseType",
    "EnumWithSelectedValue_HarmonicLoadDataType",
    "EnumWithSelectedValue_ForceDisplayOption",
    "EnumWithSelectedValue_ITDesignation",
    "EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption",
    "EnumWithSelectedValue_SplineRatingTypes",
    "EnumWithSelectedValue_Modules",
    "EnumWithSelectedValue_PressureAngleTypes",
    "EnumWithSelectedValue_SplineFitClassType",
    "EnumWithSelectedValue_SplineToleranceClassTypes",
    "EnumWithSelectedValue_Table4JointInterfaceTypes",
    "EnumWithSelectedValue_DynamicsResponseScaling",
    "EnumWithSelectedValue_CadPageOrientation",
    "EnumWithSelectedValue_FluidFilmTemperatureOptions",
    "EnumWithSelectedValue_SupportToleranceLocationDesignation",
    "EnumWithSelectedValue_LoadedBallElementPropertyType",
    "EnumWithSelectedValue_RollerBearingProfileTypes",
    "EnumWithSelectedValue_RollingBearingArrangement",
    "EnumWithSelectedValue_BasicDynamicLoadRatingCalculationMethod",
    "EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod",
    "EnumWithSelectedValue_FatigueLoadLimitCalculationMethodEnum",
    "EnumWithSelectedValue_RollingBearingRaceType",
    "EnumWithSelectedValue_RotationalDirections",
    "EnumWithSelectedValue_BearingEfficiencyRatingMethod",
    "EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing",
    "EnumWithSelectedValue_ExcitationAnalysisViewOption",
    "EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection",
    "EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection",
    "EnumWithSelectedValue_ComponentOrientationOption",
    "EnumWithSelectedValue_Axis",
    "EnumWithSelectedValue_AlignmentAxis",
    "EnumWithSelectedValue_DesignEntityId",
    "EnumWithSelectedValue_ThermalExpansionOption",
    "EnumWithSelectedValue_FESubstructureType",
    "EnumWithSelectedValue_FESubstructuringFileFormat",
    "EnumWithSelectedValue_ThreeDViewContourOption",
    "EnumWithSelectedValue_BoundaryConditionType",
    "EnumWithSelectedValue_FEExportFormat",
    "EnumWithSelectedValue_BearingNodeOption",
    "EnumWithSelectedValue_LinkNodeSource",
    "EnumWithSelectedValue_BearingToleranceClass",
    "EnumWithSelectedValue_BearingModel",
    "EnumWithSelectedValue_PreloadType",
    "EnumWithSelectedValue_RaceAxialMountingType",
    "EnumWithSelectedValue_RaceRadialMountingType",
    "EnumWithSelectedValue_InternalClearanceClass",
    "EnumWithSelectedValue_BearingToleranceDefinitionOptions",
    "EnumWithSelectedValue_OilSealLossCalculationMethod",
    "EnumWithSelectedValue_PowerLoadType",
    "EnumWithSelectedValue_RigidConnectorStiffnessType",
    "EnumWithSelectedValue_RigidConnectorToothSpacingType",
    "EnumWithSelectedValue_RigidConnectorTypes",
    "EnumWithSelectedValue_FitTypes",
    "EnumWithSelectedValue_DoeValueSpecificationOption",
    "EnumWithSelectedValue_AnalysisType",
    "EnumWithSelectedValue_BarModelExportType",
    "EnumWithSelectedValue_DynamicsResponse3DChartType",
    "EnumWithSelectedValue_ComplexPartDisplayOption",
    "EnumWithSelectedValue_DynamicsResponseType",
    "EnumWithSelectedValue_BearingStiffnessModel",
    "EnumWithSelectedValue_GearMeshStiffnessModel",
    "EnumWithSelectedValue_ShaftAndHousingFlexibilityOption",
    "EnumWithSelectedValue_ExportOutputType",
    "EnumWithSelectedValue_HarmonicAnalysisFEExportOptions_ComplexNumberOutput",
    "EnumWithSelectedValue_StiffnessOptionsForHarmonicAnalysis_StepCreation",
    "EnumWithSelectedValue_HarmonicAnalysisTorqueInputType",
    "EnumWithSelectedValue_FrictionModelForGyroscopicMoment",
    "EnumWithSelectedValue_MeshStiffnessModel",
    "EnumWithSelectedValue_ShearAreaFactorMethod",
    "EnumWithSelectedValue_StressConcentrationMethod",
    "EnumWithSelectedValue_BallBearingAnalysisMethod",
    "EnumWithSelectedValue_HertzianContactDeflectionCalculationMethod",
    "EnumWithSelectedValue_TorqueRippleInputType",
    "EnumWithSelectedValue_HarmonicExcitationType",
    "EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification",
    "EnumWithSelectedValue_TorqueSpecificationForSystemDeflection",
    "EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod",
    "EnumWithSelectedValue_TorqueConverterLockupRule",
    "EnumWithSelectedValue_DegreeOfFreedom",
    "EnumWithSelectedValue_DestinationDesignState",
)
