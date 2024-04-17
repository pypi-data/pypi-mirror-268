"""GearRatioInputOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility_gui import _1854
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_RATIO_INPUT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition",
    "GearRatioInputOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("GearRatioInputOptions",)


Self = TypeVar("Self", bound="GearRatioInputOptions")


class GearRatioInputOptions(_1854.ColumnInputOptions):
    """GearRatioInputOptions

    This is a mastapy class.
    """

    TYPE = _GEAR_RATIO_INPUT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearRatioInputOptions")

    class _Cast_GearRatioInputOptions:
        """Special nested class for casting GearRatioInputOptions to subclasses."""

        def __init__(
            self: "GearRatioInputOptions._Cast_GearRatioInputOptions",
            parent: "GearRatioInputOptions",
        ):
            self._parent = parent

        @property
        def column_input_options(
            self: "GearRatioInputOptions._Cast_GearRatioInputOptions",
        ) -> "_1854.ColumnInputOptions":
            return self._parent._cast(_1854.ColumnInputOptions)

        @property
        def gear_ratio_input_options(
            self: "GearRatioInputOptions._Cast_GearRatioInputOptions",
        ) -> "GearRatioInputOptions":
            return self._parent

        def __getattr__(
            self: "GearRatioInputOptions._Cast_GearRatioInputOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearRatioInputOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def has_gear_ratio_column(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasGearRatioColumn

        if temp is None:
            return False

        return temp

    @property
    def tolerance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Tolerance

        if temp is None:
            return 0.0

        return temp

    @tolerance.setter
    @enforce_parameter_types
    def tolerance(self: Self, value: "float"):
        self.wrapped.Tolerance = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "GearRatioInputOptions._Cast_GearRatioInputOptions":
        return self._Cast_GearRatioInputOptions(self)
