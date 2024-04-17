"""ShaftAxialBendingXBendingYTorsionalComponentValues"""

from __future__ import annotations

from typing import TypeVar

from mastapy.shafts import _18
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_AXIAL_BENDING_X_BENDING_Y_TORSIONAL_COMPONENT_VALUES = python_net_import(
    "SMT.MastaAPI.Shafts", "ShaftAxialBendingXBendingYTorsionalComponentValues"
)


__docformat__ = "restructuredtext en"
__all__ = ("ShaftAxialBendingXBendingYTorsionalComponentValues",)


Self = TypeVar("Self", bound="ShaftAxialBendingXBendingYTorsionalComponentValues")


class ShaftAxialBendingXBendingYTorsionalComponentValues(
    _18.ShaftAxialTorsionalComponentValues
):
    """ShaftAxialBendingXBendingYTorsionalComponentValues

    This is a mastapy class.
    """

    TYPE = _SHAFT_AXIAL_BENDING_X_BENDING_Y_TORSIONAL_COMPONENT_VALUES
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftAxialBendingXBendingYTorsionalComponentValues"
    )

    class _Cast_ShaftAxialBendingXBendingYTorsionalComponentValues:
        """Special nested class for casting ShaftAxialBendingXBendingYTorsionalComponentValues to subclasses."""

        def __init__(
            self: "ShaftAxialBendingXBendingYTorsionalComponentValues._Cast_ShaftAxialBendingXBendingYTorsionalComponentValues",
            parent: "ShaftAxialBendingXBendingYTorsionalComponentValues",
        ):
            self._parent = parent

        @property
        def shaft_axial_torsional_component_values(
            self: "ShaftAxialBendingXBendingYTorsionalComponentValues._Cast_ShaftAxialBendingXBendingYTorsionalComponentValues",
        ) -> "_18.ShaftAxialTorsionalComponentValues":
            return self._parent._cast(_18.ShaftAxialTorsionalComponentValues)

        @property
        def shaft_axial_bending_x_bending_y_torsional_component_values(
            self: "ShaftAxialBendingXBendingYTorsionalComponentValues._Cast_ShaftAxialBendingXBendingYTorsionalComponentValues",
        ) -> "ShaftAxialBendingXBendingYTorsionalComponentValues":
            return self._parent

        def __getattr__(
            self: "ShaftAxialBendingXBendingYTorsionalComponentValues._Cast_ShaftAxialBendingXBendingYTorsionalComponentValues",
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
        instance_to_wrap: "ShaftAxialBendingXBendingYTorsionalComponentValues.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending_x(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingX

        if temp is None:
            return 0.0

        return temp

    @property
    def bending_y(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingY

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftAxialBendingXBendingYTorsionalComponentValues._Cast_ShaftAxialBendingXBendingYTorsionalComponentValues":
        return self._Cast_ShaftAxialBendingXBendingYTorsionalComponentValues(self)
