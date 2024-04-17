"""PartTimeSeriesLoadAnalysisCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.analysis_cases import _7553
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TIME_SERIES_LOAD_ANALYSIS_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases",
    "PartTimeSeriesLoadAnalysisCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5384,
        _5385,
        _5386,
        _5389,
        _5390,
        _5392,
        _5393,
        _5396,
        _5398,
        _5399,
        _5400,
        _5401,
        _5403,
        _5404,
        _5405,
        _5406,
        _5408,
        _5409,
        _5412,
        _5414,
        _5415,
        _5417,
        _5418,
        _5420,
        _5421,
        _5423,
        _5425,
        _5426,
        _5428,
        _5429,
        _5430,
        _5432,
        _5435,
        _5436,
        _5437,
        _5438,
        _5439,
        _5441,
        _5442,
        _5443,
        _5444,
        _5447,
        _5448,
        _5449,
        _5451,
        _5452,
        _5459,
        _5460,
        _5462,
        _5463,
        _5465,
        _5466,
        _5467,
        _5471,
        _5472,
        _5474,
        _5475,
        _5477,
        _5478,
        _5480,
        _5481,
        _5482,
        _5483,
        _5484,
        _5485,
        _5487,
        _5489,
        _5490,
        _5493,
        _5494,
        _5497,
        _5499,
        _5500,
        _5502,
        _5503,
        _5505,
        _5506,
        _5508,
        _5509,
        _5510,
        _5511,
        _5512,
        _5513,
        _5514,
        _5515,
        _5518,
        _5519,
        _5521,
        _5522,
        _5523,
        _5526,
        _5527,
        _5529,
        _5530,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartTimeSeriesLoadAnalysisCase",)


Self = TypeVar("Self", bound="PartTimeSeriesLoadAnalysisCase")


class PartTimeSeriesLoadAnalysisCase(_7553.PartAnalysisCase):
    """PartTimeSeriesLoadAnalysisCase

    This is a mastapy class.
    """

    TYPE = _PART_TIME_SERIES_LOAD_ANALYSIS_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartTimeSeriesLoadAnalysisCase")

    class _Cast_PartTimeSeriesLoadAnalysisCase:
        """Special nested class for casting PartTimeSeriesLoadAnalysisCase to subclasses."""

        def __init__(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
            parent: "PartTimeSeriesLoadAnalysisCase",
        ):
            self._parent = parent

        @property
        def part_analysis_case(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_7553.PartAnalysisCase":
            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5384.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5384

            return self._parent._cast(_5384.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5385.AbstractShaftMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5385

            return self._parent._cast(_5385.AbstractShaftMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_or_housing_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5386.AbstractShaftOrHousingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5386

            return self._parent._cast(
                _5386.AbstractShaftOrHousingMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5389.AGMAGleasonConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5389

            return self._parent._cast(
                _5389.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5390.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5390

            return self._parent._cast(
                _5390.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def assembly_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5392.AssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5392

            return self._parent._cast(_5392.AssemblyMultibodyDynamicsAnalysis)

        @property
        def bearing_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5393.BearingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5393

            return self._parent._cast(_5393.BearingMultibodyDynamicsAnalysis)

        @property
        def belt_drive_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5396.BeltDriveMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5396

            return self._parent._cast(_5396.BeltDriveMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5398.BevelDifferentialGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5398

            return self._parent._cast(
                _5398.BevelDifferentialGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5399.BevelDifferentialGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5399

            return self._parent._cast(
                _5399.BevelDifferentialGearSetMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5400.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5400

            return self._parent._cast(
                _5400.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5401.BevelDifferentialSunGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5401

            return self._parent._cast(
                _5401.BevelDifferentialSunGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5403.BevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403

            return self._parent._cast(_5403.BevelGearMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5404.BevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404

            return self._parent._cast(_5404.BevelGearSetMultibodyDynamicsAnalysis)

        @property
        def bolted_joint_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5405.BoltedJointMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5405

            return self._parent._cast(_5405.BoltedJointMultibodyDynamicsAnalysis)

        @property
        def bolt_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5406.BoltMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5406

            return self._parent._cast(_5406.BoltMultibodyDynamicsAnalysis)

        @property
        def clutch_half_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5408.ClutchHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5408

            return self._parent._cast(_5408.ClutchHalfMultibodyDynamicsAnalysis)

        @property
        def clutch_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5409.ClutchMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5409

            return self._parent._cast(_5409.ClutchMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5412.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5412

            return self._parent._cast(_5412.ComponentMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5414.ConceptCouplingHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5414

            return self._parent._cast(
                _5414.ConceptCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def concept_coupling_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5415.ConceptCouplingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5415

            return self._parent._cast(_5415.ConceptCouplingMultibodyDynamicsAnalysis)

        @property
        def concept_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5417.ConceptGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5417

            return self._parent._cast(_5417.ConceptGearMultibodyDynamicsAnalysis)

        @property
        def concept_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5418.ConceptGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5418

            return self._parent._cast(_5418.ConceptGearSetMultibodyDynamicsAnalysis)

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5420.ConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5420

            return self._parent._cast(_5420.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5421.ConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5421

            return self._parent._cast(_5421.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def connector_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5423.ConnectorMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5423

            return self._parent._cast(_5423.ConnectorMultibodyDynamicsAnalysis)

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5425.CouplingHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425

            return self._parent._cast(_5425.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def coupling_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5426.CouplingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5426

            return self._parent._cast(_5426.CouplingMultibodyDynamicsAnalysis)

        @property
        def cvt_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5428.CVTMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428

            return self._parent._cast(_5428.CVTMultibodyDynamicsAnalysis)

        @property
        def cvt_pulley_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5429.CVTPulleyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5429

            return self._parent._cast(_5429.CVTPulleyMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5430.CycloidalAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5430

            return self._parent._cast(_5430.CycloidalAssemblyMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5432.CycloidalDiscMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5432

            return self._parent._cast(_5432.CycloidalDiscMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5435.CylindricalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5435

            return self._parent._cast(_5435.CylindricalGearMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5436.CylindricalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436

            return self._parent._cast(_5436.CylindricalGearSetMultibodyDynamicsAnalysis)

        @property
        def cylindrical_planet_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5437.CylindricalPlanetGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437

            return self._parent._cast(
                _5437.CylindricalPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def datum_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5438.DatumMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5438

            return self._parent._cast(_5438.DatumMultibodyDynamicsAnalysis)

        @property
        def external_cad_model_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5439.ExternalCADModelMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5439

            return self._parent._cast(_5439.ExternalCADModelMultibodyDynamicsAnalysis)

        @property
        def face_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5441.FaceGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5441

            return self._parent._cast(_5441.FaceGearMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5442.FaceGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5442

            return self._parent._cast(_5442.FaceGearSetMultibodyDynamicsAnalysis)

        @property
        def fe_part_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5443.FEPartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5443

            return self._parent._cast(_5443.FEPartMultibodyDynamicsAnalysis)

        @property
        def flexible_pin_assembly_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5444.FlexiblePinAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5444

            return self._parent._cast(
                _5444.FlexiblePinAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5447.GearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5447

            return self._parent._cast(_5447.GearMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5448.GearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5448

            return self._parent._cast(_5448.GearSetMultibodyDynamicsAnalysis)

        @property
        def guide_dxf_model_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5449.GuideDxfModelMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5449

            return self._parent._cast(_5449.GuideDxfModelMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5451.HypoidGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5451

            return self._parent._cast(_5451.HypoidGearMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5452.HypoidGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5452

            return self._parent._cast(_5452.HypoidGearSetMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5459.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5459

            return self._parent._cast(
                _5459.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5460.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5460

            return self._parent._cast(
                _5460.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5462.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5462

            return self._parent._cast(
                _5462.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5463.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(
                _5463.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5465.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5465

            return self._parent._cast(
                _5465.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> (
            "_5466.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(
                _5466.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def mass_disc_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5467.MassDiscMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(_5467.MassDiscMultibodyDynamicsAnalysis)

        @property
        def measurement_component_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5471.MeasurementComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5471

            return self._parent._cast(
                _5471.MeasurementComponentMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5472.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5472

            return self._parent._cast(_5472.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def oil_seal_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5474.OilSealMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5474

            return self._parent._cast(_5474.OilSealMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5475.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(_5475.PartMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5477.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5477

            return self._parent._cast(
                _5477.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5478.PartToPartShearCouplingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5478

            return self._parent._cast(
                _5478.PartToPartShearCouplingMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5480.PlanetaryGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5480

            return self._parent._cast(_5480.PlanetaryGearSetMultibodyDynamicsAnalysis)

        @property
        def planet_carrier_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5481.PlanetCarrierMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5481

            return self._parent._cast(_5481.PlanetCarrierMultibodyDynamicsAnalysis)

        @property
        def point_load_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5482.PointLoadMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5482

            return self._parent._cast(_5482.PointLoadMultibodyDynamicsAnalysis)

        @property
        def power_load_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5483.PowerLoadMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5483

            return self._parent._cast(_5483.PowerLoadMultibodyDynamicsAnalysis)

        @property
        def pulley_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5484.PulleyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5484

            return self._parent._cast(_5484.PulleyMultibodyDynamicsAnalysis)

        @property
        def ring_pins_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5485.RingPinsMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5485

            return self._parent._cast(_5485.RingPinsMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_assembly_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5487.RollingRingAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5487

            return self._parent._cast(
                _5487.RollingRingAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5489.RollingRingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5489

            return self._parent._cast(_5489.RollingRingMultibodyDynamicsAnalysis)

        @property
        def root_assembly_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5490.RootAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5490

            return self._parent._cast(_5490.RootAssemblyMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5493.ShaftHubConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5493

            return self._parent._cast(_5493.ShaftHubConnectionMultibodyDynamicsAnalysis)

        @property
        def shaft_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5494.ShaftMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5494

            return self._parent._cast(_5494.ShaftMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5497.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5497

            return self._parent._cast(
                _5497.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5499.SpiralBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5499

            return self._parent._cast(_5499.SpiralBevelGearMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5500.SpiralBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5500

            return self._parent._cast(_5500.SpiralBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def spring_damper_half_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5502.SpringDamperHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5502

            return self._parent._cast(_5502.SpringDamperHalfMultibodyDynamicsAnalysis)

        @property
        def spring_damper_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5503.SpringDamperMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5503

            return self._parent._cast(_5503.SpringDamperMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5505.StraightBevelDiffGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5505

            return self._parent._cast(
                _5505.StraightBevelDiffGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5506.StraightBevelDiffGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5506

            return self._parent._cast(
                _5506.StraightBevelDiffGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5508.StraightBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5508

            return self._parent._cast(_5508.StraightBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5509.StraightBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5509

            return self._parent._cast(
                _5509.StraightBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_planet_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5510.StraightBevelPlanetGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5510

            return self._parent._cast(
                _5510.StraightBevelPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5511.StraightBevelSunGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5511

            return self._parent._cast(
                _5511.StraightBevelSunGearMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_half_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5512.SynchroniserHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5512

            return self._parent._cast(_5512.SynchroniserHalfMultibodyDynamicsAnalysis)

        @property
        def synchroniser_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5513.SynchroniserMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5513

            return self._parent._cast(_5513.SynchroniserMultibodyDynamicsAnalysis)

        @property
        def synchroniser_part_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5514.SynchroniserPartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5514

            return self._parent._cast(_5514.SynchroniserPartMultibodyDynamicsAnalysis)

        @property
        def synchroniser_sleeve_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5515.SynchroniserSleeveMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5515

            return self._parent._cast(_5515.SynchroniserSleeveMultibodyDynamicsAnalysis)

        @property
        def torque_converter_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5518.TorqueConverterMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5518

            return self._parent._cast(_5518.TorqueConverterMultibodyDynamicsAnalysis)

        @property
        def torque_converter_pump_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5519.TorqueConverterPumpMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5519

            return self._parent._cast(
                _5519.TorqueConverterPumpMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5521.TorqueConverterTurbineMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5521

            return self._parent._cast(
                _5521.TorqueConverterTurbineMultibodyDynamicsAnalysis
            )

        @property
        def unbalanced_mass_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5522.UnbalancedMassMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5522

            return self._parent._cast(_5522.UnbalancedMassMultibodyDynamicsAnalysis)

        @property
        def virtual_component_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5523.VirtualComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5523

            return self._parent._cast(_5523.VirtualComponentMultibodyDynamicsAnalysis)

        @property
        def worm_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5526.WormGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5526

            return self._parent._cast(_5526.WormGearMultibodyDynamicsAnalysis)

        @property
        def worm_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5527.WormGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5527

            return self._parent._cast(_5527.WormGearSetMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5529.ZerolBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5529

            return self._parent._cast(_5529.ZerolBevelGearMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "_5530.ZerolBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5530

            return self._parent._cast(_5530.ZerolBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "PartTimeSeriesLoadAnalysisCase":
            return self._parent

        def __getattr__(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartTimeSeriesLoadAnalysisCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase":
        return self._Cast_PartTimeSeriesLoadAnalysisCase(self)
