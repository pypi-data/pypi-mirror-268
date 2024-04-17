"""ZerolBevelGearCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2875
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "ZerolBevelGearCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2560
    from mastapy.system_model.analyses_and_results.system_deflections import _2849
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2863,
        _2891,
        _2918,
        _2937,
        _2884,
        _2939,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearCompoundSystemDeflection",)


Self = TypeVar("Self", bound="ZerolBevelGearCompoundSystemDeflection")


class ZerolBevelGearCompoundSystemDeflection(_2875.BevelGearCompoundSystemDeflection):
    """ZerolBevelGearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearCompoundSystemDeflection"
    )

    class _Cast_ZerolBevelGearCompoundSystemDeflection:
        """Special nested class for casting ZerolBevelGearCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
            parent: "ZerolBevelGearCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_system_deflection(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
        ) -> "_2875.BevelGearCompoundSystemDeflection":
            return self._parent._cast(_2875.BevelGearCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
        ) -> "_2863.AGMAGleasonConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2863,
            )

            return self._parent._cast(
                _2863.AGMAGleasonConicalGearCompoundSystemDeflection
            )

        @property
        def conical_gear_compound_system_deflection(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
        ) -> "_2891.ConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2891,
            )

            return self._parent._cast(_2891.ConicalGearCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
        ) -> "_2918.GearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2918,
            )

            return self._parent._cast(_2918.GearCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
        ) -> "_2937.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2937,
            )

            return self._parent._cast(_2937.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
        ) -> "_2884.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(_2884.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
        ) -> "_2939.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_compound_system_deflection(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
        ) -> "ZerolBevelGearCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "ZerolBevelGearCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2560.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

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
    ) -> "List[_2849.ZerolBevelGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSystemDeflection]

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
    ) -> "List[_2849.ZerolBevelGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSystemDeflection]

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
    ) -> "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection":
        return self._Cast_ZerolBevelGearCompoundSystemDeflection(self)
