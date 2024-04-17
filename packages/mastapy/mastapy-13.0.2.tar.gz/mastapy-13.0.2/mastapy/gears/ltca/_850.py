"""GearStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis import _66
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_STIFFNESS = python_net_import("SMT.MastaAPI.Gears.LTCA", "GearStiffness")

if TYPE_CHECKING:
    from mastapy.gears.ltca import _836, _838
    from mastapy.gears.ltca.cylindrical import _854, _856
    from mastapy.gears.ltca.conical import _866, _868


__docformat__ = "restructuredtext en"
__all__ = ("GearStiffness",)


Self = TypeVar("Self", bound="GearStiffness")


class GearStiffness(_66.FEStiffness):
    """GearStiffness

    This is a mastapy class.
    """

    TYPE = _GEAR_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearStiffness")

    class _Cast_GearStiffness:
        """Special nested class for casting GearStiffness to subclasses."""

        def __init__(
            self: "GearStiffness._Cast_GearStiffness", parent: "GearStiffness"
        ):
            self._parent = parent

        @property
        def fe_stiffness(
            self: "GearStiffness._Cast_GearStiffness",
        ) -> "_66.FEStiffness":
            return self._parent._cast(_66.FEStiffness)

        @property
        def gear_bending_stiffness(
            self: "GearStiffness._Cast_GearStiffness",
        ) -> "_836.GearBendingStiffness":
            from mastapy.gears.ltca import _836

            return self._parent._cast(_836.GearBendingStiffness)

        @property
        def gear_contact_stiffness(
            self: "GearStiffness._Cast_GearStiffness",
        ) -> "_838.GearContactStiffness":
            from mastapy.gears.ltca import _838

            return self._parent._cast(_838.GearContactStiffness)

        @property
        def cylindrical_gear_bending_stiffness(
            self: "GearStiffness._Cast_GearStiffness",
        ) -> "_854.CylindricalGearBendingStiffness":
            from mastapy.gears.ltca.cylindrical import _854

            return self._parent._cast(_854.CylindricalGearBendingStiffness)

        @property
        def cylindrical_gear_contact_stiffness(
            self: "GearStiffness._Cast_GearStiffness",
        ) -> "_856.CylindricalGearContactStiffness":
            from mastapy.gears.ltca.cylindrical import _856

            return self._parent._cast(_856.CylindricalGearContactStiffness)

        @property
        def conical_gear_bending_stiffness(
            self: "GearStiffness._Cast_GearStiffness",
        ) -> "_866.ConicalGearBendingStiffness":
            from mastapy.gears.ltca.conical import _866

            return self._parent._cast(_866.ConicalGearBendingStiffness)

        @property
        def conical_gear_contact_stiffness(
            self: "GearStiffness._Cast_GearStiffness",
        ) -> "_868.ConicalGearContactStiffness":
            from mastapy.gears.ltca.conical import _868

            return self._parent._cast(_868.ConicalGearContactStiffness)

        @property
        def gear_stiffness(
            self: "GearStiffness._Cast_GearStiffness",
        ) -> "GearStiffness":
            return self._parent

        def __getattr__(self: "GearStiffness._Cast_GearStiffness", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearStiffness.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GearStiffness._Cast_GearStiffness":
        return self._Cast_GearStiffness(self)
