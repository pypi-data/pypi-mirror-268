"""GearContactStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.ltca import _850
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_CONTACT_STIFFNESS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "GearContactStiffness"
)

if TYPE_CHECKING:
    from mastapy.gears.ltca.cylindrical import _856
    from mastapy.gears.ltca.conical import _868
    from mastapy.nodal_analysis import _66


__docformat__ = "restructuredtext en"
__all__ = ("GearContactStiffness",)


Self = TypeVar("Self", bound="GearContactStiffness")


class GearContactStiffness(_850.GearStiffness):
    """GearContactStiffness

    This is a mastapy class.
    """

    TYPE = _GEAR_CONTACT_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearContactStiffness")

    class _Cast_GearContactStiffness:
        """Special nested class for casting GearContactStiffness to subclasses."""

        def __init__(
            self: "GearContactStiffness._Cast_GearContactStiffness",
            parent: "GearContactStiffness",
        ):
            self._parent = parent

        @property
        def gear_stiffness(
            self: "GearContactStiffness._Cast_GearContactStiffness",
        ) -> "_850.GearStiffness":
            return self._parent._cast(_850.GearStiffness)

        @property
        def fe_stiffness(
            self: "GearContactStiffness._Cast_GearContactStiffness",
        ) -> "_66.FEStiffness":
            from mastapy.nodal_analysis import _66

            return self._parent._cast(_66.FEStiffness)

        @property
        def cylindrical_gear_contact_stiffness(
            self: "GearContactStiffness._Cast_GearContactStiffness",
        ) -> "_856.CylindricalGearContactStiffness":
            from mastapy.gears.ltca.cylindrical import _856

            return self._parent._cast(_856.CylindricalGearContactStiffness)

        @property
        def conical_gear_contact_stiffness(
            self: "GearContactStiffness._Cast_GearContactStiffness",
        ) -> "_868.ConicalGearContactStiffness":
            from mastapy.gears.ltca.conical import _868

            return self._parent._cast(_868.ConicalGearContactStiffness)

        @property
        def gear_contact_stiffness(
            self: "GearContactStiffness._Cast_GearContactStiffness",
        ) -> "GearContactStiffness":
            return self._parent

        def __getattr__(
            self: "GearContactStiffness._Cast_GearContactStiffness", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearContactStiffness.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GearContactStiffness._Cast_GearContactStiffness":
        return self._Cast_GearContactStiffness(self)
