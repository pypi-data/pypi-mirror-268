"""PartDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7555
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses", "PartDynamicAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2475
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6337,
        _6285,
        _6286,
        _6287,
        _6289,
        _6291,
        _6292,
        _6293,
        _6295,
        _6296,
        _6298,
        _6299,
        _6300,
        _6301,
        _6303,
        _6304,
        _6305,
        _6307,
        _6308,
        _6310,
        _6312,
        _6313,
        _6314,
        _6316,
        _6317,
        _6319,
        _6321,
        _6323,
        _6324,
        _6326,
        _6327,
        _6328,
        _6330,
        _6332,
        _6334,
        _6335,
        _6336,
        _6339,
        _6340,
        _6342,
        _6343,
        _6344,
        _6345,
        _6347,
        _6348,
        _6349,
        _6351,
        _6353,
        _6355,
        _6356,
        _6358,
        _6359,
        _6361,
        _6362,
        _6363,
        _6364,
        _6365,
        _6368,
        _6369,
        _6371,
        _6372,
        _6373,
        _6374,
        _6375,
        _6376,
        _6378,
        _6380,
        _6381,
        _6382,
        _6383,
        _6385,
        _6386,
        _6388,
        _6390,
        _6391,
        _6392,
        _6394,
        _6395,
        _6397,
        _6398,
        _6399,
        _6400,
        _6401,
        _6402,
        _6403,
        _6405,
        _6406,
        _6407,
        _6408,
        _6409,
        _6410,
        _6412,
        _6413,
        _6415,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartDynamicAnalysis",)


Self = TypeVar("Self", bound="PartDynamicAnalysis")


class PartDynamicAnalysis(_7555.PartFEAnalysis):
    """PartDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartDynamicAnalysis")

    class _Cast_PartDynamicAnalysis:
        """Special nested class for casting PartDynamicAnalysis to subclasses."""

        def __init__(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
            parent: "PartDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def part_fe_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_7555.PartFEAnalysis":
            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6285.AbstractAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6285

            return self._parent._cast(_6285.AbstractAssemblyDynamicAnalysis)

        @property
        def abstract_shaft_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6286.AbstractShaftDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6286

            return self._parent._cast(_6286.AbstractShaftDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6287.AbstractShaftOrHousingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6287

            return self._parent._cast(_6287.AbstractShaftOrHousingDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6289.AGMAGleasonConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6289

            return self._parent._cast(_6289.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6291.AGMAGleasonConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6291

            return self._parent._cast(_6291.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def assembly_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6292.AssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6292

            return self._parent._cast(_6292.AssemblyDynamicAnalysis)

        @property
        def bearing_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6293.BearingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6293

            return self._parent._cast(_6293.BearingDynamicAnalysis)

        @property
        def belt_drive_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6295.BeltDriveDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6295

            return self._parent._cast(_6295.BeltDriveDynamicAnalysis)

        @property
        def bevel_differential_gear_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6296.BevelDifferentialGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6296

            return self._parent._cast(_6296.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6298.BevelDifferentialGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298

            return self._parent._cast(_6298.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6299.BevelDifferentialPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299

            return self._parent._cast(_6299.BevelDifferentialPlanetGearDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6300.BevelDifferentialSunGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6300

            return self._parent._cast(_6300.BevelDifferentialSunGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6301.BevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301

            return self._parent._cast(_6301.BevelGearDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6303.BevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303

            return self._parent._cast(_6303.BevelGearSetDynamicAnalysis)

        @property
        def bolt_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6304.BoltDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304

            return self._parent._cast(_6304.BoltDynamicAnalysis)

        @property
        def bolted_joint_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6305.BoltedJointDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6305

            return self._parent._cast(_6305.BoltedJointDynamicAnalysis)

        @property
        def clutch_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6307.ClutchDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307

            return self._parent._cast(_6307.ClutchDynamicAnalysis)

        @property
        def clutch_half_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6308.ClutchHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6308

            return self._parent._cast(_6308.ClutchHalfDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6310.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.ComponentDynamicAnalysis)

        @property
        def concept_coupling_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6312.ConceptCouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312

            return self._parent._cast(_6312.ConceptCouplingDynamicAnalysis)

        @property
        def concept_coupling_half_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6313.ConceptCouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6313

            return self._parent._cast(_6313.ConceptCouplingHalfDynamicAnalysis)

        @property
        def concept_gear_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6314.ConceptGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6314

            return self._parent._cast(_6314.ConceptGearDynamicAnalysis)

        @property
        def concept_gear_set_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6316.ConceptGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316

            return self._parent._cast(_6316.ConceptGearSetDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6317.ConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6317

            return self._parent._cast(_6317.ConicalGearDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6319.ConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6319

            return self._parent._cast(_6319.ConicalGearSetDynamicAnalysis)

        @property
        def connector_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6321.ConnectorDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321

            return self._parent._cast(_6321.ConnectorDynamicAnalysis)

        @property
        def coupling_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6323.CouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323

            return self._parent._cast(_6323.CouplingDynamicAnalysis)

        @property
        def coupling_half_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6324.CouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6324

            return self._parent._cast(_6324.CouplingHalfDynamicAnalysis)

        @property
        def cvt_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6326.CVTDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6326

            return self._parent._cast(_6326.CVTDynamicAnalysis)

        @property
        def cvt_pulley_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6327.CVTPulleyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6327

            return self._parent._cast(_6327.CVTPulleyDynamicAnalysis)

        @property
        def cycloidal_assembly_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6328.CycloidalAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328

            return self._parent._cast(_6328.CycloidalAssemblyDynamicAnalysis)

        @property
        def cycloidal_disc_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6330.CycloidalDiscDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6330

            return self._parent._cast(_6330.CycloidalDiscDynamicAnalysis)

        @property
        def cylindrical_gear_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6332.CylindricalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6332

            return self._parent._cast(_6332.CylindricalGearDynamicAnalysis)

        @property
        def cylindrical_gear_set_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6334.CylindricalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334

            return self._parent._cast(_6334.CylindricalGearSetDynamicAnalysis)

        @property
        def cylindrical_planet_gear_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6335.CylindricalPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335

            return self._parent._cast(_6335.CylindricalPlanetGearDynamicAnalysis)

        @property
        def datum_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6336.DatumDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6336

            return self._parent._cast(_6336.DatumDynamicAnalysis)

        @property
        def external_cad_model_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6339.ExternalCADModelDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6339

            return self._parent._cast(_6339.ExternalCADModelDynamicAnalysis)

        @property
        def face_gear_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6340.FaceGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6340

            return self._parent._cast(_6340.FaceGearDynamicAnalysis)

        @property
        def face_gear_set_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6342.FaceGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342

            return self._parent._cast(_6342.FaceGearSetDynamicAnalysis)

        @property
        def fe_part_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6343.FEPartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6343

            return self._parent._cast(_6343.FEPartDynamicAnalysis)

        @property
        def flexible_pin_assembly_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6344.FlexiblePinAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6344

            return self._parent._cast(_6344.FlexiblePinAssemblyDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6345.GearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6345

            return self._parent._cast(_6345.GearDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6347.GearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6347

            return self._parent._cast(_6347.GearSetDynamicAnalysis)

        @property
        def guide_dxf_model_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6348.GuideDxfModelDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6348

            return self._parent._cast(_6348.GuideDxfModelDynamicAnalysis)

        @property
        def hypoid_gear_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6349.HypoidGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6349

            return self._parent._cast(_6349.HypoidGearDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6351.HypoidGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6351

            return self._parent._cast(_6351.HypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6353.KlingelnbergCycloPalloidConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353

            return self._parent._cast(
                _6353.KlingelnbergCycloPalloidConicalGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6355.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(
                _6355.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6356.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356

            return self._parent._cast(
                _6356.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6358.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(
                _6358.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6359.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6359

            return self._parent._cast(
                _6359.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6361.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6361

            return self._parent._cast(
                _6361.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis
            )

        @property
        def mass_disc_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6362.MassDiscDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6362

            return self._parent._cast(_6362.MassDiscDynamicAnalysis)

        @property
        def measurement_component_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6363.MeasurementComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363

            return self._parent._cast(_6363.MeasurementComponentDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6364.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364

            return self._parent._cast(_6364.MountableComponentDynamicAnalysis)

        @property
        def oil_seal_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6365.OilSealDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6365

            return self._parent._cast(_6365.OilSealDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6368.PartToPartShearCouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6368

            return self._parent._cast(_6368.PartToPartShearCouplingDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6369.PartToPartShearCouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6369

            return self._parent._cast(_6369.PartToPartShearCouplingHalfDynamicAnalysis)

        @property
        def planetary_gear_set_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6371.PlanetaryGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6371

            return self._parent._cast(_6371.PlanetaryGearSetDynamicAnalysis)

        @property
        def planet_carrier_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6372.PlanetCarrierDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6372

            return self._parent._cast(_6372.PlanetCarrierDynamicAnalysis)

        @property
        def point_load_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6373.PointLoadDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6373

            return self._parent._cast(_6373.PointLoadDynamicAnalysis)

        @property
        def power_load_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6374.PowerLoadDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6374

            return self._parent._cast(_6374.PowerLoadDynamicAnalysis)

        @property
        def pulley_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6375.PulleyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6375

            return self._parent._cast(_6375.PulleyDynamicAnalysis)

        @property
        def ring_pins_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6376.RingPinsDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376

            return self._parent._cast(_6376.RingPinsDynamicAnalysis)

        @property
        def rolling_ring_assembly_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6378.RollingRingAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6378

            return self._parent._cast(_6378.RollingRingAssemblyDynamicAnalysis)

        @property
        def rolling_ring_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6380.RollingRingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6380

            return self._parent._cast(_6380.RollingRingDynamicAnalysis)

        @property
        def root_assembly_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6381.RootAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6381

            return self._parent._cast(_6381.RootAssemblyDynamicAnalysis)

        @property
        def shaft_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6382.ShaftDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.ShaftDynamicAnalysis)

        @property
        def shaft_hub_connection_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6383.ShaftHubConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6383

            return self._parent._cast(_6383.ShaftHubConnectionDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6385.SpecialisedAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6385

            return self._parent._cast(_6385.SpecialisedAssemblyDynamicAnalysis)

        @property
        def spiral_bevel_gear_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6386.SpiralBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6386

            return self._parent._cast(_6386.SpiralBevelGearDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6388.SpiralBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6388

            return self._parent._cast(_6388.SpiralBevelGearSetDynamicAnalysis)

        @property
        def spring_damper_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6390.SpringDamperDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6390

            return self._parent._cast(_6390.SpringDamperDynamicAnalysis)

        @property
        def spring_damper_half_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6391.SpringDamperHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6391

            return self._parent._cast(_6391.SpringDamperHalfDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6392.StraightBevelDiffGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6392

            return self._parent._cast(_6392.StraightBevelDiffGearDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6394.StraightBevelDiffGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6394

            return self._parent._cast(_6394.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6395.StraightBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6395

            return self._parent._cast(_6395.StraightBevelGearDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6397.StraightBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6397

            return self._parent._cast(_6397.StraightBevelGearSetDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6398.StraightBevelPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6398

            return self._parent._cast(_6398.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6399.StraightBevelSunGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6399

            return self._parent._cast(_6399.StraightBevelSunGearDynamicAnalysis)

        @property
        def synchroniser_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6400.SynchroniserDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6400

            return self._parent._cast(_6400.SynchroniserDynamicAnalysis)

        @property
        def synchroniser_half_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6401.SynchroniserHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6401

            return self._parent._cast(_6401.SynchroniserHalfDynamicAnalysis)

        @property
        def synchroniser_part_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6402.SynchroniserPartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6402

            return self._parent._cast(_6402.SynchroniserPartDynamicAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6403.SynchroniserSleeveDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403

            return self._parent._cast(_6403.SynchroniserSleeveDynamicAnalysis)

        @property
        def torque_converter_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6405.TorqueConverterDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6405

            return self._parent._cast(_6405.TorqueConverterDynamicAnalysis)

        @property
        def torque_converter_pump_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6406.TorqueConverterPumpDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6406

            return self._parent._cast(_6406.TorqueConverterPumpDynamicAnalysis)

        @property
        def torque_converter_turbine_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6407.TorqueConverterTurbineDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6407

            return self._parent._cast(_6407.TorqueConverterTurbineDynamicAnalysis)

        @property
        def unbalanced_mass_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6408.UnbalancedMassDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6408

            return self._parent._cast(_6408.UnbalancedMassDynamicAnalysis)

        @property
        def virtual_component_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6409.VirtualComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6409

            return self._parent._cast(_6409.VirtualComponentDynamicAnalysis)

        @property
        def worm_gear_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6410.WormGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6410

            return self._parent._cast(_6410.WormGearDynamicAnalysis)

        @property
        def worm_gear_set_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6412.WormGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6412

            return self._parent._cast(_6412.WormGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6413.ZerolBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6413

            return self._parent._cast(_6413.ZerolBevelGearDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "_6415.ZerolBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6415

            return self._parent._cast(_6415.ZerolBevelGearSetDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis",
        ) -> "PartDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "PartDynamicAnalysis._Cast_PartDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2475.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def dynamic_analysis(self: Self) -> "_6337.DynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.DynamicAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "PartDynamicAnalysis._Cast_PartDynamicAnalysis":
        return self._Cast_PartDynamicAnalysis(self)
