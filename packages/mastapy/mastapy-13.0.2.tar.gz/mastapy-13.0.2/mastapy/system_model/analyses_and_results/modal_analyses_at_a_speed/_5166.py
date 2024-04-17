"""CVTModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5135
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "CVTModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5224,
        _5125,
        _5205,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CVTModalAnalysisAtASpeed")


class CVTModalAnalysisAtASpeed(_5135.BeltDriveModalAnalysisAtASpeed):
    """CVTModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CVT_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTModalAnalysisAtASpeed")

    class _Cast_CVTModalAnalysisAtASpeed:
        """Special nested class for casting CVTModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
            parent: "CVTModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def belt_drive_modal_analysis_at_a_speed(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ) -> "_5135.BeltDriveModalAnalysisAtASpeed":
            return self._parent._cast(_5135.BeltDriveModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ) -> "_5224.SpecialisedAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5224,
            )

            return self._parent._cast(_5224.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ) -> "_5125.AbstractAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5125,
            )

            return self._parent._cast(_5125.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ) -> "_5205.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5205,
            )

            return self._parent._cast(_5205.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_modal_analysis_at_a_speed(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ) -> "CVTModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2594.CVT":
        """mastapy.system_model.part_model.couplings.CVT

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed":
        return self._Cast_CVTModalAnalysisAtASpeed(self)
