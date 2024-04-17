"""KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2926
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2545
    from mastapy.system_model.analyses_and_results.system_deflections import _2781
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2891,
        _2918,
        _2937,
        _2884,
        _2939,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection"
)


class KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection(
    _2926.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
):
    """KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection",
            parent: "KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection",
        ) -> "_2926.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection":
            return self._parent._cast(
                _2926.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
            )

        @property
        def conical_gear_compound_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection",
        ) -> "_2891.ConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2891,
            )

            return self._parent._cast(_2891.ConicalGearCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection",
        ) -> "_2918.GearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2918,
            )

            return self._parent._cast(_2918.GearCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection",
        ) -> "_2937.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2937,
            )

            return self._parent._cast(_2937.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection",
        ) -> "_2884.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(_2884.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection",
        ) -> "_2939.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection",
        ) -> "KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2545.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2781.KlingelnbergCycloPalloidHypoidGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_2781.KlingelnbergCycloPalloidHypoidGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection(
            self
        )
