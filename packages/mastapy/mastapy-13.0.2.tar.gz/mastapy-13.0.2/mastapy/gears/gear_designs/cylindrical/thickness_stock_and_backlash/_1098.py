"""NoValueSpecification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.cylindrical import _1089
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NO_VALUE_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.ThicknessStockAndBacklash",
    "NoValueSpecification",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1072


__docformat__ = "restructuredtext en"
__all__ = ("NoValueSpecification",)


Self = TypeVar("Self", bound="NoValueSpecification")
T = TypeVar("T")


class NoValueSpecification(_1089.TolerancedValueSpecification[T]):
    """NoValueSpecification

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _NO_VALUE_SPECIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NoValueSpecification")

    class _Cast_NoValueSpecification:
        """Special nested class for casting NoValueSpecification to subclasses."""

        def __init__(
            self: "NoValueSpecification._Cast_NoValueSpecification",
            parent: "NoValueSpecification",
        ):
            self._parent = parent

        @property
        def toleranced_value_specification(
            self: "NoValueSpecification._Cast_NoValueSpecification",
        ) -> "_1089.TolerancedValueSpecification":
            return self._parent._cast(_1089.TolerancedValueSpecification)

        @property
        def relative_measurement_view_model(
            self: "NoValueSpecification._Cast_NoValueSpecification",
        ) -> "_1072.RelativeMeasurementViewModel":
            from mastapy.gears.gear_designs.cylindrical import _1072

            return self._parent._cast(_1072.RelativeMeasurementViewModel)

        @property
        def no_value_specification(
            self: "NoValueSpecification._Cast_NoValueSpecification",
        ) -> "NoValueSpecification":
            return self._parent

        def __getattr__(
            self: "NoValueSpecification._Cast_NoValueSpecification", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NoValueSpecification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "NoValueSpecification._Cast_NoValueSpecification":
        return self._Cast_NoValueSpecification(self)
