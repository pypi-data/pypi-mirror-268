"""OptimizationStep"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OPTIMIZATION_STEP = python_net_import(
    "SMT.MastaAPI.SystemModel.Optimization", "OptimizationStep"
)

if TYPE_CHECKING:
    from mastapy.system_model.optimization import _2239, _2234, _2237


__docformat__ = "restructuredtext en"
__all__ = ("OptimizationStep",)


Self = TypeVar("Self", bound="OptimizationStep")


class OptimizationStep(_0.APIBase):
    """OptimizationStep

    This is a mastapy class.
    """

    TYPE = _OPTIMIZATION_STEP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OptimizationStep")

    class _Cast_OptimizationStep:
        """Special nested class for casting OptimizationStep to subclasses."""

        def __init__(
            self: "OptimizationStep._Cast_OptimizationStep", parent: "OptimizationStep"
        ):
            self._parent = parent

        @property
        def conical_gear_optimization_step(
            self: "OptimizationStep._Cast_OptimizationStep",
        ) -> "_2234.ConicalGearOptimizationStep":
            from mastapy.system_model.optimization import _2234

            return self._parent._cast(_2234.ConicalGearOptimizationStep)

        @property
        def cylindrical_gear_optimization_step(
            self: "OptimizationStep._Cast_OptimizationStep",
        ) -> "_2237.CylindricalGearOptimizationStep":
            from mastapy.system_model.optimization import _2237

            return self._parent._cast(_2237.CylindricalGearOptimizationStep)

        @property
        def optimization_step(
            self: "OptimizationStep._Cast_OptimizationStep",
        ) -> "OptimizationStep":
            return self._parent

        def __getattr__(self: "OptimizationStep._Cast_OptimizationStep", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OptimizationStep.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def optimisation_target(self: Self) -> "_2239.MicroGeometryOptimisationTarget":
        """mastapy.system_model.optimization.MicroGeometryOptimisationTarget"""
        temp = self.wrapped.OptimisationTarget

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.Optimization.MicroGeometryOptimisationTarget",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.optimization._2239", "MicroGeometryOptimisationTarget"
        )(value)

    @optimisation_target.setter
    @enforce_parameter_types
    def optimisation_target(self: Self, value: "_2239.MicroGeometryOptimisationTarget"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.Optimization.MicroGeometryOptimisationTarget",
        )
        self.wrapped.OptimisationTarget = value

    @property
    def target_edge_stress_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TargetEdgeStressFactor

        if temp is None:
            return 0.0

        return temp

    @target_edge_stress_factor.setter
    @enforce_parameter_types
    def target_edge_stress_factor(self: Self, value: "float"):
        self.wrapped.TargetEdgeStressFactor = float(value) if value is not None else 0.0

    @property
    def tolerance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Tolerance

        if temp is None:
            return 0.0

        return temp

    @tolerance.setter
    @enforce_parameter_types
    def tolerance(self: Self, value: "float"):
        self.wrapped.Tolerance = float(value) if value is not None else 0.0

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
    def cast_to(self: Self) -> "OptimizationStep._Cast_OptimizationStep":
        return self._Cast_OptimizationStep(self)
