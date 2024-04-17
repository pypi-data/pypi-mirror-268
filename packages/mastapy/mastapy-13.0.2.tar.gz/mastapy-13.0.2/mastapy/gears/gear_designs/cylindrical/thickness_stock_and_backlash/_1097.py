"""NominalValueSpecification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical import _1089
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NOMINAL_VALUE_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.ThicknessStockAndBacklash",
    "NominalValueSpecification",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1072


__docformat__ = "restructuredtext en"
__all__ = ("NominalValueSpecification",)


Self = TypeVar("Self", bound="NominalValueSpecification")
T = TypeVar("T")


class NominalValueSpecification(_1089.TolerancedValueSpecification[T]):
    """NominalValueSpecification

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _NOMINAL_VALUE_SPECIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NominalValueSpecification")

    class _Cast_NominalValueSpecification:
        """Special nested class for casting NominalValueSpecification to subclasses."""

        def __init__(
            self: "NominalValueSpecification._Cast_NominalValueSpecification",
            parent: "NominalValueSpecification",
        ):
            self._parent = parent

        @property
        def toleranced_value_specification(
            self: "NominalValueSpecification._Cast_NominalValueSpecification",
        ) -> "_1089.TolerancedValueSpecification":
            return self._parent._cast(_1089.TolerancedValueSpecification)

        @property
        def relative_measurement_view_model(
            self: "NominalValueSpecification._Cast_NominalValueSpecification",
        ) -> "_1072.RelativeMeasurementViewModel":
            from mastapy.gears.gear_designs.cylindrical import _1072

            return self._parent._cast(_1072.RelativeMeasurementViewModel)

        @property
        def nominal_value_specification(
            self: "NominalValueSpecification._Cast_NominalValueSpecification",
        ) -> "NominalValueSpecification":
            return self._parent

        def __getattr__(
            self: "NominalValueSpecification._Cast_NominalValueSpecification", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NominalValueSpecification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Design

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @design.setter
    @enforce_parameter_types
    def design(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Design = value

    @property
    def cast_to(
        self: Self,
    ) -> "NominalValueSpecification._Cast_NominalValueSpecification":
        return self._Cast_NominalValueSpecification(self)
