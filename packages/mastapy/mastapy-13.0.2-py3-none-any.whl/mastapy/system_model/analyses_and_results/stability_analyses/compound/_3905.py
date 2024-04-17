"""AbstractAssemblyCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3984
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "AbstractAssemblyCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3771
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3911,
        _3912,
        _3915,
        _3918,
        _3923,
        _3925,
        _3926,
        _3931,
        _3936,
        _3939,
        _3942,
        _3946,
        _3948,
        _3954,
        _3960,
        _3962,
        _3965,
        _3969,
        _3973,
        _3976,
        _3979,
        _3985,
        _3989,
        _3996,
        _3999,
        _4003,
        _4006,
        _4007,
        _4012,
        _4015,
        _4018,
        _4022,
        _4030,
        _4033,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundStabilityAnalysis")


class AbstractAssemblyCompoundStabilityAnalysis(_3984.PartCompoundStabilityAnalysis):
    """AbstractAssemblyCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCompoundStabilityAnalysis"
    )

    class _Cast_AbstractAssemblyCompoundStabilityAnalysis:
        """Special nested class for casting AbstractAssemblyCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
            parent: "AbstractAssemblyCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3984.PartCompoundStabilityAnalysis":
            return self._parent._cast(_3984.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3911.AGMAGleasonConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3911,
            )

            return self._parent._cast(
                _3911.AGMAGleasonConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def assembly_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3912.AssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3912,
            )

            return self._parent._cast(_3912.AssemblyCompoundStabilityAnalysis)

        @property
        def belt_drive_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3915.BeltDriveCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3915,
            )

            return self._parent._cast(_3915.BeltDriveCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3918.BevelDifferentialGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3918,
            )

            return self._parent._cast(
                _3918.BevelDifferentialGearSetCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3923.BevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3923,
            )

            return self._parent._cast(_3923.BevelGearSetCompoundStabilityAnalysis)

        @property
        def bolted_joint_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3925.BoltedJointCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3925,
            )

            return self._parent._cast(_3925.BoltedJointCompoundStabilityAnalysis)

        @property
        def clutch_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3926.ClutchCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3926,
            )

            return self._parent._cast(_3926.ClutchCompoundStabilityAnalysis)

        @property
        def concept_coupling_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3931.ConceptCouplingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3931,
            )

            return self._parent._cast(_3931.ConceptCouplingCompoundStabilityAnalysis)

        @property
        def concept_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3936.ConceptGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3936,
            )

            return self._parent._cast(_3936.ConceptGearSetCompoundStabilityAnalysis)

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3939.ConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3939,
            )

            return self._parent._cast(_3939.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def coupling_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3942.CouplingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3942,
            )

            return self._parent._cast(_3942.CouplingCompoundStabilityAnalysis)

        @property
        def cvt_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3946.CVTCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3946,
            )

            return self._parent._cast(_3946.CVTCompoundStabilityAnalysis)

        @property
        def cycloidal_assembly_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3948.CycloidalAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3948,
            )

            return self._parent._cast(_3948.CycloidalAssemblyCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3954.CylindricalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3954,
            )

            return self._parent._cast(_3954.CylindricalGearSetCompoundStabilityAnalysis)

        @property
        def face_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3960.FaceGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3960,
            )

            return self._parent._cast(_3960.FaceGearSetCompoundStabilityAnalysis)

        @property
        def flexible_pin_assembly_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3962.FlexiblePinAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3962,
            )

            return self._parent._cast(
                _3962.FlexiblePinAssemblyCompoundStabilityAnalysis
            )

        @property
        def gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3965.GearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3965,
            )

            return self._parent._cast(_3965.GearSetCompoundStabilityAnalysis)

        @property
        def hypoid_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3969.HypoidGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3969,
            )

            return self._parent._cast(_3969.HypoidGearSetCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3973.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(
                _3973.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3976.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(
                _3976.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> (
            "_3979.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3979,
            )

            return self._parent._cast(
                _3979.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3985.PartToPartShearCouplingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3985,
            )

            return self._parent._cast(
                _3985.PartToPartShearCouplingCompoundStabilityAnalysis
            )

        @property
        def planetary_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3989.PlanetaryGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3989,
            )

            return self._parent._cast(_3989.PlanetaryGearSetCompoundStabilityAnalysis)

        @property
        def rolling_ring_assembly_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3996.RollingRingAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3996,
            )

            return self._parent._cast(
                _3996.RollingRingAssemblyCompoundStabilityAnalysis
            )

        @property
        def root_assembly_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3999.RootAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(_3999.RootAssemblyCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4003.SpecialisedAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4003,
            )

            return self._parent._cast(
                _4003.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4006.SpiralBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4006,
            )

            return self._parent._cast(_4006.SpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def spring_damper_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4007.SpringDamperCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4007,
            )

            return self._parent._cast(_4007.SpringDamperCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4012.StraightBevelDiffGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4012,
            )

            return self._parent._cast(
                _4012.StraightBevelDiffGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4015.StraightBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4015,
            )

            return self._parent._cast(
                _4015.StraightBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def synchroniser_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4018.SynchroniserCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4018,
            )

            return self._parent._cast(_4018.SynchroniserCompoundStabilityAnalysis)

        @property
        def torque_converter_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4022.TorqueConverterCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4022,
            )

            return self._parent._cast(_4022.TorqueConverterCompoundStabilityAnalysis)

        @property
        def worm_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4030.WormGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4030,
            )

            return self._parent._cast(_4030.WormGearSetCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4033.ZerolBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4033,
            )

            return self._parent._cast(_4033.ZerolBevelGearSetCompoundStabilityAnalysis)

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "AbstractAssemblyCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "AbstractAssemblyCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3771.AbstractAssemblyStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AbstractAssemblyStabilityAnalysis]

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
    ) -> "List[_3771.AbstractAssemblyStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AbstractAssemblyStabilityAnalysis]

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
    ) -> "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis":
        return self._Cast_AbstractAssemblyCompoundStabilityAnalysis(self)
