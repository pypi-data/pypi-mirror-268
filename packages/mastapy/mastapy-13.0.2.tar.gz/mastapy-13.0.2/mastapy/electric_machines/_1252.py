"""CADConductor"""

from __future__ import annotations

from typing import TypeVar

from mastapy.electric_machines import _1319
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CAD_CONDUCTOR = python_net_import("SMT.MastaAPI.ElectricMachines", "CADConductor")


__docformat__ = "restructuredtext en"
__all__ = ("CADConductor",)


Self = TypeVar("Self", bound="CADConductor")


class CADConductor(_1319.WindingConductor):
    """CADConductor

    This is a mastapy class.
    """

    TYPE = _CAD_CONDUCTOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CADConductor")

    class _Cast_CADConductor:
        """Special nested class for casting CADConductor to subclasses."""

        def __init__(self: "CADConductor._Cast_CADConductor", parent: "CADConductor"):
            self._parent = parent

        @property
        def winding_conductor(
            self: "CADConductor._Cast_CADConductor",
        ) -> "_1319.WindingConductor":
            return self._parent._cast(_1319.WindingConductor)

        @property
        def cad_conductor(self: "CADConductor._Cast_CADConductor") -> "CADConductor":
            return self._parent

        def __getattr__(self: "CADConductor._Cast_CADConductor", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CADConductor.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CADConductor._Cast_CADConductor":
        return self._Cast_CADConductor(self)
