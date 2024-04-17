"""ConventionalShavingDynamicsCalculationForDesignedGears"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
    _770,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONVENTIONAL_SHAVING_DYNAMICS_CALCULATION_FOR_DESIGNED_GEARS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics",
    "ConventionalShavingDynamicsCalculationForDesignedGears",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
        _769,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConventionalShavingDynamicsCalculationForDesignedGears",)


Self = TypeVar("Self", bound="ConventionalShavingDynamicsCalculationForDesignedGears")


class ConventionalShavingDynamicsCalculationForDesignedGears(
    _770.ShavingDynamicsCalculationForDesignedGears["_754.ConventionalShavingDynamics"]
):
    """ConventionalShavingDynamicsCalculationForDesignedGears

    This is a mastapy class.
    """

    TYPE = _CONVENTIONAL_SHAVING_DYNAMICS_CALCULATION_FOR_DESIGNED_GEARS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConventionalShavingDynamicsCalculationForDesignedGears",
    )

    class _Cast_ConventionalShavingDynamicsCalculationForDesignedGears:
        """Special nested class for casting ConventionalShavingDynamicsCalculationForDesignedGears to subclasses."""

        def __init__(
            self: "ConventionalShavingDynamicsCalculationForDesignedGears._Cast_ConventionalShavingDynamicsCalculationForDesignedGears",
            parent: "ConventionalShavingDynamicsCalculationForDesignedGears",
        ):
            self._parent = parent

        @property
        def shaving_dynamics_calculation_for_designed_gears(
            self: "ConventionalShavingDynamicsCalculationForDesignedGears._Cast_ConventionalShavingDynamicsCalculationForDesignedGears",
        ) -> "_770.ShavingDynamicsCalculationForDesignedGears":
            return self._parent._cast(_770.ShavingDynamicsCalculationForDesignedGears)

        @property
        def shaving_dynamics_calculation(
            self: "ConventionalShavingDynamicsCalculationForDesignedGears._Cast_ConventionalShavingDynamicsCalculationForDesignedGears",
        ) -> "_769.ShavingDynamicsCalculation":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _769,
            )

            return self._parent._cast(_769.ShavingDynamicsCalculation)

        @property
        def conventional_shaving_dynamics_calculation_for_designed_gears(
            self: "ConventionalShavingDynamicsCalculationForDesignedGears._Cast_ConventionalShavingDynamicsCalculationForDesignedGears",
        ) -> "ConventionalShavingDynamicsCalculationForDesignedGears":
            return self._parent

        def __getattr__(
            self: "ConventionalShavingDynamicsCalculationForDesignedGears._Cast_ConventionalShavingDynamicsCalculationForDesignedGears",
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
        instance_to_wrap: "ConventionalShavingDynamicsCalculationForDesignedGears.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConventionalShavingDynamicsCalculationForDesignedGears._Cast_ConventionalShavingDynamicsCalculationForDesignedGears":
        return self._Cast_ConventionalShavingDynamicsCalculationForDesignedGears(self)
