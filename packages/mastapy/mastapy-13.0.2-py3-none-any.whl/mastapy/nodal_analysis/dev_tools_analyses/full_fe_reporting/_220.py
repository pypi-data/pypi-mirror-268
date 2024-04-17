"""MaterialPropertiesReporting"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy.fe_tools.enums import _1248
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MATERIAL_PROPERTIES_REPORTING = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting",
    "MaterialPropertiesReporting",
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import (
        _209,
        _222,
        _224,
        _225,
    )


__docformat__ = "restructuredtext en"
__all__ = ("MaterialPropertiesReporting",)


Self = TypeVar("Self", bound="MaterialPropertiesReporting")


class MaterialPropertiesReporting(_0.APIBase):
    """MaterialPropertiesReporting

    This is a mastapy class.
    """

    TYPE = _MATERIAL_PROPERTIES_REPORTING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MaterialPropertiesReporting")

    class _Cast_MaterialPropertiesReporting:
        """Special nested class for casting MaterialPropertiesReporting to subclasses."""

        def __init__(
            self: "MaterialPropertiesReporting._Cast_MaterialPropertiesReporting",
            parent: "MaterialPropertiesReporting",
        ):
            self._parent = parent

        @property
        def material_properties_reporting(
            self: "MaterialPropertiesReporting._Cast_MaterialPropertiesReporting",
        ) -> "MaterialPropertiesReporting":
            return self._parent

        def __getattr__(
            self: "MaterialPropertiesReporting._Cast_MaterialPropertiesReporting",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MaterialPropertiesReporting.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def class_(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_MaterialPropertyClass":
        """EnumWithSelectedValue[mastapy.fe_tools.enums.MaterialPropertyClass]"""
        temp = self.wrapped.Class

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_MaterialPropertyClass.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @class_.setter
    @enforce_parameter_types
    def class_(self: Self, value: "_1248.MaterialPropertyClass"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_MaterialPropertyClass.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.Class = value

    @property
    def density(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Density

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @density.setter
    @enforce_parameter_types
    def density(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Density = value

    @property
    def elastic_stiffness_tensor_lower_triangle(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticStiffnessTensorLowerTriangle

        if temp is None:
            return ""

        return temp

    @property
    def id(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ID

        if temp is None:
            return 0

        return temp

    @property
    def modulus_of_elasticity(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ModulusOfElasticity

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @modulus_of_elasticity.setter
    @enforce_parameter_types
    def modulus_of_elasticity(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ModulusOfElasticity = value

    @property
    def poissons_ratio(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PoissonsRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @poissons_ratio.setter
    @enforce_parameter_types
    def poissons_ratio(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PoissonsRatio = value

    @property
    def thermal_expansion_coefficient(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ThermalExpansionCoefficient

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @thermal_expansion_coefficient.setter
    @enforce_parameter_types
    def thermal_expansion_coefficient(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ThermalExpansionCoefficient = value

    @property
    def thermal_expansion_coefficient_vector(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThermalExpansionCoefficientVector

        if temp is None:
            return ""

        return temp

    @property
    def elastic_modulus_components(
        self: Self,
    ) -> "_209.ElasticModulusOrthotropicComponents":
        """mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting.ElasticModulusOrthotropicComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticModulusComponents

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def poissons_ratio_components(
        self: Self,
    ) -> "_222.PoissonRatioOrthotropicComponents":
        """mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting.PoissonRatioOrthotropicComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PoissonsRatioComponents

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shear_modulus_components(
        self: Self,
    ) -> "_224.ShearModulusOrthotropicComponents":
        """mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting.ShearModulusOrthotropicComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShearModulusComponents

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def thermal_expansion_coefficient_components(
        self: Self,
    ) -> "_225.ThermalExpansionOrthotropicComponents":
        """mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting.ThermalExpansionOrthotropicComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThermalExpansionCoefficientComponents

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
    def cast_to(
        self: Self,
    ) -> "MaterialPropertiesReporting._Cast_MaterialPropertiesReporting":
        return self._Cast_MaterialPropertiesReporting(self)
