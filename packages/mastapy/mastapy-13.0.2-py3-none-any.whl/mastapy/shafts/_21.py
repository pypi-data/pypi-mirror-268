"""ShaftFeature"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_FEATURE = python_net_import("SMT.MastaAPI.Shafts", "ShaftFeature")

if TYPE_CHECKING:
    from mastapy.shafts import _14, _22, _23, _33, _41


__docformat__ = "restructuredtext en"
__all__ = ("ShaftFeature",)


Self = TypeVar("Self", bound="ShaftFeature")


class ShaftFeature(_0.APIBase):
    """ShaftFeature

    This is a mastapy class.
    """

    TYPE = _SHAFT_FEATURE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftFeature")

    class _Cast_ShaftFeature:
        """Special nested class for casting ShaftFeature to subclasses."""

        def __init__(self: "ShaftFeature._Cast_ShaftFeature", parent: "ShaftFeature"):
            self._parent = parent

        @property
        def generic_stress_concentration_factor(
            self: "ShaftFeature._Cast_ShaftFeature",
        ) -> "_14.GenericStressConcentrationFactor":
            from mastapy.shafts import _14

            return self._parent._cast(_14.GenericStressConcentrationFactor)

        @property
        def shaft_groove(self: "ShaftFeature._Cast_ShaftFeature") -> "_22.ShaftGroove":
            from mastapy.shafts import _22

            return self._parent._cast(_22.ShaftGroove)

        @property
        def shaft_key(self: "ShaftFeature._Cast_ShaftFeature") -> "_23.ShaftKey":
            from mastapy.shafts import _23

            return self._parent._cast(_23.ShaftKey)

        @property
        def shaft_radial_hole(
            self: "ShaftFeature._Cast_ShaftFeature",
        ) -> "_33.ShaftRadialHole":
            from mastapy.shafts import _33

            return self._parent._cast(_33.ShaftRadialHole)

        @property
        def shaft_surface_finish_section(
            self: "ShaftFeature._Cast_ShaftFeature",
        ) -> "_41.ShaftSurfaceFinishSection":
            from mastapy.shafts import _41

            return self._parent._cast(_41.ShaftSurfaceFinishSection)

        @property
        def shaft_feature(self: "ShaftFeature._Cast_ShaftFeature") -> "ShaftFeature":
            return self._parent

        def __getattr__(self: "ShaftFeature._Cast_ShaftFeature", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftFeature.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(self: Self) -> "ShaftFeature._Cast_ShaftFeature":
        return self._Cast_ShaftFeature(self)
