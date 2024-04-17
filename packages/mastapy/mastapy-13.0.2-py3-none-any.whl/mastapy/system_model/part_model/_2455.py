"""Datum"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.part_model import _2451
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATUM = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Datum")

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("Datum",)


Self = TypeVar("Self", bound="Datum")


class Datum(_2451.Component):
    """Datum

    This is a mastapy class.
    """

    TYPE = _DATUM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Datum")

    class _Cast_Datum:
        """Special nested class for casting Datum to subclasses."""

        def __init__(self: "Datum._Cast_Datum", parent: "Datum"):
            self._parent = parent

        @property
        def component(self: "Datum._Cast_Datum") -> "_2451.Component":
            return self._parent._cast(_2451.Component)

        @property
        def part(self: "Datum._Cast_Datum") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(self: "Datum._Cast_Datum") -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def datum(self: "Datum._Cast_Datum") -> "Datum":
            return self._parent

        def __getattr__(self: "Datum._Cast_Datum", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Datum.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def drawing_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DrawingDiameter

        if temp is None:
            return 0.0

        return temp

    @drawing_diameter.setter
    @enforce_parameter_types
    def drawing_diameter(self: Self, value: "float"):
        self.wrapped.DrawingDiameter = float(value) if value is not None else 0.0

    @property
    def offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Offset

        if temp is None:
            return 0.0

        return temp

    @offset.setter
    @enforce_parameter_types
    def offset(self: Self, value: "float"):
        self.wrapped.Offset = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "Datum._Cast_Datum":
        return self._Cast_Datum(self)
