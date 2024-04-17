"""KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4802
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2545
    from mastapy.system_model.analyses_and_results.modal_analyses import _4655
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4768,
        _4794,
        _4813,
        _4761,
        _4815,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis")


class KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis(
    _4802.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis",
        ) -> "_4802.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis":
            return self._parent._cast(
                _4802.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
            )

        @property
        def conical_gear_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis",
        ) -> "_4768.ConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4768,
            )

            return self._parent._cast(_4768.ConicalGearCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis",
        ) -> "_4794.GearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4794,
            )

            return self._parent._cast(_4794.GearCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis",
        ) -> "_4813.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4813,
            )

            return self._parent._cast(_4813.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis",
        ) -> "_4761.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4761,
            )

            return self._parent._cast(_4761.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis",
        ) -> "_4815.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2545.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

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
    ) -> "List[_4655.KlingelnbergCycloPalloidHypoidGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearModalAnalysis]

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
    ) -> "List[_4655.KlingelnbergCycloPalloidHypoidGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearModalAnalysis]

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
    ) -> "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis(self)
