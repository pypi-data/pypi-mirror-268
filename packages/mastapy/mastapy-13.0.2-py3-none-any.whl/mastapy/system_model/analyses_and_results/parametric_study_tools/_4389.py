"""MountableComponentParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4329
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "MountableComponentParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4309,
        _4312,
        _4316,
        _4318,
        _4319,
        _4321,
        _4326,
        _4331,
        _4334,
        _4337,
        _4340,
        _4342,
        _4346,
        _4352,
        _4354,
        _4365,
        _4370,
        _4374,
        _4378,
        _4381,
        _4384,
        _4386,
        _4387,
        _4390,
        _4403,
        _4407,
        _4408,
        _4409,
        _4410,
        _4411,
        _4415,
        _4417,
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
        _4401,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentParametricStudyTool",)


Self = TypeVar("Self", bound="MountableComponentParametricStudyTool")


class MountableComponentParametricStudyTool(_4329.ComponentParametricStudyTool):
    """MountableComponentParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentParametricStudyTool"
    )

    class _Cast_MountableComponentParametricStudyTool:
        """Special nested class for casting MountableComponentParametricStudyTool to subclasses."""

        def __init__(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
            parent: "MountableComponentParametricStudyTool",
        ):
            self._parent = parent

        @property
        def component_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4329.ComponentParametricStudyTool":
            return self._parent._cast(_4329.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4401.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4309.AGMAGleasonConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4309,
            )

            return self._parent._cast(_4309.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def bearing_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4312.BearingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4312,
            )

            return self._parent._cast(_4312.BearingParametricStudyTool)

        @property
        def bevel_differential_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4316.BevelDifferentialGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4316,
            )

            return self._parent._cast(_4316.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_differential_planet_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4318.BevelDifferentialPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4318,
            )

            return self._parent._cast(
                _4318.BevelDifferentialPlanetGearParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4319.BevelDifferentialSunGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4319,
            )

            return self._parent._cast(_4319.BevelDifferentialSunGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4321.BevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4321,
            )

            return self._parent._cast(_4321.BevelGearParametricStudyTool)

        @property
        def clutch_half_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4326.ClutchHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4326,
            )

            return self._parent._cast(_4326.ClutchHalfParametricStudyTool)

        @property
        def concept_coupling_half_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4331.ConceptCouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4331,
            )

            return self._parent._cast(_4331.ConceptCouplingHalfParametricStudyTool)

        @property
        def concept_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4334.ConceptGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4334,
            )

            return self._parent._cast(_4334.ConceptGearParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4337.ConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4337,
            )

            return self._parent._cast(_4337.ConicalGearParametricStudyTool)

        @property
        def connector_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4340.ConnectorParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4340,
            )

            return self._parent._cast(_4340.ConnectorParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4342.CouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4342,
            )

            return self._parent._cast(_4342.CouplingHalfParametricStudyTool)

        @property
        def cvt_pulley_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4346.CVTPulleyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4346,
            )

            return self._parent._cast(_4346.CVTPulleyParametricStudyTool)

        @property
        def cylindrical_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4352.CylindricalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4352,
            )

            return self._parent._cast(_4352.CylindricalGearParametricStudyTool)

        @property
        def cylindrical_planet_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4354.CylindricalPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4354,
            )

            return self._parent._cast(_4354.CylindricalPlanetGearParametricStudyTool)

        @property
        def face_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4365.FaceGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4365,
            )

            return self._parent._cast(_4365.FaceGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4370.GearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4370,
            )

            return self._parent._cast(_4370.GearParametricStudyTool)

        @property
        def hypoid_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4374.HypoidGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4374,
            )

            return self._parent._cast(_4374.HypoidGearParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4378.KlingelnbergCycloPalloidConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4378,
            )

            return self._parent._cast(
                _4378.KlingelnbergCycloPalloidConicalGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4381.KlingelnbergCycloPalloidHypoidGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4381,
            )

            return self._parent._cast(
                _4381.KlingelnbergCycloPalloidHypoidGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4384.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4384,
            )

            return self._parent._cast(
                _4384.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
            )

        @property
        def mass_disc_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4386.MassDiscParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4386,
            )

            return self._parent._cast(_4386.MassDiscParametricStudyTool)

        @property
        def measurement_component_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4387.MeasurementComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4387,
            )

            return self._parent._cast(_4387.MeasurementComponentParametricStudyTool)

        @property
        def oil_seal_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4390.OilSealParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4390,
            )

            return self._parent._cast(_4390.OilSealParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4403.PartToPartShearCouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4403,
            )

            return self._parent._cast(
                _4403.PartToPartShearCouplingHalfParametricStudyTool
            )

        @property
        def planet_carrier_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4407.PlanetCarrierParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4407,
            )

            return self._parent._cast(_4407.PlanetCarrierParametricStudyTool)

        @property
        def point_load_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4408.PointLoadParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4408,
            )

            return self._parent._cast(_4408.PointLoadParametricStudyTool)

        @property
        def power_load_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4409.PowerLoadParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4409,
            )

            return self._parent._cast(_4409.PowerLoadParametricStudyTool)

        @property
        def pulley_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4410.PulleyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4410,
            )

            return self._parent._cast(_4410.PulleyParametricStudyTool)

        @property
        def ring_pins_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4411.RingPinsParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4411,
            )

            return self._parent._cast(_4411.RingPinsParametricStudyTool)

        @property
        def rolling_ring_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4415.RollingRingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4415,
            )

            return self._parent._cast(_4415.RollingRingParametricStudyTool)

        @property
        def shaft_hub_connection_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4417.ShaftHubConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4417,
            )

            return self._parent._cast(_4417.ShaftHubConnectionParametricStudyTool)

        @property
        def spiral_bevel_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4422.SpiralBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4422,
            )

            return self._parent._cast(_4422.SpiralBevelGearParametricStudyTool)

        @property
        def spring_damper_half_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4425.SpringDamperHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4425,
            )

            return self._parent._cast(_4425.SpringDamperHalfParametricStudyTool)

        @property
        def straight_bevel_diff_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4428.StraightBevelDiffGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4428,
            )

            return self._parent._cast(_4428.StraightBevelDiffGearParametricStudyTool)

        @property
        def straight_bevel_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4431.StraightBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4431,
            )

            return self._parent._cast(_4431.StraightBevelGearParametricStudyTool)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4433.StraightBevelPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4433,
            )

            return self._parent._cast(_4433.StraightBevelPlanetGearParametricStudyTool)

        @property
        def straight_bevel_sun_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4434.StraightBevelSunGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4434,
            )

            return self._parent._cast(_4434.StraightBevelSunGearParametricStudyTool)

        @property
        def synchroniser_half_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4435.SynchroniserHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4435,
            )

            return self._parent._cast(_4435.SynchroniserHalfParametricStudyTool)

        @property
        def synchroniser_part_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4437.SynchroniserPartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4437,
            )

            return self._parent._cast(_4437.SynchroniserPartParametricStudyTool)

        @property
        def synchroniser_sleeve_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4438.SynchroniserSleeveParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4438,
            )

            return self._parent._cast(_4438.SynchroniserSleeveParametricStudyTool)

        @property
        def torque_converter_pump_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4441.TorqueConverterPumpParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4441,
            )

            return self._parent._cast(_4441.TorqueConverterPumpParametricStudyTool)

        @property
        def torque_converter_turbine_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4442.TorqueConverterTurbineParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4442,
            )

            return self._parent._cast(_4442.TorqueConverterTurbineParametricStudyTool)

        @property
        def unbalanced_mass_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4443.UnbalancedMassParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4443,
            )

            return self._parent._cast(_4443.UnbalancedMassParametricStudyTool)

        @property
        def virtual_component_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4444.VirtualComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4444,
            )

            return self._parent._cast(_4444.VirtualComponentParametricStudyTool)

        @property
        def worm_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4446.WormGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4446,
            )

            return self._parent._cast(_4446.WormGearParametricStudyTool)

        @property
        def zerol_bevel_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "_4449.ZerolBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4449,
            )

            return self._parent._cast(_4449.ZerolBevelGearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "MountableComponentParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "MountableComponentParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2471.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

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
    ) -> "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool":
        return self._Cast_MountableComponentParametricStudyTool(self)
