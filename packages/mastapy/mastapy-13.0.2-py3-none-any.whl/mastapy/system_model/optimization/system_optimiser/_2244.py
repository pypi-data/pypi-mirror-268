"""DesignStateTargetRatio"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_STATE_TARGET_RATIO = python_net_import(
    "SMT.MastaAPI.SystemModel.Optimization.SystemOptimiser", "DesignStateTargetRatio"
)


__docformat__ = "restructuredtext en"
__all__ = ("DesignStateTargetRatio",)


Self = TypeVar("Self", bound="DesignStateTargetRatio")


class DesignStateTargetRatio(_0.APIBase):
    """DesignStateTargetRatio

    This is a mastapy class.
    """

    TYPE = _DESIGN_STATE_TARGET_RATIO
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DesignStateTargetRatio")

    class _Cast_DesignStateTargetRatio:
        """Special nested class for casting DesignStateTargetRatio to subclasses."""

        def __init__(
            self: "DesignStateTargetRatio._Cast_DesignStateTargetRatio",
            parent: "DesignStateTargetRatio",
        ):
            self._parent = parent

        @property
        def design_state_target_ratio(
            self: "DesignStateTargetRatio._Cast_DesignStateTargetRatio",
        ) -> "DesignStateTargetRatio":
            return self._parent

        def __getattr__(
            self: "DesignStateTargetRatio._Cast_DesignStateTargetRatio", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DesignStateTargetRatio.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duration(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Duration

        if temp is None:
            return 0.0

        return temp

    @duration.setter
    @enforce_parameter_types
    def duration(self: Self, value: "float"):
        self.wrapped.Duration = float(value) if value is not None else 0.0

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
    def ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Ratio

        if temp is None:
            return 0.0

        return temp

    @property
    def target_ratio(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TargetRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @target_ratio.setter
    @enforce_parameter_types
    def target_ratio(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TargetRatio = value

    @property
    def target_ratio_tolerance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TargetRatioTolerance

        if temp is None:
            return 0.0

        return temp

    @target_ratio_tolerance.setter
    @enforce_parameter_types
    def target_ratio_tolerance(self: Self, value: "float"):
        self.wrapped.TargetRatioTolerance = float(value) if value is not None else 0.0

    @property
    def target_ratio_tolerance_absolute(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TargetRatioToleranceAbsolute

        if temp is None:
            return 0.0

        return temp

    @target_ratio_tolerance_absolute.setter
    @enforce_parameter_types
    def target_ratio_tolerance_absolute(self: Self, value: "float"):
        self.wrapped.TargetRatioToleranceAbsolute = (
            float(value) if value is not None else 0.0
        )

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
    def cast_to(self: Self) -> "DesignStateTargetRatio._Cast_DesignStateTargetRatio":
        return self._Cast_DesignStateTargetRatio(self)
