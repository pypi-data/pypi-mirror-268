"""KlingelnbergCycloPalloidConicalGearModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4613
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "KlingelnbergCycloPalloidConicalGearModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.system_deflections import _2778
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4655,
        _4658,
        _4644,
        _4666,
        _4605,
        _4670,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearModalAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearModalAnalysis")


class KlingelnbergCycloPalloidConicalGearModalAnalysis(_4613.ConicalGearModalAnalysis):
    """KlingelnbergCycloPalloidConicalGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearModalAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ) -> "_4613.ConicalGearModalAnalysis":
            return self._parent._cast(_4613.ConicalGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ) -> "_4644.GearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644

            return self._parent._cast(_4644.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ) -> "_4666.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4666

            return self._parent._cast(_4666.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ) -> "_4605.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ) -> "_4670.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(_4670.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ) -> "_4655.KlingelnbergCycloPalloidHypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4655

            return self._parent._cast(
                _4655.KlingelnbergCycloPalloidHypoidGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ) -> "_4658.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(
                _4658.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2543.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2778.KlingelnbergCycloPalloidConicalGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis(self)
