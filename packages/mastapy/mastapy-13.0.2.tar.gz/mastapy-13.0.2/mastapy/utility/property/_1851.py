"""NamedRangeWithOverridableMinAndMax"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List, Generic

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_RANGE_WITH_OVERRIDABLE_MIN_AND_MAX = python_net_import(
    "SMT.MastaAPI.Utility.Property", "NamedRangeWithOverridableMinAndMax"
)

if TYPE_CHECKING:
    from mastapy.utility.units_and_measurements import _1612


__docformat__ = "restructuredtext en"
__all__ = ("NamedRangeWithOverridableMinAndMax",)


Self = TypeVar("Self", bound="NamedRangeWithOverridableMinAndMax")
T = TypeVar("T")
TMeasurement = TypeVar("TMeasurement", bound="_1612.MeasurementBase")


class NamedRangeWithOverridableMinAndMax(_0.APIBase, Generic[T, TMeasurement]):
    """NamedRangeWithOverridableMinAndMax

    This is a mastapy class.

    Generic Types:
        T
        TMeasurement
    """

    TYPE = _NAMED_RANGE_WITH_OVERRIDABLE_MIN_AND_MAX
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NamedRangeWithOverridableMinAndMax")

    class _Cast_NamedRangeWithOverridableMinAndMax:
        """Special nested class for casting NamedRangeWithOverridableMinAndMax to subclasses."""

        def __init__(
            self: "NamedRangeWithOverridableMinAndMax._Cast_NamedRangeWithOverridableMinAndMax",
            parent: "NamedRangeWithOverridableMinAndMax",
        ):
            self._parent = parent

        @property
        def named_range_with_overridable_min_and_max(
            self: "NamedRangeWithOverridableMinAndMax._Cast_NamedRangeWithOverridableMinAndMax",
        ) -> "NamedRangeWithOverridableMinAndMax":
            return self._parent

        def __getattr__(
            self: "NamedRangeWithOverridableMinAndMax._Cast_NamedRangeWithOverridableMinAndMax",
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
        self: Self, instance_to_wrap: "NamedRangeWithOverridableMinAndMax.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def max(self: Self) -> "overridable.Overridable_T":
        """Overridable[T]"""
        temp = self.wrapped.Max

        if temp is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_T"
        )(temp)

    @max.setter
    @enforce_parameter_types
    def max(self: Self, value: "Union[T, Tuple[T, bool]]"):
        wrapper_type = overridable.Overridable_T.wrapper_type()
        enclosed_type = overridable.Overridable_T.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.Max = value

    @property
    def min(self: Self) -> "overridable.Overridable_T":
        """Overridable[T]"""
        temp = self.wrapped.Min

        if temp is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_T"
        )(temp)

    @min.setter
    @enforce_parameter_types
    def min(self: Self, value: "Union[T, Tuple[T, bool]]"):
        wrapper_type = overridable.Overridable_T.wrapper_type()
        enclosed_type = overridable.Overridable_T.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.Min = value

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
    ) -> "NamedRangeWithOverridableMinAndMax._Cast_NamedRangeWithOverridableMinAndMax":
        return self._Cast_NamedRangeWithOverridableMinAndMax(self)
