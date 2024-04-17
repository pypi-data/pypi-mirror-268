"""DataScalingReferenceValues"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, Generic

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.math_utility.measured_data_scaling import _1578
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATA_SCALING_REFERENCE_VALUES = python_net_import(
    "SMT.MastaAPI.MathUtility.MeasuredDataScaling", "DataScalingReferenceValues"
)

if TYPE_CHECKING:
    from mastapy.utility.units_and_measurements import _1612


__docformat__ = "restructuredtext en"
__all__ = ("DataScalingReferenceValues",)


Self = TypeVar("Self", bound="DataScalingReferenceValues")
TMeasurement = TypeVar("TMeasurement", bound="_1612.MeasurementBase")


class DataScalingReferenceValues(
    _1578.DataScalingReferenceValuesBase, Generic[TMeasurement]
):
    """DataScalingReferenceValues

    This is a mastapy class.

    Generic Types:
        TMeasurement
    """

    TYPE = _DATA_SCALING_REFERENCE_VALUES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DataScalingReferenceValues")

    class _Cast_DataScalingReferenceValues:
        """Special nested class for casting DataScalingReferenceValues to subclasses."""

        def __init__(
            self: "DataScalingReferenceValues._Cast_DataScalingReferenceValues",
            parent: "DataScalingReferenceValues",
        ):
            self._parent = parent

        @property
        def data_scaling_reference_values_base(
            self: "DataScalingReferenceValues._Cast_DataScalingReferenceValues",
        ) -> "_1578.DataScalingReferenceValuesBase":
            return self._parent._cast(_1578.DataScalingReferenceValuesBase)

        @property
        def data_scaling_reference_values(
            self: "DataScalingReferenceValues._Cast_DataScalingReferenceValues",
        ) -> "DataScalingReferenceValues":
            return self._parent

        def __getattr__(
            self: "DataScalingReferenceValues._Cast_DataScalingReferenceValues",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DataScalingReferenceValues.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def decibel_reference(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DecibelReference

        if temp is None:
            return 0.0

        return temp

    @decibel_reference.setter
    @enforce_parameter_types
    def decibel_reference(self: Self, value: "float"):
        self.wrapped.DecibelReference = float(value) if value is not None else 0.0

    @property
    def maximum(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Maximum

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum.setter
    @enforce_parameter_types
    def maximum(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Maximum = value

    @property
    def minimum(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Minimum

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum.setter
    @enforce_parameter_types
    def minimum(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Minimum = value

    @property
    def cast_to(
        self: Self,
    ) -> "DataScalingReferenceValues._Cast_DataScalingReferenceValues":
        return self._Cast_DataScalingReferenceValues(self)
