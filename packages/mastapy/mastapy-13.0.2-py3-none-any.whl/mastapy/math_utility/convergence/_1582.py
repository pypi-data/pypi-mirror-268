"""DataLogger"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy._math.vector_3d import Vector3D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATA_LOGGER = python_net_import("SMT.MastaAPI.MathUtility.Convergence", "DataLogger")

if TYPE_CHECKING:
    from mastapy.math_utility.convergence import _1581
    from mastapy.utility_gui import _1857


__docformat__ = "restructuredtext en"
__all__ = ("DataLogger",)


Self = TypeVar("Self", bound="DataLogger")


class DataLogger(_0.APIBase):
    """DataLogger

    This is a mastapy class.
    """

    TYPE = _DATA_LOGGER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DataLogger")

    class _Cast_DataLogger:
        """Special nested class for casting DataLogger to subclasses."""

        def __init__(self: "DataLogger._Cast_DataLogger", parent: "DataLogger"):
            self._parent = parent

        @property
        def convergence_logger(
            self: "DataLogger._Cast_DataLogger",
        ) -> "_1581.ConvergenceLogger":
            from mastapy.math_utility.convergence import _1581

            return self._parent._cast(_1581.ConvergenceLogger)

        @property
        def data_logger_with_charts(
            self: "DataLogger._Cast_DataLogger",
        ) -> "_1857.DataLoggerWithCharts":
            from mastapy.utility_gui import _1857

            return self._parent._cast(_1857.DataLoggerWithCharts)

        @property
        def data_logger(self: "DataLogger._Cast_DataLogger") -> "DataLogger":
            return self._parent

        def __getattr__(self: "DataLogger._Cast_DataLogger", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DataLogger.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def available_properties(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AvailableProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @property
    def has_logged_data(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasLoggedData

        if temp is None:
            return False

        return temp

    @enforce_parameter_types
    def get_double_data_for(self: Self, property_name: "str") -> "List[float]":
        """List[float]

        Args:
            property_name (str)
        """
        property_name = str(property_name)
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.GetDoubleDataFor(property_name if property_name else ""), float
        )

    @enforce_parameter_types
    def get_int_data_for(self: Self, property_name: "str") -> "List[int]":
        """List[int]

        Args:
            property_name (str)
        """
        property_name = str(property_name)
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.GetIntDataFor(property_name if property_name else ""), int
        )

    @enforce_parameter_types
    def get_vector_data_for(self: Self, property_name: "str") -> "List[Vector3D]":
        """List[Vector3D]

        Args:
            property_name (str)
        """
        property_name = str(property_name)
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.GetVectorDataFor(property_name if property_name else ""),
            Vector3D,
        )

    @property
    def cast_to(self: Self) -> "DataLogger._Cast_DataLogger":
        return self._Cast_DataLogger(self)
