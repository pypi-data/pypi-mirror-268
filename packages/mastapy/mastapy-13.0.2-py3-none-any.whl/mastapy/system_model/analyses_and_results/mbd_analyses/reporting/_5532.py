"""DynamicForceResultAtTime"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.mbd_analyses.reporting import _5531
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_FORCE_RESULT_AT_TIME = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Reporting",
    "DynamicForceResultAtTime",
)


__docformat__ = "restructuredtext en"
__all__ = ("DynamicForceResultAtTime",)


Self = TypeVar("Self", bound="DynamicForceResultAtTime")


class DynamicForceResultAtTime(_5531.AbstractMeasuredDynamicResponseAtTime):
    """DynamicForceResultAtTime

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_FORCE_RESULT_AT_TIME
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicForceResultAtTime")

    class _Cast_DynamicForceResultAtTime:
        """Special nested class for casting DynamicForceResultAtTime to subclasses."""

        def __init__(
            self: "DynamicForceResultAtTime._Cast_DynamicForceResultAtTime",
            parent: "DynamicForceResultAtTime",
        ):
            self._parent = parent

        @property
        def abstract_measured_dynamic_response_at_time(
            self: "DynamicForceResultAtTime._Cast_DynamicForceResultAtTime",
        ) -> "_5531.AbstractMeasuredDynamicResponseAtTime":
            return self._parent._cast(_5531.AbstractMeasuredDynamicResponseAtTime)

        @property
        def dynamic_force_result_at_time(
            self: "DynamicForceResultAtTime._Cast_DynamicForceResultAtTime",
        ) -> "DynamicForceResultAtTime":
            return self._parent

        def __getattr__(
            self: "DynamicForceResultAtTime._Cast_DynamicForceResultAtTime", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicForceResultAtTime.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def absolute_dynamic_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AbsoluteDynamicForce

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicForce

        if temp is None:
            return 0.0

        return temp

    @property
    def force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Force

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanForce

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "DynamicForceResultAtTime._Cast_DynamicForceResultAtTime":
        return self._Cast_DynamicForceResultAtTime(self)
