"""SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7014,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2483
    from mastapy.system_model.analyses_and_results.system_deflections import _2814
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7024,
        _7029,
        _7032,
        _7037,
        _7039,
        _7040,
        _7045,
        _7050,
        _7053,
        _7056,
        _7059,
        _7062,
        _7068,
        _7074,
        _7076,
        _7079,
        _7084,
        _7088,
        _7091,
        _7094,
        _7100,
        _7104,
        _7112,
        _7121,
        _7122,
        _7127,
        _7130,
        _7133,
        _7137,
        _7145,
        _7148,
        _7099,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation"
)


class SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation(
    _7014.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
):
    """SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
            parent: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7014.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7014.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7099.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7099,
            )

            return self._parent._cast(
                _7099.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7024.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7024,
            )

            return self._parent._cast(
                _7024.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_drive_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7029.BeltDriveAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7029,
            )

            return self._parent._cast(
                _7029.BeltDriveAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7032.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7032,
            )

            return self._parent._cast(
                _7032.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7037.BevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7037,
            )

            return self._parent._cast(
                _7037.BevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolted_joint_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7039.BoltedJointAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7039,
            )

            return self._parent._cast(
                _7039.BoltedJointAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7040.ClutchAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7040,
            )

            return self._parent._cast(
                _7040.ClutchAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7045.ConceptCouplingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7045,
            )

            return self._parent._cast(
                _7045.ConceptCouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7050.ConceptGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7050,
            )

            return self._parent._cast(
                _7050.ConceptGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7053.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7053,
            )

            return self._parent._cast(
                _7053.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7056.CouplingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7056,
            )

            return self._parent._cast(
                _7056.CouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7059.CVTAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7059,
            )

            return self._parent._cast(
                _7059.CVTAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7062.CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7062,
            )

            return self._parent._cast(
                _7062.CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7068.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7068,
            )

            return self._parent._cast(
                _7068.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7074.FaceGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7074,
            )

            return self._parent._cast(
                _7074.FaceGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def flexible_pin_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7076.FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7076,
            )

            return self._parent._cast(
                _7076.FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7079.GearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7079,
            )

            return self._parent._cast(
                _7079.GearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7084.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7084,
            )

            return self._parent._cast(
                _7084.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7088.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7088,
            )

            return self._parent._cast(
                _7088.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7091.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7091,
            )

            return self._parent._cast(
                _7091.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7094.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7094,
            )

            return self._parent._cast(
                _7094.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7100.PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7100,
            )

            return self._parent._cast(
                _7100.PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7104.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7104,
            )

            return self._parent._cast(
                _7104.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7112.RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7112,
            )

            return self._parent._cast(
                _7112.RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7121.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7121,
            )

            return self._parent._cast(
                _7121.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7122.SpringDamperAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7122,
            )

            return self._parent._cast(
                _7122.SpringDamperAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7127.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7127,
            )

            return self._parent._cast(
                _7127.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7130.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7130,
            )

            return self._parent._cast(
                _7130.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7133.SynchroniserAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7133,
            )

            return self._parent._cast(
                _7133.SynchroniserAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7137.TorqueConverterAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7137,
            )

            return self._parent._cast(
                _7137.TorqueConverterAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7145.WormGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7145,
            )

            return self._parent._cast(
                _7145.WormGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7148.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7148,
            )

            return self._parent._cast(
                _7148.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
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
        self: Self,
        instance_to_wrap: "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2483.SpecialisedAssembly":
        """mastapy.system_model.part_model.SpecialisedAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2814.SpecialisedAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SpecialisedAssemblySystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation(
            self
        )
