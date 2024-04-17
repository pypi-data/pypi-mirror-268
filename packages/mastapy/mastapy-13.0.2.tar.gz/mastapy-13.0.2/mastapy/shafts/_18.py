"""ShaftAxialTorsionalComponentValues"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_AXIAL_TORSIONAL_COMPONENT_VALUES = python_net_import(
    "SMT.MastaAPI.Shafts", "ShaftAxialTorsionalComponentValues"
)

if TYPE_CHECKING:
    from mastapy.shafts import _16, _17


__docformat__ = "restructuredtext en"
__all__ = ("ShaftAxialTorsionalComponentValues",)


Self = TypeVar("Self", bound="ShaftAxialTorsionalComponentValues")


class ShaftAxialTorsionalComponentValues(_0.APIBase):
    """ShaftAxialTorsionalComponentValues

    This is a mastapy class.
    """

    TYPE = _SHAFT_AXIAL_TORSIONAL_COMPONENT_VALUES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftAxialTorsionalComponentValues")

    class _Cast_ShaftAxialTorsionalComponentValues:
        """Special nested class for casting ShaftAxialTorsionalComponentValues to subclasses."""

        def __init__(
            self: "ShaftAxialTorsionalComponentValues._Cast_ShaftAxialTorsionalComponentValues",
            parent: "ShaftAxialTorsionalComponentValues",
        ):
            self._parent = parent

        @property
        def shaft_axial_bending_torsional_component_values(
            self: "ShaftAxialTorsionalComponentValues._Cast_ShaftAxialTorsionalComponentValues",
        ) -> "_16.ShaftAxialBendingTorsionalComponentValues":
            from mastapy.shafts import _16

            return self._parent._cast(_16.ShaftAxialBendingTorsionalComponentValues)

        @property
        def shaft_axial_bending_x_bending_y_torsional_component_values(
            self: "ShaftAxialTorsionalComponentValues._Cast_ShaftAxialTorsionalComponentValues",
        ) -> "_17.ShaftAxialBendingXBendingYTorsionalComponentValues":
            from mastapy.shafts import _17

            return self._parent._cast(
                _17.ShaftAxialBendingXBendingYTorsionalComponentValues
            )

        @property
        def shaft_axial_torsional_component_values(
            self: "ShaftAxialTorsionalComponentValues._Cast_ShaftAxialTorsionalComponentValues",
        ) -> "ShaftAxialTorsionalComponentValues":
            return self._parent

        def __getattr__(
            self: "ShaftAxialTorsionalComponentValues._Cast_ShaftAxialTorsionalComponentValues",
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
        self: Self, instance_to_wrap: "ShaftAxialTorsionalComponentValues.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Axial

        if temp is None:
            return 0.0

        return temp

    @property
    def torsional(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Torsional

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftAxialTorsionalComponentValues._Cast_ShaftAxialTorsionalComponentValues":
        return self._Cast_ShaftAxialTorsionalComponentValues(self)
