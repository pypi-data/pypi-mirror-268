"""ShaftSurfaceRoughness"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy.shafts import _45
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_SURFACE_ROUGHNESS = python_net_import(
    "SMT.MastaAPI.Shafts", "ShaftSurfaceRoughness"
)


__docformat__ = "restructuredtext en"
__all__ = ("ShaftSurfaceRoughness",)


Self = TypeVar("Self", bound="ShaftSurfaceRoughness")


class ShaftSurfaceRoughness(_0.APIBase):
    """ShaftSurfaceRoughness

    This is a mastapy class.
    """

    TYPE = _SHAFT_SURFACE_ROUGHNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftSurfaceRoughness")

    class _Cast_ShaftSurfaceRoughness:
        """Special nested class for casting ShaftSurfaceRoughness to subclasses."""

        def __init__(
            self: "ShaftSurfaceRoughness._Cast_ShaftSurfaceRoughness",
            parent: "ShaftSurfaceRoughness",
        ):
            self._parent = parent

        @property
        def shaft_surface_roughness(
            self: "ShaftSurfaceRoughness._Cast_ShaftSurfaceRoughness",
        ) -> "ShaftSurfaceRoughness":
            return self._parent

        def __getattr__(
            self: "ShaftSurfaceRoughness._Cast_ShaftSurfaceRoughness", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftSurfaceRoughness.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def surface_finish(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_SurfaceFinishes":
        """EnumWithSelectedValue[mastapy.shafts.SurfaceFinishes]"""
        temp = self.wrapped.SurfaceFinish

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_SurfaceFinishes.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @surface_finish.setter
    @enforce_parameter_types
    def surface_finish(self: Self, value: "_45.SurfaceFinishes"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_SurfaceFinishes.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.SurfaceFinish = value

    @property
    def surface_roughness(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SurfaceRoughness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @surface_roughness.setter
    @enforce_parameter_types
    def surface_roughness(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SurfaceRoughness = value

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
    def cast_to(self: Self) -> "ShaftSurfaceRoughness._Cast_ShaftSurfaceRoughness":
        return self._Cast_ShaftSurfaceRoughness(self)
