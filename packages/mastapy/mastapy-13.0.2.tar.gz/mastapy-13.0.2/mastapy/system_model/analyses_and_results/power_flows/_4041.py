"""AbstractShaftOrHousingPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4065
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "AbstractShaftOrHousingPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2443
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4042,
        _4086,
        _4099,
        _4141,
        _4122,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingPowerFlow",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingPowerFlow")


class AbstractShaftOrHousingPowerFlow(_4065.ComponentPowerFlow):
    """AbstractShaftOrHousingPowerFlow

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftOrHousingPowerFlow")

    class _Cast_AbstractShaftOrHousingPowerFlow:
        """Special nested class for casting AbstractShaftOrHousingPowerFlow to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingPowerFlow._Cast_AbstractShaftOrHousingPowerFlow",
            parent: "AbstractShaftOrHousingPowerFlow",
        ):
            self._parent = parent

        @property
        def component_power_flow(
            self: "AbstractShaftOrHousingPowerFlow._Cast_AbstractShaftOrHousingPowerFlow",
        ) -> "_4065.ComponentPowerFlow":
            return self._parent._cast(_4065.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "AbstractShaftOrHousingPowerFlow._Cast_AbstractShaftOrHousingPowerFlow",
        ) -> "_4122.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingPowerFlow._Cast_AbstractShaftOrHousingPowerFlow",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingPowerFlow._Cast_AbstractShaftOrHousingPowerFlow",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingPowerFlow._Cast_AbstractShaftOrHousingPowerFlow",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingPowerFlow._Cast_AbstractShaftOrHousingPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingPowerFlow._Cast_AbstractShaftOrHousingPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_power_flow(
            self: "AbstractShaftOrHousingPowerFlow._Cast_AbstractShaftOrHousingPowerFlow",
        ) -> "_4042.AbstractShaftPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4042

            return self._parent._cast(_4042.AbstractShaftPowerFlow)

        @property
        def cycloidal_disc_power_flow(
            self: "AbstractShaftOrHousingPowerFlow._Cast_AbstractShaftOrHousingPowerFlow",
        ) -> "_4086.CycloidalDiscPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4086

            return self._parent._cast(_4086.CycloidalDiscPowerFlow)

        @property
        def fe_part_power_flow(
            self: "AbstractShaftOrHousingPowerFlow._Cast_AbstractShaftOrHousingPowerFlow",
        ) -> "_4099.FEPartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4099

            return self._parent._cast(_4099.FEPartPowerFlow)

        @property
        def shaft_power_flow(
            self: "AbstractShaftOrHousingPowerFlow._Cast_AbstractShaftOrHousingPowerFlow",
        ) -> "_4141.ShaftPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4141

            return self._parent._cast(_4141.ShaftPowerFlow)

        @property
        def abstract_shaft_or_housing_power_flow(
            self: "AbstractShaftOrHousingPowerFlow._Cast_AbstractShaftOrHousingPowerFlow",
        ) -> "AbstractShaftOrHousingPowerFlow":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingPowerFlow._Cast_AbstractShaftOrHousingPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaftOrHousingPowerFlow.TYPE"):
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
    ) -> "AbstractShaftOrHousingPowerFlow._Cast_AbstractShaftOrHousingPowerFlow":
        return self._Cast_AbstractShaftOrHousingPowerFlow(self)
