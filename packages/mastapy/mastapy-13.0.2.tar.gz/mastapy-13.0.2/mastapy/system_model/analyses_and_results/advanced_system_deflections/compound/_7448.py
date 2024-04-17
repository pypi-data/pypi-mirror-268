"""ConicalGearSetCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7474,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ConicalGearSetCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.conical import _544
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7315,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7420,
        _7427,
        _7432,
        _7478,
        _7482,
        _7485,
        _7488,
        _7515,
        _7521,
        _7524,
        _7542,
        _7512,
        _7414,
        _7493,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConicalGearSetCompoundAdvancedSystemDeflection")


class ConicalGearSetCompoundAdvancedSystemDeflection(
    _7474.GearSetCompoundAdvancedSystemDeflection
):
    """ConicalGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSetCompoundAdvancedSystemDeflection"
    )

    class _Cast_ConicalGearSetCompoundAdvancedSystemDeflection:
        """Special nested class for casting ConicalGearSetCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
            parent: "ConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7474.GearSetCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7474.GearSetCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7512.SpecialisedAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7512,
            )

            return self._parent._cast(
                _7512.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7414.AbstractAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7414,
            )

            return self._parent._cast(
                _7414.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7493.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7493,
            )

            return self._parent._cast(_7493.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7420.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7420,
            )

            return self._parent._cast(
                _7420.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7427.BevelDifferentialGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7427,
            )

            return self._parent._cast(
                _7427.BevelDifferentialGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7432.BevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7432,
            )

            return self._parent._cast(
                _7432.BevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def hypoid_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7478.HypoidGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7478,
            )

            return self._parent._cast(
                _7478.HypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7482.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7482,
            )

            return self._parent._cast(
                _7482.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7485.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(
                _7485.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7488.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7488,
            )

            return self._parent._cast(
                _7488.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7515.SpiralBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7515,
            )

            return self._parent._cast(
                _7515.SpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7521.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7521,
            )

            return self._parent._cast(
                _7521.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7524.StraightBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7524,
            )

            return self._parent._cast(
                _7524.StraightBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7542.ZerolBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7542,
            )

            return self._parent._cast(
                _7542.ZerolBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "ConicalGearSetCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "ConicalGearSetCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_duty_cycle_rating(self: Self) -> "_544.ConicalGearSetDutyCycleRating":
        """mastapy.gears.rating.conical.ConicalGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gear_duty_cycle_rating(
        self: Self,
    ) -> "_544.ConicalGearSetDutyCycleRating":
        """mastapy.gears.rating.conical.ConicalGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7315.ConicalGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConicalGearSetAdvancedSystemDeflection]

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
    ) -> "List[_7315.ConicalGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConicalGearSetAdvancedSystemDeflection]

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
    ) -> "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection":
        return self._Cast_ConicalGearSetCompoundAdvancedSystemDeflection(self)
