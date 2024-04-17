"""KinematicViscosity"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KINEMATIC_VISCOSITY = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "KinematicViscosity"
)


__docformat__ = "restructuredtext en"
__all__ = ("KinematicViscosity",)


Self = TypeVar("Self", bound="KinematicViscosity")


class KinematicViscosity(_1612.MeasurementBase):
    """KinematicViscosity

    This is a mastapy class.
    """

    TYPE = _KINEMATIC_VISCOSITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_KinematicViscosity")

    class _Cast_KinematicViscosity:
        """Special nested class for casting KinematicViscosity to subclasses."""

        def __init__(
            self: "KinematicViscosity._Cast_KinematicViscosity",
            parent: "KinematicViscosity",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "KinematicViscosity._Cast_KinematicViscosity",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def kinematic_viscosity(
            self: "KinematicViscosity._Cast_KinematicViscosity",
        ) -> "KinematicViscosity":
            return self._parent

        def __getattr__(self: "KinematicViscosity._Cast_KinematicViscosity", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "KinematicViscosity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "KinematicViscosity._Cast_KinematicViscosity":
        return self._Cast_KinematicViscosity(self)
