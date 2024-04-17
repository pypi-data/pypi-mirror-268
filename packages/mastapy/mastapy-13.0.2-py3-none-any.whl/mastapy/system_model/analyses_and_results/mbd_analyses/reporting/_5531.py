"""AbstractMeasuredDynamicResponseAtTime"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_MEASURED_DYNAMIC_RESPONSE_AT_TIME = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Reporting",
    "AbstractMeasuredDynamicResponseAtTime",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses.reporting import (
        _5532,
        _5534,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractMeasuredDynamicResponseAtTime",)


Self = TypeVar("Self", bound="AbstractMeasuredDynamicResponseAtTime")


class AbstractMeasuredDynamicResponseAtTime(_0.APIBase):
    """AbstractMeasuredDynamicResponseAtTime

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_MEASURED_DYNAMIC_RESPONSE_AT_TIME
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractMeasuredDynamicResponseAtTime"
    )

    class _Cast_AbstractMeasuredDynamicResponseAtTime:
        """Special nested class for casting AbstractMeasuredDynamicResponseAtTime to subclasses."""

        def __init__(
            self: "AbstractMeasuredDynamicResponseAtTime._Cast_AbstractMeasuredDynamicResponseAtTime",
            parent: "AbstractMeasuredDynamicResponseAtTime",
        ):
            self._parent = parent

        @property
        def dynamic_force_result_at_time(
            self: "AbstractMeasuredDynamicResponseAtTime._Cast_AbstractMeasuredDynamicResponseAtTime",
        ) -> "_5532.DynamicForceResultAtTime":
            from mastapy.system_model.analyses_and_results.mbd_analyses.reporting import (
                _5532,
            )

            return self._parent._cast(_5532.DynamicForceResultAtTime)

        @property
        def dynamic_torque_result_at_time(
            self: "AbstractMeasuredDynamicResponseAtTime._Cast_AbstractMeasuredDynamicResponseAtTime",
        ) -> "_5534.DynamicTorqueResultAtTime":
            from mastapy.system_model.analyses_and_results.mbd_analyses.reporting import (
                _5534,
            )

            return self._parent._cast(_5534.DynamicTorqueResultAtTime)

        @property
        def abstract_measured_dynamic_response_at_time(
            self: "AbstractMeasuredDynamicResponseAtTime._Cast_AbstractMeasuredDynamicResponseAtTime",
        ) -> "AbstractMeasuredDynamicResponseAtTime":
            return self._parent

        def __getattr__(
            self: "AbstractMeasuredDynamicResponseAtTime._Cast_AbstractMeasuredDynamicResponseAtTime",
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
        self: Self, instance_to_wrap: "AbstractMeasuredDynamicResponseAtTime.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def percentage_increase(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PercentageIncrease

        if temp is None:
            return 0.0

        return temp

    @property
    def time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Time

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractMeasuredDynamicResponseAtTime._Cast_AbstractMeasuredDynamicResponseAtTime":
        return self._Cast_AbstractMeasuredDynamicResponseAtTime(self)
