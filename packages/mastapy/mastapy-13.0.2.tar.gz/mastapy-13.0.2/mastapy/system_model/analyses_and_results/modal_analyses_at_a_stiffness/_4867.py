"""AbstractShaftOrHousingModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4890,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "AbstractShaftOrHousingModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2443
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4866,
        _4910,
        _4922,
        _4963,
        _4946,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingModalAnalysisAtAStiffness")


class AbstractShaftOrHousingModalAnalysisAtAStiffness(
    _4890.ComponentModalAnalysisAtAStiffness
):
    """AbstractShaftOrHousingModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness"
    )

    class _Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness:
        """Special nested class for casting AbstractShaftOrHousingModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
            parent: "AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "_4890.ComponentModalAnalysisAtAStiffness":
            return self._parent._cast(_4890.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "_4946.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4946,
            )

            return self._parent._cast(_4946.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "_4866.AbstractShaftModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4866,
            )

            return self._parent._cast(_4866.AbstractShaftModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "_4910.CycloidalDiscModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4910,
            )

            return self._parent._cast(_4910.CycloidalDiscModalAnalysisAtAStiffness)

        @property
        def fe_part_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "_4922.FEPartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4922,
            )

            return self._parent._cast(_4922.FEPartModalAnalysisAtAStiffness)

        @property
        def shaft_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "_4963.ShaftModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4963,
            )

            return self._parent._cast(_4963.ShaftModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "AbstractShaftOrHousingModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
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
        instance_to_wrap: "AbstractShaftOrHousingModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2443.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness":
        return self._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness(self)
