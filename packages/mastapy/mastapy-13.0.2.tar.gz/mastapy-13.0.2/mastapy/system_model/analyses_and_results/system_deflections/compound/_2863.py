"""AGMAGleasonConicalGearCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2891
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "AGMAGleasonConicalGearCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2699
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2870,
        _2873,
        _2874,
        _2875,
        _2922,
        _2960,
        _2966,
        _2969,
        _2972,
        _2973,
        _2987,
        _2918,
        _2937,
        _2884,
        _2939,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundSystemDeflection",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearCompoundSystemDeflection")


class AGMAGleasonConicalGearCompoundSystemDeflection(
    _2891.ConicalGearCompoundSystemDeflection
):
    """AGMAGleasonConicalGearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearCompoundSystemDeflection"
    )

    class _Cast_AGMAGleasonConicalGearCompoundSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
            parent: "AGMAGleasonConicalGearCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2891.ConicalGearCompoundSystemDeflection":
            return self._parent._cast(_2891.ConicalGearCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2918.GearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2918,
            )

            return self._parent._cast(_2918.GearCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2937.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2937,
            )

            return self._parent._cast(_2937.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2884.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(_2884.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2939.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2870.BevelDifferentialGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2870,
            )

            return self._parent._cast(
                _2870.BevelDifferentialGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2873.BevelDifferentialPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2873,
            )

            return self._parent._cast(
                _2873.BevelDifferentialPlanetGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2874.BevelDifferentialSunGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2874,
            )

            return self._parent._cast(
                _2874.BevelDifferentialSunGearCompoundSystemDeflection
            )

        @property
        def bevel_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2875.BevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2875,
            )

            return self._parent._cast(_2875.BevelGearCompoundSystemDeflection)

        @property
        def hypoid_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2922.HypoidGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2922,
            )

            return self._parent._cast(_2922.HypoidGearCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2960.SpiralBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2960,
            )

            return self._parent._cast(_2960.SpiralBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2966.StraightBevelDiffGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2966,
            )

            return self._parent._cast(
                _2966.StraightBevelDiffGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2969.StraightBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2969,
            )

            return self._parent._cast(_2969.StraightBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_planet_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2972.StraightBevelPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2972,
            )

            return self._parent._cast(
                _2972.StraightBevelPlanetGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2973.StraightBevelSunGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2973,
            )

            return self._parent._cast(
                _2973.StraightBevelSunGearCompoundSystemDeflection
            )

        @property
        def zerol_bevel_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2987.ZerolBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2987,
            )

            return self._parent._cast(_2987.ZerolBevelGearCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "AGMAGleasonConicalGearCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
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
        instance_to_wrap: "AGMAGleasonConicalGearCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_2699.AGMAGleasonConicalGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSystemDeflection]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2699.AGMAGleasonConicalGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection":
        return self._Cast_AGMAGleasonConicalGearCompoundSystemDeflection(self)
