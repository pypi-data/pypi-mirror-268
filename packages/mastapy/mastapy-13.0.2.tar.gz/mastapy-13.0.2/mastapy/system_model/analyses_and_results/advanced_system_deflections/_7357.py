"""KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7351
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
        "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2548
    from mastapy.system_model.analyses_and_results.static_loads import _6929
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _410
    from mastapy.system_model.analyses_and_results.system_deflections import _2783
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7355,
        _7356,
        _7315,
        _7343,
        _7382,
        _7278,
        _7363,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection"
)


class KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection(
    _7351.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
):
    """KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",
        ) -> "_7351.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection":
            return self._parent._cast(
                _7351.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
            )

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",
        ) -> "_7315.ConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7315,
            )

            return self._parent._cast(_7315.ConicalGearSetAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",
        ) -> "_7343.GearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7343,
            )

            return self._parent._cast(_7343.GearSetAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",
        ) -> "_7382.SpecialisedAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7382,
            )

            return self._parent._cast(_7382.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",
        ) -> "_7278.AbstractAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7278,
            )

            return self._parent._cast(_7278.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",
        ) -> "_7363.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(_7363.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(
        self: Self,
    ) -> "_2548.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(
        self: Self,
    ) -> "_6929.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_410.KlingelnbergCycloPalloidSpiralBevelGearSetRating":
        """mastapy.gears.rating.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(
        self: Self,
    ) -> "_410.KlingelnbergCycloPalloidSpiralBevelGearSetRating":
        """mastapy.gears.rating.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_system_deflection_results(
        self: Self,
    ) -> "List[_2783.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_advanced_system_deflection(
        self: Self,
    ) -> "List[_7355.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsAdvancedSystemDeflection
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_advanced_system_deflection(
        self: Self,
    ) -> "List[_7356.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesAdvancedSystemDeflection
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection(
            self
        )
