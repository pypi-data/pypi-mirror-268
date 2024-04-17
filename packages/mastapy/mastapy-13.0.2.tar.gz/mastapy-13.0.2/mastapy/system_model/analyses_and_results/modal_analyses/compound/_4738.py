"""AbstractShaftOrHousingCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4761
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "AbstractShaftOrHousingCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4582
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4737,
        _4781,
        _4792,
        _4831,
        _4815,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundModalAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingCompoundModalAnalysis")


class AbstractShaftOrHousingCompoundModalAnalysis(_4761.ComponentCompoundModalAnalysis):
    """AbstractShaftOrHousingCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingCompoundModalAnalysis"
    )

    class _Cast_AbstractShaftOrHousingCompoundModalAnalysis:
        """Special nested class for casting AbstractShaftOrHousingCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
            parent: "AbstractShaftOrHousingCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_modal_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
        ) -> "_4761.ComponentCompoundModalAnalysis":
            return self._parent._cast(_4761.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
        ) -> "_4815.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_modal_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
        ) -> "_4737.AbstractShaftCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4737,
            )

            return self._parent._cast(_4737.AbstractShaftCompoundModalAnalysis)

        @property
        def cycloidal_disc_compound_modal_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
        ) -> "_4781.CycloidalDiscCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4781,
            )

            return self._parent._cast(_4781.CycloidalDiscCompoundModalAnalysis)

        @property
        def fe_part_compound_modal_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
        ) -> "_4792.FEPartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4792,
            )

            return self._parent._cast(_4792.FEPartCompoundModalAnalysis)

        @property
        def shaft_compound_modal_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
        ) -> "_4831.ShaftCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4831,
            )

            return self._parent._cast(_4831.ShaftCompoundModalAnalysis)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
        ) -> "AbstractShaftOrHousingCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftOrHousingCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4582.AbstractShaftOrHousingModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AbstractShaftOrHousingModalAnalysis]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4582.AbstractShaftOrHousingModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AbstractShaftOrHousingModalAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis":
        return self._Cast_AbstractShaftOrHousingCompoundModalAnalysis(self)
