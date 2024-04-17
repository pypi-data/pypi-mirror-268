"""ConicalGearSetLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6904
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConicalGearSetLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2531
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6856,
        _6824,
        _6833,
        _6838,
        _6916,
        _6923,
        _6926,
        _6929,
        _6964,
        _6970,
        _6973,
        _6996,
        _6961,
        _6815,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetLoadCase",)


Self = TypeVar("Self", bound="ConicalGearSetLoadCase")


class ConicalGearSetLoadCase(_6904.GearSetLoadCase):
    """ConicalGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetLoadCase")

    class _Cast_ConicalGearSetLoadCase:
        """Special nested class for casting ConicalGearSetLoadCase to subclasses."""

        def __init__(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
            parent: "ConicalGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6904.GearSetLoadCase":
            return self._parent._cast(_6904.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6961.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6961

            return self._parent._cast(_6961.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6815.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6815

            return self._parent._cast(_6815.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6824.AGMAGleasonConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6824

            return self._parent._cast(_6824.AGMAGleasonConicalGearSetLoadCase)

        @property
        def bevel_differential_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6833.BevelDifferentialGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6833

            return self._parent._cast(_6833.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6838.BevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6838

            return self._parent._cast(_6838.BevelGearSetLoadCase)

        @property
        def hypoid_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6916.HypoidGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6916

            return self._parent._cast(_6916.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6923.KlingelnbergCycloPalloidConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6923

            return self._parent._cast(
                _6923.KlingelnbergCycloPalloidConicalGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6926.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6926

            return self._parent._cast(
                _6926.KlingelnbergCycloPalloidHypoidGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6929.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6929

            return self._parent._cast(
                _6929.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
            )

        @property
        def spiral_bevel_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6964.SpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6964

            return self._parent._cast(_6964.SpiralBevelGearSetLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6970.StraightBevelDiffGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6970

            return self._parent._cast(_6970.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6973.StraightBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6973

            return self._parent._cast(_6973.StraightBevelGearSetLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6996.ZerolBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6996

            return self._parent._cast(_6996.ZerolBevelGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "ConicalGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2531.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def get_harmonic_load_data_for_import(
        self: Self,
    ) -> "_6856.ConicalGearSetHarmonicLoadData":
        """mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetHarmonicLoadData"""
        method_result = self.wrapped.GetHarmonicLoadDataForImport()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase":
        return self._Cast_ConicalGearSetLoadCase(self)
