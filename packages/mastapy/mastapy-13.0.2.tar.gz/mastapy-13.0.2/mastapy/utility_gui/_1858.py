"""ScalingDrawStyle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SCALING_DRAW_STYLE = python_net_import("SMT.MastaAPI.UtilityGUI", "ScalingDrawStyle")

if TYPE_CHECKING:
    from mastapy.utility.enums import _1826


__docformat__ = "restructuredtext en"
__all__ = ("ScalingDrawStyle",)


Self = TypeVar("Self", bound="ScalingDrawStyle")


class ScalingDrawStyle(_0.APIBase):
    """ScalingDrawStyle

    This is a mastapy class.
    """

    TYPE = _SCALING_DRAW_STYLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ScalingDrawStyle")

    class _Cast_ScalingDrawStyle:
        """Special nested class for casting ScalingDrawStyle to subclasses."""

        def __init__(
            self: "ScalingDrawStyle._Cast_ScalingDrawStyle", parent: "ScalingDrawStyle"
        ):
            self._parent = parent

        @property
        def scaling_draw_style(
            self: "ScalingDrawStyle._Cast_ScalingDrawStyle",
        ) -> "ScalingDrawStyle":
            return self._parent

        def __getattr__(self: "ScalingDrawStyle._Cast_ScalingDrawStyle", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ScalingDrawStyle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bearing_force_arrows(self: Self) -> "_1826.BearingForceArrowOption":
        """mastapy.utility.enums.BearingForceArrowOption"""
        temp = self.wrapped.BearingForceArrows

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.Enums.BearingForceArrowOption"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility.enums._1826", "BearingForceArrowOption"
        )(value)

    @bearing_force_arrows.setter
    @enforce_parameter_types
    def bearing_force_arrows(self: Self, value: "_1826.BearingForceArrowOption"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.Enums.BearingForceArrowOption"
        )
        self.wrapped.BearingForceArrows = value

    @property
    def max_scale(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaxScale

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @max_scale.setter
    @enforce_parameter_types
    def max_scale(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaxScale = value

    @property
    def min_scale(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinScale

        if temp is None:
            return 0.0

        return temp

    @min_scale.setter
    @enforce_parameter_types
    def min_scale(self: Self, value: "float"):
        self.wrapped.MinScale = float(value) if value is not None else 0.0

    @property
    def scale(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Scale

        if temp is None:
            return 0.0

        return temp

    @scale.setter
    @enforce_parameter_types
    def scale(self: Self, value: "float"):
        self.wrapped.Scale = float(value) if value is not None else 0.0

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
    def cast_to(self: Self) -> "ScalingDrawStyle._Cast_ScalingDrawStyle":
        return self._Cast_ScalingDrawStyle(self)
