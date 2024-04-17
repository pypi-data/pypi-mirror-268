"""PlungeShavingDynamicsCalculationForHobbedGears"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
    _771,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLUNGE_SHAVING_DYNAMICS_CALCULATION_FOR_HOBBED_GEARS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics",
    "PlungeShavingDynamicsCalculationForHobbedGears",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
        _769,
    )


__docformat__ = "restructuredtext en"
__all__ = ("PlungeShavingDynamicsCalculationForHobbedGears",)


Self = TypeVar("Self", bound="PlungeShavingDynamicsCalculationForHobbedGears")


class PlungeShavingDynamicsCalculationForHobbedGears(
    _771.ShavingDynamicsCalculationForHobbedGears["_758.PlungeShaverDynamics"]
):
    """PlungeShavingDynamicsCalculationForHobbedGears

    This is a mastapy class.
    """

    TYPE = _PLUNGE_SHAVING_DYNAMICS_CALCULATION_FOR_HOBBED_GEARS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlungeShavingDynamicsCalculationForHobbedGears"
    )

    class _Cast_PlungeShavingDynamicsCalculationForHobbedGears:
        """Special nested class for casting PlungeShavingDynamicsCalculationForHobbedGears to subclasses."""

        def __init__(
            self: "PlungeShavingDynamicsCalculationForHobbedGears._Cast_PlungeShavingDynamicsCalculationForHobbedGears",
            parent: "PlungeShavingDynamicsCalculationForHobbedGears",
        ):
            self._parent = parent

        @property
        def shaving_dynamics_calculation_for_hobbed_gears(
            self: "PlungeShavingDynamicsCalculationForHobbedGears._Cast_PlungeShavingDynamicsCalculationForHobbedGears",
        ) -> "_771.ShavingDynamicsCalculationForHobbedGears":
            return self._parent._cast(_771.ShavingDynamicsCalculationForHobbedGears)

        @property
        def shaving_dynamics_calculation(
            self: "PlungeShavingDynamicsCalculationForHobbedGears._Cast_PlungeShavingDynamicsCalculationForHobbedGears",
        ) -> "_769.ShavingDynamicsCalculation":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _769,
            )

            return self._parent._cast(_769.ShavingDynamicsCalculation)

        @property
        def plunge_shaving_dynamics_calculation_for_hobbed_gears(
            self: "PlungeShavingDynamicsCalculationForHobbedGears._Cast_PlungeShavingDynamicsCalculationForHobbedGears",
        ) -> "PlungeShavingDynamicsCalculationForHobbedGears":
            return self._parent

        def __getattr__(
            self: "PlungeShavingDynamicsCalculationForHobbedGears._Cast_PlungeShavingDynamicsCalculationForHobbedGears",
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
        instance_to_wrap: "PlungeShavingDynamicsCalculationForHobbedGears.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PlungeShavingDynamicsCalculationForHobbedGears._Cast_PlungeShavingDynamicsCalculationForHobbedGears":
        return self._Cast_PlungeShavingDynamicsCalculationForHobbedGears(self)
