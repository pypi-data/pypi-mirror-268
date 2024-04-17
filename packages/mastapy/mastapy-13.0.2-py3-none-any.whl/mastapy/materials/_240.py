"""AcousticRadiationEfficiency"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ACOUSTIC_RADIATION_EFFICIENCY = python_net_import(
    "SMT.MastaAPI.Materials", "AcousticRadiationEfficiency"
)

if TYPE_CHECKING:
    from mastapy.materials import _241
    from mastapy.math_utility import _1542


__docformat__ = "restructuredtext en"
__all__ = ("AcousticRadiationEfficiency",)


Self = TypeVar("Self", bound="AcousticRadiationEfficiency")


class AcousticRadiationEfficiency(_0.APIBase):
    """AcousticRadiationEfficiency

    This is a mastapy class.
    """

    TYPE = _ACOUSTIC_RADIATION_EFFICIENCY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AcousticRadiationEfficiency")

    class _Cast_AcousticRadiationEfficiency:
        """Special nested class for casting AcousticRadiationEfficiency to subclasses."""

        def __init__(
            self: "AcousticRadiationEfficiency._Cast_AcousticRadiationEfficiency",
            parent: "AcousticRadiationEfficiency",
        ):
            self._parent = parent

        @property
        def acoustic_radiation_efficiency(
            self: "AcousticRadiationEfficiency._Cast_AcousticRadiationEfficiency",
        ) -> "AcousticRadiationEfficiency":
            return self._parent

        def __getattr__(
            self: "AcousticRadiationEfficiency._Cast_AcousticRadiationEfficiency",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AcousticRadiationEfficiency.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def input_type(self: Self) -> "_241.AcousticRadiationEfficiencyInputType":
        """mastapy.materials.AcousticRadiationEfficiencyInputType"""
        temp = self.wrapped.InputType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.AcousticRadiationEfficiencyInputType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.materials._241", "AcousticRadiationEfficiencyInputType"
        )(value)

    @input_type.setter
    @enforce_parameter_types
    def input_type(self: Self, value: "_241.AcousticRadiationEfficiencyInputType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Materials.AcousticRadiationEfficiencyInputType"
        )
        self.wrapped.InputType = value

    @property
    def knee_frequency(self: Self) -> "float":
        """float"""
        temp = self.wrapped.KneeFrequency

        if temp is None:
            return 0.0

        return temp

    @knee_frequency.setter
    @enforce_parameter_types
    def knee_frequency(self: Self, value: "float"):
        self.wrapped.KneeFrequency = float(value) if value is not None else 0.0

    @property
    def low_frequency_power(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LowFrequencyPower

        if temp is None:
            return 0.0

        return temp

    @low_frequency_power.setter
    @enforce_parameter_types
    def low_frequency_power(self: Self, value: "float"):
        self.wrapped.LowFrequencyPower = float(value) if value is not None else 0.0

    @property
    def radiation_efficiency_curve(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.RadiationEfficiencyCurve

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @radiation_efficiency_curve.setter
    @enforce_parameter_types
    def radiation_efficiency_curve(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.RadiationEfficiencyCurve = value.wrapped

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
    ) -> "AcousticRadiationEfficiency._Cast_AcousticRadiationEfficiency":
        return self._Cast_AcousticRadiationEfficiency(self)
