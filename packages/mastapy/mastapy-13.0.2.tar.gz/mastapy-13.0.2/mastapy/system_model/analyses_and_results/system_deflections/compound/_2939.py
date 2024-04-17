"""PartCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7554
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "PartCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2793
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2859,
        _2860,
        _2861,
        _2863,
        _2865,
        _2866,
        _2867,
        _2869,
        _2870,
        _2872,
        _2873,
        _2874,
        _2875,
        _2877,
        _2878,
        _2879,
        _2880,
        _2882,
        _2884,
        _2885,
        _2887,
        _2888,
        _2890,
        _2891,
        _2893,
        _2895,
        _2896,
        _2898,
        _2900,
        _2901,
        _2902,
        _2904,
        _2906,
        _2908,
        _2909,
        _2910,
        _2912,
        _2913,
        _2915,
        _2916,
        _2917,
        _2918,
        _2920,
        _2921,
        _2922,
        _2924,
        _2926,
        _2928,
        _2929,
        _2931,
        _2932,
        _2934,
        _2935,
        _2936,
        _2937,
        _2938,
        _2940,
        _2942,
        _2944,
        _2945,
        _2946,
        _2947,
        _2948,
        _2949,
        _2951,
        _2952,
        _2954,
        _2955,
        _2957,
        _2959,
        _2960,
        _2962,
        _2963,
        _2965,
        _2966,
        _2968,
        _2969,
        _2971,
        _2972,
        _2973,
        _2974,
        _2975,
        _2976,
        _2977,
        _2978,
        _2980,
        _2981,
        _2982,
        _2983,
        _2984,
        _2986,
        _2987,
        _2989,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundSystemDeflection",)


Self = TypeVar("Self", bound="PartCompoundSystemDeflection")


class PartCompoundSystemDeflection(_7554.PartCompoundAnalysis):
    """PartCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartCompoundSystemDeflection")

    class _Cast_PartCompoundSystemDeflection:
        """Special nested class for casting PartCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
            parent: "PartCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_compound_analysis(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2859.AbstractAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2859,
            )

            return self._parent._cast(_2859.AbstractAssemblyCompoundSystemDeflection)

        @property
        def abstract_shaft_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2860.AbstractShaftCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2860,
            )

            return self._parent._cast(_2860.AbstractShaftCompoundSystemDeflection)

        @property
        def abstract_shaft_or_housing_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2861.AbstractShaftOrHousingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2861,
            )

            return self._parent._cast(
                _2861.AbstractShaftOrHousingCompoundSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2863.AGMAGleasonConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2863,
            )

            return self._parent._cast(
                _2863.AGMAGleasonConicalGearCompoundSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2865.AGMAGleasonConicalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2865,
            )

            return self._parent._cast(
                _2865.AGMAGleasonConicalGearSetCompoundSystemDeflection
            )

        @property
        def assembly_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2866.AssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2866,
            )

            return self._parent._cast(_2866.AssemblyCompoundSystemDeflection)

        @property
        def bearing_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2867.BearingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2867,
            )

            return self._parent._cast(_2867.BearingCompoundSystemDeflection)

        @property
        def belt_drive_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2869.BeltDriveCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2869,
            )

            return self._parent._cast(_2869.BeltDriveCompoundSystemDeflection)

        @property
        def bevel_differential_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2870.BevelDifferentialGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2870,
            )

            return self._parent._cast(
                _2870.BevelDifferentialGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2872.BevelDifferentialGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2872,
            )

            return self._parent._cast(
                _2872.BevelDifferentialGearSetCompoundSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2873.BevelDifferentialPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2873,
            )

            return self._parent._cast(
                _2873.BevelDifferentialPlanetGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2874.BevelDifferentialSunGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2874,
            )

            return self._parent._cast(
                _2874.BevelDifferentialSunGearCompoundSystemDeflection
            )

        @property
        def bevel_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2875.BevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2875,
            )

            return self._parent._cast(_2875.BevelGearCompoundSystemDeflection)

        @property
        def bevel_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2877.BevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2877,
            )

            return self._parent._cast(_2877.BevelGearSetCompoundSystemDeflection)

        @property
        def bolt_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2878.BoltCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2878,
            )

            return self._parent._cast(_2878.BoltCompoundSystemDeflection)

        @property
        def bolted_joint_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2879.BoltedJointCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2879,
            )

            return self._parent._cast(_2879.BoltedJointCompoundSystemDeflection)

        @property
        def clutch_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2880.ClutchCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2880,
            )

            return self._parent._cast(_2880.ClutchCompoundSystemDeflection)

        @property
        def clutch_half_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2882.ClutchHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2882,
            )

            return self._parent._cast(_2882.ClutchHalfCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2884.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(_2884.ComponentCompoundSystemDeflection)

        @property
        def concept_coupling_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2885.ConceptCouplingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2885,
            )

            return self._parent._cast(_2885.ConceptCouplingCompoundSystemDeflection)

        @property
        def concept_coupling_half_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2887.ConceptCouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2887,
            )

            return self._parent._cast(_2887.ConceptCouplingHalfCompoundSystemDeflection)

        @property
        def concept_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2888.ConceptGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2888,
            )

            return self._parent._cast(_2888.ConceptGearCompoundSystemDeflection)

        @property
        def concept_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2890.ConceptGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2890,
            )

            return self._parent._cast(_2890.ConceptGearSetCompoundSystemDeflection)

        @property
        def conical_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2891.ConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2891,
            )

            return self._parent._cast(_2891.ConicalGearCompoundSystemDeflection)

        @property
        def conical_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2893.ConicalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2893,
            )

            return self._parent._cast(_2893.ConicalGearSetCompoundSystemDeflection)

        @property
        def connector_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2895.ConnectorCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2895,
            )

            return self._parent._cast(_2895.ConnectorCompoundSystemDeflection)

        @property
        def coupling_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2896.CouplingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2896,
            )

            return self._parent._cast(_2896.CouplingCompoundSystemDeflection)

        @property
        def coupling_half_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2898.CouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2898,
            )

            return self._parent._cast(_2898.CouplingHalfCompoundSystemDeflection)

        @property
        def cvt_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2900.CVTCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2900,
            )

            return self._parent._cast(_2900.CVTCompoundSystemDeflection)

        @property
        def cvt_pulley_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2901.CVTPulleyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2901,
            )

            return self._parent._cast(_2901.CVTPulleyCompoundSystemDeflection)

        @property
        def cycloidal_assembly_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2902.CycloidalAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2902,
            )

            return self._parent._cast(_2902.CycloidalAssemblyCompoundSystemDeflection)

        @property
        def cycloidal_disc_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2904.CycloidalDiscCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2904,
            )

            return self._parent._cast(_2904.CycloidalDiscCompoundSystemDeflection)

        @property
        def cylindrical_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2906.CylindricalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2906,
            )

            return self._parent._cast(_2906.CylindricalGearCompoundSystemDeflection)

        @property
        def cylindrical_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2908.CylindricalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2908,
            )

            return self._parent._cast(_2908.CylindricalGearSetCompoundSystemDeflection)

        @property
        def cylindrical_planet_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2909.CylindricalPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2909,
            )

            return self._parent._cast(
                _2909.CylindricalPlanetGearCompoundSystemDeflection
            )

        @property
        def datum_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2910.DatumCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2910,
            )

            return self._parent._cast(_2910.DatumCompoundSystemDeflection)

        @property
        def external_cad_model_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2912.ExternalCADModelCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2912,
            )

            return self._parent._cast(_2912.ExternalCADModelCompoundSystemDeflection)

        @property
        def face_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2913.FaceGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2913,
            )

            return self._parent._cast(_2913.FaceGearCompoundSystemDeflection)

        @property
        def face_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2915.FaceGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2915,
            )

            return self._parent._cast(_2915.FaceGearSetCompoundSystemDeflection)

        @property
        def fe_part_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2916.FEPartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2916,
            )

            return self._parent._cast(_2916.FEPartCompoundSystemDeflection)

        @property
        def flexible_pin_assembly_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2917.FlexiblePinAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2917,
            )

            return self._parent._cast(_2917.FlexiblePinAssemblyCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2918.GearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2918,
            )

            return self._parent._cast(_2918.GearCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2920.GearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2920,
            )

            return self._parent._cast(_2920.GearSetCompoundSystemDeflection)

        @property
        def guide_dxf_model_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2921.GuideDxfModelCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2921,
            )

            return self._parent._cast(_2921.GuideDxfModelCompoundSystemDeflection)

        @property
        def hypoid_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2922.HypoidGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2922,
            )

            return self._parent._cast(_2922.HypoidGearCompoundSystemDeflection)

        @property
        def hypoid_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2924.HypoidGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2924,
            )

            return self._parent._cast(_2924.HypoidGearSetCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2926.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2926,
            )

            return self._parent._cast(
                _2926.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2928.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2928,
            )

            return self._parent._cast(
                _2928.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2929.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(
                _2929.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2931.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(
                _2931.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2932.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2932,
            )

            return self._parent._cast(
                _2932.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2934.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2934,
            )

            return self._parent._cast(
                _2934.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection
            )

        @property
        def mass_disc_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2935.MassDiscCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2935,
            )

            return self._parent._cast(_2935.MassDiscCompoundSystemDeflection)

        @property
        def measurement_component_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2936.MeasurementComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2936,
            )

            return self._parent._cast(
                _2936.MeasurementComponentCompoundSystemDeflection
            )

        @property
        def mountable_component_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2937.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2937,
            )

            return self._parent._cast(_2937.MountableComponentCompoundSystemDeflection)

        @property
        def oil_seal_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2938.OilSealCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2938,
            )

            return self._parent._cast(_2938.OilSealCompoundSystemDeflection)

        @property
        def part_to_part_shear_coupling_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2940.PartToPartShearCouplingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2940,
            )

            return self._parent._cast(
                _2940.PartToPartShearCouplingCompoundSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_half_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2942.PartToPartShearCouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2942,
            )

            return self._parent._cast(
                _2942.PartToPartShearCouplingHalfCompoundSystemDeflection
            )

        @property
        def planetary_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2944.PlanetaryGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2944,
            )

            return self._parent._cast(_2944.PlanetaryGearSetCompoundSystemDeflection)

        @property
        def planet_carrier_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2945.PlanetCarrierCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2945,
            )

            return self._parent._cast(_2945.PlanetCarrierCompoundSystemDeflection)

        @property
        def point_load_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2946.PointLoadCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2946,
            )

            return self._parent._cast(_2946.PointLoadCompoundSystemDeflection)

        @property
        def power_load_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2947.PowerLoadCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2947,
            )

            return self._parent._cast(_2947.PowerLoadCompoundSystemDeflection)

        @property
        def pulley_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2948.PulleyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2948,
            )

            return self._parent._cast(_2948.PulleyCompoundSystemDeflection)

        @property
        def ring_pins_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2949.RingPinsCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2949,
            )

            return self._parent._cast(_2949.RingPinsCompoundSystemDeflection)

        @property
        def rolling_ring_assembly_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2951.RollingRingAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2951,
            )

            return self._parent._cast(_2951.RollingRingAssemblyCompoundSystemDeflection)

        @property
        def rolling_ring_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2952.RollingRingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.RollingRingCompoundSystemDeflection)

        @property
        def root_assembly_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2954.RootAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(_2954.RootAssemblyCompoundSystemDeflection)

        @property
        def shaft_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2955.ShaftCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2955,
            )

            return self._parent._cast(_2955.ShaftCompoundSystemDeflection)

        @property
        def shaft_hub_connection_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2957.ShaftHubConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2957,
            )

            return self._parent._cast(_2957.ShaftHubConnectionCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2959.SpecialisedAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2959,
            )

            return self._parent._cast(_2959.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2960.SpiralBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2960,
            )

            return self._parent._cast(_2960.SpiralBevelGearCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2962.SpiralBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2962,
            )

            return self._parent._cast(_2962.SpiralBevelGearSetCompoundSystemDeflection)

        @property
        def spring_damper_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2963.SpringDamperCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2963,
            )

            return self._parent._cast(_2963.SpringDamperCompoundSystemDeflection)

        @property
        def spring_damper_half_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2965.SpringDamperHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2965,
            )

            return self._parent._cast(_2965.SpringDamperHalfCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2966.StraightBevelDiffGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2966,
            )

            return self._parent._cast(
                _2966.StraightBevelDiffGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2968.StraightBevelDiffGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2968,
            )

            return self._parent._cast(
                _2968.StraightBevelDiffGearSetCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2969.StraightBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2969,
            )

            return self._parent._cast(_2969.StraightBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2971.StraightBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2971,
            )

            return self._parent._cast(
                _2971.StraightBevelGearSetCompoundSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2972.StraightBevelPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2972,
            )

            return self._parent._cast(
                _2972.StraightBevelPlanetGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2973.StraightBevelSunGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2973,
            )

            return self._parent._cast(
                _2973.StraightBevelSunGearCompoundSystemDeflection
            )

        @property
        def synchroniser_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2974.SynchroniserCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2974,
            )

            return self._parent._cast(_2974.SynchroniserCompoundSystemDeflection)

        @property
        def synchroniser_half_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2975.SynchroniserHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2975,
            )

            return self._parent._cast(_2975.SynchroniserHalfCompoundSystemDeflection)

        @property
        def synchroniser_part_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2976.SynchroniserPartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2976,
            )

            return self._parent._cast(_2976.SynchroniserPartCompoundSystemDeflection)

        @property
        def synchroniser_sleeve_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2977.SynchroniserSleeveCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2977,
            )

            return self._parent._cast(_2977.SynchroniserSleeveCompoundSystemDeflection)

        @property
        def torque_converter_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2978.TorqueConverterCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2978,
            )

            return self._parent._cast(_2978.TorqueConverterCompoundSystemDeflection)

        @property
        def torque_converter_pump_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2980.TorqueConverterPumpCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2980,
            )

            return self._parent._cast(_2980.TorqueConverterPumpCompoundSystemDeflection)

        @property
        def torque_converter_turbine_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2981.TorqueConverterTurbineCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2981,
            )

            return self._parent._cast(
                _2981.TorqueConverterTurbineCompoundSystemDeflection
            )

        @property
        def unbalanced_mass_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2982.UnbalancedMassCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2982,
            )

            return self._parent._cast(_2982.UnbalancedMassCompoundSystemDeflection)

        @property
        def virtual_component_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2983.VirtualComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2983,
            )

            return self._parent._cast(_2983.VirtualComponentCompoundSystemDeflection)

        @property
        def worm_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2984.WormGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2984,
            )

            return self._parent._cast(_2984.WormGearCompoundSystemDeflection)

        @property
        def worm_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2986.WormGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2986,
            )

            return self._parent._cast(_2986.WormGearSetCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2987.ZerolBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2987,
            )

            return self._parent._cast(_2987.ZerolBevelGearCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "_2989.ZerolBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2989,
            )

            return self._parent._cast(_2989.ZerolBevelGearSetCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "PartCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartCompoundSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_2793.PartSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PartSystemDeflection]

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
    ) -> "List[_2793.PartSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PartSystemDeflection]

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
    ) -> "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection":
        return self._Cast_PartCompoundSystemDeflection(self)
