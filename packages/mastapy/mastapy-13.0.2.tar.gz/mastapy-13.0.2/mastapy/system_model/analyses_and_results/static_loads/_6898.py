"""ForceAndTorqueScalingFactor"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FORCE_AND_TORQUE_SCALING_FACTOR = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ForceAndTorqueScalingFactor",
)


__docformat__ = "restructuredtext en"
__all__ = ("ForceAndTorqueScalingFactor",)


Self = TypeVar("Self", bound="ForceAndTorqueScalingFactor")


class ForceAndTorqueScalingFactor(_0.APIBase):
    """ForceAndTorqueScalingFactor

    This is a mastapy class.
    """

    TYPE = _FORCE_AND_TORQUE_SCALING_FACTOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ForceAndTorqueScalingFactor")

    class _Cast_ForceAndTorqueScalingFactor:
        """Special nested class for casting ForceAndTorqueScalingFactor to subclasses."""

        def __init__(
            self: "ForceAndTorqueScalingFactor._Cast_ForceAndTorqueScalingFactor",
            parent: "ForceAndTorqueScalingFactor",
        ):
            self._parent = parent

        @property
        def force_and_torque_scaling_factor(
            self: "ForceAndTorqueScalingFactor._Cast_ForceAndTorqueScalingFactor",
        ) -> "ForceAndTorqueScalingFactor":
            return self._parent

        def __getattr__(
            self: "ForceAndTorqueScalingFactor._Cast_ForceAndTorqueScalingFactor",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ForceAndTorqueScalingFactor.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def force_scaling_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ForceScalingFactor

        if temp is None:
            return 0.0

        return temp

    @force_scaling_factor.setter
    @enforce_parameter_types
    def force_scaling_factor(self: Self, value: "float"):
        self.wrapped.ForceScalingFactor = float(value) if value is not None else 0.0

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_scaling_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TorqueScalingFactor

        if temp is None:
            return 0.0

        return temp

    @torque_scaling_factor.setter
    @enforce_parameter_types
    def torque_scaling_factor(self: Self, value: "float"):
        self.wrapped.TorqueScalingFactor = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "ForceAndTorqueScalingFactor._Cast_ForceAndTorqueScalingFactor":
        return self._Cast_ForceAndTorqueScalingFactor(self)
