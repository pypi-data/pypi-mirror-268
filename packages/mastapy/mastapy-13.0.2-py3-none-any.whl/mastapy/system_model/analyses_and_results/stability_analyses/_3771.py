"""AbstractAssemblyStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3852
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "AbstractAssemblyStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2441
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3776,
        _3778,
        _3781,
        _3783,
        _3788,
        _3790,
        _3794,
        _3799,
        _3801,
        _3804,
        _3810,
        _3814,
        _3815,
        _3820,
        _3827,
        _3830,
        _3832,
        _3836,
        _3840,
        _3843,
        _3846,
        _3855,
        _3857,
        _3864,
        _3867,
        _3871,
        _3873,
        _3877,
        _3882,
        _3885,
        _3892,
        _3895,
        _3900,
        _3903,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyStabilityAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyStabilityAnalysis")


class AbstractAssemblyStabilityAnalysis(_3852.PartStabilityAnalysis):
    """AbstractAssemblyStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyStabilityAnalysis")

    class _Cast_AbstractAssemblyStabilityAnalysis:
        """Special nested class for casting AbstractAssemblyStabilityAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
            parent: "AbstractAssemblyStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def part_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3852.PartStabilityAnalysis":
            return self._parent._cast(_3852.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3776.AGMAGleasonConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3776,
            )

            return self._parent._cast(_3776.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3778.AssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3778,
            )

            return self._parent._cast(_3778.AssemblyStabilityAnalysis)

        @property
        def belt_drive_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3781.BeltDriveStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3781,
            )

            return self._parent._cast(_3781.BeltDriveStabilityAnalysis)

        @property
        def bevel_differential_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3783.BevelDifferentialGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3783,
            )

            return self._parent._cast(_3783.BevelDifferentialGearSetStabilityAnalysis)

        @property
        def bevel_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3788.BevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.BevelGearSetStabilityAnalysis)

        @property
        def bolted_joint_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3790.BoltedJointStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3790,
            )

            return self._parent._cast(_3790.BoltedJointStabilityAnalysis)

        @property
        def clutch_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3794.ClutchStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3794,
            )

            return self._parent._cast(_3794.ClutchStabilityAnalysis)

        @property
        def concept_coupling_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3799.ConceptCouplingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3799,
            )

            return self._parent._cast(_3799.ConceptCouplingStabilityAnalysis)

        @property
        def concept_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3801.ConceptGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3801,
            )

            return self._parent._cast(_3801.ConceptGearSetStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3804.ConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3804,
            )

            return self._parent._cast(_3804.ConicalGearSetStabilityAnalysis)

        @property
        def coupling_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3810.CouplingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3810,
            )

            return self._parent._cast(_3810.CouplingStabilityAnalysis)

        @property
        def cvt_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3814.CVTStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3814,
            )

            return self._parent._cast(_3814.CVTStabilityAnalysis)

        @property
        def cycloidal_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3815.CycloidalAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3815,
            )

            return self._parent._cast(_3815.CycloidalAssemblyStabilityAnalysis)

        @property
        def cylindrical_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3820.CylindricalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3820,
            )

            return self._parent._cast(_3820.CylindricalGearSetStabilityAnalysis)

        @property
        def face_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3827.FaceGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3827,
            )

            return self._parent._cast(_3827.FaceGearSetStabilityAnalysis)

        @property
        def flexible_pin_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3830.FlexiblePinAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3830,
            )

            return self._parent._cast(_3830.FlexiblePinAssemblyStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3832.GearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3832,
            )

            return self._parent._cast(_3832.GearSetStabilityAnalysis)

        @property
        def hypoid_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3836.HypoidGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3836,
            )

            return self._parent._cast(_3836.HypoidGearSetStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3840.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(
                _3840.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3843.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3843,
            )

            return self._parent._cast(
                _3843.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3846.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(
                _3846.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3855.PartToPartShearCouplingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3855,
            )

            return self._parent._cast(_3855.PartToPartShearCouplingStabilityAnalysis)

        @property
        def planetary_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3857.PlanetaryGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3857,
            )

            return self._parent._cast(_3857.PlanetaryGearSetStabilityAnalysis)

        @property
        def rolling_ring_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3864.RollingRingAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3864,
            )

            return self._parent._cast(_3864.RollingRingAssemblyStabilityAnalysis)

        @property
        def root_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3867.RootAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.RootAssemblyStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3871.SpecialisedAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3871,
            )

            return self._parent._cast(_3871.SpecialisedAssemblyStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3873.SpiralBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3873,
            )

            return self._parent._cast(_3873.SpiralBevelGearSetStabilityAnalysis)

        @property
        def spring_damper_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3877.SpringDamperStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3877,
            )

            return self._parent._cast(_3877.SpringDamperStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3882.StraightBevelDiffGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3882,
            )

            return self._parent._cast(_3882.StraightBevelDiffGearSetStabilityAnalysis)

        @property
        def straight_bevel_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3885.StraightBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3885,
            )

            return self._parent._cast(_3885.StraightBevelGearSetStabilityAnalysis)

        @property
        def synchroniser_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3892.SynchroniserStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3892,
            )

            return self._parent._cast(_3892.SynchroniserStabilityAnalysis)

        @property
        def torque_converter_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3895.TorqueConverterStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3895,
            )

            return self._parent._cast(_3895.TorqueConverterStabilityAnalysis)

        @property
        def worm_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3900.WormGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3900,
            )

            return self._parent._cast(_3900.WormGearSetStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3903.ZerolBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3903,
            )

            return self._parent._cast(_3903.ZerolBevelGearSetStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "AbstractAssemblyStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
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
        self: Self, instance_to_wrap: "AbstractAssemblyStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2441.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2441.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis":
        return self._Cast_AbstractAssemblyStabilityAnalysis(self)
