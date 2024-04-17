"""ConventionalShavingDynamicsCalculationForHobbedGears"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
    _771,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONVENTIONAL_SHAVING_DYNAMICS_CALCULATION_FOR_HOBBED_GEARS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics",
    "ConventionalShavingDynamicsCalculationForHobbedGears",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
        _769,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConventionalShavingDynamicsCalculationForHobbedGears",)


Self = TypeVar("Self", bound="ConventionalShavingDynamicsCalculationForHobbedGears")


class ConventionalShavingDynamicsCalculationForHobbedGears(
    _771.ShavingDynamicsCalculationForHobbedGears["_754.ConventionalShavingDynamics"]
):
    """ConventionalShavingDynamicsCalculationForHobbedGears

    This is a mastapy class.
    """

    TYPE = _CONVENTIONAL_SHAVING_DYNAMICS_CALCULATION_FOR_HOBBED_GEARS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConventionalShavingDynamicsCalculationForHobbedGears"
    )

    class _Cast_ConventionalShavingDynamicsCalculationForHobbedGears:
        """Special nested class for casting ConventionalShavingDynamicsCalculationForHobbedGears to subclasses."""

        def __init__(
            self: "ConventionalShavingDynamicsCalculationForHobbedGears._Cast_ConventionalShavingDynamicsCalculationForHobbedGears",
            parent: "ConventionalShavingDynamicsCalculationForHobbedGears",
        ):
            self._parent = parent

        @property
        def shaving_dynamics_calculation_for_hobbed_gears(
            self: "ConventionalShavingDynamicsCalculationForHobbedGears._Cast_ConventionalShavingDynamicsCalculationForHobbedGears",
        ) -> "_771.ShavingDynamicsCalculationForHobbedGears":
            return self._parent._cast(_771.ShavingDynamicsCalculationForHobbedGears)

        @property
        def shaving_dynamics_calculation(
            self: "ConventionalShavingDynamicsCalculationForHobbedGears._Cast_ConventionalShavingDynamicsCalculationForHobbedGears",
        ) -> "_769.ShavingDynamicsCalculation":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _769,
            )

            return self._parent._cast(_769.ShavingDynamicsCalculation)

        @property
        def conventional_shaving_dynamics_calculation_for_hobbed_gears(
            self: "ConventionalShavingDynamicsCalculationForHobbedGears._Cast_ConventionalShavingDynamicsCalculationForHobbedGears",
        ) -> "ConventionalShavingDynamicsCalculationForHobbedGears":
            return self._parent

        def __getattr__(
            self: "ConventionalShavingDynamicsCalculationForHobbedGears._Cast_ConventionalShavingDynamicsCalculationForHobbedGears",
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
        instance_to_wrap: "ConventionalShavingDynamicsCalculationForHobbedGears.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConventionalShavingDynamicsCalculationForHobbedGears._Cast_ConventionalShavingDynamicsCalculationForHobbedGears":
        return self._Cast_ConventionalShavingDynamicsCalculationForHobbedGears(self)
