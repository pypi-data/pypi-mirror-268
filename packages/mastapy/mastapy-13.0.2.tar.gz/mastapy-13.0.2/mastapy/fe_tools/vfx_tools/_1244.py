"""ProSolveOptions"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy.fe_tools.vfx_tools.vfx_enums import _1245, _1246
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PRO_SOLVE_OPTIONS = python_net_import(
    "SMT.MastaAPI.FETools.VfxTools", "ProSolveOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("ProSolveOptions",)


Self = TypeVar("Self", bound="ProSolveOptions")


class ProSolveOptions(_0.APIBase):
    """ProSolveOptions

    This is a mastapy class.
    """

    TYPE = _PRO_SOLVE_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ProSolveOptions")

    class _Cast_ProSolveOptions:
        """Special nested class for casting ProSolveOptions to subclasses."""

        def __init__(
            self: "ProSolveOptions._Cast_ProSolveOptions", parent: "ProSolveOptions"
        ):
            self._parent = parent

        @property
        def pro_solve_options(
            self: "ProSolveOptions._Cast_ProSolveOptions",
        ) -> "ProSolveOptions":
            return self._parent

        def __getattr__(self: "ProSolveOptions._Cast_ProSolveOptions", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ProSolveOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def compensate_for_singularities_in_model(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CompensateForSingularitiesInModel

        if temp is None:
            return False

        return temp

    @compensate_for_singularities_in_model.setter
    @enforce_parameter_types
    def compensate_for_singularities_in_model(self: Self, value: "bool"):
        self.wrapped.CompensateForSingularitiesInModel = (
            bool(value) if value is not None else False
        )

    @property
    def mpc_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ProSolveMpcType":
        """EnumWithSelectedValue[mastapy.fe_tools.vfx_tools.vfx_enums.ProSolveMpcType]"""
        temp = self.wrapped.MPCType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ProSolveMpcType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @mpc_type.setter
    @enforce_parameter_types
    def mpc_type(self: Self, value: "_1245.ProSolveMpcType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ProSolveMpcType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.MPCType = value

    @property
    def penalty_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PenaltyFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @penalty_factor.setter
    @enforce_parameter_types
    def penalty_factor(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PenaltyFactor = value

    @property
    def type_of_solver(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ProSolveSolverType":
        """EnumWithSelectedValue[mastapy.fe_tools.vfx_tools.vfx_enums.ProSolveSolverType]"""
        temp = self.wrapped.TypeOfSolver

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ProSolveSolverType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @type_of_solver.setter
    @enforce_parameter_types
    def type_of_solver(self: Self, value: "_1246.ProSolveSolverType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ProSolveSolverType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.TypeOfSolver = value

    @property
    def use_jacobian_checking(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseJacobianChecking

        if temp is None:
            return False

        return temp

    @use_jacobian_checking.setter
    @enforce_parameter_types
    def use_jacobian_checking(self: Self, value: "bool"):
        self.wrapped.UseJacobianChecking = bool(value) if value is not None else False

    @property
    def use_out_of_core_solver(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseOutOfCoreSolver

        if temp is None:
            return False

        return temp

    @use_out_of_core_solver.setter
    @enforce_parameter_types
    def use_out_of_core_solver(self: Self, value: "bool"):
        self.wrapped.UseOutOfCoreSolver = bool(value) if value is not None else False

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
    def cast_to(self: Self) -> "ProSolveOptions._Cast_ProSolveOptions":
        return self._Cast_ProSolveOptions(self)
