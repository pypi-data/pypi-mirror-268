"""AbstractShaftOrHousingCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4200
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "AbstractShaftOrHousingCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4041
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4176,
        _4220,
        _4231,
        _4270,
        _4254,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundPowerFlow",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingCompoundPowerFlow")


class AbstractShaftOrHousingCompoundPowerFlow(_4200.ComponentCompoundPowerFlow):
    """AbstractShaftOrHousingCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingCompoundPowerFlow"
    )

    class _Cast_AbstractShaftOrHousingCompoundPowerFlow:
        """Special nested class for casting AbstractShaftOrHousingCompoundPowerFlow to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
            parent: "AbstractShaftOrHousingCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def component_compound_power_flow(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
        ) -> "_4200.ComponentCompoundPowerFlow":
            return self._parent._cast(_4200.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
        ) -> "_4254.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_power_flow(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
        ) -> "_4176.AbstractShaftCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4176,
            )

            return self._parent._cast(_4176.AbstractShaftCompoundPowerFlow)

        @property
        def cycloidal_disc_compound_power_flow(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
        ) -> "_4220.CycloidalDiscCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4220,
            )

            return self._parent._cast(_4220.CycloidalDiscCompoundPowerFlow)

        @property
        def fe_part_compound_power_flow(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
        ) -> "_4231.FEPartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4231,
            )

            return self._parent._cast(_4231.FEPartCompoundPowerFlow)

        @property
        def shaft_compound_power_flow(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
        ) -> "_4270.ShaftCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4270,
            )

            return self._parent._cast(_4270.ShaftCompoundPowerFlow)

        @property
        def abstract_shaft_or_housing_compound_power_flow(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
        ) -> "AbstractShaftOrHousingCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "AbstractShaftOrHousingCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4041.AbstractShaftOrHousingPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AbstractShaftOrHousingPowerFlow]

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
    ) -> "List[_4041.AbstractShaftOrHousingPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AbstractShaftOrHousingPowerFlow]

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
    ) -> "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow":
        return self._Cast_AbstractShaftOrHousingCompoundPowerFlow(self)
