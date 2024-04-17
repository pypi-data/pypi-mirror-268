"""AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7044,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2443
    from mastapy.system_model.analyses_and_results.system_deflections import _2694
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7015,
        _7063,
        _7075,
        _7115,
        _7099,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation"
)


class AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation(
    _7044.ComponentAdvancedTimeSteppingAnalysisForModulation
):
    """AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
            parent: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7044.ComponentAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7044.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7099.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7099,
            )

            return self._parent._cast(
                _7099.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7015.AbstractShaftAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7015,
            )

            return self._parent._cast(
                _7015.AbstractShaftAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7063.CycloidalDiscAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7063,
            )

            return self._parent._cast(
                _7063.CycloidalDiscAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def fe_part_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7075.FEPartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7075,
            )

            return self._parent._cast(
                _7075.FEPartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7115.ShaftAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7115,
            )

            return self._parent._cast(
                _7115.ShaftAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_or_housing_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation.TYPE",
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
    def system_deflection_results(
        self: Self,
    ) -> "_2694.AbstractShaftOrHousingSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftOrHousingSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation":
        return (
            self._Cast_AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation(
                self
            )
        )
