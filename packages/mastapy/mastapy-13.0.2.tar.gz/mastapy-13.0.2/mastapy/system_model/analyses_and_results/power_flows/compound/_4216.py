"""CVTCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4185
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "CVTCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4081
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4273,
        _4175,
        _4254,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTCompoundPowerFlow",)


Self = TypeVar("Self", bound="CVTCompoundPowerFlow")


class CVTCompoundPowerFlow(_4185.BeltDriveCompoundPowerFlow):
    """CVTCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CVT_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTCompoundPowerFlow")

    class _Cast_CVTCompoundPowerFlow:
        """Special nested class for casting CVTCompoundPowerFlow to subclasses."""

        def __init__(
            self: "CVTCompoundPowerFlow._Cast_CVTCompoundPowerFlow",
            parent: "CVTCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def belt_drive_compound_power_flow(
            self: "CVTCompoundPowerFlow._Cast_CVTCompoundPowerFlow",
        ) -> "_4185.BeltDriveCompoundPowerFlow":
            return self._parent._cast(_4185.BeltDriveCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "CVTCompoundPowerFlow._Cast_CVTCompoundPowerFlow",
        ) -> "_4273.SpecialisedAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4273,
            )

            return self._parent._cast(_4273.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "CVTCompoundPowerFlow._Cast_CVTCompoundPowerFlow",
        ) -> "_4175.AbstractAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4175,
            )

            return self._parent._cast(_4175.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "CVTCompoundPowerFlow._Cast_CVTCompoundPowerFlow",
        ) -> "_4254.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "CVTCompoundPowerFlow._Cast_CVTCompoundPowerFlow",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTCompoundPowerFlow._Cast_CVTCompoundPowerFlow",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTCompoundPowerFlow._Cast_CVTCompoundPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_compound_power_flow(
            self: "CVTCompoundPowerFlow._Cast_CVTCompoundPowerFlow",
        ) -> "CVTCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "CVTCompoundPowerFlow._Cast_CVTCompoundPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self: Self) -> "List[_4081.CVTPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CVTPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4081.CVTPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CVTPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "CVTCompoundPowerFlow._Cast_CVTCompoundPowerFlow":
        return self._Cast_CVTCompoundPowerFlow(self)
