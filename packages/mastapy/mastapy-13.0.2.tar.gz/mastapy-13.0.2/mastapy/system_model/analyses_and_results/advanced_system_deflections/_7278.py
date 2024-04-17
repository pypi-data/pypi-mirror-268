"""AbstractAssemblyAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7363
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "AbstractAssemblyAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2441
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7287,
        _7288,
        _7291,
        _7294,
        _7299,
        _7301,
        _7302,
        _7307,
        _7312,
        _7315,
        _7319,
        _7322,
        _7325,
        _7331,
        _7338,
        _7340,
        _7343,
        _7347,
        _7351,
        _7354,
        _7357,
        _7364,
        _7368,
        _7376,
        _7378,
        _7382,
        _7385,
        _7386,
        _7391,
        _7394,
        _7397,
        _7401,
        _7410,
        _7413,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="AbstractAssemblyAdvancedSystemDeflection")


class AbstractAssemblyAdvancedSystemDeflection(_7363.PartAdvancedSystemDeflection):
    """AbstractAssemblyAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyAdvancedSystemDeflection"
    )

    class _Cast_AbstractAssemblyAdvancedSystemDeflection:
        """Special nested class for casting AbstractAssemblyAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
            parent: "AbstractAssemblyAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7363.PartAdvancedSystemDeflection":
            return self._parent._cast(_7363.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7287.AGMAGleasonConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7287,
            )

            return self._parent._cast(
                _7287.AGMAGleasonConicalGearSetAdvancedSystemDeflection
            )

        @property
        def assembly_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7288.AssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7288,
            )

            return self._parent._cast(_7288.AssemblyAdvancedSystemDeflection)

        @property
        def belt_drive_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7291.BeltDriveAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7291,
            )

            return self._parent._cast(_7291.BeltDriveAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7294.BevelDifferentialGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7294,
            )

            return self._parent._cast(
                _7294.BevelDifferentialGearSetAdvancedSystemDeflection
            )

        @property
        def bevel_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7299.BevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7299,
            )

            return self._parent._cast(_7299.BevelGearSetAdvancedSystemDeflection)

        @property
        def bolted_joint_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7301.BoltedJointAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7301,
            )

            return self._parent._cast(_7301.BoltedJointAdvancedSystemDeflection)

        @property
        def clutch_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7302.ClutchAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7302,
            )

            return self._parent._cast(_7302.ClutchAdvancedSystemDeflection)

        @property
        def concept_coupling_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7307.ConceptCouplingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7307,
            )

            return self._parent._cast(_7307.ConceptCouplingAdvancedSystemDeflection)

        @property
        def concept_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7312.ConceptGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7312,
            )

            return self._parent._cast(_7312.ConceptGearSetAdvancedSystemDeflection)

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7315.ConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7315,
            )

            return self._parent._cast(_7315.ConicalGearSetAdvancedSystemDeflection)

        @property
        def coupling_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7319.CouplingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7319,
            )

            return self._parent._cast(_7319.CouplingAdvancedSystemDeflection)

        @property
        def cvt_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7322.CVTAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7322,
            )

            return self._parent._cast(_7322.CVTAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7325.CycloidalAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7325,
            )

            return self._parent._cast(_7325.CycloidalAssemblyAdvancedSystemDeflection)

        @property
        def cylindrical_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7331.CylindricalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7331,
            )

            return self._parent._cast(_7331.CylindricalGearSetAdvancedSystemDeflection)

        @property
        def face_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7338.FaceGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7338,
            )

            return self._parent._cast(_7338.FaceGearSetAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7340.FlexiblePinAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7340,
            )

            return self._parent._cast(_7340.FlexiblePinAssemblyAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7343.GearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7343,
            )

            return self._parent._cast(_7343.GearSetAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7347.HypoidGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7347,
            )

            return self._parent._cast(_7347.HypoidGearSetAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7351.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(
                _7351.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7354.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(
                _7354.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7357.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7357,
            )

            return self._parent._cast(
                _7357.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7364.PartToPartShearCouplingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7364,
            )

            return self._parent._cast(
                _7364.PartToPartShearCouplingAdvancedSystemDeflection
            )

        @property
        def planetary_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7368.PlanetaryGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7368,
            )

            return self._parent._cast(_7368.PlanetaryGearSetAdvancedSystemDeflection)

        @property
        def rolling_ring_assembly_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7376.RollingRingAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7376,
            )

            return self._parent._cast(_7376.RollingRingAssemblyAdvancedSystemDeflection)

        @property
        def root_assembly_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7378.RootAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7378,
            )

            return self._parent._cast(_7378.RootAssemblyAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7382.SpecialisedAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7382,
            )

            return self._parent._cast(_7382.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7385.SpiralBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7385,
            )

            return self._parent._cast(_7385.SpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def spring_damper_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7386.SpringDamperAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7386,
            )

            return self._parent._cast(_7386.SpringDamperAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7391.StraightBevelDiffGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7391,
            )

            return self._parent._cast(
                _7391.StraightBevelDiffGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7394.StraightBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7394,
            )

            return self._parent._cast(
                _7394.StraightBevelGearSetAdvancedSystemDeflection
            )

        @property
        def synchroniser_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7397.SynchroniserAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7397,
            )

            return self._parent._cast(_7397.SynchroniserAdvancedSystemDeflection)

        @property
        def torque_converter_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7401.TorqueConverterAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7401,
            )

            return self._parent._cast(_7401.TorqueConverterAdvancedSystemDeflection)

        @property
        def worm_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7410.WormGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7410,
            )

            return self._parent._cast(_7410.WormGearSetAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "_7413.ZerolBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7413,
            )

            return self._parent._cast(_7413.ZerolBevelGearSetAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
        ) -> "AbstractAssemblyAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "AbstractAssemblyAdvancedSystemDeflection.TYPE"
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
    ) -> "AbstractAssemblyAdvancedSystemDeflection._Cast_AbstractAssemblyAdvancedSystemDeflection":
        return self._Cast_AbstractAssemblyAdvancedSystemDeflection(self)
