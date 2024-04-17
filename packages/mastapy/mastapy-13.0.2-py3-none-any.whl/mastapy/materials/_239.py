"""AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_STRESS_CYCLES_DATA_FOR_AN_SN_CURVE_OF_A_PLASTIC_MATERIAL = python_net_import(
    "SMT.MastaAPI.Materials", "AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial"
)

if TYPE_CHECKING:
    from mastapy.materials import _288, _289


__docformat__ = "restructuredtext en"
__all__ = ("AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial",)


Self = TypeVar("Self", bound="AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial")


class AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial(_0.APIBase):
    """AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_STRESS_CYCLES_DATA_FOR_AN_SN_CURVE_OF_A_PLASTIC_MATERIAL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial",
    )

    class _Cast_AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial:
        """Special nested class for casting AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial to subclasses."""

        def __init__(
            self: "AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial._Cast_AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial",
            parent: "AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial",
        ):
            self._parent = parent

        @property
        def stress_cycles_data_for_the_bending_sn_curve_of_a_plastic_material(
            self: "AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial._Cast_AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial",
        ) -> "_288.StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial":
            from mastapy.materials import _288

            return self._parent._cast(
                _288.StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial
            )

        @property
        def stress_cycles_data_for_the_contact_sn_curve_of_a_plastic_material(
            self: "AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial._Cast_AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial",
        ) -> "_289.StressCyclesDataForTheContactSNCurveOfAPlasticMaterial":
            from mastapy.materials import _289

            return self._parent._cast(
                _289.StressCyclesDataForTheContactSNCurveOfAPlasticMaterial
            )

        @property
        def abstract_stress_cycles_data_for_an_sn_curve_of_a_plastic_material(
            self: "AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial._Cast_AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial",
        ) -> "AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial":
            return self._parent

        def __getattr__(
            self: "AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial._Cast_AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial",
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
        self: Self,
        instance_to_wrap: "AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_load_cycles(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NumberOfLoadCycles

        if temp is None:
            return 0.0

        return temp

    @number_of_load_cycles.setter
    @enforce_parameter_types
    def number_of_load_cycles(self: Self, value: "float"):
        self.wrapped.NumberOfLoadCycles = float(value) if value is not None else 0.0

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
    ) -> "AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial._Cast_AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial":
        return self._Cast_AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial(self)
