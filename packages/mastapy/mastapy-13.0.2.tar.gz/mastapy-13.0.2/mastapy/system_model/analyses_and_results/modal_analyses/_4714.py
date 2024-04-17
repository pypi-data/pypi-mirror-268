"""VirtualComponentModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4666
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "VirtualComponentModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2486
    from mastapy.system_model.analyses_and_results.system_deflections import _2843
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4660,
        _4661,
        _4677,
        _4678,
        _4713,
        _4605,
        _4670,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentModalAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentModalAnalysis")


class VirtualComponentModalAnalysis(_4666.MountableComponentModalAnalysis):
    """VirtualComponentModalAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentModalAnalysis")

    class _Cast_VirtualComponentModalAnalysis:
        """Special nested class for casting VirtualComponentModalAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
            parent: "VirtualComponentModalAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_4666.MountableComponentModalAnalysis":
            return self._parent._cast(_4666.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_4605.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_4670.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(_4670.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def mass_disc_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_4660.MassDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660

            return self._parent._cast(_4660.MassDiscModalAnalysis)

        @property
        def measurement_component_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_4661.MeasurementComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661

            return self._parent._cast(_4661.MeasurementComponentModalAnalysis)

        @property
        def point_load_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_4677.PointLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4677

            return self._parent._cast(_4677.PointLoadModalAnalysis)

        @property
        def power_load_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_4678.PowerLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4678

            return self._parent._cast(_4678.PowerLoadModalAnalysis)

        @property
        def unbalanced_mass_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "_4713.UnbalancedMassModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4713

            return self._parent._cast(_4713.UnbalancedMassModalAnalysis)

        @property
        def virtual_component_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "VirtualComponentModalAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualComponentModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2486.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

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
    ) -> "_2843.VirtualComponentSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.VirtualComponentSystemDeflection

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
    ) -> "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis":
        return self._Cast_VirtualComponentModalAnalysis(self)
