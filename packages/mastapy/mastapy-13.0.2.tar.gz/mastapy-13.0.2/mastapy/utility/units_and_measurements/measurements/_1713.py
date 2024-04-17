"""QuadraticDrag"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_QUADRATIC_DRAG = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "QuadraticDrag"
)


__docformat__ = "restructuredtext en"
__all__ = ("QuadraticDrag",)


Self = TypeVar("Self", bound="QuadraticDrag")


class QuadraticDrag(_1612.MeasurementBase):
    """QuadraticDrag

    This is a mastapy class.
    """

    TYPE = _QUADRATIC_DRAG
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_QuadraticDrag")

    class _Cast_QuadraticDrag:
        """Special nested class for casting QuadraticDrag to subclasses."""

        def __init__(
            self: "QuadraticDrag._Cast_QuadraticDrag", parent: "QuadraticDrag"
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "QuadraticDrag._Cast_QuadraticDrag",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def quadratic_drag(
            self: "QuadraticDrag._Cast_QuadraticDrag",
        ) -> "QuadraticDrag":
            return self._parent

        def __getattr__(self: "QuadraticDrag._Cast_QuadraticDrag", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "QuadraticDrag.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "QuadraticDrag._Cast_QuadraticDrag":
        return self._Cast_QuadraticDrag(self)
