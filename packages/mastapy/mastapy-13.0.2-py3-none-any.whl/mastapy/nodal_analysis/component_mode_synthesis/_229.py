"""CMSModel"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CMS_MODEL = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis", "CMSModel"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.component_mode_synthesis import _237, _231, _227
    from mastapy.nodal_analysis.dev_tools_analyses import _187
    from mastapy.utility import _1585


__docformat__ = "restructuredtext en"
__all__ = ("CMSModel",)


Self = TypeVar("Self", bound="CMSModel")


class CMSModel(_0.APIBase):
    """CMSModel

    This is a mastapy class.
    """

    TYPE = _CMS_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CMSModel")

    class _Cast_CMSModel:
        """Special nested class for casting CMSModel to subclasses."""

        def __init__(self: "CMSModel._Cast_CMSModel", parent: "CMSModel"):
            self._parent = parent

        @property
        def cms_model(self: "CMSModel._Cast_CMSModel") -> "CMSModel":
            return self._parent

        def __getattr__(self: "CMSModel._Cast_CMSModel", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CMSModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def estimated_memory_required_for_displacement_expansion(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EstimatedMemoryRequiredForDisplacementExpansion

        if temp is None:
            return ""

        return temp

    @property
    def estimated_memory_required_for_stiffness_and_mass_matrices(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EstimatedMemoryRequiredForStiffnessAndMassMatrices

        if temp is None:
            return ""

        return temp

    @property
    def estimated_total_memory_required_for_results(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EstimatedTotalMemoryRequiredForResults

        if temp is None:
            return ""

        return temp

    @property
    def has_condensation_result(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasCondensationResult

        if temp is None:
            return False

        return temp

    @property
    def memory_required_for_displacement_expansion(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MemoryRequiredForDisplacementExpansion

        if temp is None:
            return ""

        return temp

    @property
    def memory_required_for_stiffness_and_mass_matrices(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MemoryRequiredForStiffnessAndMassMatrices

        if temp is None:
            return ""

        return temp

    @property
    def software_used_for_reduction(self: Self) -> "_237.SoftwareUsedForReductionType":
        """mastapy.nodal_analysis.component_mode_synthesis.SoftwareUsedForReductionType

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SoftwareUsedForReduction

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis.SoftwareUsedForReductionType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis.component_mode_synthesis._237",
            "SoftwareUsedForReductionType",
        )(value)

    @property
    def total_memory_required_for_mesh(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalMemoryRequiredForMesh

        if temp is None:
            return ""

        return temp

    @property
    def total_memory_required_for_results(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalMemoryRequiredForResults

        if temp is None:
            return ""

        return temp

    @property
    def fe_model(self: Self) -> "_187.FEModel":
        """mastapy.nodal_analysis.dev_tools_analyses.FEModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def reduction_information(self: Self) -> "_1585.AnalysisRunInformation":
        """mastapy.utility.AnalysisRunInformation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReductionInformation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def reduction_options(self: Self) -> "_231.CMSOptions":
        """mastapy.nodal_analysis.component_mode_synthesis.CMSOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReductionOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def element_face_groups(self: Self) -> "List[_227.CMSElementFaceGroup]":
        """List[mastapy.nodal_analysis.component_mode_synthesis.CMSElementFaceGroup]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementFaceGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

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
    def save_surface_mesh_as_stl(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.SaveSurfaceMeshAsStl(file_path if file_path else "")

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
    def cast_to(self: Self) -> "CMSModel._Cast_CMSModel":
        return self._Cast_CMSModel(self)
