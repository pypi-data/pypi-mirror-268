"""VirtualComponentCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3982
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "VirtualComponentCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3898
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3980,
        _3981,
        _3991,
        _3992,
        _4026,
        _3930,
        _3984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentCompoundStabilityAnalysis")


class VirtualComponentCompoundStabilityAnalysis(
    _3982.MountableComponentCompoundStabilityAnalysis
):
    """VirtualComponentCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentCompoundStabilityAnalysis"
    )

    class _Cast_VirtualComponentCompoundStabilityAnalysis:
        """Special nested class for casting VirtualComponentCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
            parent: "VirtualComponentCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_stability_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "_3982.MountableComponentCompoundStabilityAnalysis":
            return self._parent._cast(_3982.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "_3930.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "_3984.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(_3984.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def mass_disc_compound_stability_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "_3980.MassDiscCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3980,
            )

            return self._parent._cast(_3980.MassDiscCompoundStabilityAnalysis)

        @property
        def measurement_component_compound_stability_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "_3981.MeasurementComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3981,
            )

            return self._parent._cast(
                _3981.MeasurementComponentCompoundStabilityAnalysis
            )

        @property
        def point_load_compound_stability_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "_3991.PointLoadCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3991,
            )

            return self._parent._cast(_3991.PointLoadCompoundStabilityAnalysis)

        @property
        def power_load_compound_stability_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "_3992.PowerLoadCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3992,
            )

            return self._parent._cast(_3992.PowerLoadCompoundStabilityAnalysis)

        @property
        def unbalanced_mass_compound_stability_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "_4026.UnbalancedMassCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4026,
            )

            return self._parent._cast(_4026.UnbalancedMassCompoundStabilityAnalysis)

        @property
        def virtual_component_compound_stability_analysis(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
        ) -> "VirtualComponentCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "VirtualComponentCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3898.VirtualComponentStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.VirtualComponentStabilityAnalysis]

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
    ) -> "List[_3898.VirtualComponentStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.VirtualComponentStabilityAnalysis]

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
    ) -> "VirtualComponentCompoundStabilityAnalysis._Cast_VirtualComponentCompoundStabilityAnalysis":
        return self._Cast_VirtualComponentCompoundStabilityAnalysis(self)
