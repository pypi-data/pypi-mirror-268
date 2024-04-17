"""ComponentParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4401
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ComponentParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2451
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4305,
        _4306,
        _4309,
        _4312,
        _4316,
        _4318,
        _4319,
        _4321,
        _4324,
        _4326,
        _4331,
        _4334,
        _4337,
        _4340,
        _4342,
        _4346,
        _4349,
        _4352,
        _4354,
        _4355,
        _4363,
        _4365,
        _4367,
        _4370,
        _4372,
        _4374,
        _4378,
        _4381,
        _4384,
        _4386,
        _4387,
        _4389,
        _4390,
        _4403,
        _4407,
        _4408,
        _4409,
        _4410,
        _4411,
        _4415,
        _4417,
        _4418,
        _4422,
        _4425,
        _4428,
        _4431,
        _4433,
        _4434,
        _4435,
        _4437,
        _4438,
        _4441,
        _4442,
        _4443,
        _4444,
        _4446,
        _4449,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ComponentParametricStudyTool",)


Self = TypeVar("Self", bound="ComponentParametricStudyTool")


class ComponentParametricStudyTool(_4401.PartParametricStudyTool):
    """ComponentParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COMPONENT_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentParametricStudyTool")

    class _Cast_ComponentParametricStudyTool:
        """Special nested class for casting ComponentParametricStudyTool to subclasses."""

        def __init__(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
            parent: "ComponentParametricStudyTool",
        ):
            self._parent = parent

        @property
        def part_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4401.PartParametricStudyTool":
            return self._parent._cast(_4401.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_or_housing_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4305.AbstractShaftOrHousingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4305,
            )

            return self._parent._cast(_4305.AbstractShaftOrHousingParametricStudyTool)

        @property
        def abstract_shaft_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4306.AbstractShaftParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4306,
            )

            return self._parent._cast(_4306.AbstractShaftParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4309.AGMAGleasonConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4309,
            )

            return self._parent._cast(_4309.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def bearing_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4312.BearingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4312,
            )

            return self._parent._cast(_4312.BearingParametricStudyTool)

        @property
        def bevel_differential_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4316.BevelDifferentialGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4316,
            )

            return self._parent._cast(_4316.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_differential_planet_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4318.BevelDifferentialPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4318,
            )

            return self._parent._cast(
                _4318.BevelDifferentialPlanetGearParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4319.BevelDifferentialSunGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4319,
            )

            return self._parent._cast(_4319.BevelDifferentialSunGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4321.BevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4321,
            )

            return self._parent._cast(_4321.BevelGearParametricStudyTool)

        @property
        def bolt_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4324.BoltParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4324,
            )

            return self._parent._cast(_4324.BoltParametricStudyTool)

        @property
        def clutch_half_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4326.ClutchHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4326,
            )

            return self._parent._cast(_4326.ClutchHalfParametricStudyTool)

        @property
        def concept_coupling_half_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4331.ConceptCouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4331,
            )

            return self._parent._cast(_4331.ConceptCouplingHalfParametricStudyTool)

        @property
        def concept_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4334.ConceptGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4334,
            )

            return self._parent._cast(_4334.ConceptGearParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4337.ConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4337,
            )

            return self._parent._cast(_4337.ConicalGearParametricStudyTool)

        @property
        def connector_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4340.ConnectorParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4340,
            )

            return self._parent._cast(_4340.ConnectorParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4342.CouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4342,
            )

            return self._parent._cast(_4342.CouplingHalfParametricStudyTool)

        @property
        def cvt_pulley_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4346.CVTPulleyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4346,
            )

            return self._parent._cast(_4346.CVTPulleyParametricStudyTool)

        @property
        def cycloidal_disc_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4349.CycloidalDiscParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4349,
            )

            return self._parent._cast(_4349.CycloidalDiscParametricStudyTool)

        @property
        def cylindrical_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4352.CylindricalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4352,
            )

            return self._parent._cast(_4352.CylindricalGearParametricStudyTool)

        @property
        def cylindrical_planet_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4354.CylindricalPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4354,
            )

            return self._parent._cast(_4354.CylindricalPlanetGearParametricStudyTool)

        @property
        def datum_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4355.DatumParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4355,
            )

            return self._parent._cast(_4355.DatumParametricStudyTool)

        @property
        def external_cad_model_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4363.ExternalCADModelParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4363,
            )

            return self._parent._cast(_4363.ExternalCADModelParametricStudyTool)

        @property
        def face_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4365.FaceGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4365,
            )

            return self._parent._cast(_4365.FaceGearParametricStudyTool)

        @property
        def fe_part_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4367.FEPartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4367,
            )

            return self._parent._cast(_4367.FEPartParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4370.GearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4370,
            )

            return self._parent._cast(_4370.GearParametricStudyTool)

        @property
        def guide_dxf_model_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4372.GuideDxfModelParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4372,
            )

            return self._parent._cast(_4372.GuideDxfModelParametricStudyTool)

        @property
        def hypoid_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4374.HypoidGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4374,
            )

            return self._parent._cast(_4374.HypoidGearParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4378.KlingelnbergCycloPalloidConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4378,
            )

            return self._parent._cast(
                _4378.KlingelnbergCycloPalloidConicalGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4381.KlingelnbergCycloPalloidHypoidGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4381,
            )

            return self._parent._cast(
                _4381.KlingelnbergCycloPalloidHypoidGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4384.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4384,
            )

            return self._parent._cast(
                _4384.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
            )

        @property
        def mass_disc_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4386.MassDiscParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4386,
            )

            return self._parent._cast(_4386.MassDiscParametricStudyTool)

        @property
        def measurement_component_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4387.MeasurementComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4387,
            )

            return self._parent._cast(_4387.MeasurementComponentParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4389.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4389,
            )

            return self._parent._cast(_4389.MountableComponentParametricStudyTool)

        @property
        def oil_seal_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4390.OilSealParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4390,
            )

            return self._parent._cast(_4390.OilSealParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4403.PartToPartShearCouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4403,
            )

            return self._parent._cast(
                _4403.PartToPartShearCouplingHalfParametricStudyTool
            )

        @property
        def planet_carrier_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4407.PlanetCarrierParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4407,
            )

            return self._parent._cast(_4407.PlanetCarrierParametricStudyTool)

        @property
        def point_load_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4408.PointLoadParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4408,
            )

            return self._parent._cast(_4408.PointLoadParametricStudyTool)

        @property
        def power_load_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4409.PowerLoadParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4409,
            )

            return self._parent._cast(_4409.PowerLoadParametricStudyTool)

        @property
        def pulley_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4410.PulleyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4410,
            )

            return self._parent._cast(_4410.PulleyParametricStudyTool)

        @property
        def ring_pins_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4411.RingPinsParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4411,
            )

            return self._parent._cast(_4411.RingPinsParametricStudyTool)

        @property
        def rolling_ring_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4415.RollingRingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4415,
            )

            return self._parent._cast(_4415.RollingRingParametricStudyTool)

        @property
        def shaft_hub_connection_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4417.ShaftHubConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4417,
            )

            return self._parent._cast(_4417.ShaftHubConnectionParametricStudyTool)

        @property
        def shaft_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4418.ShaftParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4418,
            )

            return self._parent._cast(_4418.ShaftParametricStudyTool)

        @property
        def spiral_bevel_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4422.SpiralBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4422,
            )

            return self._parent._cast(_4422.SpiralBevelGearParametricStudyTool)

        @property
        def spring_damper_half_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4425.SpringDamperHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4425,
            )

            return self._parent._cast(_4425.SpringDamperHalfParametricStudyTool)

        @property
        def straight_bevel_diff_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4428.StraightBevelDiffGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4428,
            )

            return self._parent._cast(_4428.StraightBevelDiffGearParametricStudyTool)

        @property
        def straight_bevel_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4431.StraightBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4431,
            )

            return self._parent._cast(_4431.StraightBevelGearParametricStudyTool)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4433.StraightBevelPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4433,
            )

            return self._parent._cast(_4433.StraightBevelPlanetGearParametricStudyTool)

        @property
        def straight_bevel_sun_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4434.StraightBevelSunGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4434,
            )

            return self._parent._cast(_4434.StraightBevelSunGearParametricStudyTool)

        @property
        def synchroniser_half_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4435.SynchroniserHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4435,
            )

            return self._parent._cast(_4435.SynchroniserHalfParametricStudyTool)

        @property
        def synchroniser_part_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4437.SynchroniserPartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4437,
            )

            return self._parent._cast(_4437.SynchroniserPartParametricStudyTool)

        @property
        def synchroniser_sleeve_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4438.SynchroniserSleeveParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4438,
            )

            return self._parent._cast(_4438.SynchroniserSleeveParametricStudyTool)

        @property
        def torque_converter_pump_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4441.TorqueConverterPumpParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4441,
            )

            return self._parent._cast(_4441.TorqueConverterPumpParametricStudyTool)

        @property
        def torque_converter_turbine_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4442.TorqueConverterTurbineParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4442,
            )

            return self._parent._cast(_4442.TorqueConverterTurbineParametricStudyTool)

        @property
        def unbalanced_mass_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4443.UnbalancedMassParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4443,
            )

            return self._parent._cast(_4443.UnbalancedMassParametricStudyTool)

        @property
        def virtual_component_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4444.VirtualComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4444,
            )

            return self._parent._cast(_4444.VirtualComponentParametricStudyTool)

        @property
        def worm_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4446.WormGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4446,
            )

            return self._parent._cast(_4446.WormGearParametricStudyTool)

        @property
        def zerol_bevel_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4449.ZerolBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4449,
            )

            return self._parent._cast(_4449.ZerolBevelGearParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "ComponentParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2451.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool":
        return self._Cast_ComponentParametricStudyTool(self)
