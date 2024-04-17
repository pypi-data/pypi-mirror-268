"""TimeStepInputOptions"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.utility_gui import _1854
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TIME_STEP_INPUT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition",
    "TimeStepInputOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("TimeStepInputOptions",)


Self = TypeVar("Self", bound="TimeStepInputOptions")


class TimeStepInputOptions(_1854.ColumnInputOptions):
    """TimeStepInputOptions

    This is a mastapy class.
    """

    TYPE = _TIME_STEP_INPUT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TimeStepInputOptions")

    class _Cast_TimeStepInputOptions:
        """Special nested class for casting TimeStepInputOptions to subclasses."""

        def __init__(
            self: "TimeStepInputOptions._Cast_TimeStepInputOptions",
            parent: "TimeStepInputOptions",
        ):
            self._parent = parent

        @property
        def column_input_options(
            self: "TimeStepInputOptions._Cast_TimeStepInputOptions",
        ) -> "_1854.ColumnInputOptions":
            return self._parent._cast(_1854.ColumnInputOptions)

        @property
        def time_step_input_options(
            self: "TimeStepInputOptions._Cast_TimeStepInputOptions",
        ) -> "TimeStepInputOptions":
            return self._parent

        def __getattr__(
            self: "TimeStepInputOptions._Cast_TimeStepInputOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TimeStepInputOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def time_increment(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TimeIncrement

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @time_increment.setter
    @enforce_parameter_types
    def time_increment(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TimeIncrement = value

    @property
    def cast_to(self: Self) -> "TimeStepInputOptions._Cast_TimeStepInputOptions":
        return self._Cast_TimeStepInputOptions(self)
