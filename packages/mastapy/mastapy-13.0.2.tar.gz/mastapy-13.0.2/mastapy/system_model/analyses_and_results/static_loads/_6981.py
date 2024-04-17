"""TorqueConverterConnectionLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6860
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "TorqueConverterConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2359
    from mastapy.system_model.analyses_and_results.static_loads import _6920, _6858
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionLoadCase",)


Self = TypeVar("Self", bound="TorqueConverterConnectionLoadCase")


class TorqueConverterConnectionLoadCase(_6860.CouplingConnectionLoadCase):
    """TorqueConverterConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterConnectionLoadCase")

    class _Cast_TorqueConverterConnectionLoadCase:
        """Special nested class for casting TorqueConverterConnectionLoadCase to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionLoadCase._Cast_TorqueConverterConnectionLoadCase",
            parent: "TorqueConverterConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_connection_load_case(
            self: "TorqueConverterConnectionLoadCase._Cast_TorqueConverterConnectionLoadCase",
        ) -> "_6860.CouplingConnectionLoadCase":
            return self._parent._cast(_6860.CouplingConnectionLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "TorqueConverterConnectionLoadCase._Cast_TorqueConverterConnectionLoadCase",
        ) -> "_6920.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6920

            return self._parent._cast(_6920.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "TorqueConverterConnectionLoadCase._Cast_TorqueConverterConnectionLoadCase",
        ) -> "_6858.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6858

            return self._parent._cast(_6858.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "TorqueConverterConnectionLoadCase._Cast_TorqueConverterConnectionLoadCase",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterConnectionLoadCase._Cast_TorqueConverterConnectionLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionLoadCase._Cast_TorqueConverterConnectionLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def torque_converter_connection_load_case(
            self: "TorqueConverterConnectionLoadCase._Cast_TorqueConverterConnectionLoadCase",
        ) -> "TorqueConverterConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionLoadCase._Cast_TorqueConverterConnectionLoadCase",
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
        self: Self, instance_to_wrap: "TorqueConverterConnectionLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2359.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterConnectionLoadCase._Cast_TorqueConverterConnectionLoadCase":
        return self._Cast_TorqueConverterConnectionLoadCase(self)
