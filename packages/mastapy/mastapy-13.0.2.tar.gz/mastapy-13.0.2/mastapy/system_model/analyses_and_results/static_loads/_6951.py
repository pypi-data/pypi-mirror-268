"""RingPinManufacturingError"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PIN_MANUFACTURING_ERROR = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "RingPinManufacturingError",
)

if TYPE_CHECKING:
    from mastapy.bearings.tolerances import _1925


__docformat__ = "restructuredtext en"
__all__ = ("RingPinManufacturingError",)


Self = TypeVar("Self", bound="RingPinManufacturingError")


class RingPinManufacturingError(_0.APIBase):
    """RingPinManufacturingError

    This is a mastapy class.
    """

    TYPE = _RING_PIN_MANUFACTURING_ERROR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinManufacturingError")

    class _Cast_RingPinManufacturingError:
        """Special nested class for casting RingPinManufacturingError to subclasses."""

        def __init__(
            self: "RingPinManufacturingError._Cast_RingPinManufacturingError",
            parent: "RingPinManufacturingError",
        ):
            self._parent = parent

        @property
        def ring_pin_manufacturing_error(
            self: "RingPinManufacturingError._Cast_RingPinManufacturingError",
        ) -> "RingPinManufacturingError":
            return self._parent

        def __getattr__(
            self: "RingPinManufacturingError._Cast_RingPinManufacturingError", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingPinManufacturingError.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def override_all_pins_roundness_specification(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OverrideAllPinsRoundnessSpecification

        if temp is None:
            return False

        return temp

    @override_all_pins_roundness_specification.setter
    @enforce_parameter_types
    def override_all_pins_roundness_specification(self: Self, value: "bool"):
        self.wrapped.OverrideAllPinsRoundnessSpecification = (
            bool(value) if value is not None else False
        )

    @property
    def pin_angular_position_error(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PinAngularPositionError

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @pin_angular_position_error.setter
    @enforce_parameter_types
    def pin_angular_position_error(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PinAngularPositionError = value

    @property
    def pin_diameter_error(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PinDiameterError

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @pin_diameter_error.setter
    @enforce_parameter_types
    def pin_diameter_error(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PinDiameterError = value

    @property
    def pin_radial_position_error(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PinRadialPositionError

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @pin_radial_position_error.setter
    @enforce_parameter_types
    def pin_radial_position_error(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PinRadialPositionError = value

    @property
    def pin_roundness_chart(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinRoundnessChart

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def show_pin_roundness_chart(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowPinRoundnessChart

        if temp is None:
            return False

        return temp

    @show_pin_roundness_chart.setter
    @enforce_parameter_types
    def show_pin_roundness_chart(self: Self, value: "bool"):
        self.wrapped.ShowPinRoundnessChart = bool(value) if value is not None else False

    @property
    def roundness_specification(self: Self) -> "_1925.RoundnessSpecification":
        """mastapy.bearings.tolerances.RoundnessSpecification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoundnessSpecification

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RingPinManufacturingError._Cast_RingPinManufacturingError":
        return self._Cast_RingPinManufacturingError(self)
