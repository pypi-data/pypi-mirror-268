"""AbstractShaftOrHousingCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6576
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "AbstractShaftOrHousingCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2443
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6552,
        _6599,
        _6610,
        _6649,
        _6633,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingCriticalSpeedAnalysis")


class AbstractShaftOrHousingCriticalSpeedAnalysis(_6576.ComponentCriticalSpeedAnalysis):
    """AbstractShaftOrHousingCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingCriticalSpeedAnalysis"
    )

    class _Cast_AbstractShaftOrHousingCriticalSpeedAnalysis:
        """Special nested class for casting AbstractShaftOrHousingCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
            parent: "AbstractShaftOrHousingCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def component_critical_speed_analysis(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "_6576.ComponentCriticalSpeedAnalysis":
            return self._parent._cast(_6576.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "_6633.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_critical_speed_analysis(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "_6552.AbstractShaftCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6552,
            )

            return self._parent._cast(_6552.AbstractShaftCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_critical_speed_analysis(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "_6599.CycloidalDiscCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6599,
            )

            return self._parent._cast(_6599.CycloidalDiscCriticalSpeedAnalysis)

        @property
        def fe_part_critical_speed_analysis(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "_6610.FEPartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6610,
            )

            return self._parent._cast(_6610.FEPartCriticalSpeedAnalysis)

        @property
        def shaft_critical_speed_analysis(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "_6649.ShaftCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6649,
            )

            return self._parent._cast(_6649.ShaftCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_critical_speed_analysis(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "AbstractShaftOrHousingCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftOrHousingCriticalSpeedAnalysis.TYPE"
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
    ) -> "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis":
        return self._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis(self)
