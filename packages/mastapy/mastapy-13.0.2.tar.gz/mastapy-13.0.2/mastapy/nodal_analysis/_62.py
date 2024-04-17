"""FEMeshingProblem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_MESHING_PROBLEM = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "FEMeshingProblem"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _63


__docformat__ = "restructuredtext en"
__all__ = ("FEMeshingProblem",)


Self = TypeVar("Self", bound="FEMeshingProblem")


class FEMeshingProblem(_0.APIBase):
    """FEMeshingProblem

    This is a mastapy class.
    """

    TYPE = _FE_MESHING_PROBLEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEMeshingProblem")

    class _Cast_FEMeshingProblem:
        """Special nested class for casting FEMeshingProblem to subclasses."""

        def __init__(
            self: "FEMeshingProblem._Cast_FEMeshingProblem", parent: "FEMeshingProblem"
        ):
            self._parent = parent

        @property
        def fe_meshing_problem(
            self: "FEMeshingProblem._Cast_FEMeshingProblem",
        ) -> "FEMeshingProblem":
            return self._parent

        def __getattr__(self: "FEMeshingProblem._Cast_FEMeshingProblem", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEMeshingProblem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def icon(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Icon

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def show_in_3d_view(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowIn3DView

        if temp is None:
            return False

        return temp

    @show_in_3d_view.setter
    @enforce_parameter_types
    def show_in_3d_view(self: Self, value: "bool"):
        self.wrapped.ShowIn3DView = bool(value) if value is not None else False

    @property
    def type_(self: Self) -> "_63.FEMeshingProblems":
        """mastapy.nodal_analysis.FEMeshingProblems

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Type

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.FEMeshingProblems"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis._63", "FEMeshingProblems"
        )(value)

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

    def show_in_geometry_modeller(self: Self):
        """Method does not return."""
        self.wrapped.ShowInGeometryModeller()

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
    def cast_to(self: Self) -> "FEMeshingProblem._Cast_FEMeshingProblem":
        return self._Cast_FEMeshingProblem(self)
