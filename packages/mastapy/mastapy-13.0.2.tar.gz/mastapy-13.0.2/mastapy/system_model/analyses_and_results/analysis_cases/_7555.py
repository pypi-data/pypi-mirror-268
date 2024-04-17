"""PartFEAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.analysis_cases import _7556
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_FE_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases", "PartFEAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2693,
        _2694,
        _2695,
        _2698,
        _2699,
        _2700,
        _2706,
        _2708,
        _2710,
        _2711,
        _2712,
        _2713,
        _2715,
        _2716,
        _2717,
        _2718,
        _2720,
        _2721,
        _2723,
        _2726,
        _2727,
        _2729,
        _2730,
        _2733,
        _2734,
        _2736,
        _2738,
        _2739,
        _2741,
        _2742,
        _2743,
        _2746,
        _2750,
        _2751,
        _2752,
        _2753,
        _2754,
        _2755,
        _2758,
        _2759,
        _2760,
        _2763,
        _2764,
        _2765,
        _2766,
        _2768,
        _2769,
        _2770,
        _2772,
        _2773,
        _2777,
        _2778,
        _2780,
        _2781,
        _2783,
        _2784,
        _2787,
        _2788,
        _2790,
        _2792,
        _2793,
        _2795,
        _2796,
        _2798,
        _2799,
        _2800,
        _2801,
        _2802,
        _2805,
        _2807,
        _2808,
        _2809,
        _2812,
        _2814,
        _2816,
        _2817,
        _2819,
        _2820,
        _2822,
        _2823,
        _2825,
        _2826,
        _2827,
        _2828,
        _2829,
        _2830,
        _2831,
        _2832,
        _2837,
        _2838,
        _2839,
        _2842,
        _2843,
        _2845,
        _2846,
        _2848,
        _2849,
    )
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
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
        _6366,
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
    from mastapy.system_model.analyses_and_results.analysis_cases import _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartFEAnalysis",)


Self = TypeVar("Self", bound="PartFEAnalysis")


class PartFEAnalysis(_7556.PartStaticLoadAnalysisCase):
    """PartFEAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_FE_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartFEAnalysis")

    class _Cast_PartFEAnalysis:
        """Special nested class for casting PartFEAnalysis to subclasses."""

        def __init__(
            self: "PartFEAnalysis._Cast_PartFEAnalysis", parent: "PartFEAnalysis"
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2693.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2693,
            )

            return self._parent._cast(_2693.AbstractAssemblySystemDeflection)

        @property
        def abstract_shaft_or_housing_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2694.AbstractShaftOrHousingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2694,
            )

            return self._parent._cast(_2694.AbstractShaftOrHousingSystemDeflection)

        @property
        def abstract_shaft_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2695.AbstractShaftSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2695,
            )

            return self._parent._cast(_2695.AbstractShaftSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2698.AGMAGleasonConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2698,
            )

            return self._parent._cast(_2698.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2699.AGMAGleasonConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2699,
            )

            return self._parent._cast(_2699.AGMAGleasonConicalGearSystemDeflection)

        @property
        def assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2700.AssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2700,
            )

            return self._parent._cast(_2700.AssemblySystemDeflection)

        @property
        def bearing_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2706.BearingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2706,
            )

            return self._parent._cast(_2706.BearingSystemDeflection)

        @property
        def belt_drive_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2708.BeltDriveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2708,
            )

            return self._parent._cast(_2708.BeltDriveSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2710.BevelDifferentialGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2710,
            )

            return self._parent._cast(_2710.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2711.BevelDifferentialGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2711,
            )

            return self._parent._cast(_2711.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2712.BevelDifferentialPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2713.BevelDifferentialSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2715.BevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.BevelGearSetSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2716.BevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2716,
            )

            return self._parent._cast(_2716.BevelGearSystemDeflection)

        @property
        def bolted_joint_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2717.BoltedJointSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2717,
            )

            return self._parent._cast(_2717.BoltedJointSystemDeflection)

        @property
        def bolt_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2718.BoltSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2718,
            )

            return self._parent._cast(_2718.BoltSystemDeflection)

        @property
        def clutch_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2720.ClutchHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2720,
            )

            return self._parent._cast(_2720.ClutchHalfSystemDeflection)

        @property
        def clutch_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2721.ClutchSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2721,
            )

            return self._parent._cast(_2721.ClutchSystemDeflection)

        @property
        def component_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2723.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.ComponentSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2726.ConceptCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2726,
            )

            return self._parent._cast(_2726.ConceptCouplingHalfSystemDeflection)

        @property
        def concept_coupling_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2727.ConceptCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.ConceptCouplingSystemDeflection)

        @property
        def concept_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2729.ConceptGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2729,
            )

            return self._parent._cast(_2729.ConceptGearSetSystemDeflection)

        @property
        def concept_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2730.ConceptGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2730,
            )

            return self._parent._cast(_2730.ConceptGearSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2733.ConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2733,
            )

            return self._parent._cast(_2733.ConicalGearSetSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2734.ConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2734,
            )

            return self._parent._cast(_2734.ConicalGearSystemDeflection)

        @property
        def connector_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2736.ConnectorSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(_2736.ConnectorSystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2738.CouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.CouplingHalfSystemDeflection)

        @property
        def coupling_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2739.CouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2739,
            )

            return self._parent._cast(_2739.CouplingSystemDeflection)

        @property
        def cvt_pulley_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2741.CVTPulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2741,
            )

            return self._parent._cast(_2741.CVTPulleySystemDeflection)

        @property
        def cvt_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2742.CVTSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2742,
            )

            return self._parent._cast(_2742.CVTSystemDeflection)

        @property
        def cycloidal_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2743.CycloidalAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2743,
            )

            return self._parent._cast(_2743.CycloidalAssemblySystemDeflection)

        @property
        def cycloidal_disc_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2746.CycloidalDiscSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2746,
            )

            return self._parent._cast(_2746.CycloidalDiscSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2750.CylindricalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2750,
            )

            return self._parent._cast(_2750.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2751.CylindricalGearSetSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2751,
            )

            return self._parent._cast(_2751.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2752.CylindricalGearSetSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2752,
            )

            return self._parent._cast(
                _2752.CylindricalGearSetSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2753.CylindricalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2753,
            )

            return self._parent._cast(_2753.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2754.CylindricalGearSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2754,
            )

            return self._parent._cast(_2754.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2755.CylindricalGearSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2755,
            )

            return self._parent._cast(
                _2755.CylindricalGearSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2758.CylindricalPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.CylindricalPlanetGearSystemDeflection)

        @property
        def datum_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2759.DatumSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2759,
            )

            return self._parent._cast(_2759.DatumSystemDeflection)

        @property
        def external_cad_model_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2760.ExternalCADModelSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2760,
            )

            return self._parent._cast(_2760.ExternalCADModelSystemDeflection)

        @property
        def face_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2763.FaceGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2763,
            )

            return self._parent._cast(_2763.FaceGearSetSystemDeflection)

        @property
        def face_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2764.FaceGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2764,
            )

            return self._parent._cast(_2764.FaceGearSystemDeflection)

        @property
        def fe_part_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2765.FEPartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2765,
            )

            return self._parent._cast(_2765.FEPartSystemDeflection)

        @property
        def flexible_pin_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2766.FlexiblePinAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2766,
            )

            return self._parent._cast(_2766.FlexiblePinAssemblySystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2768.GearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2768,
            )

            return self._parent._cast(_2768.GearSetSystemDeflection)

        @property
        def gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2769.GearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2769,
            )

            return self._parent._cast(_2769.GearSystemDeflection)

        @property
        def guide_dxf_model_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2770.GuideDxfModelSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2770,
            )

            return self._parent._cast(_2770.GuideDxfModelSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2772.HypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2772,
            )

            return self._parent._cast(_2772.HypoidGearSetSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2773.HypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2773,
            )

            return self._parent._cast(_2773.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2777.KlingelnbergCycloPalloidConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2777,
            )

            return self._parent._cast(
                _2777.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2778.KlingelnbergCycloPalloidConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2778,
            )

            return self._parent._cast(
                _2778.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2780.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2780,
            )

            return self._parent._cast(
                _2780.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2781.KlingelnbergCycloPalloidHypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2781,
            )

            return self._parent._cast(
                _2781.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2783.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(
                _2783.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2784.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(
                _2784.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def mass_disc_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2787.MassDiscSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2788.MeasurementComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2788,
            )

            return self._parent._cast(_2788.MeasurementComponentSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2790.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(_2790.MountableComponentSystemDeflection)

        @property
        def oil_seal_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2792.OilSealSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2792,
            )

            return self._parent._cast(_2792.OilSealSystemDeflection)

        @property
        def part_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2793.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.PartSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2795.PartToPartShearCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2795,
            )

            return self._parent._cast(_2795.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def part_to_part_shear_coupling_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2796.PartToPartShearCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2796,
            )

            return self._parent._cast(_2796.PartToPartShearCouplingSystemDeflection)

        @property
        def planet_carrier_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2798.PlanetCarrierSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2798,
            )

            return self._parent._cast(_2798.PlanetCarrierSystemDeflection)

        @property
        def point_load_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2799.PointLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2799,
            )

            return self._parent._cast(_2799.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2800.PowerLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2800,
            )

            return self._parent._cast(_2800.PowerLoadSystemDeflection)

        @property
        def pulley_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2801.PulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2801,
            )

            return self._parent._cast(_2801.PulleySystemDeflection)

        @property
        def ring_pins_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2802.RingPinsSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2802,
            )

            return self._parent._cast(_2802.RingPinsSystemDeflection)

        @property
        def rolling_ring_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2805.RollingRingAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2805,
            )

            return self._parent._cast(_2805.RollingRingAssemblySystemDeflection)

        @property
        def rolling_ring_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2807.RollingRingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2807,
            )

            return self._parent._cast(_2807.RollingRingSystemDeflection)

        @property
        def root_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2808.RootAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.RootAssemblySystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2809.ShaftHubConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2809,
            )

            return self._parent._cast(_2809.ShaftHubConnectionSystemDeflection)

        @property
        def shaft_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2812.ShaftSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2812,
            )

            return self._parent._cast(_2812.ShaftSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2814.SpecialisedAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2814,
            )

            return self._parent._cast(_2814.SpecialisedAssemblySystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2816.SpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2816,
            )

            return self._parent._cast(_2816.SpiralBevelGearSetSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2817.SpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.SpiralBevelGearSystemDeflection)

        @property
        def spring_damper_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2819.SpringDamperHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2819,
            )

            return self._parent._cast(_2819.SpringDamperHalfSystemDeflection)

        @property
        def spring_damper_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2820.SpringDamperSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2820,
            )

            return self._parent._cast(_2820.SpringDamperSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2822.StraightBevelDiffGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2822,
            )

            return self._parent._cast(_2822.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2823.StraightBevelDiffGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2823,
            )

            return self._parent._cast(_2823.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2825.StraightBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2825,
            )

            return self._parent._cast(_2825.StraightBevelGearSetSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2826.StraightBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2826,
            )

            return self._parent._cast(_2826.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2827.StraightBevelPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2827,
            )

            return self._parent._cast(_2827.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2828.StraightBevelSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2828,
            )

            return self._parent._cast(_2828.StraightBevelSunGearSystemDeflection)

        @property
        def synchroniser_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2829.SynchroniserHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2829,
            )

            return self._parent._cast(_2829.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2830.SynchroniserPartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2830,
            )

            return self._parent._cast(_2830.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2831.SynchroniserSleeveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2831,
            )

            return self._parent._cast(_2831.SynchroniserSleeveSystemDeflection)

        @property
        def synchroniser_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2832.SynchroniserSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2832,
            )

            return self._parent._cast(_2832.SynchroniserSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2837.TorqueConverterPumpSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2838.TorqueConverterSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2838,
            )

            return self._parent._cast(_2838.TorqueConverterSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2839.TorqueConverterTurbineSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2839,
            )

            return self._parent._cast(_2839.TorqueConverterTurbineSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2842.UnbalancedMassSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2842,
            )

            return self._parent._cast(_2842.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2843.VirtualComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2843,
            )

            return self._parent._cast(_2843.VirtualComponentSystemDeflection)

        @property
        def worm_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2845.WormGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2845,
            )

            return self._parent._cast(_2845.WormGearSetSystemDeflection)

        @property
        def worm_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2846.WormGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2846,
            )

            return self._parent._cast(_2846.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2848.ZerolBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2848,
            )

            return self._parent._cast(_2848.ZerolBevelGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2849.ZerolBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2849,
            )

            return self._parent._cast(_2849.ZerolBevelGearSystemDeflection)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6285.AbstractAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6285

            return self._parent._cast(_6285.AbstractAssemblyDynamicAnalysis)

        @property
        def abstract_shaft_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6286.AbstractShaftDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6286

            return self._parent._cast(_6286.AbstractShaftDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6287.AbstractShaftOrHousingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6287

            return self._parent._cast(_6287.AbstractShaftOrHousingDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6289.AGMAGleasonConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6289

            return self._parent._cast(_6289.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6291.AGMAGleasonConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6291

            return self._parent._cast(_6291.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6292.AssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6292

            return self._parent._cast(_6292.AssemblyDynamicAnalysis)

        @property
        def bearing_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6293.BearingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6293

            return self._parent._cast(_6293.BearingDynamicAnalysis)

        @property
        def belt_drive_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6295.BeltDriveDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6295

            return self._parent._cast(_6295.BeltDriveDynamicAnalysis)

        @property
        def bevel_differential_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6296.BevelDifferentialGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6296

            return self._parent._cast(_6296.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6298.BevelDifferentialGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298

            return self._parent._cast(_6298.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6299.BevelDifferentialPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299

            return self._parent._cast(_6299.BevelDifferentialPlanetGearDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6300.BevelDifferentialSunGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6300

            return self._parent._cast(_6300.BevelDifferentialSunGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6301.BevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301

            return self._parent._cast(_6301.BevelGearDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6303.BevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303

            return self._parent._cast(_6303.BevelGearSetDynamicAnalysis)

        @property
        def bolt_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6304.BoltDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304

            return self._parent._cast(_6304.BoltDynamicAnalysis)

        @property
        def bolted_joint_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6305.BoltedJointDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6305

            return self._parent._cast(_6305.BoltedJointDynamicAnalysis)

        @property
        def clutch_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6307.ClutchDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307

            return self._parent._cast(_6307.ClutchDynamicAnalysis)

        @property
        def clutch_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6308.ClutchHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6308

            return self._parent._cast(_6308.ClutchHalfDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6310.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.ComponentDynamicAnalysis)

        @property
        def concept_coupling_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6312.ConceptCouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312

            return self._parent._cast(_6312.ConceptCouplingDynamicAnalysis)

        @property
        def concept_coupling_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6313.ConceptCouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6313

            return self._parent._cast(_6313.ConceptCouplingHalfDynamicAnalysis)

        @property
        def concept_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6314.ConceptGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6314

            return self._parent._cast(_6314.ConceptGearDynamicAnalysis)

        @property
        def concept_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6316.ConceptGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316

            return self._parent._cast(_6316.ConceptGearSetDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6317.ConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6317

            return self._parent._cast(_6317.ConicalGearDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6319.ConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6319

            return self._parent._cast(_6319.ConicalGearSetDynamicAnalysis)

        @property
        def connector_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6321.ConnectorDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321

            return self._parent._cast(_6321.ConnectorDynamicAnalysis)

        @property
        def coupling_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6323.CouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323

            return self._parent._cast(_6323.CouplingDynamicAnalysis)

        @property
        def coupling_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6324.CouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6324

            return self._parent._cast(_6324.CouplingHalfDynamicAnalysis)

        @property
        def cvt_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6326.CVTDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6326

            return self._parent._cast(_6326.CVTDynamicAnalysis)

        @property
        def cvt_pulley_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6327.CVTPulleyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6327

            return self._parent._cast(_6327.CVTPulleyDynamicAnalysis)

        @property
        def cycloidal_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6328.CycloidalAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328

            return self._parent._cast(_6328.CycloidalAssemblyDynamicAnalysis)

        @property
        def cycloidal_disc_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6330.CycloidalDiscDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6330

            return self._parent._cast(_6330.CycloidalDiscDynamicAnalysis)

        @property
        def cylindrical_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6332.CylindricalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6332

            return self._parent._cast(_6332.CylindricalGearDynamicAnalysis)

        @property
        def cylindrical_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6334.CylindricalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334

            return self._parent._cast(_6334.CylindricalGearSetDynamicAnalysis)

        @property
        def cylindrical_planet_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6335.CylindricalPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335

            return self._parent._cast(_6335.CylindricalPlanetGearDynamicAnalysis)

        @property
        def datum_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6336.DatumDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6336

            return self._parent._cast(_6336.DatumDynamicAnalysis)

        @property
        def external_cad_model_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6339.ExternalCADModelDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6339

            return self._parent._cast(_6339.ExternalCADModelDynamicAnalysis)

        @property
        def face_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6340.FaceGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6340

            return self._parent._cast(_6340.FaceGearDynamicAnalysis)

        @property
        def face_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6342.FaceGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342

            return self._parent._cast(_6342.FaceGearSetDynamicAnalysis)

        @property
        def fe_part_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6343.FEPartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6343

            return self._parent._cast(_6343.FEPartDynamicAnalysis)

        @property
        def flexible_pin_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6344.FlexiblePinAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6344

            return self._parent._cast(_6344.FlexiblePinAssemblyDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6345.GearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6345

            return self._parent._cast(_6345.GearDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6347.GearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6347

            return self._parent._cast(_6347.GearSetDynamicAnalysis)

        @property
        def guide_dxf_model_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6348.GuideDxfModelDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6348

            return self._parent._cast(_6348.GuideDxfModelDynamicAnalysis)

        @property
        def hypoid_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6349.HypoidGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6349

            return self._parent._cast(_6349.HypoidGearDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6351.HypoidGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6351

            return self._parent._cast(_6351.HypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6353.KlingelnbergCycloPalloidConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353

            return self._parent._cast(
                _6353.KlingelnbergCycloPalloidConicalGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6355.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(
                _6355.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6356.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356

            return self._parent._cast(
                _6356.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6358.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(
                _6358.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6359.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6359

            return self._parent._cast(
                _6359.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6361.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6361

            return self._parent._cast(
                _6361.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis
            )

        @property
        def mass_disc_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6362.MassDiscDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6362

            return self._parent._cast(_6362.MassDiscDynamicAnalysis)

        @property
        def measurement_component_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6363.MeasurementComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363

            return self._parent._cast(_6363.MeasurementComponentDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6364.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364

            return self._parent._cast(_6364.MountableComponentDynamicAnalysis)

        @property
        def oil_seal_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6365.OilSealDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6365

            return self._parent._cast(_6365.OilSealDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6366.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.PartDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6368.PartToPartShearCouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6368

            return self._parent._cast(_6368.PartToPartShearCouplingDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6369.PartToPartShearCouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6369

            return self._parent._cast(_6369.PartToPartShearCouplingHalfDynamicAnalysis)

        @property
        def planetary_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6371.PlanetaryGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6371

            return self._parent._cast(_6371.PlanetaryGearSetDynamicAnalysis)

        @property
        def planet_carrier_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6372.PlanetCarrierDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6372

            return self._parent._cast(_6372.PlanetCarrierDynamicAnalysis)

        @property
        def point_load_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6373.PointLoadDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6373

            return self._parent._cast(_6373.PointLoadDynamicAnalysis)

        @property
        def power_load_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6374.PowerLoadDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6374

            return self._parent._cast(_6374.PowerLoadDynamicAnalysis)

        @property
        def pulley_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6375.PulleyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6375

            return self._parent._cast(_6375.PulleyDynamicAnalysis)

        @property
        def ring_pins_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6376.RingPinsDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376

            return self._parent._cast(_6376.RingPinsDynamicAnalysis)

        @property
        def rolling_ring_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6378.RollingRingAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6378

            return self._parent._cast(_6378.RollingRingAssemblyDynamicAnalysis)

        @property
        def rolling_ring_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6380.RollingRingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6380

            return self._parent._cast(_6380.RollingRingDynamicAnalysis)

        @property
        def root_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6381.RootAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6381

            return self._parent._cast(_6381.RootAssemblyDynamicAnalysis)

        @property
        def shaft_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6382.ShaftDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.ShaftDynamicAnalysis)

        @property
        def shaft_hub_connection_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6383.ShaftHubConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6383

            return self._parent._cast(_6383.ShaftHubConnectionDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6385.SpecialisedAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6385

            return self._parent._cast(_6385.SpecialisedAssemblyDynamicAnalysis)

        @property
        def spiral_bevel_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6386.SpiralBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6386

            return self._parent._cast(_6386.SpiralBevelGearDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6388.SpiralBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6388

            return self._parent._cast(_6388.SpiralBevelGearSetDynamicAnalysis)

        @property
        def spring_damper_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6390.SpringDamperDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6390

            return self._parent._cast(_6390.SpringDamperDynamicAnalysis)

        @property
        def spring_damper_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6391.SpringDamperHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6391

            return self._parent._cast(_6391.SpringDamperHalfDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6392.StraightBevelDiffGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6392

            return self._parent._cast(_6392.StraightBevelDiffGearDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6394.StraightBevelDiffGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6394

            return self._parent._cast(_6394.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6395.StraightBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6395

            return self._parent._cast(_6395.StraightBevelGearDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6397.StraightBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6397

            return self._parent._cast(_6397.StraightBevelGearSetDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6398.StraightBevelPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6398

            return self._parent._cast(_6398.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6399.StraightBevelSunGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6399

            return self._parent._cast(_6399.StraightBevelSunGearDynamicAnalysis)

        @property
        def synchroniser_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6400.SynchroniserDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6400

            return self._parent._cast(_6400.SynchroniserDynamicAnalysis)

        @property
        def synchroniser_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6401.SynchroniserHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6401

            return self._parent._cast(_6401.SynchroniserHalfDynamicAnalysis)

        @property
        def synchroniser_part_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6402.SynchroniserPartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6402

            return self._parent._cast(_6402.SynchroniserPartDynamicAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6403.SynchroniserSleeveDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403

            return self._parent._cast(_6403.SynchroniserSleeveDynamicAnalysis)

        @property
        def torque_converter_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6405.TorqueConverterDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6405

            return self._parent._cast(_6405.TorqueConverterDynamicAnalysis)

        @property
        def torque_converter_pump_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6406.TorqueConverterPumpDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6406

            return self._parent._cast(_6406.TorqueConverterPumpDynamicAnalysis)

        @property
        def torque_converter_turbine_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6407.TorqueConverterTurbineDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6407

            return self._parent._cast(_6407.TorqueConverterTurbineDynamicAnalysis)

        @property
        def unbalanced_mass_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6408.UnbalancedMassDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6408

            return self._parent._cast(_6408.UnbalancedMassDynamicAnalysis)

        @property
        def virtual_component_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6409.VirtualComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6409

            return self._parent._cast(_6409.VirtualComponentDynamicAnalysis)

        @property
        def worm_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6410.WormGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6410

            return self._parent._cast(_6410.WormGearDynamicAnalysis)

        @property
        def worm_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6412.WormGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6412

            return self._parent._cast(_6412.WormGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6413.ZerolBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6413

            return self._parent._cast(_6413.ZerolBevelGearDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6415.ZerolBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6415

            return self._parent._cast(_6415.ZerolBevelGearSetDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "PartFEAnalysis":
            return self._parent

        def __getattr__(self: "PartFEAnalysis._Cast_PartFEAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartFEAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "PartFEAnalysis._Cast_PartFEAnalysis":
        return self._Cast_PartFEAnalysis(self)
