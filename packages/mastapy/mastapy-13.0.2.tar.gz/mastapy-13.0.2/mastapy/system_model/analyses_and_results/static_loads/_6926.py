"""KlingelnbergCycloPalloidHypoidGearSetLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6923
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidHypoidGearSetLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2546
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6924,
        _6925,
        _6857,
        _6904,
        _6961,
        _6815,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSetLoadCase",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearSetLoadCase")


class KlingelnbergCycloPalloidHypoidGearSetLoadCase(
    _6923.KlingelnbergCycloPalloidConicalGearSetLoadCase
):
    """KlingelnbergCycloPalloidHypoidGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetLoadCase to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
            parent: "KlingelnbergCycloPalloidHypoidGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
        ) -> "_6923.KlingelnbergCycloPalloidConicalGearSetLoadCase":
            return self._parent._cast(
                _6923.KlingelnbergCycloPalloidConicalGearSetLoadCase
            )

        @property
        def conical_gear_set_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
        ) -> "_6857.ConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6857

            return self._parent._cast(_6857.ConicalGearSetLoadCase)

        @property
        def gear_set_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
        ) -> "_6904.GearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6904

            return self._parent._cast(_6904.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
        ) -> "_6961.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6961

            return self._parent._cast(_6961.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
        ) -> "_6815.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6815

            return self._parent._cast(_6815.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetLoadCase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2546.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(self: Self) -> "List[_6924.KlingelnbergCycloPalloidHypoidGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase]

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
    def klingelnberg_cyclo_palloid_hypoid_gears_load_case(
        self: Self,
    ) -> "List[_6924.KlingelnbergCycloPalloidHypoidGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_load_case(
        self: Self,
    ) -> "List[_6925.KlingelnbergCycloPalloidHypoidGearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase(self)
