"""SpiralBevelGearSetLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6838
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpiralBevelGearSetLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2551
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6962,
        _6963,
        _6824,
        _6857,
        _6904,
        _6961,
        _6815,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetLoadCase",)


Self = TypeVar("Self", bound="SpiralBevelGearSetLoadCase")


class SpiralBevelGearSetLoadCase(_6838.BevelGearSetLoadCase):
    """SpiralBevelGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearSetLoadCase")

    class _Cast_SpiralBevelGearSetLoadCase:
        """Special nested class for casting SpiralBevelGearSetLoadCase to subclasses."""

        def __init__(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
            parent: "SpiralBevelGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_load_case(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
        ) -> "_6838.BevelGearSetLoadCase":
            return self._parent._cast(_6838.BevelGearSetLoadCase)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
        ) -> "_6824.AGMAGleasonConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6824

            return self._parent._cast(_6824.AGMAGleasonConicalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
        ) -> "_6857.ConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6857

            return self._parent._cast(_6857.ConicalGearSetLoadCase)

        @property
        def gear_set_load_case(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
        ) -> "_6904.GearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6904

            return self._parent._cast(_6904.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
        ) -> "_6961.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6961

            return self._parent._cast(_6961.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
        ) -> "_6815.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6815

            return self._parent._cast(_6815.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_set_load_case(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
        ) -> "SpiralBevelGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2551.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(self: Self) -> "List[_6962.SpiralBevelGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_gears_load_case(
        self: Self,
    ) -> "List[_6962.SpiralBevelGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_meshes_load_case(
        self: Self,
    ) -> "List[_6963.SpiralBevelGearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase":
        return self._Cast_SpiralBevelGearSetLoadCase(self)
