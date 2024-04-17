"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from .float import Overridable_float
    from .int import Overridable_int
    from .iso_tolerance_standard import Overridable_ISOToleranceStandard
    from .cylindrical_gear_rating_methods import (
        Overridable_CylindricalGearRatingMethods,
    )
    from .coefficient_of_friction_calculation_method import (
        Overridable_CoefficientOfFrictionCalculationMethod,
    )
    from .bool import Overridable_bool
    from .dq_axis_convention import Overridable_DQAxisConvention
    from .t import Overridable_T
    from .diameter_series import Overridable_DiameterSeries
    from .height_series import Overridable_HeightSeries
    from .width_series import Overridable_WidthSeries
    from .seal_location import Overridable_SealLocation
    from .rigid_coupling_type import Overridable_RigidCouplingType
    from .boundary_condition_type import Overridable_BoundaryConditionType
    from .node_selection_depth_option import Overridable_NodeSelectionDepthOption
    from .bearing_efficiency_rating_method import (
        Overridable_BearingEfficiencyRatingMethod,
    )
    from .cylindrical_roller_max_axial_load_method import (
        Overridable_CylindricalRollerMaxAxialLoadMethod,
    )
    from .contact_ratio_requirements import Overridable_ContactRatioRequirements
    from .micro_geometry_model import Overridable_MicroGeometryModel
    from .unbalanced_mass_inclusion_option import (
        Overridable_UnbalancedMassInclusionOption,
    )
    from .ball_bearing_contact_calculation import (
        Overridable_BallBearingContactCalculation,
    )
    from .friction_model_for_gyroscopic_moment import (
        Overridable_FrictionModelForGyroscopicMoment,
    )
    from .bearing_f0_input_method import Overridable_BearingF0InputMethod
    from .roller_analysis_method import Overridable_RollerAnalysisMethod
    from .helical_gear_micro_geometry_option import (
        Overridable_HelicalGearMicroGeometryOption,
    )
    from .efficiency_rating_method import Overridable_EfficiencyRatingMethod
    from .mesh_stiffness_source import Overridable_MeshStiffnessSource
else:
    import_structure = {
        "float": ["Overridable_float"],
        "int": ["Overridable_int"],
        "iso_tolerance_standard": ["Overridable_ISOToleranceStandard"],
        "cylindrical_gear_rating_methods": ["Overridable_CylindricalGearRatingMethods"],
        "coefficient_of_friction_calculation_method": [
            "Overridable_CoefficientOfFrictionCalculationMethod"
        ],
        "bool": ["Overridable_bool"],
        "dq_axis_convention": ["Overridable_DQAxisConvention"],
        "t": ["Overridable_T"],
        "diameter_series": ["Overridable_DiameterSeries"],
        "height_series": ["Overridable_HeightSeries"],
        "width_series": ["Overridable_WidthSeries"],
        "seal_location": ["Overridable_SealLocation"],
        "rigid_coupling_type": ["Overridable_RigidCouplingType"],
        "boundary_condition_type": ["Overridable_BoundaryConditionType"],
        "node_selection_depth_option": ["Overridable_NodeSelectionDepthOption"],
        "bearing_efficiency_rating_method": [
            "Overridable_BearingEfficiencyRatingMethod"
        ],
        "cylindrical_roller_max_axial_load_method": [
            "Overridable_CylindricalRollerMaxAxialLoadMethod"
        ],
        "contact_ratio_requirements": ["Overridable_ContactRatioRequirements"],
        "micro_geometry_model": ["Overridable_MicroGeometryModel"],
        "unbalanced_mass_inclusion_option": [
            "Overridable_UnbalancedMassInclusionOption"
        ],
        "ball_bearing_contact_calculation": [
            "Overridable_BallBearingContactCalculation"
        ],
        "friction_model_for_gyroscopic_moment": [
            "Overridable_FrictionModelForGyroscopicMoment"
        ],
        "bearing_f0_input_method": ["Overridable_BearingF0InputMethod"],
        "roller_analysis_method": ["Overridable_RollerAnalysisMethod"],
        "helical_gear_micro_geometry_option": [
            "Overridable_HelicalGearMicroGeometryOption"
        ],
        "efficiency_rating_method": ["Overridable_EfficiencyRatingMethod"],
        "mesh_stiffness_source": ["Overridable_MeshStiffnessSource"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Overridable_float",
    "Overridable_int",
    "Overridable_ISOToleranceStandard",
    "Overridable_CylindricalGearRatingMethods",
    "Overridable_CoefficientOfFrictionCalculationMethod",
    "Overridable_bool",
    "Overridable_DQAxisConvention",
    "Overridable_T",
    "Overridable_DiameterSeries",
    "Overridable_HeightSeries",
    "Overridable_WidthSeries",
    "Overridable_SealLocation",
    "Overridable_RigidCouplingType",
    "Overridable_BoundaryConditionType",
    "Overridable_NodeSelectionDepthOption",
    "Overridable_BearingEfficiencyRatingMethod",
    "Overridable_CylindricalRollerMaxAxialLoadMethod",
    "Overridable_ContactRatioRequirements",
    "Overridable_MicroGeometryModel",
    "Overridable_UnbalancedMassInclusionOption",
    "Overridable_BallBearingContactCalculation",
    "Overridable_FrictionModelForGyroscopicMoment",
    "Overridable_BearingF0InputMethod",
    "Overridable_RollerAnalysisMethod",
    "Overridable_HelicalGearMicroGeometryOption",
    "Overridable_EfficiencyRatingMethod",
    "Overridable_MeshStiffnessSource",
)
