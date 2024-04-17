"""VirtualComponentCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4813
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "VirtualComponentCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4714
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4811,
        _4812,
        _4822,
        _4823,
        _4857,
        _4761,
        _4815,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundModalAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentCompoundModalAnalysis")


class VirtualComponentCompoundModalAnalysis(
    _4813.MountableComponentCompoundModalAnalysis
):
    """VirtualComponentCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentCompoundModalAnalysis"
    )

    class _Cast_VirtualComponentCompoundModalAnalysis:
        """Special nested class for casting VirtualComponentCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundModalAnalysis._Cast_VirtualComponentCompoundModalAnalysis",
            parent: "VirtualComponentCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis(
            self: "VirtualComponentCompoundModalAnalysis._Cast_VirtualComponentCompoundModalAnalysis",
        ) -> "_4813.MountableComponentCompoundModalAnalysis":
            return self._parent._cast(_4813.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "VirtualComponentCompoundModalAnalysis._Cast_VirtualComponentCompoundModalAnalysis",
        ) -> "_4761.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4761,
            )

            return self._parent._cast(_4761.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "VirtualComponentCompoundModalAnalysis._Cast_VirtualComponentCompoundModalAnalysis",
        ) -> "_4815.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundModalAnalysis._Cast_VirtualComponentCompoundModalAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundModalAnalysis._Cast_VirtualComponentCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundModalAnalysis._Cast_VirtualComponentCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def mass_disc_compound_modal_analysis(
            self: "VirtualComponentCompoundModalAnalysis._Cast_VirtualComponentCompoundModalAnalysis",
        ) -> "_4811.MassDiscCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4811,
            )

            return self._parent._cast(_4811.MassDiscCompoundModalAnalysis)

        @property
        def measurement_component_compound_modal_analysis(
            self: "VirtualComponentCompoundModalAnalysis._Cast_VirtualComponentCompoundModalAnalysis",
        ) -> "_4812.MeasurementComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4812,
            )

            return self._parent._cast(_4812.MeasurementComponentCompoundModalAnalysis)

        @property
        def point_load_compound_modal_analysis(
            self: "VirtualComponentCompoundModalAnalysis._Cast_VirtualComponentCompoundModalAnalysis",
        ) -> "_4822.PointLoadCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4822,
            )

            return self._parent._cast(_4822.PointLoadCompoundModalAnalysis)

        @property
        def power_load_compound_modal_analysis(
            self: "VirtualComponentCompoundModalAnalysis._Cast_VirtualComponentCompoundModalAnalysis",
        ) -> "_4823.PowerLoadCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4823,
            )

            return self._parent._cast(_4823.PowerLoadCompoundModalAnalysis)

        @property
        def unbalanced_mass_compound_modal_analysis(
            self: "VirtualComponentCompoundModalAnalysis._Cast_VirtualComponentCompoundModalAnalysis",
        ) -> "_4857.UnbalancedMassCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4857,
            )

            return self._parent._cast(_4857.UnbalancedMassCompoundModalAnalysis)

        @property
        def virtual_component_compound_modal_analysis(
            self: "VirtualComponentCompoundModalAnalysis._Cast_VirtualComponentCompoundModalAnalysis",
        ) -> "VirtualComponentCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundModalAnalysis._Cast_VirtualComponentCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "VirtualComponentCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4714.VirtualComponentModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.VirtualComponentModalAnalysis]

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
    ) -> "List[_4714.VirtualComponentModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.VirtualComponentModalAnalysis]

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
    ) -> "VirtualComponentCompoundModalAnalysis._Cast_VirtualComponentCompoundModalAnalysis":
        return self._Cast_VirtualComponentCompoundModalAnalysis(self)
