"""RelativeValuesSpecification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RELATIVE_VALUES_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "RelativeValuesSpecification"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1003
    from mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash import (
        _1095,
    )


__docformat__ = "restructuredtext en"
__all__ = ("RelativeValuesSpecification",)


Self = TypeVar("Self", bound="RelativeValuesSpecification")
T = TypeVar("T", bound="RelativeValuesSpecification")


class RelativeValuesSpecification(_0.APIBase, Generic[T]):
    """RelativeValuesSpecification

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _RELATIVE_VALUES_SPECIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RelativeValuesSpecification")

    class _Cast_RelativeValuesSpecification:
        """Special nested class for casting RelativeValuesSpecification to subclasses."""

        def __init__(
            self: "RelativeValuesSpecification._Cast_RelativeValuesSpecification",
            parent: "RelativeValuesSpecification",
        ):
            self._parent = parent

        @property
        def backlash_specification(
            self: "RelativeValuesSpecification._Cast_RelativeValuesSpecification",
        ) -> "_1003.BacklashSpecification":
            from mastapy.gears.gear_designs.cylindrical import _1003

            return self._parent._cast(_1003.BacklashSpecification)

        @property
        def finish_stock_specification(
            self: "RelativeValuesSpecification._Cast_RelativeValuesSpecification",
        ) -> "_1095.FinishStockSpecification":
            from mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash import (
                _1095,
            )

            return self._parent._cast(_1095.FinishStockSpecification)

        @property
        def relative_values_specification(
            self: "RelativeValuesSpecification._Cast_RelativeValuesSpecification",
        ) -> "RelativeValuesSpecification":
            return self._parent

        def __getattr__(
            self: "RelativeValuesSpecification._Cast_RelativeValuesSpecification",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RelativeValuesSpecification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "RelativeValuesSpecification._Cast_RelativeValuesSpecification":
        return self._Cast_RelativeValuesSpecification(self)
