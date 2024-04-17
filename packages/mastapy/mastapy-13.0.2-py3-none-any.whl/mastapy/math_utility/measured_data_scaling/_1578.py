"""DataScalingReferenceValuesBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATA_SCALING_REFERENCE_VALUES_BASE = python_net_import(
    "SMT.MastaAPI.MathUtility.MeasuredDataScaling", "DataScalingReferenceValuesBase"
)

if TYPE_CHECKING:
    from mastapy.math_utility.measured_data_scaling import _1577


__docformat__ = "restructuredtext en"
__all__ = ("DataScalingReferenceValuesBase",)


Self = TypeVar("Self", bound="DataScalingReferenceValuesBase")


class DataScalingReferenceValuesBase(_0.APIBase):
    """DataScalingReferenceValuesBase

    This is a mastapy class.
    """

    TYPE = _DATA_SCALING_REFERENCE_VALUES_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DataScalingReferenceValuesBase")

    class _Cast_DataScalingReferenceValuesBase:
        """Special nested class for casting DataScalingReferenceValuesBase to subclasses."""

        def __init__(
            self: "DataScalingReferenceValuesBase._Cast_DataScalingReferenceValuesBase",
            parent: "DataScalingReferenceValuesBase",
        ):
            self._parent = parent

        @property
        def data_scaling_reference_values(
            self: "DataScalingReferenceValuesBase._Cast_DataScalingReferenceValuesBase",
        ) -> "_1577.DataScalingReferenceValues":
            from mastapy.math_utility.measured_data_scaling import _1577

            return self._parent._cast(_1577.DataScalingReferenceValues)

        @property
        def data_scaling_reference_values_base(
            self: "DataScalingReferenceValuesBase._Cast_DataScalingReferenceValuesBase",
        ) -> "DataScalingReferenceValuesBase":
            return self._parent

        def __getattr__(
            self: "DataScalingReferenceValuesBase._Cast_DataScalingReferenceValuesBase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DataScalingReferenceValuesBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_db(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumDB

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_db.setter
    @enforce_parameter_types
    def maximum_db(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumDB = value

    @property
    def minimum_db(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumDB

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_db.setter
    @enforce_parameter_types
    def minimum_db(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumDB = value

    @property
    def cast_to(
        self: Self,
    ) -> "DataScalingReferenceValuesBase._Cast_DataScalingReferenceValuesBase":
        return self._Cast_DataScalingReferenceValuesBase(self)
