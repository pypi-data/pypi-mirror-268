"""HypoidGearCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2863
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "HypoidGearCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.analyses_and_results.system_deflections import _2773
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
__all__ = ("HypoidGearCompoundSystemDeflection",)


Self = TypeVar("Self", bound="HypoidGearCompoundSystemDeflection")


class HypoidGearCompoundSystemDeflection(
    _2863.AGMAGleasonConicalGearCompoundSystemDeflection
):
    """HypoidGearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearCompoundSystemDeflection")

    class _Cast_HypoidGearCompoundSystemDeflection:
        """Special nested class for casting HypoidGearCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "HypoidGearCompoundSystemDeflection._Cast_HypoidGearCompoundSystemDeflection",
            parent: "HypoidGearCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "HypoidGearCompoundSystemDeflection._Cast_HypoidGearCompoundSystemDeflection",
        ) -> "_2863.AGMAGleasonConicalGearCompoundSystemDeflection":
            return self._parent._cast(
                _2863.AGMAGleasonConicalGearCompoundSystemDeflection
            )

        @property
        def conical_gear_compound_system_deflection(
            self: "HypoidGearCompoundSystemDeflection._Cast_HypoidGearCompoundSystemDeflection",
        ) -> "_2891.ConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2891,
            )

            return self._parent._cast(_2891.ConicalGearCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "HypoidGearCompoundSystemDeflection._Cast_HypoidGearCompoundSystemDeflection",
        ) -> "_2918.GearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2918,
            )

            return self._parent._cast(_2918.GearCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "HypoidGearCompoundSystemDeflection._Cast_HypoidGearCompoundSystemDeflection",
        ) -> "_2937.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2937,
            )

            return self._parent._cast(_2937.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "HypoidGearCompoundSystemDeflection._Cast_HypoidGearCompoundSystemDeflection",
        ) -> "_2884.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(_2884.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "HypoidGearCompoundSystemDeflection._Cast_HypoidGearCompoundSystemDeflection",
        ) -> "_2939.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "HypoidGearCompoundSystemDeflection._Cast_HypoidGearCompoundSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "HypoidGearCompoundSystemDeflection._Cast_HypoidGearCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearCompoundSystemDeflection._Cast_HypoidGearCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def hypoid_gear_compound_system_deflection(
            self: "HypoidGearCompoundSystemDeflection._Cast_HypoidGearCompoundSystemDeflection",
        ) -> "HypoidGearCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "HypoidGearCompoundSystemDeflection._Cast_HypoidGearCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "HypoidGearCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2541.HypoidGear":
        """mastapy.system_model.part_model.gears.HypoidGear

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
    ) -> "List[_2773.HypoidGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSystemDeflection]

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
    ) -> "List[_2773.HypoidGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSystemDeflection]

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
    ) -> "HypoidGearCompoundSystemDeflection._Cast_HypoidGearCompoundSystemDeflection":
        return self._Cast_HypoidGearCompoundSystemDeflection(self)
