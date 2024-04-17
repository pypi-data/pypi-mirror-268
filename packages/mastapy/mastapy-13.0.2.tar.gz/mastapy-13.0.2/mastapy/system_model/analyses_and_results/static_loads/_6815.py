"""AbstractAssemblyLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6937
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AbstractAssemblyLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2441
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6824,
        _6827,
        _6830,
        _6833,
        _6838,
        _6839,
        _6843,
        _6849,
        _6852,
        _6857,
        _6862,
        _6864,
        _6866,
        _6874,
        _6895,
        _6897,
        _6904,
        _6916,
        _6923,
        _6926,
        _6929,
        _6940,
        _6942,
        _6954,
        _6957,
        _6961,
        _6964,
        _6967,
        _6970,
        _6973,
        _6977,
        _6982,
        _6993,
        _6996,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyLoadCase",)


Self = TypeVar("Self", bound="AbstractAssemblyLoadCase")


class AbstractAssemblyLoadCase(_6937.PartLoadCase):
    """AbstractAssemblyLoadCase

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyLoadCase")

    class _Cast_AbstractAssemblyLoadCase:
        """Special nested class for casting AbstractAssemblyLoadCase to subclasses."""

        def __init__(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
            parent: "AbstractAssemblyLoadCase",
        ):
            self._parent = parent

        @property
        def part_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6937.PartLoadCase":
            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6824.AGMAGleasonConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6824

            return self._parent._cast(_6824.AGMAGleasonConicalGearSetLoadCase)

        @property
        def assembly_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6827.AssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6827

            return self._parent._cast(_6827.AssemblyLoadCase)

        @property
        def belt_drive_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6830.BeltDriveLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6830

            return self._parent._cast(_6830.BeltDriveLoadCase)

        @property
        def bevel_differential_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6833.BevelDifferentialGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6833

            return self._parent._cast(_6833.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6838.BevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6838

            return self._parent._cast(_6838.BevelGearSetLoadCase)

        @property
        def bolted_joint_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6839.BoltedJointLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6839

            return self._parent._cast(_6839.BoltedJointLoadCase)

        @property
        def clutch_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6843.ClutchLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6843

            return self._parent._cast(_6843.ClutchLoadCase)

        @property
        def concept_coupling_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6849.ConceptCouplingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.ConceptCouplingLoadCase)

        @property
        def concept_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6852.ConceptGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6852

            return self._parent._cast(_6852.ConceptGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6857.ConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6857

            return self._parent._cast(_6857.ConicalGearSetLoadCase)

        @property
        def coupling_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6862.CouplingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6862

            return self._parent._cast(_6862.CouplingLoadCase)

        @property
        def cvt_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6864.CVTLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6864

            return self._parent._cast(_6864.CVTLoadCase)

        @property
        def cycloidal_assembly_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6866.CycloidalAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6866

            return self._parent._cast(_6866.CycloidalAssemblyLoadCase)

        @property
        def cylindrical_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6874.CylindricalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6874

            return self._parent._cast(_6874.CylindricalGearSetLoadCase)

        @property
        def face_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6895.FaceGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6895

            return self._parent._cast(_6895.FaceGearSetLoadCase)

        @property
        def flexible_pin_assembly_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6897.FlexiblePinAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6897

            return self._parent._cast(_6897.FlexiblePinAssemblyLoadCase)

        @property
        def gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6904.GearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6904

            return self._parent._cast(_6904.GearSetLoadCase)

        @property
        def hypoid_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6916.HypoidGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6916

            return self._parent._cast(_6916.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6923.KlingelnbergCycloPalloidConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6923

            return self._parent._cast(
                _6923.KlingelnbergCycloPalloidConicalGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6926.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6926

            return self._parent._cast(
                _6926.KlingelnbergCycloPalloidHypoidGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6929.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6929

            return self._parent._cast(
                _6929.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
            )

        @property
        def part_to_part_shear_coupling_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6940.PartToPartShearCouplingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6940

            return self._parent._cast(_6940.PartToPartShearCouplingLoadCase)

        @property
        def planetary_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6942.PlanetaryGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6942

            return self._parent._cast(_6942.PlanetaryGearSetLoadCase)

        @property
        def rolling_ring_assembly_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6954.RollingRingAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6954

            return self._parent._cast(_6954.RollingRingAssemblyLoadCase)

        @property
        def root_assembly_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6957.RootAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6957

            return self._parent._cast(_6957.RootAssemblyLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6961.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6961

            return self._parent._cast(_6961.SpecialisedAssemblyLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6964.SpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6964

            return self._parent._cast(_6964.SpiralBevelGearSetLoadCase)

        @property
        def spring_damper_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6967.SpringDamperLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6967

            return self._parent._cast(_6967.SpringDamperLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6970.StraightBevelDiffGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6970

            return self._parent._cast(_6970.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6973.StraightBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6973

            return self._parent._cast(_6973.StraightBevelGearSetLoadCase)

        @property
        def synchroniser_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6977.SynchroniserLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6977

            return self._parent._cast(_6977.SynchroniserLoadCase)

        @property
        def torque_converter_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6982.TorqueConverterLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6982

            return self._parent._cast(_6982.TorqueConverterLoadCase)

        @property
        def worm_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6993.WormGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6993

            return self._parent._cast(_6993.WormGearSetLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6996.ZerolBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6996

            return self._parent._cast(_6996.ZerolBevelGearSetLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "AbstractAssemblyLoadCase":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractAssemblyLoadCase.TYPE"):
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
    ) -> "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase":
        return self._Cast_AbstractAssemblyLoadCase(self)
