"""CMSOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CMS_OPTIONS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis", "CMSOptions"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.dev_tools_analyses import _201, _182
    from mastapy.math_utility import _1510
    from mastapy.fe_tools.vfx_tools import _1244


__docformat__ = "restructuredtext en"
__all__ = ("CMSOptions",)


Self = TypeVar("Self", bound="CMSOptions")


class CMSOptions(_0.APIBase):
    """CMSOptions

    This is a mastapy class.
    """

    TYPE = _CMS_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CMSOptions")

    class _Cast_CMSOptions:
        """Special nested class for casting CMSOptions to subclasses."""

        def __init__(self: "CMSOptions._Cast_CMSOptions", parent: "CMSOptions"):
            self._parent = parent

        @property
        def cms_options(self: "CMSOptions._Cast_CMSOptions") -> "CMSOptions":
            return self._parent

        def __getattr__(self: "CMSOptions._Cast_CMSOptions", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CMSOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def calculate_reduced_gravity_load(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CalculateReducedGravityLoad

        if temp is None:
            return False

        return temp

    @calculate_reduced_gravity_load.setter
    @enforce_parameter_types
    def calculate_reduced_gravity_load(self: Self, value: "bool"):
        self.wrapped.CalculateReducedGravityLoad = (
            bool(value) if value is not None else False
        )

    @property
    def calculate_reduced_thermal_expansion_force(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CalculateReducedThermalExpansionForce

        if temp is None:
            return False

        return temp

    @calculate_reduced_thermal_expansion_force.setter
    @enforce_parameter_types
    def calculate_reduced_thermal_expansion_force(self: Self, value: "bool"):
        self.wrapped.CalculateReducedThermalExpansionForce = (
            bool(value) if value is not None else False
        )

    @property
    def mass_matrix_type(self: Self) -> "_201.MassMatrixType":
        """mastapy.nodal_analysis.dev_tools_analyses.MassMatrixType"""
        temp = self.wrapped.MassMatrixType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.MassMatrixType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis.dev_tools_analyses._201", "MassMatrixType"
        )(value)

    @mass_matrix_type.setter
    @enforce_parameter_types
    def mass_matrix_type(self: Self, value: "_201.MassMatrixType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.MassMatrixType"
        )
        self.wrapped.MassMatrixType = value

    @property
    def mode_options_description(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModeOptionsDescription

        if temp is None:
            return ""

        return temp

    @property
    def precision_when_saving_expansion_vectors(self: Self) -> "_1510.DataPrecision":
        """mastapy.math_utility.DataPrecision"""
        temp = self.wrapped.PrecisionWhenSavingExpansionVectors

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.MathUtility.DataPrecision")

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.math_utility._1510", "DataPrecision"
        )(value)

    @precision_when_saving_expansion_vectors.setter
    @enforce_parameter_types
    def precision_when_saving_expansion_vectors(
        self: Self, value: "_1510.DataPrecision"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.MathUtility.DataPrecision"
        )
        self.wrapped.PrecisionWhenSavingExpansionVectors = value

    @property
    def store_condensation_node_displacement_expansion(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.StoreCondensationNodeDisplacementExpansion

        if temp is None:
            return False

        return temp

    @store_condensation_node_displacement_expansion.setter
    @enforce_parameter_types
    def store_condensation_node_displacement_expansion(self: Self, value: "bool"):
        self.wrapped.StoreCondensationNodeDisplacementExpansion = (
            bool(value) if value is not None else False
        )

    @property
    def internal_mode_options(self: Self) -> "_182.EigenvalueOptions":
        """mastapy.nodal_analysis.dev_tools_analyses.EigenvalueOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InternalModeOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def solver_options(self: Self) -> "_1244.ProSolveOptions":
        """mastapy.fe_tools.vfx_tools.ProSolveOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SolverOptions

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
    def cast_to(self: Self) -> "CMSOptions._Cast_CMSOptions":
        return self._Cast_CMSOptions(self)
