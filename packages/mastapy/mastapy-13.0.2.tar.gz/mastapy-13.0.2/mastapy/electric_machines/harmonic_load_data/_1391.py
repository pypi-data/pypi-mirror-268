"""StatorToothInterpolator"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATOR_TOOTH_INTERPOLATOR = python_net_import(
    "SMT.MastaAPI.ElectricMachines.HarmonicLoadData", "StatorToothInterpolator"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1528
    from mastapy.electric_machines.harmonic_load_data import _1392, _1393


__docformat__ = "restructuredtext en"
__all__ = ("StatorToothInterpolator",)


Self = TypeVar("Self", bound="StatorToothInterpolator")


class StatorToothInterpolator(_0.APIBase):
    """StatorToothInterpolator

    This is a mastapy class.
    """

    TYPE = _STATOR_TOOTH_INTERPOLATOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StatorToothInterpolator")

    class _Cast_StatorToothInterpolator:
        """Special nested class for casting StatorToothInterpolator to subclasses."""

        def __init__(
            self: "StatorToothInterpolator._Cast_StatorToothInterpolator",
            parent: "StatorToothInterpolator",
        ):
            self._parent = parent

        @property
        def stator_tooth_load_interpolator(
            self: "StatorToothInterpolator._Cast_StatorToothInterpolator",
        ) -> "_1392.StatorToothLoadInterpolator":
            from mastapy.electric_machines.harmonic_load_data import _1392

            return self._parent._cast(_1392.StatorToothLoadInterpolator)

        @property
        def stator_tooth_moment_interpolator(
            self: "StatorToothInterpolator._Cast_StatorToothInterpolator",
        ) -> "_1393.StatorToothMomentInterpolator":
            from mastapy.electric_machines.harmonic_load_data import _1393

            return self._parent._cast(_1393.StatorToothMomentInterpolator)

        @property
        def stator_tooth_interpolator(
            self: "StatorToothInterpolator._Cast_StatorToothInterpolator",
        ) -> "StatorToothInterpolator":
            return self._parent

        def __getattr__(
            self: "StatorToothInterpolator._Cast_StatorToothInterpolator", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StatorToothInterpolator.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def multiple_fourier_series_interpolator_for(
        self: Self, node_index: "int"
    ) -> "_1528.MultipleFourierSeriesInterpolator":
        """mastapy.math_utility.MultipleFourierSeriesInterpolator

        Args:
            node_index (int)
        """
        node_index = int(node_index)
        method_result = self.wrapped.MultipleFourierSeriesInterpolatorFor(
            node_index if node_index else 0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "StatorToothInterpolator._Cast_StatorToothInterpolator":
        return self._Cast_StatorToothInterpolator(self)
