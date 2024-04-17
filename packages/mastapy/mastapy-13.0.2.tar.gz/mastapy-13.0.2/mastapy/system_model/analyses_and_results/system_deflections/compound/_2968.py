"""StraightBevelDiffGearSetCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2877
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "StraightBevelDiffGearSetCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2553
    from mastapy.system_model.analyses_and_results.system_deflections import _2822
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2966,
        _2967,
        _2865,
        _2893,
        _2920,
        _2959,
        _2859,
        _2939,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetCompoundSystemDeflection",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetCompoundSystemDeflection")


class StraightBevelDiffGearSetCompoundSystemDeflection(
    _2877.BevelGearSetCompoundSystemDeflection
):
    """StraightBevelDiffGearSetCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearSetCompoundSystemDeflection"
    )

    class _Cast_StraightBevelDiffGearSetCompoundSystemDeflection:
        """Special nested class for casting StraightBevelDiffGearSetCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetCompoundSystemDeflection._Cast_StraightBevelDiffGearSetCompoundSystemDeflection",
            parent: "StraightBevelDiffGearSetCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_system_deflection(
            self: "StraightBevelDiffGearSetCompoundSystemDeflection._Cast_StraightBevelDiffGearSetCompoundSystemDeflection",
        ) -> "_2877.BevelGearSetCompoundSystemDeflection":
            return self._parent._cast(_2877.BevelGearSetCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_compound_system_deflection(
            self: "StraightBevelDiffGearSetCompoundSystemDeflection._Cast_StraightBevelDiffGearSetCompoundSystemDeflection",
        ) -> "_2865.AGMAGleasonConicalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2865,
            )

            return self._parent._cast(
                _2865.AGMAGleasonConicalGearSetCompoundSystemDeflection
            )

        @property
        def conical_gear_set_compound_system_deflection(
            self: "StraightBevelDiffGearSetCompoundSystemDeflection._Cast_StraightBevelDiffGearSetCompoundSystemDeflection",
        ) -> "_2893.ConicalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2893,
            )

            return self._parent._cast(_2893.ConicalGearSetCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(
            self: "StraightBevelDiffGearSetCompoundSystemDeflection._Cast_StraightBevelDiffGearSetCompoundSystemDeflection",
        ) -> "_2920.GearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2920,
            )

            return self._parent._cast(_2920.GearSetCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "StraightBevelDiffGearSetCompoundSystemDeflection._Cast_StraightBevelDiffGearSetCompoundSystemDeflection",
        ) -> "_2959.SpecialisedAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2959,
            )

            return self._parent._cast(_2959.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "StraightBevelDiffGearSetCompoundSystemDeflection._Cast_StraightBevelDiffGearSetCompoundSystemDeflection",
        ) -> "_2859.AbstractAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2859,
            )

            return self._parent._cast(_2859.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "StraightBevelDiffGearSetCompoundSystemDeflection._Cast_StraightBevelDiffGearSetCompoundSystemDeflection",
        ) -> "_2939.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundSystemDeflection._Cast_StraightBevelDiffGearSetCompoundSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundSystemDeflection._Cast_StraightBevelDiffGearSetCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetCompoundSystemDeflection._Cast_StraightBevelDiffGearSetCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_system_deflection(
            self: "StraightBevelDiffGearSetCompoundSystemDeflection._Cast_StraightBevelDiffGearSetCompoundSystemDeflection",
        ) -> "StraightBevelDiffGearSetCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetCompoundSystemDeflection._Cast_StraightBevelDiffGearSetCompoundSystemDeflection",
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
        instance_to_wrap: "StraightBevelDiffGearSetCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2553.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2553.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_2822.StraightBevelDiffGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearSetSystemDeflection]

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
    def straight_bevel_diff_gears_compound_system_deflection(
        self: Self,
    ) -> "List[_2966.StraightBevelDiffGearCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.StraightBevelDiffGearCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsCompoundSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_compound_system_deflection(
        self: Self,
    ) -> "List[_2967.StraightBevelDiffGearMeshCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.StraightBevelDiffGearMeshCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesCompoundSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_2822.StraightBevelDiffGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearSetSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSetCompoundSystemDeflection._Cast_StraightBevelDiffGearSetCompoundSystemDeflection":
        return self._Cast_StraightBevelDiffGearSetCompoundSystemDeflection(self)
