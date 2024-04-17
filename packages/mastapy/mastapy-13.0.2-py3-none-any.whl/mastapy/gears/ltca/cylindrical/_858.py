"""CylindricalGearFESettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility import _1601
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FE_SETTINGS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA.Cylindrical", "CylindricalGearFESettings"
)

if TYPE_CHECKING:
    from mastapy.utility import _1602


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearFESettings",)


Self = TypeVar("Self", bound="CylindricalGearFESettings")


class CylindricalGearFESettings(_1601.PerMachineSettings):
    """CylindricalGearFESettings

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_FE_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearFESettings")

    class _Cast_CylindricalGearFESettings:
        """Special nested class for casting CylindricalGearFESettings to subclasses."""

        def __init__(
            self: "CylindricalGearFESettings._Cast_CylindricalGearFESettings",
            parent: "CylindricalGearFESettings",
        ):
            self._parent = parent

        @property
        def per_machine_settings(
            self: "CylindricalGearFESettings._Cast_CylindricalGearFESettings",
        ) -> "_1601.PerMachineSettings":
            return self._parent._cast(_1601.PerMachineSettings)

        @property
        def persistent_singleton(
            self: "CylindricalGearFESettings._Cast_CylindricalGearFESettings",
        ) -> "_1602.PersistentSingleton":
            from mastapy.utility import _1602

            return self._parent._cast(_1602.PersistentSingleton)

        @property
        def cylindrical_gear_fe_settings(
            self: "CylindricalGearFESettings._Cast_CylindricalGearFESettings",
        ) -> "CylindricalGearFESettings":
            return self._parent

        def __getattr__(
            self: "CylindricalGearFESettings._Cast_CylindricalGearFESettings", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearFESettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearFESettings._Cast_CylindricalGearFESettings":
        return self._Cast_CylindricalGearFESettings(self)
