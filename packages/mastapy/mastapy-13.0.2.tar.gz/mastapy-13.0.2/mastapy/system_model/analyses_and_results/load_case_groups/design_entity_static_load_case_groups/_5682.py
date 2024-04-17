"""ConnectionStaticLoadCaseGroup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Generic

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
    _5683,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_STATIC_LOAD_CASE_GROUP = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.DesignEntityStaticLoadCaseGroups",
    "ConnectionStaticLoadCaseGroup",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2279
    from mastapy.system_model.analyses_and_results.static_loads import _6858


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionStaticLoadCaseGroup",)


Self = TypeVar("Self", bound="ConnectionStaticLoadCaseGroup")
TConnection = TypeVar("TConnection", bound="_2279.Connection")
TConnectionStaticLoad = TypeVar(
    "TConnectionStaticLoad", bound="_6858.ConnectionLoadCase"
)


class ConnectionStaticLoadCaseGroup(
    _5683.DesignEntityStaticLoadCaseGroup, Generic[TConnection, TConnectionStaticLoad]
):
    """ConnectionStaticLoadCaseGroup

    This is a mastapy class.

    Generic Types:
        TConnection
        TConnectionStaticLoad
    """

    TYPE = _CONNECTION_STATIC_LOAD_CASE_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionStaticLoadCaseGroup")

    class _Cast_ConnectionStaticLoadCaseGroup:
        """Special nested class for casting ConnectionStaticLoadCaseGroup to subclasses."""

        def __init__(
            self: "ConnectionStaticLoadCaseGroup._Cast_ConnectionStaticLoadCaseGroup",
            parent: "ConnectionStaticLoadCaseGroup",
        ):
            self._parent = parent

        @property
        def design_entity_static_load_case_group(
            self: "ConnectionStaticLoadCaseGroup._Cast_ConnectionStaticLoadCaseGroup",
        ) -> "_5683.DesignEntityStaticLoadCaseGroup":
            return self._parent._cast(_5683.DesignEntityStaticLoadCaseGroup)

        @property
        def connection_static_load_case_group(
            self: "ConnectionStaticLoadCaseGroup._Cast_ConnectionStaticLoadCaseGroup",
        ) -> "ConnectionStaticLoadCaseGroup":
            return self._parent

        def __getattr__(
            self: "ConnectionStaticLoadCaseGroup._Cast_ConnectionStaticLoadCaseGroup",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectionStaticLoadCaseGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection(self: Self) -> "TConnection":
        """TConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Connection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_cases(self: Self) -> "List[TConnectionStaticLoad]":
        """List[TConnectionStaticLoad]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectionStaticLoadCaseGroup._Cast_ConnectionStaticLoadCaseGroup":
        return self._Cast_ConnectionStaticLoadCaseGroup(self)
