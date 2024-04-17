"""DynamicTorqueResultAtTime"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.mbd_analyses.reporting import _5531
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_TORQUE_RESULT_AT_TIME = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Reporting",
    "DynamicTorqueResultAtTime",
)


__docformat__ = "restructuredtext en"
__all__ = ("DynamicTorqueResultAtTime",)


Self = TypeVar("Self", bound="DynamicTorqueResultAtTime")


class DynamicTorqueResultAtTime(_5531.AbstractMeasuredDynamicResponseAtTime):
    """DynamicTorqueResultAtTime

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_TORQUE_RESULT_AT_TIME
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicTorqueResultAtTime")

    class _Cast_DynamicTorqueResultAtTime:
        """Special nested class for casting DynamicTorqueResultAtTime to subclasses."""

        def __init__(
            self: "DynamicTorqueResultAtTime._Cast_DynamicTorqueResultAtTime",
            parent: "DynamicTorqueResultAtTime",
        ):
            self._parent = parent

        @property
        def abstract_measured_dynamic_response_at_time(
            self: "DynamicTorqueResultAtTime._Cast_DynamicTorqueResultAtTime",
        ) -> "_5531.AbstractMeasuredDynamicResponseAtTime":
            return self._parent._cast(_5531.AbstractMeasuredDynamicResponseAtTime)

        @property
        def dynamic_torque_result_at_time(
            self: "DynamicTorqueResultAtTime._Cast_DynamicTorqueResultAtTime",
        ) -> "DynamicTorqueResultAtTime":
            return self._parent

        def __getattr__(
            self: "DynamicTorqueResultAtTime._Cast_DynamicTorqueResultAtTime", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicTorqueResultAtTime.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def absolute_dynamic_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AbsoluteDynamicTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "DynamicTorqueResultAtTime._Cast_DynamicTorqueResultAtTime":
        return self._Cast_DynamicTorqueResultAtTime(self)
