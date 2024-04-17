"""WormGearSetCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4796
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "WormGearSetCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2559
    from mastapy.system_model.analyses_and_results.modal_analyses import _4720
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4859,
        _4860,
        _4834,
        _4736,
        _4815,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("WormGearSetCompoundModalAnalysis",)


Self = TypeVar("Self", bound="WormGearSetCompoundModalAnalysis")


class WormGearSetCompoundModalAnalysis(_4796.GearSetCompoundModalAnalysis):
    """WormGearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearSetCompoundModalAnalysis")

    class _Cast_WormGearSetCompoundModalAnalysis:
        """Special nested class for casting WormGearSetCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "WormGearSetCompoundModalAnalysis._Cast_WormGearSetCompoundModalAnalysis",
            parent: "WormGearSetCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_compound_modal_analysis(
            self: "WormGearSetCompoundModalAnalysis._Cast_WormGearSetCompoundModalAnalysis",
        ) -> "_4796.GearSetCompoundModalAnalysis":
            return self._parent._cast(_4796.GearSetCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "WormGearSetCompoundModalAnalysis._Cast_WormGearSetCompoundModalAnalysis",
        ) -> "_4834.SpecialisedAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4834,
            )

            return self._parent._cast(_4834.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "WormGearSetCompoundModalAnalysis._Cast_WormGearSetCompoundModalAnalysis",
        ) -> "_4736.AbstractAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4736,
            )

            return self._parent._cast(_4736.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "WormGearSetCompoundModalAnalysis._Cast_WormGearSetCompoundModalAnalysis",
        ) -> "_4815.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "WormGearSetCompoundModalAnalysis._Cast_WormGearSetCompoundModalAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "WormGearSetCompoundModalAnalysis._Cast_WormGearSetCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearSetCompoundModalAnalysis._Cast_WormGearSetCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def worm_gear_set_compound_modal_analysis(
            self: "WormGearSetCompoundModalAnalysis._Cast_WormGearSetCompoundModalAnalysis",
        ) -> "WormGearSetCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearSetCompoundModalAnalysis._Cast_WormGearSetCompoundModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearSetCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2559.WormGearSet":
        """mastapy.system_model.part_model.gears.WormGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2559.WormGearSet":
        """mastapy.system_model.part_model.gears.WormGearSet

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
    ) -> "List[_4720.WormGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.WormGearSetModalAnalysis]

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
    def worm_gears_compound_modal_analysis(
        self: Self,
    ) -> "List[_4859.WormGearCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.WormGearCompoundModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearsCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_meshes_compound_modal_analysis(
        self: Self,
    ) -> "List[_4860.WormGearMeshCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.WormGearMeshCompoundModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormMeshesCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4720.WormGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.WormGearSetModalAnalysis]

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
    ) -> "WormGearSetCompoundModalAnalysis._Cast_WormGearSetCompoundModalAnalysis":
        return self._Cast_WormGearSetCompoundModalAnalysis(self)
