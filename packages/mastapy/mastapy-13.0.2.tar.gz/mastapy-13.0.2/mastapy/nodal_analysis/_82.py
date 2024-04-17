"""NodalMatrixEditorWrapperConceptCouplingStiffness"""

from __future__ import annotations

from typing import TypeVar, Optional, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy.nodal_analysis import _80
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODAL_MATRIX_EDITOR_WRAPPER_CONCEPT_COUPLING_STIFFNESS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "NodalMatrixEditorWrapperConceptCouplingStiffness"
)


__docformat__ = "restructuredtext en"
__all__ = ("NodalMatrixEditorWrapperConceptCouplingStiffness",)


Self = TypeVar("Self", bound="NodalMatrixEditorWrapperConceptCouplingStiffness")


class NodalMatrixEditorWrapperConceptCouplingStiffness(_80.NodalMatrixEditorWrapper):
    """NodalMatrixEditorWrapperConceptCouplingStiffness

    This is a mastapy class.
    """

    TYPE = _NODAL_MATRIX_EDITOR_WRAPPER_CONCEPT_COUPLING_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_NodalMatrixEditorWrapperConceptCouplingStiffness"
    )

    class _Cast_NodalMatrixEditorWrapperConceptCouplingStiffness:
        """Special nested class for casting NodalMatrixEditorWrapperConceptCouplingStiffness to subclasses."""

        def __init__(
            self: "NodalMatrixEditorWrapperConceptCouplingStiffness._Cast_NodalMatrixEditorWrapperConceptCouplingStiffness",
            parent: "NodalMatrixEditorWrapperConceptCouplingStiffness",
        ):
            self._parent = parent

        @property
        def nodal_matrix_editor_wrapper(
            self: "NodalMatrixEditorWrapperConceptCouplingStiffness._Cast_NodalMatrixEditorWrapperConceptCouplingStiffness",
        ) -> "_80.NodalMatrixEditorWrapper":
            return self._parent._cast(_80.NodalMatrixEditorWrapper)

        @property
        def nodal_matrix_editor_wrapper_concept_coupling_stiffness(
            self: "NodalMatrixEditorWrapperConceptCouplingStiffness._Cast_NodalMatrixEditorWrapperConceptCouplingStiffness",
        ) -> "NodalMatrixEditorWrapperConceptCouplingStiffness":
            return self._parent

        def __getattr__(
            self: "NodalMatrixEditorWrapperConceptCouplingStiffness._Cast_NodalMatrixEditorWrapperConceptCouplingStiffness",
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
        instance_to_wrap: "NodalMatrixEditorWrapperConceptCouplingStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial(self: Self) -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.Axial

        if temp is None:
            return None

        return temp

    @axial.setter
    @enforce_parameter_types
    def axial(self: Self, value: "Optional[float]"):
        self.wrapped.Axial = value

    @property
    def theta_y_theta_y(self: Self) -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.ThetaYThetaY

        if temp is None:
            return None

        return temp

    @theta_y_theta_y.setter
    @enforce_parameter_types
    def theta_y_theta_y(self: Self, value: "Optional[float]"):
        self.wrapped.ThetaYThetaY = value

    @property
    def theta_y_theta_y_cross(self: Self) -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.ThetaYThetaYCross

        if temp is None:
            return None

        return temp

    @theta_y_theta_y_cross.setter
    @enforce_parameter_types
    def theta_y_theta_y_cross(self: Self, value: "Optional[float]"):
        self.wrapped.ThetaYThetaYCross = value

    @property
    def torsional(self: Self) -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.Torsional

        if temp is None:
            return None

        return temp

    @torsional.setter
    @enforce_parameter_types
    def torsional(self: Self, value: "Optional[float]"):
        self.wrapped.Torsional = value

    @property
    def x_theta_y(self: Self) -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.XThetaY

        if temp is None:
            return None

        return temp

    @x_theta_y.setter
    @enforce_parameter_types
    def x_theta_y(self: Self, value: "Optional[float]"):
        self.wrapped.XThetaY = value

    @property
    def xx(self: Self) -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.XX

        if temp is None:
            return None

        return temp

    @xx.setter
    @enforce_parameter_types
    def xx(self: Self, value: "Optional[float]"):
        self.wrapped.XX = value

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
    ) -> "NodalMatrixEditorWrapperConceptCouplingStiffness._Cast_NodalMatrixEditorWrapperConceptCouplingStiffness":
        return self._Cast_NodalMatrixEditorWrapperConceptCouplingStiffness(self)
