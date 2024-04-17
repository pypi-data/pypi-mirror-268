"""ComponentCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4530,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "ComponentCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4329
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4452,
        _4453,
        _4455,
        _4459,
        _4462,
        _4465,
        _4466,
        _4467,
        _4470,
        _4474,
        _4479,
        _4480,
        _4483,
        _4487,
        _4490,
        _4493,
        _4496,
        _4498,
        _4501,
        _4502,
        _4503,
        _4504,
        _4507,
        _4509,
        _4512,
        _4513,
        _4517,
        _4520,
        _4523,
        _4526,
        _4527,
        _4528,
        _4529,
        _4533,
        _4536,
        _4537,
        _4538,
        _4539,
        _4540,
        _4543,
        _4546,
        _4547,
        _4550,
        _4555,
        _4556,
        _4559,
        _4562,
        _4563,
        _4565,
        _4566,
        _4567,
        _4570,
        _4571,
        _4572,
        _4573,
        _4574,
        _4577,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="ComponentCompoundParametricStudyTool")


class ComponentCompoundParametricStudyTool(_4530.PartCompoundParametricStudyTool):
    """ComponentCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentCompoundParametricStudyTool")

    class _Cast_ComponentCompoundParametricStudyTool:
        """Special nested class for casting ComponentCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
            parent: "ComponentCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def part_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4530.PartCompoundParametricStudyTool":
            return self._parent._cast(_4530.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4452.AbstractShaftCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4452,
            )

            return self._parent._cast(_4452.AbstractShaftCompoundParametricStudyTool)

        @property
        def abstract_shaft_or_housing_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4453.AbstractShaftOrHousingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4453,
            )

            return self._parent._cast(
                _4453.AbstractShaftOrHousingCompoundParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4455.AGMAGleasonConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4455,
            )

            return self._parent._cast(
                _4455.AGMAGleasonConicalGearCompoundParametricStudyTool
            )

        @property
        def bearing_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4459.BearingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4459,
            )

            return self._parent._cast(_4459.BearingCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4462.BevelDifferentialGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4462,
            )

            return self._parent._cast(
                _4462.BevelDifferentialGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_planet_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4465.BevelDifferentialPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4465,
            )

            return self._parent._cast(
                _4465.BevelDifferentialPlanetGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4466.BevelDifferentialSunGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4466,
            )

            return self._parent._cast(
                _4466.BevelDifferentialSunGearCompoundParametricStudyTool
            )

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4467.BevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4467,
            )

            return self._parent._cast(_4467.BevelGearCompoundParametricStudyTool)

        @property
        def bolt_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4470.BoltCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4470,
            )

            return self._parent._cast(_4470.BoltCompoundParametricStudyTool)

        @property
        def clutch_half_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4474.ClutchHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4474,
            )

            return self._parent._cast(_4474.ClutchHalfCompoundParametricStudyTool)

        @property
        def concept_coupling_half_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4479.ConceptCouplingHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4479,
            )

            return self._parent._cast(
                _4479.ConceptCouplingHalfCompoundParametricStudyTool
            )

        @property
        def concept_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4480.ConceptGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4480,
            )

            return self._parent._cast(_4480.ConceptGearCompoundParametricStudyTool)

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4483.ConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4483,
            )

            return self._parent._cast(_4483.ConicalGearCompoundParametricStudyTool)

        @property
        def connector_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4487.ConnectorCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4487,
            )

            return self._parent._cast(_4487.ConnectorCompoundParametricStudyTool)

        @property
        def coupling_half_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4490.CouplingHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4490,
            )

            return self._parent._cast(_4490.CouplingHalfCompoundParametricStudyTool)

        @property
        def cvt_pulley_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4493.CVTPulleyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4493,
            )

            return self._parent._cast(_4493.CVTPulleyCompoundParametricStudyTool)

        @property
        def cycloidal_disc_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4496.CycloidalDiscCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4496,
            )

            return self._parent._cast(_4496.CycloidalDiscCompoundParametricStudyTool)

        @property
        def cylindrical_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4498.CylindricalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4498,
            )

            return self._parent._cast(_4498.CylindricalGearCompoundParametricStudyTool)

        @property
        def cylindrical_planet_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4501.CylindricalPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4501,
            )

            return self._parent._cast(
                _4501.CylindricalPlanetGearCompoundParametricStudyTool
            )

        @property
        def datum_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4502.DatumCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4502,
            )

            return self._parent._cast(_4502.DatumCompoundParametricStudyTool)

        @property
        def external_cad_model_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4503.ExternalCADModelCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4503,
            )

            return self._parent._cast(_4503.ExternalCADModelCompoundParametricStudyTool)

        @property
        def face_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4504.FaceGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4504,
            )

            return self._parent._cast(_4504.FaceGearCompoundParametricStudyTool)

        @property
        def fe_part_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4507.FEPartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4507,
            )

            return self._parent._cast(_4507.FEPartCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4509.GearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4509,
            )

            return self._parent._cast(_4509.GearCompoundParametricStudyTool)

        @property
        def guide_dxf_model_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4512.GuideDxfModelCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4512,
            )

            return self._parent._cast(_4512.GuideDxfModelCompoundParametricStudyTool)

        @property
        def hypoid_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4513.HypoidGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4513,
            )

            return self._parent._cast(_4513.HypoidGearCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4517.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4517,
            )

            return self._parent._cast(
                _4517.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4520.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4520,
            )

            return self._parent._cast(
                _4520.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4523.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4523,
            )

            return self._parent._cast(
                _4523.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool
            )

        @property
        def mass_disc_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4526.MassDiscCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4526,
            )

            return self._parent._cast(_4526.MassDiscCompoundParametricStudyTool)

        @property
        def measurement_component_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4527.MeasurementComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4527,
            )

            return self._parent._cast(
                _4527.MeasurementComponentCompoundParametricStudyTool
            )

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4528.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4528,
            )

            return self._parent._cast(
                _4528.MountableComponentCompoundParametricStudyTool
            )

        @property
        def oil_seal_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4529.OilSealCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4529,
            )

            return self._parent._cast(_4529.OilSealCompoundParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4533.PartToPartShearCouplingHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4533,
            )

            return self._parent._cast(
                _4533.PartToPartShearCouplingHalfCompoundParametricStudyTool
            )

        @property
        def planet_carrier_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4536.PlanetCarrierCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4536,
            )

            return self._parent._cast(_4536.PlanetCarrierCompoundParametricStudyTool)

        @property
        def point_load_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4537.PointLoadCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4537,
            )

            return self._parent._cast(_4537.PointLoadCompoundParametricStudyTool)

        @property
        def power_load_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4538.PowerLoadCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4538,
            )

            return self._parent._cast(_4538.PowerLoadCompoundParametricStudyTool)

        @property
        def pulley_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4539.PulleyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4539,
            )

            return self._parent._cast(_4539.PulleyCompoundParametricStudyTool)

        @property
        def ring_pins_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4540.RingPinsCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4540,
            )

            return self._parent._cast(_4540.RingPinsCompoundParametricStudyTool)

        @property
        def rolling_ring_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4543.RollingRingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(_4543.RollingRingCompoundParametricStudyTool)

        @property
        def shaft_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4546.ShaftCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4546,
            )

            return self._parent._cast(_4546.ShaftCompoundParametricStudyTool)

        @property
        def shaft_hub_connection_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4547.ShaftHubConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4547,
            )

            return self._parent._cast(
                _4547.ShaftHubConnectionCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4550.SpiralBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4550,
            )

            return self._parent._cast(_4550.SpiralBevelGearCompoundParametricStudyTool)

        @property
        def spring_damper_half_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4555.SpringDamperHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4555,
            )

            return self._parent._cast(_4555.SpringDamperHalfCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4556.StraightBevelDiffGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4556,
            )

            return self._parent._cast(
                _4556.StraightBevelDiffGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4559.StraightBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4559,
            )

            return self._parent._cast(
                _4559.StraightBevelGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_planet_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4562.StraightBevelPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4562,
            )

            return self._parent._cast(
                _4562.StraightBevelPlanetGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_sun_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4563.StraightBevelSunGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4563,
            )

            return self._parent._cast(
                _4563.StraightBevelSunGearCompoundParametricStudyTool
            )

        @property
        def synchroniser_half_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4565.SynchroniserHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4565,
            )

            return self._parent._cast(_4565.SynchroniserHalfCompoundParametricStudyTool)

        @property
        def synchroniser_part_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4566.SynchroniserPartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4566,
            )

            return self._parent._cast(_4566.SynchroniserPartCompoundParametricStudyTool)

        @property
        def synchroniser_sleeve_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4567.SynchroniserSleeveCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4567,
            )

            return self._parent._cast(
                _4567.SynchroniserSleeveCompoundParametricStudyTool
            )

        @property
        def torque_converter_pump_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4570.TorqueConverterPumpCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4570,
            )

            return self._parent._cast(
                _4570.TorqueConverterPumpCompoundParametricStudyTool
            )

        @property
        def torque_converter_turbine_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4571.TorqueConverterTurbineCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4571,
            )

            return self._parent._cast(
                _4571.TorqueConverterTurbineCompoundParametricStudyTool
            )

        @property
        def unbalanced_mass_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4572.UnbalancedMassCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4572,
            )

            return self._parent._cast(_4572.UnbalancedMassCompoundParametricStudyTool)

        @property
        def virtual_component_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4573.VirtualComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4573,
            )

            return self._parent._cast(_4573.VirtualComponentCompoundParametricStudyTool)

        @property
        def worm_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4574.WormGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4574,
            )

            return self._parent._cast(_4574.WormGearCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4577.ZerolBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4577,
            )

            return self._parent._cast(_4577.ZerolBevelGearCompoundParametricStudyTool)

        @property
        def component_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "ComponentCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "ComponentCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4329.ComponentParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ComponentParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4329.ComponentParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ComponentParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool":
        return self._Cast_ComponentCompoundParametricStudyTool(self)
