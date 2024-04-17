"""CVTModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4875,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "CVTModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4965,
        _4865,
        _4946,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CVTModalAnalysisAtAStiffness")


class CVTModalAnalysisAtAStiffness(_4875.BeltDriveModalAnalysisAtAStiffness):
    """CVTModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CVT_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTModalAnalysisAtAStiffness")

    class _Cast_CVTModalAnalysisAtAStiffness:
        """Special nested class for casting CVTModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
            parent: "CVTModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def belt_drive_modal_analysis_at_a_stiffness(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_4875.BeltDriveModalAnalysisAtAStiffness":
            return self._parent._cast(_4875.BeltDriveModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_4965.SpecialisedAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4965,
            )

            return self._parent._cast(
                _4965.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_4865.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4865,
            )

            return self._parent._cast(_4865.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_4946.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4946,
            )

            return self._parent._cast(_4946.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_modal_analysis_at_a_stiffness(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
        ) -> "CVTModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTModalAnalysisAtAStiffness.TYPE"):
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
    ) -> "CVTModalAnalysisAtAStiffness._Cast_CVTModalAnalysisAtAStiffness":
        return self._Cast_CVTModalAnalysisAtAStiffness(self)
