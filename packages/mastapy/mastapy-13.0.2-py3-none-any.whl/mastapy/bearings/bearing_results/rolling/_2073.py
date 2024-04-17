"""PreloadFactorLookupTable"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PRELOAD_FACTOR_LOOKUP_TABLE = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "PreloadFactorLookupTable"
)


__docformat__ = "restructuredtext en"
__all__ = ("PreloadFactorLookupTable",)


Self = TypeVar("Self", bound="PreloadFactorLookupTable")


class PreloadFactorLookupTable(_0.APIBase):
    """PreloadFactorLookupTable

    This is a mastapy class.
    """

    TYPE = _PRELOAD_FACTOR_LOOKUP_TABLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PreloadFactorLookupTable")

    class _Cast_PreloadFactorLookupTable:
        """Special nested class for casting PreloadFactorLookupTable to subclasses."""

        def __init__(
            self: "PreloadFactorLookupTable._Cast_PreloadFactorLookupTable",
            parent: "PreloadFactorLookupTable",
        ):
            self._parent = parent

        @property
        def preload_factor_lookup_table(
            self: "PreloadFactorLookupTable._Cast_PreloadFactorLookupTable",
        ) -> "PreloadFactorLookupTable":
            return self._parent

        def __getattr__(
            self: "PreloadFactorLookupTable._Cast_PreloadFactorLookupTable", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PreloadFactorLookupTable.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def high(self: Self) -> "float":
        """float"""
        temp = self.wrapped.High

        if temp is None:
            return 0.0

        return temp

    @high.setter
    @enforce_parameter_types
    def high(self: Self, value: "float"):
        self.wrapped.High = float(value) if value is not None else 0.0

    @property
    def low(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Low

        if temp is None:
            return 0.0

        return temp

    @low.setter
    @enforce_parameter_types
    def low(self: Self, value: "float"):
        self.wrapped.Low = float(value) if value is not None else 0.0

    @property
    def medium(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Medium

        if temp is None:
            return 0.0

        return temp

    @medium.setter
    @enforce_parameter_types
    def medium(self: Self, value: "float"):
        self.wrapped.Medium = float(value) if value is not None else 0.0

    @property
    def zero(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Zero

        if temp is None:
            return 0.0

        return temp

    @zero.setter
    @enforce_parameter_types
    def zero(self: Self, value: "float"):
        self.wrapped.Zero = float(value) if value is not None else 0.0

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
    def cast_to(
        self: Self,
    ) -> "PreloadFactorLookupTable._Cast_PreloadFactorLookupTable":
        return self._Cast_PreloadFactorLookupTable(self)
