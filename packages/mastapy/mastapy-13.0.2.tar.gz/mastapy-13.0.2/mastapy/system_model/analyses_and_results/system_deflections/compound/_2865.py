"""AGMAGleasonConicalGearSetCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2893
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "AGMAGleasonConicalGearSetCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2698
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2872,
        _2877,
        _2924,
        _2962,
        _2968,
        _2971,
        _2989,
        _2920,
        _2959,
        _2859,
        _2939,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundSystemDeflection",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetCompoundSystemDeflection")


class AGMAGleasonConicalGearSetCompoundSystemDeflection(
    _2893.ConicalGearSetCompoundSystemDeflection
):
    """AGMAGleasonConicalGearSetCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection"
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
            parent: "AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2893.ConicalGearSetCompoundSystemDeflection":
            return self._parent._cast(_2893.ConicalGearSetCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2920.GearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2920,
            )

            return self._parent._cast(_2920.GearSetCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2959.SpecialisedAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2959,
            )

            return self._parent._cast(_2959.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2859.AbstractAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2859,
            )

            return self._parent._cast(_2859.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2939.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2872.BevelDifferentialGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2872,
            )

            return self._parent._cast(
                _2872.BevelDifferentialGearSetCompoundSystemDeflection
            )

        @property
        def bevel_gear_set_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2877.BevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2877,
            )

            return self._parent._cast(_2877.BevelGearSetCompoundSystemDeflection)

        @property
        def hypoid_gear_set_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2924.HypoidGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2924,
            )

            return self._parent._cast(_2924.HypoidGearSetCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_set_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2962.SpiralBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2962,
            )

            return self._parent._cast(_2962.SpiralBevelGearSetCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2968.StraightBevelDiffGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2968,
            )

            return self._parent._cast(
                _2968.StraightBevelDiffGearSetCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2971.StraightBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2971,
            )

            return self._parent._cast(
                _2971.StraightBevelGearSetCompoundSystemDeflection
            )

        @property
        def zerol_bevel_gear_set_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2989.ZerolBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2989,
            )

            return self._parent._cast(_2989.ZerolBevelGearSetCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "AGMAGleasonConicalGearSetCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_2698.AGMAGleasonConicalGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSetSystemDeflection]

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
    ) -> "List[_2698.AGMAGleasonConicalGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSetSystemDeflection]

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
    ) -> "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection":
        return self._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection(self)
