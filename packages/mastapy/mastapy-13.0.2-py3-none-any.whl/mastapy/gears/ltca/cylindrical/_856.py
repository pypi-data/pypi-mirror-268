"""CylindricalGearContactStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.ltca import _838
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_CONTACT_STIFFNESS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA.Cylindrical", "CylindricalGearContactStiffness"
)

if TYPE_CHECKING:
    from mastapy.gears.ltca import _850
    from mastapy.nodal_analysis import _66


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearContactStiffness",)


Self = TypeVar("Self", bound="CylindricalGearContactStiffness")


class CylindricalGearContactStiffness(_838.GearContactStiffness):
    """CylindricalGearContactStiffness

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_CONTACT_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearContactStiffness")

    class _Cast_CylindricalGearContactStiffness:
        """Special nested class for casting CylindricalGearContactStiffness to subclasses."""

        def __init__(
            self: "CylindricalGearContactStiffness._Cast_CylindricalGearContactStiffness",
            parent: "CylindricalGearContactStiffness",
        ):
            self._parent = parent

        @property
        def gear_contact_stiffness(
            self: "CylindricalGearContactStiffness._Cast_CylindricalGearContactStiffness",
        ) -> "_838.GearContactStiffness":
            return self._parent._cast(_838.GearContactStiffness)

        @property
        def gear_stiffness(
            self: "CylindricalGearContactStiffness._Cast_CylindricalGearContactStiffness",
        ) -> "_850.GearStiffness":
            from mastapy.gears.ltca import _850

            return self._parent._cast(_850.GearStiffness)

        @property
        def fe_stiffness(
            self: "CylindricalGearContactStiffness._Cast_CylindricalGearContactStiffness",
        ) -> "_66.FEStiffness":
            from mastapy.nodal_analysis import _66

            return self._parent._cast(_66.FEStiffness)

        @property
        def cylindrical_gear_contact_stiffness(
            self: "CylindricalGearContactStiffness._Cast_CylindricalGearContactStiffness",
        ) -> "CylindricalGearContactStiffness":
            return self._parent

        def __getattr__(
            self: "CylindricalGearContactStiffness._Cast_CylindricalGearContactStiffness",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearContactStiffness.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearContactStiffness._Cast_CylindricalGearContactStiffness":
        return self._Cast_CylindricalGearContactStiffness(self)
