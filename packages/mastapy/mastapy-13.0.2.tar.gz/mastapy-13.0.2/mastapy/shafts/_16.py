"""ShaftAxialBendingTorsionalComponentValues"""

from __future__ import annotations

from typing import TypeVar

from mastapy.shafts import _18
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_AXIAL_BENDING_TORSIONAL_COMPONENT_VALUES = python_net_import(
    "SMT.MastaAPI.Shafts", "ShaftAxialBendingTorsionalComponentValues"
)


__docformat__ = "restructuredtext en"
__all__ = ("ShaftAxialBendingTorsionalComponentValues",)


Self = TypeVar("Self", bound="ShaftAxialBendingTorsionalComponentValues")


class ShaftAxialBendingTorsionalComponentValues(_18.ShaftAxialTorsionalComponentValues):
    """ShaftAxialBendingTorsionalComponentValues

    This is a mastapy class.
    """

    TYPE = _SHAFT_AXIAL_BENDING_TORSIONAL_COMPONENT_VALUES
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftAxialBendingTorsionalComponentValues"
    )

    class _Cast_ShaftAxialBendingTorsionalComponentValues:
        """Special nested class for casting ShaftAxialBendingTorsionalComponentValues to subclasses."""

        def __init__(
            self: "ShaftAxialBendingTorsionalComponentValues._Cast_ShaftAxialBendingTorsionalComponentValues",
            parent: "ShaftAxialBendingTorsionalComponentValues",
        ):
            self._parent = parent

        @property
        def shaft_axial_torsional_component_values(
            self: "ShaftAxialBendingTorsionalComponentValues._Cast_ShaftAxialBendingTorsionalComponentValues",
        ) -> "_18.ShaftAxialTorsionalComponentValues":
            return self._parent._cast(_18.ShaftAxialTorsionalComponentValues)

        @property
        def shaft_axial_bending_torsional_component_values(
            self: "ShaftAxialBendingTorsionalComponentValues._Cast_ShaftAxialBendingTorsionalComponentValues",
        ) -> "ShaftAxialBendingTorsionalComponentValues":
            return self._parent

        def __getattr__(
            self: "ShaftAxialBendingTorsionalComponentValues._Cast_ShaftAxialBendingTorsionalComponentValues",
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
        self: Self, instance_to_wrap: "ShaftAxialBendingTorsionalComponentValues.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Bending

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftAxialBendingTorsionalComponentValues._Cast_ShaftAxialBendingTorsionalComponentValues":
        return self._Cast_ShaftAxialBendingTorsionalComponentValues(self)
