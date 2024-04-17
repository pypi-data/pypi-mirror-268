"""ConventionalShavingDynamics"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
    _768,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONVENTIONAL_SHAVING_DYNAMICS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics",
    "ConventionalShavingDynamics",
)


__docformat__ = "restructuredtext en"
__all__ = ("ConventionalShavingDynamics",)


Self = TypeVar("Self", bound="ConventionalShavingDynamics")


class ConventionalShavingDynamics(_768.ShavingDynamics):
    """ConventionalShavingDynamics

    This is a mastapy class.
    """

    TYPE = _CONVENTIONAL_SHAVING_DYNAMICS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConventionalShavingDynamics")

    class _Cast_ConventionalShavingDynamics:
        """Special nested class for casting ConventionalShavingDynamics to subclasses."""

        def __init__(
            self: "ConventionalShavingDynamics._Cast_ConventionalShavingDynamics",
            parent: "ConventionalShavingDynamics",
        ):
            self._parent = parent

        @property
        def shaving_dynamics(
            self: "ConventionalShavingDynamics._Cast_ConventionalShavingDynamics",
        ) -> "_768.ShavingDynamics":
            return self._parent._cast(_768.ShavingDynamics)

        @property
        def conventional_shaving_dynamics(
            self: "ConventionalShavingDynamics._Cast_ConventionalShavingDynamics",
        ) -> "ConventionalShavingDynamics":
            return self._parent

        def __getattr__(
            self: "ConventionalShavingDynamics._Cast_ConventionalShavingDynamics",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConventionalShavingDynamics.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConventionalShavingDynamics._Cast_ConventionalShavingDynamics":
        return self._Cast_ConventionalShavingDynamics(self)
