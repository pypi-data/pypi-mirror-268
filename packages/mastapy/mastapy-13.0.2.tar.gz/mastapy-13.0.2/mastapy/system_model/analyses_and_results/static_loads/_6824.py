"""AGMAGleasonConicalGearSetLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6857
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AGMAGleasonConicalGearSetLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2521
    from mastapy.gears.manufacturing.bevel import _796
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6833,
        _6838,
        _6916,
        _6964,
        _6970,
        _6973,
        _6996,
        _6904,
        _6961,
        _6815,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetLoadCase",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetLoadCase")


class AGMAGleasonConicalGearSetLoadCase(_6857.ConicalGearSetLoadCase):
    """AGMAGleasonConicalGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetLoadCase")

    class _Cast_AGMAGleasonConicalGearSetLoadCase:
        """Special nested class for casting AGMAGleasonConicalGearSetLoadCase to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetLoadCase._Cast_AGMAGleasonConicalGearSetLoadCase",
            parent: "AGMAGleasonConicalGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def conical_gear_set_load_case(
            self: "AGMAGleasonConicalGearSetLoadCase._Cast_AGMAGleasonConicalGearSetLoadCase",
        ) -> "_6857.ConicalGearSetLoadCase":
            return self._parent._cast(_6857.ConicalGearSetLoadCase)

        @property
        def gear_set_load_case(
            self: "AGMAGleasonConicalGearSetLoadCase._Cast_AGMAGleasonConicalGearSetLoadCase",
        ) -> "_6904.GearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6904

            return self._parent._cast(_6904.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "AGMAGleasonConicalGearSetLoadCase._Cast_AGMAGleasonConicalGearSetLoadCase",
        ) -> "_6961.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6961

            return self._parent._cast(_6961.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "AGMAGleasonConicalGearSetLoadCase._Cast_AGMAGleasonConicalGearSetLoadCase",
        ) -> "_6815.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6815

            return self._parent._cast(_6815.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "AGMAGleasonConicalGearSetLoadCase._Cast_AGMAGleasonConicalGearSetLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetLoadCase._Cast_AGMAGleasonConicalGearSetLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetLoadCase._Cast_AGMAGleasonConicalGearSetLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetLoadCase._Cast_AGMAGleasonConicalGearSetLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_load_case(
            self: "AGMAGleasonConicalGearSetLoadCase._Cast_AGMAGleasonConicalGearSetLoadCase",
        ) -> "_6833.BevelDifferentialGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6833

            return self._parent._cast(_6833.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_gear_set_load_case(
            self: "AGMAGleasonConicalGearSetLoadCase._Cast_AGMAGleasonConicalGearSetLoadCase",
        ) -> "_6838.BevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6838

            return self._parent._cast(_6838.BevelGearSetLoadCase)

        @property
        def hypoid_gear_set_load_case(
            self: "AGMAGleasonConicalGearSetLoadCase._Cast_AGMAGleasonConicalGearSetLoadCase",
        ) -> "_6916.HypoidGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6916

            return self._parent._cast(_6916.HypoidGearSetLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(
            self: "AGMAGleasonConicalGearSetLoadCase._Cast_AGMAGleasonConicalGearSetLoadCase",
        ) -> "_6964.SpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6964

            return self._parent._cast(_6964.SpiralBevelGearSetLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "AGMAGleasonConicalGearSetLoadCase._Cast_AGMAGleasonConicalGearSetLoadCase",
        ) -> "_6970.StraightBevelDiffGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6970

            return self._parent._cast(_6970.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_set_load_case(
            self: "AGMAGleasonConicalGearSetLoadCase._Cast_AGMAGleasonConicalGearSetLoadCase",
        ) -> "_6973.StraightBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6973

            return self._parent._cast(_6973.StraightBevelGearSetLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(
            self: "AGMAGleasonConicalGearSetLoadCase._Cast_AGMAGleasonConicalGearSetLoadCase",
        ) -> "_6996.ZerolBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6996

            return self._parent._cast(_6996.ZerolBevelGearSetLoadCase)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "AGMAGleasonConicalGearSetLoadCase._Cast_AGMAGleasonConicalGearSetLoadCase",
        ) -> "AGMAGleasonConicalGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetLoadCase._Cast_AGMAGleasonConicalGearSetLoadCase",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearSetLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def override_manufacturing_config_micro_geometry(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OverrideManufacturingConfigMicroGeometry

        if temp is None:
            return False

        return temp

    @override_manufacturing_config_micro_geometry.setter
    @enforce_parameter_types
    def override_manufacturing_config_micro_geometry(self: Self, value: "bool"):
        self.wrapped.OverrideManufacturingConfigMicroGeometry = (
            bool(value) if value is not None else False
        )

    @property
    def assembly_design(self: Self) -> "_2521.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def overridden_manufacturing_config_micro_geometry(
        self: Self,
    ) -> "_796.ConicalSetMicroGeometryConfigBase":
        """mastapy.gears.manufacturing.bevel.ConicalSetMicroGeometryConfigBase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverriddenManufacturingConfigMicroGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetLoadCase._Cast_AGMAGleasonConicalGearSetLoadCase":
        return self._Cast_AGMAGleasonConicalGearSetLoadCase(self)
