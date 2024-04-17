"""TorqueInputOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
    _7007,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_INPUT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition",
    "TorqueInputOptions",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
        _7013,
    )
    from mastapy.utility_gui import _1854


__docformat__ = "restructuredtext en"
__all__ = ("TorqueInputOptions",)


Self = TypeVar("Self", bound="TorqueInputOptions")


class TorqueInputOptions(_7007.PowerLoadInputOptions):
    """TorqueInputOptions

    This is a mastapy class.
    """

    TYPE = _TORQUE_INPUT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueInputOptions")

    class _Cast_TorqueInputOptions:
        """Special nested class for casting TorqueInputOptions to subclasses."""

        def __init__(
            self: "TorqueInputOptions._Cast_TorqueInputOptions",
            parent: "TorqueInputOptions",
        ):
            self._parent = parent

        @property
        def power_load_input_options(
            self: "TorqueInputOptions._Cast_TorqueInputOptions",
        ) -> "_7007.PowerLoadInputOptions":
            return self._parent._cast(_7007.PowerLoadInputOptions)

        @property
        def column_input_options(
            self: "TorqueInputOptions._Cast_TorqueInputOptions",
        ) -> "_1854.ColumnInputOptions":
            from mastapy.utility_gui import _1854

            return self._parent._cast(_1854.ColumnInputOptions)

        @property
        def torque_input_options(
            self: "TorqueInputOptions._Cast_TorqueInputOptions",
        ) -> "TorqueInputOptions":
            return self._parent

        def __getattr__(self: "TorqueInputOptions._Cast_TorqueInputOptions", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueInputOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bin_start(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BinStart

        if temp is None:
            return 0.0

        return temp

    @bin_start.setter
    @enforce_parameter_types
    def bin_start(self: Self, value: "float"):
        self.wrapped.BinStart = float(value) if value is not None else 0.0

    @property
    def bin_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BinWidth

        if temp is None:
            return 0.0

        return temp

    @bin_width.setter
    @enforce_parameter_types
    def bin_width(self: Self, value: "float"):
        self.wrapped.BinWidth = float(value) if value is not None else 0.0

    @property
    def conversion_to_load_case(self: Self) -> "_7013.TorqueValuesObtainedFrom":
        """mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition.TorqueValuesObtainedFrom"""
        temp = self.wrapped.ConversionToLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition.TorqueValuesObtainedFrom",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition._7013",
            "TorqueValuesObtainedFrom",
        )(value)

    @conversion_to_load_case.setter
    @enforce_parameter_types
    def conversion_to_load_case(self: Self, value: "_7013.TorqueValuesObtainedFrom"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition.TorqueValuesObtainedFrom",
        )
        self.wrapped.ConversionToLoadCase = value

    @property
    def include_bin_boundary_at_zero(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeBinBoundaryAtZero

        if temp is None:
            return False

        return temp

    @include_bin_boundary_at_zero.setter
    @enforce_parameter_types
    def include_bin_boundary_at_zero(self: Self, value: "bool"):
        self.wrapped.IncludeBinBoundaryAtZero = (
            bool(value) if value is not None else False
        )

    @property
    def number_of_bins(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfBins

        if temp is None:
            return 0

        return temp

    @number_of_bins.setter
    @enforce_parameter_types
    def number_of_bins(self: Self, value: "int"):
        self.wrapped.NumberOfBins = int(value) if value is not None else 0

    @property
    def specify_bins(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyBins

        if temp is None:
            return False

        return temp

    @specify_bins.setter
    @enforce_parameter_types
    def specify_bins(self: Self, value: "bool"):
        self.wrapped.SpecifyBins = bool(value) if value is not None else False

    @property
    def cast_to(self: Self) -> "TorqueInputOptions._Cast_TorqueInputOptions":
        return self._Cast_TorqueInputOptions(self)
