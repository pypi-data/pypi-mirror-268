"""MultiTimeSeriesDataInputFileOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.utility_gui import _1855
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MULTI_TIME_SERIES_DATA_INPUT_FILE_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition",
    "MultiTimeSeriesDataInputFileOptions",
)

if TYPE_CHECKING:
    from mastapy.utility.file_access_helpers import _1825


__docformat__ = "restructuredtext en"
__all__ = ("MultiTimeSeriesDataInputFileOptions",)


Self = TypeVar("Self", bound="MultiTimeSeriesDataInputFileOptions")


class MultiTimeSeriesDataInputFileOptions(_1855.DataInputFileOptions):
    """MultiTimeSeriesDataInputFileOptions

    This is a mastapy class.
    """

    TYPE = _MULTI_TIME_SERIES_DATA_INPUT_FILE_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MultiTimeSeriesDataInputFileOptions")

    class _Cast_MultiTimeSeriesDataInputFileOptions:
        """Special nested class for casting MultiTimeSeriesDataInputFileOptions to subclasses."""

        def __init__(
            self: "MultiTimeSeriesDataInputFileOptions._Cast_MultiTimeSeriesDataInputFileOptions",
            parent: "MultiTimeSeriesDataInputFileOptions",
        ):
            self._parent = parent

        @property
        def data_input_file_options(
            self: "MultiTimeSeriesDataInputFileOptions._Cast_MultiTimeSeriesDataInputFileOptions",
        ) -> "_1855.DataInputFileOptions":
            return self._parent._cast(_1855.DataInputFileOptions)

        @property
        def multi_time_series_data_input_file_options(
            self: "MultiTimeSeriesDataInputFileOptions._Cast_MultiTimeSeriesDataInputFileOptions",
        ) -> "MultiTimeSeriesDataInputFileOptions":
            return self._parent

        def __getattr__(
            self: "MultiTimeSeriesDataInputFileOptions._Cast_MultiTimeSeriesDataInputFileOptions",
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
        self: Self, instance_to_wrap: "MultiTimeSeriesDataInputFileOptions.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duration(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Duration

        if temp is None:
            return 0.0

        return temp

    @property
    def duration_scaling(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DurationScaling

        if temp is None:
            return 0.0

        return temp

    @duration_scaling.setter
    @enforce_parameter_types
    def duration_scaling(self: Self, value: "float"):
        self.wrapped.DurationScaling = float(value) if value is not None else 0.0

    @property
    def proportion_of_duty_cycle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProportionOfDutyCycle

        if temp is None:
            return 0.0

        return temp

    @proportion_of_duty_cycle.setter
    @enforce_parameter_types
    def proportion_of_duty_cycle(self: Self, value: "float"):
        self.wrapped.ProportionOfDutyCycle = float(value) if value is not None else 0.0

    @property
    def delimiter_options(self: Self) -> "_1825.TextFileDelimiterOptions":
        """mastapy.utility.file_access_helpers.TextFileDelimiterOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DelimiterOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "MultiTimeSeriesDataInputFileOptions._Cast_MultiTimeSeriesDataInputFileOptions"
    ):
        return self._Cast_MultiTimeSeriesDataInputFileOptions(self)
