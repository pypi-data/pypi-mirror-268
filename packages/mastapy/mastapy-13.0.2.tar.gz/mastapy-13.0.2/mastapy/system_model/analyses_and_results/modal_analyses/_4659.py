"""KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4653
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2548
    from mastapy.system_model.analyses_and_results.static_loads import _6929
    from mastapy.system_model.analyses_and_results.system_deflections import _2783
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4658,
        _4657,
        _4614,
        _4645,
        _4690,
        _4580,
        _4670,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis")


class KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis(
    _4653.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
):
    """KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis",
        ) -> "_4653.KlingelnbergCycloPalloidConicalGearSetModalAnalysis":
            return self._parent._cast(
                _4653.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
            )

        @property
        def conical_gear_set_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis",
        ) -> "_4614.ConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4614

            return self._parent._cast(_4614.ConicalGearSetModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis",
        ) -> "_4645.GearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4645

            return self._parent._cast(_4645.GearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis",
        ) -> "_4690.SpecialisedAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690

            return self._parent._cast(_4690.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis",
        ) -> "_4580.AbstractAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4580

            return self._parent._cast(_4580.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis",
        ) -> "_4670.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(_4670.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(
        self: Self,
    ) -> "_2548.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(
        self: Self,
    ) -> "_6929.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2783.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_modal_analysis(
        self: Self,
    ) -> "List[_4658.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_modal_analysis(
        self: Self,
    ) -> "List[_4657.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis(self)
