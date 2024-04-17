"""LoadedNonLinearBearingDutyCycleResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results import _1955
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NON_LINEAR_BEARING_DUTY_CYCLE_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedNonLinearBearingDutyCycleResults"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results import _1966
    from mastapy.bearings.bearing_results.rolling import (
        _1999,
        _2006,
        _2014,
        _2030,
        _2053,
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedNonLinearBearingDutyCycleResults",)


Self = TypeVar("Self", bound="LoadedNonLinearBearingDutyCycleResults")


class LoadedNonLinearBearingDutyCycleResults(_1955.LoadedBearingDutyCycle):
    """LoadedNonLinearBearingDutyCycleResults

    This is a mastapy class.
    """

    TYPE = _LOADED_NON_LINEAR_BEARING_DUTY_CYCLE_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedNonLinearBearingDutyCycleResults"
    )

    class _Cast_LoadedNonLinearBearingDutyCycleResults:
        """Special nested class for casting LoadedNonLinearBearingDutyCycleResults to subclasses."""

        def __init__(
            self: "LoadedNonLinearBearingDutyCycleResults._Cast_LoadedNonLinearBearingDutyCycleResults",
            parent: "LoadedNonLinearBearingDutyCycleResults",
        ):
            self._parent = parent

        @property
        def loaded_bearing_duty_cycle(
            self: "LoadedNonLinearBearingDutyCycleResults._Cast_LoadedNonLinearBearingDutyCycleResults",
        ) -> "_1955.LoadedBearingDutyCycle":
            return self._parent._cast(_1955.LoadedBearingDutyCycle)

        @property
        def loaded_rolling_bearing_duty_cycle(
            self: "LoadedNonLinearBearingDutyCycleResults._Cast_LoadedNonLinearBearingDutyCycleResults",
        ) -> "_1966.LoadedRollingBearingDutyCycle":
            from mastapy.bearings.bearing_results import _1966

            return self._parent._cast(_1966.LoadedRollingBearingDutyCycle)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_duty_cycle(
            self: "LoadedNonLinearBearingDutyCycleResults._Cast_LoadedNonLinearBearingDutyCycleResults",
        ) -> "_1999.LoadedAxialThrustCylindricalRollerBearingDutyCycle":
            from mastapy.bearings.bearing_results.rolling import _1999

            return self._parent._cast(
                _1999.LoadedAxialThrustCylindricalRollerBearingDutyCycle
            )

        @property
        def loaded_ball_bearing_duty_cycle(
            self: "LoadedNonLinearBearingDutyCycleResults._Cast_LoadedNonLinearBearingDutyCycleResults",
        ) -> "_2006.LoadedBallBearingDutyCycle":
            from mastapy.bearings.bearing_results.rolling import _2006

            return self._parent._cast(_2006.LoadedBallBearingDutyCycle)

        @property
        def loaded_cylindrical_roller_bearing_duty_cycle(
            self: "LoadedNonLinearBearingDutyCycleResults._Cast_LoadedNonLinearBearingDutyCycleResults",
        ) -> "_2014.LoadedCylindricalRollerBearingDutyCycle":
            from mastapy.bearings.bearing_results.rolling import _2014

            return self._parent._cast(_2014.LoadedCylindricalRollerBearingDutyCycle)

        @property
        def loaded_non_barrel_roller_bearing_duty_cycle(
            self: "LoadedNonLinearBearingDutyCycleResults._Cast_LoadedNonLinearBearingDutyCycleResults",
        ) -> "_2030.LoadedNonBarrelRollerBearingDutyCycle":
            from mastapy.bearings.bearing_results.rolling import _2030

            return self._parent._cast(_2030.LoadedNonBarrelRollerBearingDutyCycle)

        @property
        def loaded_taper_roller_bearing_duty_cycle(
            self: "LoadedNonLinearBearingDutyCycleResults._Cast_LoadedNonLinearBearingDutyCycleResults",
        ) -> "_2053.LoadedTaperRollerBearingDutyCycle":
            from mastapy.bearings.bearing_results.rolling import _2053

            return self._parent._cast(_2053.LoadedTaperRollerBearingDutyCycle)

        @property
        def loaded_non_linear_bearing_duty_cycle_results(
            self: "LoadedNonLinearBearingDutyCycleResults._Cast_LoadedNonLinearBearingDutyCycleResults",
        ) -> "LoadedNonLinearBearingDutyCycleResults":
            return self._parent

        def __getattr__(
            self: "LoadedNonLinearBearingDutyCycleResults._Cast_LoadedNonLinearBearingDutyCycleResults",
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
        self: Self, instance_to_wrap: "LoadedNonLinearBearingDutyCycleResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def total_power_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedNonLinearBearingDutyCycleResults._Cast_LoadedNonLinearBearingDutyCycleResults":
        return self._Cast_LoadedNonLinearBearingDutyCycleResults(self)
