"""PartCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7554
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "PartCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4670
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4736,
        _4737,
        _4738,
        _4740,
        _4742,
        _4743,
        _4744,
        _4746,
        _4747,
        _4749,
        _4750,
        _4751,
        _4752,
        _4754,
        _4755,
        _4756,
        _4757,
        _4759,
        _4761,
        _4762,
        _4764,
        _4765,
        _4767,
        _4768,
        _4770,
        _4772,
        _4773,
        _4775,
        _4777,
        _4778,
        _4779,
        _4781,
        _4783,
        _4785,
        _4786,
        _4787,
        _4788,
        _4789,
        _4791,
        _4792,
        _4793,
        _4794,
        _4796,
        _4797,
        _4798,
        _4800,
        _4802,
        _4804,
        _4805,
        _4807,
        _4808,
        _4810,
        _4811,
        _4812,
        _4813,
        _4814,
        _4816,
        _4818,
        _4820,
        _4821,
        _4822,
        _4823,
        _4824,
        _4825,
        _4827,
        _4828,
        _4830,
        _4831,
        _4832,
        _4834,
        _4835,
        _4837,
        _4838,
        _4840,
        _4841,
        _4843,
        _4844,
        _4846,
        _4847,
        _4848,
        _4849,
        _4850,
        _4851,
        _4852,
        _4853,
        _4855,
        _4856,
        _4857,
        _4858,
        _4859,
        _4861,
        _4862,
        _4864,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundModalAnalysis",)


Self = TypeVar("Self", bound="PartCompoundModalAnalysis")


class PartCompoundModalAnalysis(_7554.PartCompoundAnalysis):
    """PartCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartCompoundModalAnalysis")

    class _Cast_PartCompoundModalAnalysis:
        """Special nested class for casting PartCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
            parent: "PartCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4736.AbstractAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4736,
            )

            return self._parent._cast(_4736.AbstractAssemblyCompoundModalAnalysis)

        @property
        def abstract_shaft_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4737.AbstractShaftCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4737,
            )

            return self._parent._cast(_4737.AbstractShaftCompoundModalAnalysis)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4738.AbstractShaftOrHousingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4738,
            )

            return self._parent._cast(_4738.AbstractShaftOrHousingCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4740.AGMAGleasonConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4740,
            )

            return self._parent._cast(_4740.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4742.AGMAGleasonConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4742,
            )

            return self._parent._cast(
                _4742.AGMAGleasonConicalGearSetCompoundModalAnalysis
            )

        @property
        def assembly_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4743.AssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4743,
            )

            return self._parent._cast(_4743.AssemblyCompoundModalAnalysis)

        @property
        def bearing_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4744.BearingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4744,
            )

            return self._parent._cast(_4744.BearingCompoundModalAnalysis)

        @property
        def belt_drive_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4746.BeltDriveCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4746,
            )

            return self._parent._cast(_4746.BeltDriveCompoundModalAnalysis)

        @property
        def bevel_differential_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4747.BevelDifferentialGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4747,
            )

            return self._parent._cast(_4747.BevelDifferentialGearCompoundModalAnalysis)

        @property
        def bevel_differential_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4749.BevelDifferentialGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4749,
            )

            return self._parent._cast(
                _4749.BevelDifferentialGearSetCompoundModalAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4750.BevelDifferentialPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4750,
            )

            return self._parent._cast(
                _4750.BevelDifferentialPlanetGearCompoundModalAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4751.BevelDifferentialSunGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4751,
            )

            return self._parent._cast(
                _4751.BevelDifferentialSunGearCompoundModalAnalysis
            )

        @property
        def bevel_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4752.BevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4752,
            )

            return self._parent._cast(_4752.BevelGearCompoundModalAnalysis)

        @property
        def bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4754.BevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4754,
            )

            return self._parent._cast(_4754.BevelGearSetCompoundModalAnalysis)

        @property
        def bolt_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4755.BoltCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4755,
            )

            return self._parent._cast(_4755.BoltCompoundModalAnalysis)

        @property
        def bolted_joint_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4756.BoltedJointCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4756,
            )

            return self._parent._cast(_4756.BoltedJointCompoundModalAnalysis)

        @property
        def clutch_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4757.ClutchCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4757,
            )

            return self._parent._cast(_4757.ClutchCompoundModalAnalysis)

        @property
        def clutch_half_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4759.ClutchHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4759,
            )

            return self._parent._cast(_4759.ClutchHalfCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4761.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4761,
            )

            return self._parent._cast(_4761.ComponentCompoundModalAnalysis)

        @property
        def concept_coupling_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4762.ConceptCouplingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4762,
            )

            return self._parent._cast(_4762.ConceptCouplingCompoundModalAnalysis)

        @property
        def concept_coupling_half_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4764.ConceptCouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4764,
            )

            return self._parent._cast(_4764.ConceptCouplingHalfCompoundModalAnalysis)

        @property
        def concept_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4765.ConceptGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4765,
            )

            return self._parent._cast(_4765.ConceptGearCompoundModalAnalysis)

        @property
        def concept_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4767.ConceptGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4767,
            )

            return self._parent._cast(_4767.ConceptGearSetCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4768.ConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4768,
            )

            return self._parent._cast(_4768.ConicalGearCompoundModalAnalysis)

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4770.ConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4770,
            )

            return self._parent._cast(_4770.ConicalGearSetCompoundModalAnalysis)

        @property
        def connector_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4772.ConnectorCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4772,
            )

            return self._parent._cast(_4772.ConnectorCompoundModalAnalysis)

        @property
        def coupling_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4773.CouplingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4773,
            )

            return self._parent._cast(_4773.CouplingCompoundModalAnalysis)

        @property
        def coupling_half_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4775.CouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4775,
            )

            return self._parent._cast(_4775.CouplingHalfCompoundModalAnalysis)

        @property
        def cvt_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4777.CVTCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4777,
            )

            return self._parent._cast(_4777.CVTCompoundModalAnalysis)

        @property
        def cvt_pulley_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4778.CVTPulleyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4778,
            )

            return self._parent._cast(_4778.CVTPulleyCompoundModalAnalysis)

        @property
        def cycloidal_assembly_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4779.CycloidalAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4779,
            )

            return self._parent._cast(_4779.CycloidalAssemblyCompoundModalAnalysis)

        @property
        def cycloidal_disc_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4781.CycloidalDiscCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4781,
            )

            return self._parent._cast(_4781.CycloidalDiscCompoundModalAnalysis)

        @property
        def cylindrical_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4783.CylindricalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4783,
            )

            return self._parent._cast(_4783.CylindricalGearCompoundModalAnalysis)

        @property
        def cylindrical_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4785.CylindricalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4785,
            )

            return self._parent._cast(_4785.CylindricalGearSetCompoundModalAnalysis)

        @property
        def cylindrical_planet_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4786.CylindricalPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4786,
            )

            return self._parent._cast(_4786.CylindricalPlanetGearCompoundModalAnalysis)

        @property
        def datum_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4787.DatumCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4787,
            )

            return self._parent._cast(_4787.DatumCompoundModalAnalysis)

        @property
        def external_cad_model_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4788.ExternalCADModelCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4788,
            )

            return self._parent._cast(_4788.ExternalCADModelCompoundModalAnalysis)

        @property
        def face_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4789.FaceGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4789,
            )

            return self._parent._cast(_4789.FaceGearCompoundModalAnalysis)

        @property
        def face_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4791.FaceGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4791,
            )

            return self._parent._cast(_4791.FaceGearSetCompoundModalAnalysis)

        @property
        def fe_part_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4792.FEPartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4792,
            )

            return self._parent._cast(_4792.FEPartCompoundModalAnalysis)

        @property
        def flexible_pin_assembly_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4793.FlexiblePinAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4793,
            )

            return self._parent._cast(_4793.FlexiblePinAssemblyCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4794.GearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4794,
            )

            return self._parent._cast(_4794.GearCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4796.GearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4796,
            )

            return self._parent._cast(_4796.GearSetCompoundModalAnalysis)

        @property
        def guide_dxf_model_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4797.GuideDxfModelCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4797,
            )

            return self._parent._cast(_4797.GuideDxfModelCompoundModalAnalysis)

        @property
        def hypoid_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4798.HypoidGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4798,
            )

            return self._parent._cast(_4798.HypoidGearCompoundModalAnalysis)

        @property
        def hypoid_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4800.HypoidGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4800,
            )

            return self._parent._cast(_4800.HypoidGearSetCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4802.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4802,
            )

            return self._parent._cast(
                _4802.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4804.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(
                _4804.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4805.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4805,
            )

            return self._parent._cast(
                _4805.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4807.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(
                _4807.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4808.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4808,
            )

            return self._parent._cast(
                _4808.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4810.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4810,
            )

            return self._parent._cast(
                _4810.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
            )

        @property
        def mass_disc_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4811.MassDiscCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4811,
            )

            return self._parent._cast(_4811.MassDiscCompoundModalAnalysis)

        @property
        def measurement_component_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4812.MeasurementComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4812,
            )

            return self._parent._cast(_4812.MeasurementComponentCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4813.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4813,
            )

            return self._parent._cast(_4813.MountableComponentCompoundModalAnalysis)

        @property
        def oil_seal_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4814.OilSealCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4814,
            )

            return self._parent._cast(_4814.OilSealCompoundModalAnalysis)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4816.PartToPartShearCouplingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4816,
            )

            return self._parent._cast(
                _4816.PartToPartShearCouplingCompoundModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4818.PartToPartShearCouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4818,
            )

            return self._parent._cast(
                _4818.PartToPartShearCouplingHalfCompoundModalAnalysis
            )

        @property
        def planetary_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4820.PlanetaryGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4820,
            )

            return self._parent._cast(_4820.PlanetaryGearSetCompoundModalAnalysis)

        @property
        def planet_carrier_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4821.PlanetCarrierCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4821,
            )

            return self._parent._cast(_4821.PlanetCarrierCompoundModalAnalysis)

        @property
        def point_load_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4822.PointLoadCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4822,
            )

            return self._parent._cast(_4822.PointLoadCompoundModalAnalysis)

        @property
        def power_load_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4823.PowerLoadCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4823,
            )

            return self._parent._cast(_4823.PowerLoadCompoundModalAnalysis)

        @property
        def pulley_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4824.PulleyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4824,
            )

            return self._parent._cast(_4824.PulleyCompoundModalAnalysis)

        @property
        def ring_pins_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4825.RingPinsCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4825,
            )

            return self._parent._cast(_4825.RingPinsCompoundModalAnalysis)

        @property
        def rolling_ring_assembly_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4827.RollingRingAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4827,
            )

            return self._parent._cast(_4827.RollingRingAssemblyCompoundModalAnalysis)

        @property
        def rolling_ring_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4828.RollingRingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.RollingRingCompoundModalAnalysis)

        @property
        def root_assembly_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4830.RootAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4830,
            )

            return self._parent._cast(_4830.RootAssemblyCompoundModalAnalysis)

        @property
        def shaft_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4831.ShaftCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4831,
            )

            return self._parent._cast(_4831.ShaftCompoundModalAnalysis)

        @property
        def shaft_hub_connection_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4832.ShaftHubConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4832,
            )

            return self._parent._cast(_4832.ShaftHubConnectionCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4834.SpecialisedAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4834,
            )

            return self._parent._cast(_4834.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4835.SpiralBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4835,
            )

            return self._parent._cast(_4835.SpiralBevelGearCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4837.SpiralBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4837,
            )

            return self._parent._cast(_4837.SpiralBevelGearSetCompoundModalAnalysis)

        @property
        def spring_damper_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4838.SpringDamperCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4838,
            )

            return self._parent._cast(_4838.SpringDamperCompoundModalAnalysis)

        @property
        def spring_damper_half_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4840.SpringDamperHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4840,
            )

            return self._parent._cast(_4840.SpringDamperHalfCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4841.StraightBevelDiffGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4841,
            )

            return self._parent._cast(_4841.StraightBevelDiffGearCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4843.StraightBevelDiffGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4843,
            )

            return self._parent._cast(
                _4843.StraightBevelDiffGearSetCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4844.StraightBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4844,
            )

            return self._parent._cast(_4844.StraightBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4846.StraightBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4846,
            )

            return self._parent._cast(_4846.StraightBevelGearSetCompoundModalAnalysis)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4847.StraightBevelPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4847,
            )

            return self._parent._cast(
                _4847.StraightBevelPlanetGearCompoundModalAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4848.StraightBevelSunGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4848,
            )

            return self._parent._cast(_4848.StraightBevelSunGearCompoundModalAnalysis)

        @property
        def synchroniser_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4849.SynchroniserCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4849,
            )

            return self._parent._cast(_4849.SynchroniserCompoundModalAnalysis)

        @property
        def synchroniser_half_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4850.SynchroniserHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4850,
            )

            return self._parent._cast(_4850.SynchroniserHalfCompoundModalAnalysis)

        @property
        def synchroniser_part_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4851.SynchroniserPartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4851,
            )

            return self._parent._cast(_4851.SynchroniserPartCompoundModalAnalysis)

        @property
        def synchroniser_sleeve_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4852.SynchroniserSleeveCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4852,
            )

            return self._parent._cast(_4852.SynchroniserSleeveCompoundModalAnalysis)

        @property
        def torque_converter_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4853.TorqueConverterCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4853,
            )

            return self._parent._cast(_4853.TorqueConverterCompoundModalAnalysis)

        @property
        def torque_converter_pump_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4855.TorqueConverterPumpCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4855,
            )

            return self._parent._cast(_4855.TorqueConverterPumpCompoundModalAnalysis)

        @property
        def torque_converter_turbine_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4856.TorqueConverterTurbineCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4856,
            )

            return self._parent._cast(_4856.TorqueConverterTurbineCompoundModalAnalysis)

        @property
        def unbalanced_mass_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4857.UnbalancedMassCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4857,
            )

            return self._parent._cast(_4857.UnbalancedMassCompoundModalAnalysis)

        @property
        def virtual_component_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4858.VirtualComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4858,
            )

            return self._parent._cast(_4858.VirtualComponentCompoundModalAnalysis)

        @property
        def worm_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4859.WormGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4859,
            )

            return self._parent._cast(_4859.WormGearCompoundModalAnalysis)

        @property
        def worm_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4861.WormGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4861,
            )

            return self._parent._cast(_4861.WormGearSetCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4862.ZerolBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4862,
            )

            return self._parent._cast(_4862.ZerolBevelGearCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "_4864.ZerolBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4864,
            )

            return self._parent._cast(_4864.ZerolBevelGearSetCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "PartCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4670.PartModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.PartModalAnalysis]

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
    def component_analysis_cases_ready(self: Self) -> "List[_4670.PartModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.PartModalAnalysis]

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
    ) -> "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis":
        return self._Cast_PartCompoundModalAnalysis(self)
