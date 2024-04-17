"""LoadedAxialThrustCylindricalRollerBearingDutyCycle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2030
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_AXIAL_THRUST_CYLINDRICAL_ROLLER_BEARING_DUTY_CYCLE = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedAxialThrustCylindricalRollerBearingDutyCycle",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results import _1966, _1963, _1955


__docformat__ = "restructuredtext en"
__all__ = ("LoadedAxialThrustCylindricalRollerBearingDutyCycle",)


Self = TypeVar("Self", bound="LoadedAxialThrustCylindricalRollerBearingDutyCycle")


class LoadedAxialThrustCylindricalRollerBearingDutyCycle(
    _2030.LoadedNonBarrelRollerBearingDutyCycle
):
    """LoadedAxialThrustCylindricalRollerBearingDutyCycle

    This is a mastapy class.
    """

    TYPE = _LOADED_AXIAL_THRUST_CYLINDRICAL_ROLLER_BEARING_DUTY_CYCLE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedAxialThrustCylindricalRollerBearingDutyCycle"
    )

    class _Cast_LoadedAxialThrustCylindricalRollerBearingDutyCycle:
        """Special nested class for casting LoadedAxialThrustCylindricalRollerBearingDutyCycle to subclasses."""

        def __init__(
            self: "LoadedAxialThrustCylindricalRollerBearingDutyCycle._Cast_LoadedAxialThrustCylindricalRollerBearingDutyCycle",
            parent: "LoadedAxialThrustCylindricalRollerBearingDutyCycle",
        ):
            self._parent = parent

        @property
        def loaded_non_barrel_roller_bearing_duty_cycle(
            self: "LoadedAxialThrustCylindricalRollerBearingDutyCycle._Cast_LoadedAxialThrustCylindricalRollerBearingDutyCycle",
        ) -> "_2030.LoadedNonBarrelRollerBearingDutyCycle":
            return self._parent._cast(_2030.LoadedNonBarrelRollerBearingDutyCycle)

        @property
        def loaded_rolling_bearing_duty_cycle(
            self: "LoadedAxialThrustCylindricalRollerBearingDutyCycle._Cast_LoadedAxialThrustCylindricalRollerBearingDutyCycle",
        ) -> "_1966.LoadedRollingBearingDutyCycle":
            from mastapy.bearings.bearing_results import _1966

            return self._parent._cast(_1966.LoadedRollingBearingDutyCycle)

        @property
        def loaded_non_linear_bearing_duty_cycle_results(
            self: "LoadedAxialThrustCylindricalRollerBearingDutyCycle._Cast_LoadedAxialThrustCylindricalRollerBearingDutyCycle",
        ) -> "_1963.LoadedNonLinearBearingDutyCycleResults":
            from mastapy.bearings.bearing_results import _1963

            return self._parent._cast(_1963.LoadedNonLinearBearingDutyCycleResults)

        @property
        def loaded_bearing_duty_cycle(
            self: "LoadedAxialThrustCylindricalRollerBearingDutyCycle._Cast_LoadedAxialThrustCylindricalRollerBearingDutyCycle",
        ) -> "_1955.LoadedBearingDutyCycle":
            from mastapy.bearings.bearing_results import _1955

            return self._parent._cast(_1955.LoadedBearingDutyCycle)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_duty_cycle(
            self: "LoadedAxialThrustCylindricalRollerBearingDutyCycle._Cast_LoadedAxialThrustCylindricalRollerBearingDutyCycle",
        ) -> "LoadedAxialThrustCylindricalRollerBearingDutyCycle":
            return self._parent

        def __getattr__(
            self: "LoadedAxialThrustCylindricalRollerBearingDutyCycle._Cast_LoadedAxialThrustCylindricalRollerBearingDutyCycle",
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
        instance_to_wrap: "LoadedAxialThrustCylindricalRollerBearingDutyCycle.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedAxialThrustCylindricalRollerBearingDutyCycle._Cast_LoadedAxialThrustCylindricalRollerBearingDutyCycle":
        return self._Cast_LoadedAxialThrustCylindricalRollerBearingDutyCycle(self)
