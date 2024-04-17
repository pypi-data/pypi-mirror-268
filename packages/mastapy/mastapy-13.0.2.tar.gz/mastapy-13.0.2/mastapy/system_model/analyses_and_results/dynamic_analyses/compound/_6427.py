"""BevelDifferentialGearCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6432
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "BevelDifferentialGearCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2522
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6296
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6430,
        _6431,
        _6420,
        _6448,
        _6474,
        _6493,
        _6441,
        _6495,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearCompoundDynamicAnalysis")


class BevelDifferentialGearCompoundDynamicAnalysis(
    _6432.BevelGearCompoundDynamicAnalysis
):
    """BevelDifferentialGearCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearCompoundDynamicAnalysis"
    )

    class _Cast_BevelDifferentialGearCompoundDynamicAnalysis:
        """Special nested class for casting BevelDifferentialGearCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
            parent: "BevelDifferentialGearCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_dynamic_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_6432.BevelGearCompoundDynamicAnalysis":
            return self._parent._cast(_6432.BevelGearCompoundDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_6420.AGMAGleasonConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6420,
            )

            return self._parent._cast(
                _6420.AGMAGleasonConicalGearCompoundDynamicAnalysis
            )

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_6448.ConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6448,
            )

            return self._parent._cast(_6448.ConicalGearCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_6474.GearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6474,
            )

            return self._parent._cast(_6474.GearCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_6493.MountableComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6493,
            )

            return self._parent._cast(_6493.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_6441.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6441,
            )

            return self._parent._cast(_6441.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_6495.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6495,
            )

            return self._parent._cast(_6495.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_dynamic_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_6430.BevelDifferentialPlanetGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6430,
            )

            return self._parent._cast(
                _6430.BevelDifferentialPlanetGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_dynamic_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_6431.BevelDifferentialSunGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6431,
            )

            return self._parent._cast(
                _6431.BevelDifferentialSunGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_gear_compound_dynamic_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "BevelDifferentialGearCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
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
        instance_to_wrap: "BevelDifferentialGearCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2522.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

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
    ) -> "List[_6296.BevelDifferentialGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialGearDynamicAnalysis]

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
    ) -> "List[_6296.BevelDifferentialGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialGearDynamicAnalysis]

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
    ) -> "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis":
        return self._Cast_BevelDifferentialGearCompoundDynamicAnalysis(self)
