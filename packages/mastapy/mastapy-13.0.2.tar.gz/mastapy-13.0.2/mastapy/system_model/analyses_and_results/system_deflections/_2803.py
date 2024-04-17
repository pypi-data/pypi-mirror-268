"""RingPinsToDiscConnectionSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2775
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "RingPinsToDiscConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2348
    from mastapy.system_model.analyses_and_results.static_loads import _6953
    from mastapy.system_model.analyses_and_results.power_flows import _4135
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2804,
        _2735,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7548,
        _7549,
        _7546,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionSystemDeflection",)


Self = TypeVar("Self", bound="RingPinsToDiscConnectionSystemDeflection")


class RingPinsToDiscConnectionSystemDeflection(
    _2775.InterMountableComponentConnectionSystemDeflection
):
    """RingPinsToDiscConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsToDiscConnectionSystemDeflection"
    )

    class _Cast_RingPinsToDiscConnectionSystemDeflection:
        """Special nested class for casting RingPinsToDiscConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionSystemDeflection._Cast_RingPinsToDiscConnectionSystemDeflection",
            parent: "RingPinsToDiscConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "RingPinsToDiscConnectionSystemDeflection._Cast_RingPinsToDiscConnectionSystemDeflection",
        ) -> "_2775.InterMountableComponentConnectionSystemDeflection":
            return self._parent._cast(
                _2775.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "RingPinsToDiscConnectionSystemDeflection._Cast_RingPinsToDiscConnectionSystemDeflection",
        ) -> "_2735.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(_2735.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "RingPinsToDiscConnectionSystemDeflection._Cast_RingPinsToDiscConnectionSystemDeflection",
        ) -> "_7548.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "RingPinsToDiscConnectionSystemDeflection._Cast_RingPinsToDiscConnectionSystemDeflection",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "RingPinsToDiscConnectionSystemDeflection._Cast_RingPinsToDiscConnectionSystemDeflection",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RingPinsToDiscConnectionSystemDeflection._Cast_RingPinsToDiscConnectionSystemDeflection",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsToDiscConnectionSystemDeflection._Cast_RingPinsToDiscConnectionSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionSystemDeflection._Cast_RingPinsToDiscConnectionSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_system_deflection(
            self: "RingPinsToDiscConnectionSystemDeflection._Cast_RingPinsToDiscConnectionSystemDeflection",
        ) -> "RingPinsToDiscConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionSystemDeflection._Cast_RingPinsToDiscConnectionSystemDeflection",
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
        self: Self, instance_to_wrap: "RingPinsToDiscConnectionSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_contact_stress_across_all_pins(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumContactStressAcrossAllPins

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_deflections(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalDeflections

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def number_of_pins_in_contact(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfPinsInContact

        if temp is None:
            return 0

        return temp

    @property
    def pin_with_maximum_contact_stress(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinWithMaximumContactStress

        if temp is None:
            return 0

        return temp

    @property
    def strain_energy(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StrainEnergy

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self: Self) -> "_2348.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6953.RingPinsToDiscConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsToDiscConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4135.RingPinsToDiscConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.RingPinsToDiscConnectionPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def ring_pin_to_disc_contacts(
        self: Self,
    ) -> "List[_2804.RingPinToDiscContactReporting]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.RingPinToDiscContactReporting]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RingPinToDiscContacts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RingPinsToDiscConnectionSystemDeflection._Cast_RingPinsToDiscConnectionSystemDeflection":
        return self._Cast_RingPinsToDiscConnectionSystemDeflection(self)
