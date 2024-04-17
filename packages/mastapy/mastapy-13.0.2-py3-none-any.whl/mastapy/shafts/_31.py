"""ShaftProfilePoint"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_PROFILE_POINT = python_net_import("SMT.MastaAPI.Shafts", "ShaftProfilePoint")

if TYPE_CHECKING:
    from mastapy.shafts import _15, _32


__docformat__ = "restructuredtext en"
__all__ = ("ShaftProfilePoint",)


Self = TypeVar("Self", bound="ShaftProfilePoint")


class ShaftProfilePoint(_0.APIBase):
    """ShaftProfilePoint

    This is a mastapy class.
    """

    TYPE = _SHAFT_PROFILE_POINT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftProfilePoint")

    class _Cast_ShaftProfilePoint:
        """Special nested class for casting ShaftProfilePoint to subclasses."""

        def __init__(
            self: "ShaftProfilePoint._Cast_ShaftProfilePoint",
            parent: "ShaftProfilePoint",
        ):
            self._parent = parent

        @property
        def shaft_profile_point_copy(
            self: "ShaftProfilePoint._Cast_ShaftProfilePoint",
        ) -> "_32.ShaftProfilePointCopy":
            from mastapy.shafts import _32

            return self._parent._cast(_32.ShaftProfilePointCopy)

        @property
        def shaft_profile_point(
            self: "ShaftProfilePoint._Cast_ShaftProfilePoint",
        ) -> "ShaftProfilePoint":
            return self._parent

        def __getattr__(self: "ShaftProfilePoint._Cast_ShaftProfilePoint", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftProfilePoint.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Diameter

        if temp is None:
            return 0.0

        return temp

    @diameter.setter
    @enforce_parameter_types
    def diameter(self: Self, value: "float"):
        self.wrapped.Diameter = float(value) if value is not None else 0.0

    @property
    def fillet_radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.FilletRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @fillet_radius.setter
    @enforce_parameter_types
    def fillet_radius(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.FilletRadius = value

    @property
    def offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Offset

        if temp is None:
            return 0.0

        return temp

    @offset.setter
    @enforce_parameter_types
    def offset(self: Self, value: "float"):
        self.wrapped.Offset = float(value) if value is not None else 0.0

    @property
    def stress_concentration_factors(
        self: Self,
    ) -> "_15.ProfilePointFilletStressConcentrationFactors":
        """mastapy.shafts.ProfilePointFilletStressConcentrationFactors

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressConcentrationFactors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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

    def delete(self: Self):
        """Method does not return."""
        self.wrapped.Delete()

    def insert(self: Self):
        """Method does not return."""
        self.wrapped.Insert()

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
    def cast_to(self: Self) -> "ShaftProfilePoint._Cast_ShaftProfilePoint":
        return self._Cast_ShaftProfilePoint(self)
