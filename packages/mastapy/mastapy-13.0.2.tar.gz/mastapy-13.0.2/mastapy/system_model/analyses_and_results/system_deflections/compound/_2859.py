"""AbstractAssemblyCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2939
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "AbstractAssemblyCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2693
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2865,
        _2866,
        _2869,
        _2872,
        _2877,
        _2879,
        _2880,
        _2885,
        _2890,
        _2893,
        _2896,
        _2900,
        _2902,
        _2908,
        _2915,
        _2917,
        _2920,
        _2924,
        _2928,
        _2931,
        _2934,
        _2940,
        _2944,
        _2951,
        _2954,
        _2959,
        _2962,
        _2963,
        _2968,
        _2971,
        _2974,
        _2978,
        _2986,
        _2989,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundSystemDeflection",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundSystemDeflection")


class AbstractAssemblyCompoundSystemDeflection(_2939.PartCompoundSystemDeflection):
    """AbstractAssemblyCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCompoundSystemDeflection"
    )

    class _Cast_AbstractAssemblyCompoundSystemDeflection:
        """Special nested class for casting AbstractAssemblyCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
            parent: "AbstractAssemblyCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2939.PartCompoundSystemDeflection":
            return self._parent._cast(_2939.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2865.AGMAGleasonConicalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2865,
            )

            return self._parent._cast(
                _2865.AGMAGleasonConicalGearSetCompoundSystemDeflection
            )

        @property
        def assembly_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2866.AssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2866,
            )

            return self._parent._cast(_2866.AssemblyCompoundSystemDeflection)

        @property
        def belt_drive_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2869.BeltDriveCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2869,
            )

            return self._parent._cast(_2869.BeltDriveCompoundSystemDeflection)

        @property
        def bevel_differential_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2872.BevelDifferentialGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2872,
            )

            return self._parent._cast(
                _2872.BevelDifferentialGearSetCompoundSystemDeflection
            )

        @property
        def bevel_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2877.BevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2877,
            )

            return self._parent._cast(_2877.BevelGearSetCompoundSystemDeflection)

        @property
        def bolted_joint_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2879.BoltedJointCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2879,
            )

            return self._parent._cast(_2879.BoltedJointCompoundSystemDeflection)

        @property
        def clutch_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2880.ClutchCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2880,
            )

            return self._parent._cast(_2880.ClutchCompoundSystemDeflection)

        @property
        def concept_coupling_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2885.ConceptCouplingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2885,
            )

            return self._parent._cast(_2885.ConceptCouplingCompoundSystemDeflection)

        @property
        def concept_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2890.ConceptGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2890,
            )

            return self._parent._cast(_2890.ConceptGearSetCompoundSystemDeflection)

        @property
        def conical_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2893.ConicalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2893,
            )

            return self._parent._cast(_2893.ConicalGearSetCompoundSystemDeflection)

        @property
        def coupling_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2896.CouplingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2896,
            )

            return self._parent._cast(_2896.CouplingCompoundSystemDeflection)

        @property
        def cvt_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2900.CVTCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2900,
            )

            return self._parent._cast(_2900.CVTCompoundSystemDeflection)

        @property
        def cycloidal_assembly_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2902.CycloidalAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2902,
            )

            return self._parent._cast(_2902.CycloidalAssemblyCompoundSystemDeflection)

        @property
        def cylindrical_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2908.CylindricalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2908,
            )

            return self._parent._cast(_2908.CylindricalGearSetCompoundSystemDeflection)

        @property
        def face_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2915.FaceGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2915,
            )

            return self._parent._cast(_2915.FaceGearSetCompoundSystemDeflection)

        @property
        def flexible_pin_assembly_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2917.FlexiblePinAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2917,
            )

            return self._parent._cast(_2917.FlexiblePinAssemblyCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2920.GearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2920,
            )

            return self._parent._cast(_2920.GearSetCompoundSystemDeflection)

        @property
        def hypoid_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2924.HypoidGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2924,
            )

            return self._parent._cast(_2924.HypoidGearSetCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2928.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2928,
            )

            return self._parent._cast(
                _2928.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2931.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(
                _2931.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2934.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2934,
            )

            return self._parent._cast(
                _2934.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2940.PartToPartShearCouplingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2940,
            )

            return self._parent._cast(
                _2940.PartToPartShearCouplingCompoundSystemDeflection
            )

        @property
        def planetary_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2944.PlanetaryGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2944,
            )

            return self._parent._cast(_2944.PlanetaryGearSetCompoundSystemDeflection)

        @property
        def rolling_ring_assembly_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2951.RollingRingAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2951,
            )

            return self._parent._cast(_2951.RollingRingAssemblyCompoundSystemDeflection)

        @property
        def root_assembly_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2954.RootAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(_2954.RootAssemblyCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2959.SpecialisedAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2959,
            )

            return self._parent._cast(_2959.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2962.SpiralBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2962,
            )

            return self._parent._cast(_2962.SpiralBevelGearSetCompoundSystemDeflection)

        @property
        def spring_damper_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2963.SpringDamperCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2963,
            )

            return self._parent._cast(_2963.SpringDamperCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2968.StraightBevelDiffGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2968,
            )

            return self._parent._cast(
                _2968.StraightBevelDiffGearSetCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2971.StraightBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2971,
            )

            return self._parent._cast(
                _2971.StraightBevelGearSetCompoundSystemDeflection
            )

        @property
        def synchroniser_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2974.SynchroniserCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2974,
            )

            return self._parent._cast(_2974.SynchroniserCompoundSystemDeflection)

        @property
        def torque_converter_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2978.TorqueConverterCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2978,
            )

            return self._parent._cast(_2978.TorqueConverterCompoundSystemDeflection)

        @property
        def worm_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2986.WormGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2986,
            )

            return self._parent._cast(_2986.WormGearSetCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "_2989.ZerolBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2989,
            )

            return self._parent._cast(_2989.ZerolBevelGearSetCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "AbstractAssemblyCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "AbstractAssemblyCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_2693.AbstractAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AbstractAssemblySystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_2693.AbstractAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AbstractAssemblySystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection":
        return self._Cast_AbstractAssemblyCompoundSystemDeflection(self)
