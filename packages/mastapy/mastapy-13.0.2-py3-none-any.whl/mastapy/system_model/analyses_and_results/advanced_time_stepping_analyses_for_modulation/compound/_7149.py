"""AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7228,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7014,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7155,
        _7156,
        _7159,
        _7162,
        _7167,
        _7169,
        _7170,
        _7175,
        _7180,
        _7183,
        _7186,
        _7190,
        _7192,
        _7198,
        _7204,
        _7206,
        _7209,
        _7213,
        _7217,
        _7220,
        _7223,
        _7229,
        _7233,
        _7240,
        _7243,
        _7247,
        _7250,
        _7251,
        _7256,
        _7259,
        _7262,
        _7266,
        _7274,
        _7277,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7155.AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7155,
            )

            return self._parent._cast(
                _7155.AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7156.AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7156,
            )

            return self._parent._cast(
                _7156.AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_drive_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7159.BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7159,
            )

            return self._parent._cast(
                _7159.BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7162.BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7162,
            )

            return self._parent._cast(
                _7162.BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7167.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7167,
            )

            return self._parent._cast(
                _7167.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolted_joint_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7169.BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7169,
            )

            return self._parent._cast(
                _7169.BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7170.ClutchCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7170,
            )

            return self._parent._cast(
                _7170.ClutchCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7175.ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7175,
            )

            return self._parent._cast(
                _7175.ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7180.ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7180,
            )

            return self._parent._cast(
                _7180.ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7183.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7183,
            )

            return self._parent._cast(
                _7183.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7186.CouplingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7186,
            )

            return self._parent._cast(
                _7186.CouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7190.CVTCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7190,
            )

            return self._parent._cast(
                _7190.CVTCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7192.CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7192,
            )

            return self._parent._cast(
                _7192.CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7198.CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7198,
            )

            return self._parent._cast(
                _7198.CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7204.FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7204,
            )

            return self._parent._cast(
                _7204.FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def flexible_pin_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7206.FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7206,
            )

            return self._parent._cast(
                _7206.FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7209.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7209,
            )

            return self._parent._cast(
                _7209.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7213.HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7213,
            )

            return self._parent._cast(
                _7213.HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7217.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7217,
            )

            return self._parent._cast(
                _7217.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7220.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7220,
            )

            return self._parent._cast(
                _7220.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7223.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7223,
            )

            return self._parent._cast(
                _7223.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7229.PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7229,
            )

            return self._parent._cast(
                _7229.PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7233.PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7233,
            )

            return self._parent._cast(
                _7233.PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7240.RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7240,
            )

            return self._parent._cast(
                _7240.RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def root_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7243.RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7243,
            )

            return self._parent._cast(
                _7243.RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7247.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7247,
            )

            return self._parent._cast(
                _7247.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7250.SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7250,
            )

            return self._parent._cast(
                _7250.SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7251.SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7251,
            )

            return self._parent._cast(
                _7251.SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7256.StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7256,
            )

            return self._parent._cast(
                _7256.StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7259.StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7259,
            )

            return self._parent._cast(
                _7259.StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7262.SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7262,
            )

            return self._parent._cast(
                _7262.SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7266.TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7266,
            )

            return self._parent._cast(
                _7266.TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7274.WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7274,
            )

            return self._parent._cast(
                _7274.WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7277.ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7277,
            )

            return self._parent._cast(
                _7277.ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7014.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7014.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
