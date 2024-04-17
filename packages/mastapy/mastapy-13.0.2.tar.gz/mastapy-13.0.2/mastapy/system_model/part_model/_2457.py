"""EnginePartLoad"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ENGINE_PART_LOAD = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "EnginePartLoad"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnginePartLoad",)


Self = TypeVar("Self", bound="EnginePartLoad")


class EnginePartLoad(_0.APIBase):
    """EnginePartLoad

    This is a mastapy class.
    """

    TYPE = _ENGINE_PART_LOAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_EnginePartLoad")

    class _Cast_EnginePartLoad:
        """Special nested class for casting EnginePartLoad to subclasses."""

        def __init__(
            self: "EnginePartLoad._Cast_EnginePartLoad", parent: "EnginePartLoad"
        ):
            self._parent = parent

        @property
        def engine_part_load(
            self: "EnginePartLoad._Cast_EnginePartLoad",
        ) -> "EnginePartLoad":
            return self._parent

        def __getattr__(self: "EnginePartLoad._Cast_EnginePartLoad", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "EnginePartLoad.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def consumption(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Consumption

        if temp is None:
            return 0.0

        return temp

    @consumption.setter
    @enforce_parameter_types
    def consumption(self: Self, value: "float"):
        self.wrapped.Consumption = float(value) if value is not None else 0.0

    @property
    def throttle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Throttle

        if temp is None:
            return 0.0

        return temp

    @property
    def torque(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return temp

    @torque.setter
    @enforce_parameter_types
    def torque(self: Self, value: "float"):
        self.wrapped.Torque = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "EnginePartLoad._Cast_EnginePartLoad":
        return self._Cast_EnginePartLoad(self)
