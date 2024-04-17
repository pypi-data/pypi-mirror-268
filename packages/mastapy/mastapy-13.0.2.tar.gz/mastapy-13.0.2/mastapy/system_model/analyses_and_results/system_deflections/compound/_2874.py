"""BevelDifferentialSunGearCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2870
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "BevelDifferentialSunGearCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2713
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2875,
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
__all__ = ("BevelDifferentialSunGearCompoundSystemDeflection",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearCompoundSystemDeflection")


class BevelDifferentialSunGearCompoundSystemDeflection(
    _2870.BevelDifferentialGearCompoundSystemDeflection
):
    """BevelDifferentialSunGearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialSunGearCompoundSystemDeflection"
    )

    class _Cast_BevelDifferentialSunGearCompoundSystemDeflection:
        """Special nested class for casting BevelDifferentialSunGearCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
            parent: "BevelDifferentialSunGearCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_system_deflection(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "_2870.BevelDifferentialGearCompoundSystemDeflection":
            return self._parent._cast(
                _2870.BevelDifferentialGearCompoundSystemDeflection
            )

        @property
        def bevel_gear_compound_system_deflection(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "_2875.BevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2875,
            )

            return self._parent._cast(_2875.BevelGearCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "_2863.AGMAGleasonConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2863,
            )

            return self._parent._cast(
                _2863.AGMAGleasonConicalGearCompoundSystemDeflection
            )

        @property
        def conical_gear_compound_system_deflection(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "_2891.ConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2891,
            )

            return self._parent._cast(_2891.ConicalGearCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "_2918.GearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2918,
            )

            return self._parent._cast(_2918.GearCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "_2937.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2937,
            )

            return self._parent._cast(_2937.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "_2884.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(_2884.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "_2939.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_compound_system_deflection(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
        ) -> "BevelDifferentialSunGearCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection",
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
        instance_to_wrap: "BevelDifferentialSunGearCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2713.BevelDifferentialSunGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialSunGearSystemDeflection]

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
    ) -> "List[_2713.BevelDifferentialSunGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialSunGearSystemDeflection]

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
    ) -> "BevelDifferentialSunGearCompoundSystemDeflection._Cast_BevelDifferentialSunGearCompoundSystemDeflection":
        return self._Cast_BevelDifferentialSunGearCompoundSystemDeflection(self)
