"""VirtualComponentCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6760,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "VirtualComponentCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6676
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6758,
        _6759,
        _6769,
        _6770,
        _6804,
        _6708,
        _6762,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentCompoundCriticalSpeedAnalysis")


class VirtualComponentCompoundCriticalSpeedAnalysis(
    _6760.MountableComponentCompoundCriticalSpeedAnalysis
):
    """VirtualComponentCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentCompoundCriticalSpeedAnalysis"
    )

    class _Cast_VirtualComponentCompoundCriticalSpeedAnalysis:
        """Special nested class for casting VirtualComponentCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
            parent: "VirtualComponentCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6760.MountableComponentCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6760.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6708.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6708,
            )

            return self._parent._cast(_6708.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6762.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6762,
            )

            return self._parent._cast(_6762.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def mass_disc_compound_critical_speed_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6758.MassDiscCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6758,
            )

            return self._parent._cast(_6758.MassDiscCompoundCriticalSpeedAnalysis)

        @property
        def measurement_component_compound_critical_speed_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6759.MeasurementComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6759,
            )

            return self._parent._cast(
                _6759.MeasurementComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def point_load_compound_critical_speed_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6769.PointLoadCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6769,
            )

            return self._parent._cast(_6769.PointLoadCompoundCriticalSpeedAnalysis)

        @property
        def power_load_compound_critical_speed_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6770.PowerLoadCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6770,
            )

            return self._parent._cast(_6770.PowerLoadCompoundCriticalSpeedAnalysis)

        @property
        def unbalanced_mass_compound_critical_speed_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ) -> "_6804.UnbalancedMassCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6804,
            )

            return self._parent._cast(_6804.UnbalancedMassCompoundCriticalSpeedAnalysis)

        @property
        def virtual_component_compound_critical_speed_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ) -> "VirtualComponentCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "VirtualComponentCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6676.VirtualComponentCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.VirtualComponentCriticalSpeedAnalysis]

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
    ) -> "List[_6676.VirtualComponentCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.VirtualComponentCriticalSpeedAnalysis]

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
    ) -> "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis":
        return self._Cast_VirtualComponentCompoundCriticalSpeedAnalysis(self)
