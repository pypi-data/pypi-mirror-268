"""KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7313
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7352,
        _7355,
        _7341,
        _7361,
        _7306,
        _7363,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection"
)


class KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection(
    _7313.ConicalGearAdvancedSystemDeflection
):
    """KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
            parent: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ) -> "_7313.ConicalGearAdvancedSystemDeflection":
            return self._parent._cast(_7313.ConicalGearAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ) -> "_7341.GearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7341,
            )

            return self._parent._cast(_7341.GearAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ) -> "_7361.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(_7361.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ) -> "_7306.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7306,
            )

            return self._parent._cast(_7306.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ) -> "_7363.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(_7363.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ) -> "_7352.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(
                _7352.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ) -> "_7355.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(
                _7355.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
        ) -> "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2543.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection":
        return self._Cast_KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection(
            self
        )
