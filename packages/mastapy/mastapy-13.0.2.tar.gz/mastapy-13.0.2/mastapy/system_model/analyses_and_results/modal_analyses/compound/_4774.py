"""CouplingConnectionCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4801
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "CouplingConnectionCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4618
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4758,
        _4763,
        _4817,
        _4839,
        _4854,
        _4771,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionCompoundModalAnalysis",)


Self = TypeVar("Self", bound="CouplingConnectionCompoundModalAnalysis")


class CouplingConnectionCompoundModalAnalysis(
    _4801.InterMountableComponentConnectionCompoundModalAnalysis
):
    """CouplingConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionCompoundModalAnalysis"
    )

    class _Cast_CouplingConnectionCompoundModalAnalysis:
        """Special nested class for casting CouplingConnectionCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
            parent: "CouplingConnectionCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
        ) -> "_4801.InterMountableComponentConnectionCompoundModalAnalysis":
            return self._parent._cast(
                _4801.InterMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
        ) -> "_4771.ConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4771,
            )

            return self._parent._cast(_4771.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_modal_analysis(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
        ) -> "_4758.ClutchConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4758,
            )

            return self._parent._cast(_4758.ClutchConnectionCompoundModalAnalysis)

        @property
        def concept_coupling_connection_compound_modal_analysis(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
        ) -> "_4763.ConceptCouplingConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4763,
            )

            return self._parent._cast(
                _4763.ConceptCouplingConnectionCompoundModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
        ) -> "_4817.PartToPartShearCouplingConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4817,
            )

            return self._parent._cast(
                _4817.PartToPartShearCouplingConnectionCompoundModalAnalysis
            )

        @property
        def spring_damper_connection_compound_modal_analysis(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
        ) -> "_4839.SpringDamperConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4839,
            )

            return self._parent._cast(_4839.SpringDamperConnectionCompoundModalAnalysis)

        @property
        def torque_converter_connection_compound_modal_analysis(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
        ) -> "_4854.TorqueConverterConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4854,
            )

            return self._parent._cast(
                _4854.TorqueConverterConnectionCompoundModalAnalysis
            )

        @property
        def coupling_connection_compound_modal_analysis(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
        ) -> "CouplingConnectionCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "CouplingConnectionCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4618.CouplingConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CouplingConnectionModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4618.CouplingConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CouplingConnectionModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingConnectionCompoundModalAnalysis._Cast_CouplingConnectionCompoundModalAnalysis":
        return self._Cast_CouplingConnectionCompoundModalAnalysis(self)
