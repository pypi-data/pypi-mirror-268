"""SplineLeadRelief"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPLINE_LEAD_RELIEF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SplineLeadRelief"
)

if TYPE_CHECKING:
    from mastapy.math_utility.stiffness_calculators import _1544
    from mastapy.utility_gui.charts import _1874
    from mastapy.system_model.part_model.couplings import _2593


__docformat__ = "restructuredtext en"
__all__ = ("SplineLeadRelief",)


Self = TypeVar("Self", bound="SplineLeadRelief")


class SplineLeadRelief(_0.APIBase):
    """SplineLeadRelief

    This is a mastapy class.
    """

    TYPE = _SPLINE_LEAD_RELIEF
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SplineLeadRelief")

    class _Cast_SplineLeadRelief:
        """Special nested class for casting SplineLeadRelief to subclasses."""

        def __init__(
            self: "SplineLeadRelief._Cast_SplineLeadRelief", parent: "SplineLeadRelief"
        ):
            self._parent = parent

        @property
        def spline_lead_relief(
            self: "SplineLeadRelief._Cast_SplineLeadRelief",
        ) -> "SplineLeadRelief":
            return self._parent

        def __getattr__(self: "SplineLeadRelief._Cast_SplineLeadRelief", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SplineLeadRelief.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_position(self: Self) -> "_1544.IndividualContactPosition":
        """mastapy.math_utility.stiffness_calculators.IndividualContactPosition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactPosition

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.MathUtility.StiffnessCalculators.IndividualContactPosition",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.math_utility.stiffness_calculators._1544",
            "IndividualContactPosition",
        )(value)

    @property
    def linear_relief(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.LinearRelief

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @linear_relief.setter
    @enforce_parameter_types
    def linear_relief(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.LinearRelief = value

    @property
    def microgeometry_clearance_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicrogeometryClearanceChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def crowning(self: Self) -> "_2593.CrowningSpecification":
        """mastapy.system_model.part_model.couplings.CrowningSpecification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Crowning

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
    def cast_to(self: Self) -> "SplineLeadRelief._Cast_SplineLeadRelief":
        return self._Cast_SplineLeadRelief(self)
