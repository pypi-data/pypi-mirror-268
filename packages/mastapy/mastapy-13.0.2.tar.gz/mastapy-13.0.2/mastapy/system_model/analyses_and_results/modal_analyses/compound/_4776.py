"""CVTBeltConnectionCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4745
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "CVTBeltConnectionCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4621
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4801,
        _4771,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionCompoundModalAnalysis",)


Self = TypeVar("Self", bound="CVTBeltConnectionCompoundModalAnalysis")


class CVTBeltConnectionCompoundModalAnalysis(_4745.BeltConnectionCompoundModalAnalysis):
    """CVTBeltConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTBeltConnectionCompoundModalAnalysis"
    )

    class _Cast_CVTBeltConnectionCompoundModalAnalysis:
        """Special nested class for casting CVTBeltConnectionCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "CVTBeltConnectionCompoundModalAnalysis._Cast_CVTBeltConnectionCompoundModalAnalysis",
            parent: "CVTBeltConnectionCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def belt_connection_compound_modal_analysis(
            self: "CVTBeltConnectionCompoundModalAnalysis._Cast_CVTBeltConnectionCompoundModalAnalysis",
        ) -> "_4745.BeltConnectionCompoundModalAnalysis":
            return self._parent._cast(_4745.BeltConnectionCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "CVTBeltConnectionCompoundModalAnalysis._Cast_CVTBeltConnectionCompoundModalAnalysis",
        ) -> "_4801.InterMountableComponentConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4801,
            )

            return self._parent._cast(
                _4801.InterMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "CVTBeltConnectionCompoundModalAnalysis._Cast_CVTBeltConnectionCompoundModalAnalysis",
        ) -> "_4771.ConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4771,
            )

            return self._parent._cast(_4771.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "CVTBeltConnectionCompoundModalAnalysis._Cast_CVTBeltConnectionCompoundModalAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTBeltConnectionCompoundModalAnalysis._Cast_CVTBeltConnectionCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionCompoundModalAnalysis._Cast_CVTBeltConnectionCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_modal_analysis(
            self: "CVTBeltConnectionCompoundModalAnalysis._Cast_CVTBeltConnectionCompoundModalAnalysis",
        ) -> "CVTBeltConnectionCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionCompoundModalAnalysis._Cast_CVTBeltConnectionCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "CVTBeltConnectionCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4621.CVTBeltConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CVTBeltConnectionModalAnalysis]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4621.CVTBeltConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CVTBeltConnectionModalAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "CVTBeltConnectionCompoundModalAnalysis._Cast_CVTBeltConnectionCompoundModalAnalysis":
        return self._Cast_CVTBeltConnectionCompoundModalAnalysis(self)
