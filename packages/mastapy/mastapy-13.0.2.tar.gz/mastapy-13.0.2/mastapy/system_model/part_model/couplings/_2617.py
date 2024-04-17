"""TorqueConverterSpeedRatio"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_SPEED_RATIO = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverterSpeedRatio"
)


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterSpeedRatio",)


Self = TypeVar("Self", bound="TorqueConverterSpeedRatio")


class TorqueConverterSpeedRatio(_0.APIBase):
    """TorqueConverterSpeedRatio

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_SPEED_RATIO
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterSpeedRatio")

    class _Cast_TorqueConverterSpeedRatio:
        """Special nested class for casting TorqueConverterSpeedRatio to subclasses."""

        def __init__(
            self: "TorqueConverterSpeedRatio._Cast_TorqueConverterSpeedRatio",
            parent: "TorqueConverterSpeedRatio",
        ):
            self._parent = parent

        @property
        def torque_converter_speed_ratio(
            self: "TorqueConverterSpeedRatio._Cast_TorqueConverterSpeedRatio",
        ) -> "TorqueConverterSpeedRatio":
            return self._parent

        def __getattr__(
            self: "TorqueConverterSpeedRatio._Cast_TorqueConverterSpeedRatio", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverterSpeedRatio.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def inverse_k(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InverseK

        if temp is None:
            return 0.0

        return temp

    @inverse_k.setter
    @enforce_parameter_types
    def inverse_k(self: Self, value: "float"):
        self.wrapped.InverseK = float(value) if value is not None else 0.0

    @property
    def speed_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpeedRatio

        if temp is None:
            return 0.0

        return temp

    @speed_ratio.setter
    @enforce_parameter_types
    def speed_ratio(self: Self, value: "float"):
        self.wrapped.SpeedRatio = float(value) if value is not None else 0.0

    @property
    def torque_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TorqueRatio

        if temp is None:
            return 0.0

        return temp

    @torque_ratio.setter
    @enforce_parameter_types
    def torque_ratio(self: Self, value: "float"):
        self.wrapped.TorqueRatio = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterSpeedRatio._Cast_TorqueConverterSpeedRatio":
        return self._Cast_TorqueConverterSpeedRatio(self)
