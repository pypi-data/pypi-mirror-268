"""PlungeShavingDynamicsCalculationForDesignedGears"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
    _770,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLUNGE_SHAVING_DYNAMICS_CALCULATION_FOR_DESIGNED_GEARS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics",
    "PlungeShavingDynamicsCalculationForDesignedGears",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
        _769,
    )


__docformat__ = "restructuredtext en"
__all__ = ("PlungeShavingDynamicsCalculationForDesignedGears",)


Self = TypeVar("Self", bound="PlungeShavingDynamicsCalculationForDesignedGears")


class PlungeShavingDynamicsCalculationForDesignedGears(
    _770.ShavingDynamicsCalculationForDesignedGears["_758.PlungeShaverDynamics"]
):
    """PlungeShavingDynamicsCalculationForDesignedGears

    This is a mastapy class.
    """

    TYPE = _PLUNGE_SHAVING_DYNAMICS_CALCULATION_FOR_DESIGNED_GEARS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlungeShavingDynamicsCalculationForDesignedGears"
    )

    class _Cast_PlungeShavingDynamicsCalculationForDesignedGears:
        """Special nested class for casting PlungeShavingDynamicsCalculationForDesignedGears to subclasses."""

        def __init__(
            self: "PlungeShavingDynamicsCalculationForDesignedGears._Cast_PlungeShavingDynamicsCalculationForDesignedGears",
            parent: "PlungeShavingDynamicsCalculationForDesignedGears",
        ):
            self._parent = parent

        @property
        def shaving_dynamics_calculation_for_designed_gears(
            self: "PlungeShavingDynamicsCalculationForDesignedGears._Cast_PlungeShavingDynamicsCalculationForDesignedGears",
        ) -> "_770.ShavingDynamicsCalculationForDesignedGears":
            return self._parent._cast(_770.ShavingDynamicsCalculationForDesignedGears)

        @property
        def shaving_dynamics_calculation(
            self: "PlungeShavingDynamicsCalculationForDesignedGears._Cast_PlungeShavingDynamicsCalculationForDesignedGears",
        ) -> "_769.ShavingDynamicsCalculation":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _769,
            )

            return self._parent._cast(_769.ShavingDynamicsCalculation)

        @property
        def plunge_shaving_dynamics_calculation_for_designed_gears(
            self: "PlungeShavingDynamicsCalculationForDesignedGears._Cast_PlungeShavingDynamicsCalculationForDesignedGears",
        ) -> "PlungeShavingDynamicsCalculationForDesignedGears":
            return self._parent

        def __getattr__(
            self: "PlungeShavingDynamicsCalculationForDesignedGears._Cast_PlungeShavingDynamicsCalculationForDesignedGears",
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
        instance_to_wrap: "PlungeShavingDynamicsCalculationForDesignedGears.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PlungeShavingDynamicsCalculationForDesignedGears._Cast_PlungeShavingDynamicsCalculationForDesignedGears":
        return self._Cast_PlungeShavingDynamicsCalculationForDesignedGears(self)
