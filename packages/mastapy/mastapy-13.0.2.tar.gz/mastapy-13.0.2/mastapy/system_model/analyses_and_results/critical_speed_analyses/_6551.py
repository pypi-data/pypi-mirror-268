"""AbstractAssemblyCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6633
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "AbstractAssemblyCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2441
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6557,
        _6558,
        _6561,
        _6564,
        _6569,
        _6571,
        _6573,
        _6578,
        _6582,
        _6585,
        _6589,
        _6595,
        _6597,
        _6603,
        _6609,
        _6611,
        _6614,
        _6618,
        _6622,
        _6625,
        _6628,
        _6635,
        _6638,
        _6645,
        _6648,
        _6652,
        _6655,
        _6657,
        _6661,
        _6664,
        _6667,
        _6672,
        _6679,
        _6682,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyCriticalSpeedAnalysis")


class AbstractAssemblyCriticalSpeedAnalysis(_6633.PartCriticalSpeedAnalysis):
    """AbstractAssemblyCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCriticalSpeedAnalysis"
    )

    class _Cast_AbstractAssemblyCriticalSpeedAnalysis:
        """Special nested class for casting AbstractAssemblyCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
            parent: "AbstractAssemblyCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def part_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6633.PartCriticalSpeedAnalysis":
            return self._parent._cast(_6633.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6557.AGMAGleasonConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6557,
            )

            return self._parent._cast(
                _6557.AGMAGleasonConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def assembly_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6558.AssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6558,
            )

            return self._parent._cast(_6558.AssemblyCriticalSpeedAnalysis)

        @property
        def belt_drive_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6561.BeltDriveCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6561,
            )

            return self._parent._cast(_6561.BeltDriveCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6564.BevelDifferentialGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(
                _6564.BevelDifferentialGearSetCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6569.BevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6569,
            )

            return self._parent._cast(_6569.BevelGearSetCriticalSpeedAnalysis)

        @property
        def bolted_joint_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6571.BoltedJointCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6571,
            )

            return self._parent._cast(_6571.BoltedJointCriticalSpeedAnalysis)

        @property
        def clutch_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6573.ClutchCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6573,
            )

            return self._parent._cast(_6573.ClutchCriticalSpeedAnalysis)

        @property
        def concept_coupling_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6578.ConceptCouplingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6578,
            )

            return self._parent._cast(_6578.ConceptCouplingCriticalSpeedAnalysis)

        @property
        def concept_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6582.ConceptGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6582,
            )

            return self._parent._cast(_6582.ConceptGearSetCriticalSpeedAnalysis)

        @property
        def conical_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6585.ConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6585,
            )

            return self._parent._cast(_6585.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def coupling_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6589.CouplingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6589,
            )

            return self._parent._cast(_6589.CouplingCriticalSpeedAnalysis)

        @property
        def cvt_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6595.CVTCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6595,
            )

            return self._parent._cast(_6595.CVTCriticalSpeedAnalysis)

        @property
        def cycloidal_assembly_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6597.CycloidalAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6597,
            )

            return self._parent._cast(_6597.CycloidalAssemblyCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6603.CylindricalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6603,
            )

            return self._parent._cast(_6603.CylindricalGearSetCriticalSpeedAnalysis)

        @property
        def face_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6609.FaceGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6609,
            )

            return self._parent._cast(_6609.FaceGearSetCriticalSpeedAnalysis)

        @property
        def flexible_pin_assembly_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6611.FlexiblePinAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6611,
            )

            return self._parent._cast(_6611.FlexiblePinAssemblyCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6614.GearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6614,
            )

            return self._parent._cast(_6614.GearSetCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6618.HypoidGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6618,
            )

            return self._parent._cast(_6618.HypoidGearSetCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6622.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(
                _6622.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6625.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(
                _6625.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6628.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6628,
            )

            return self._parent._cast(
                _6628.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6635.PartToPartShearCouplingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6635,
            )

            return self._parent._cast(
                _6635.PartToPartShearCouplingCriticalSpeedAnalysis
            )

        @property
        def planetary_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6638.PlanetaryGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6638,
            )

            return self._parent._cast(_6638.PlanetaryGearSetCriticalSpeedAnalysis)

        @property
        def rolling_ring_assembly_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6645.RollingRingAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6645,
            )

            return self._parent._cast(_6645.RollingRingAssemblyCriticalSpeedAnalysis)

        @property
        def root_assembly_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6648.RootAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6648,
            )

            return self._parent._cast(_6648.RootAssemblyCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6652.SpecialisedAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6652,
            )

            return self._parent._cast(_6652.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6655.SpiralBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6655,
            )

            return self._parent._cast(_6655.SpiralBevelGearSetCriticalSpeedAnalysis)

        @property
        def spring_damper_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6657.SpringDamperCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6657,
            )

            return self._parent._cast(_6657.SpringDamperCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6661.StraightBevelDiffGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6661,
            )

            return self._parent._cast(
                _6661.StraightBevelDiffGearSetCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6664.StraightBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6664,
            )

            return self._parent._cast(_6664.StraightBevelGearSetCriticalSpeedAnalysis)

        @property
        def synchroniser_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6667.SynchroniserCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6667,
            )

            return self._parent._cast(_6667.SynchroniserCriticalSpeedAnalysis)

        @property
        def torque_converter_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6672.TorqueConverterCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6672,
            )

            return self._parent._cast(_6672.TorqueConverterCriticalSpeedAnalysis)

        @property
        def worm_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6679.WormGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6679,
            )

            return self._parent._cast(_6679.WormGearSetCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "_6682.ZerolBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6682,
            )

            return self._parent._cast(_6682.ZerolBevelGearSetCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
        ) -> "AbstractAssemblyCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "AbstractAssemblyCriticalSpeedAnalysis.TYPE"
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
    ) -> "AbstractAssemblyCriticalSpeedAnalysis._Cast_AbstractAssemblyCriticalSpeedAnalysis":
        return self._Cast_AbstractAssemblyCriticalSpeedAnalysis(self)
