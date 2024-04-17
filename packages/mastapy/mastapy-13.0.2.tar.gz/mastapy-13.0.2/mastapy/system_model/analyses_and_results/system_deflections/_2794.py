"""PartToPartShearCouplingConnectionSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2737
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "PartToPartShearCouplingConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2355
    from mastapy.system_model.analyses_and_results.static_loads import _6938
    from mastapy.system_model.analyses_and_results.power_flows import _4123
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2775,
        _2735,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7548,
        _7549,
        _7546,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionSystemDeflection",)


Self = TypeVar("Self", bound="PartToPartShearCouplingConnectionSystemDeflection")


class PartToPartShearCouplingConnectionSystemDeflection(
    _2737.CouplingConnectionSystemDeflection
):
    """PartToPartShearCouplingConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingConnectionSystemDeflection"
    )

    class _Cast_PartToPartShearCouplingConnectionSystemDeflection:
        """Special nested class for casting PartToPartShearCouplingConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
            parent: "PartToPartShearCouplingConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_connection_system_deflection(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
        ) -> "_2737.CouplingConnectionSystemDeflection":
            return self._parent._cast(_2737.CouplingConnectionSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
        ) -> "_2775.InterMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2775,
            )

            return self._parent._cast(
                _2775.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
        ) -> "_2735.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(_2735.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
        ) -> "_7548.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_system_deflection(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
        ) -> "PartToPartShearCouplingConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2355.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6938.PartToPartShearCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(
        self: Self,
    ) -> "_4123.PartToPartShearCouplingConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.PartToPartShearCouplingConnectionPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection":
        return self._Cast_PartToPartShearCouplingConnectionSystemDeflection(self)
