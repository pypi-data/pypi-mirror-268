"""SurfacePermanentMagnetRotor"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.electric_machines import _1297
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SURFACE_PERMANENT_MAGNET_ROTOR = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "SurfacePermanentMagnetRotor"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1300


__docformat__ = "restructuredtext en"
__all__ = ("SurfacePermanentMagnetRotor",)


Self = TypeVar("Self", bound="SurfacePermanentMagnetRotor")


class SurfacePermanentMagnetRotor(_1297.PermanentMagnetRotor):
    """SurfacePermanentMagnetRotor

    This is a mastapy class.
    """

    TYPE = _SURFACE_PERMANENT_MAGNET_ROTOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SurfacePermanentMagnetRotor")

    class _Cast_SurfacePermanentMagnetRotor:
        """Special nested class for casting SurfacePermanentMagnetRotor to subclasses."""

        def __init__(
            self: "SurfacePermanentMagnetRotor._Cast_SurfacePermanentMagnetRotor",
            parent: "SurfacePermanentMagnetRotor",
        ):
            self._parent = parent

        @property
        def permanent_magnet_rotor(
            self: "SurfacePermanentMagnetRotor._Cast_SurfacePermanentMagnetRotor",
        ) -> "_1297.PermanentMagnetRotor":
            return self._parent._cast(_1297.PermanentMagnetRotor)

        @property
        def rotor(
            self: "SurfacePermanentMagnetRotor._Cast_SurfacePermanentMagnetRotor",
        ) -> "_1300.Rotor":
            from mastapy.electric_machines import _1300

            return self._parent._cast(_1300.Rotor)

        @property
        def surface_permanent_magnet_rotor(
            self: "SurfacePermanentMagnetRotor._Cast_SurfacePermanentMagnetRotor",
        ) -> "SurfacePermanentMagnetRotor":
            return self._parent

        def __getattr__(
            self: "SurfacePermanentMagnetRotor._Cast_SurfacePermanentMagnetRotor",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SurfacePermanentMagnetRotor.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "SurfacePermanentMagnetRotor._Cast_SurfacePermanentMagnetRotor":
        return self._Cast_SurfacePermanentMagnetRotor(self)
