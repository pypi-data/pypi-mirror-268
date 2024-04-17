"""ConceptGearCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7472,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ConceptGearCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2528
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7310,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7491,
        _7439,
        _7493,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConceptGearCompoundAdvancedSystemDeflection")


class ConceptGearCompoundAdvancedSystemDeflection(
    _7472.GearCompoundAdvancedSystemDeflection
):
    """ConceptGearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearCompoundAdvancedSystemDeflection"
    )

    class _Cast_ConceptGearCompoundAdvancedSystemDeflection:
        """Special nested class for casting ConceptGearCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConceptGearCompoundAdvancedSystemDeflection._Cast_ConceptGearCompoundAdvancedSystemDeflection",
            parent: "ConceptGearCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_compound_advanced_system_deflection(
            self: "ConceptGearCompoundAdvancedSystemDeflection._Cast_ConceptGearCompoundAdvancedSystemDeflection",
        ) -> "_7472.GearCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7472.GearCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "ConceptGearCompoundAdvancedSystemDeflection._Cast_ConceptGearCompoundAdvancedSystemDeflection",
        ) -> "_7491.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7491,
            )

            return self._parent._cast(
                _7491.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "ConceptGearCompoundAdvancedSystemDeflection._Cast_ConceptGearCompoundAdvancedSystemDeflection",
        ) -> "_7439.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7439,
            )

            return self._parent._cast(_7439.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "ConceptGearCompoundAdvancedSystemDeflection._Cast_ConceptGearCompoundAdvancedSystemDeflection",
        ) -> "_7493.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7493,
            )

            return self._parent._cast(_7493.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ConceptGearCompoundAdvancedSystemDeflection._Cast_ConceptGearCompoundAdvancedSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptGearCompoundAdvancedSystemDeflection._Cast_ConceptGearCompoundAdvancedSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearCompoundAdvancedSystemDeflection._Cast_ConceptGearCompoundAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_gear_compound_advanced_system_deflection(
            self: "ConceptGearCompoundAdvancedSystemDeflection._Cast_ConceptGearCompoundAdvancedSystemDeflection",
        ) -> "ConceptGearCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConceptGearCompoundAdvancedSystemDeflection._Cast_ConceptGearCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ConceptGearCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2528.ConceptGear":
        """mastapy.system_model.part_model.gears.ConceptGear

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
    ) -> "List[_7310.ConceptGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConceptGearAdvancedSystemDeflection]

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
    ) -> "List[_7310.ConceptGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConceptGearAdvancedSystemDeflection]

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
    ) -> "ConceptGearCompoundAdvancedSystemDeflection._Cast_ConceptGearCompoundAdvancedSystemDeflection":
        return self._Cast_ConceptGearCompoundAdvancedSystemDeflection(self)
