"""InternalClearanceTolerance"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy.bearings.tolerances import _1909, _1911
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTERNAL_CLEARANCE_TOLERANCE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "InternalClearanceTolerance"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2445, _2480


__docformat__ = "restructuredtext en"
__all__ = ("InternalClearanceTolerance",)


Self = TypeVar("Self", bound="InternalClearanceTolerance")


class InternalClearanceTolerance(_0.APIBase):
    """InternalClearanceTolerance

    This is a mastapy class.
    """

    TYPE = _INTERNAL_CLEARANCE_TOLERANCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InternalClearanceTolerance")

    class _Cast_InternalClearanceTolerance:
        """Special nested class for casting InternalClearanceTolerance to subclasses."""

        def __init__(
            self: "InternalClearanceTolerance._Cast_InternalClearanceTolerance",
            parent: "InternalClearanceTolerance",
        ):
            self._parent = parent

        @property
        def axial_internal_clearance_tolerance(
            self: "InternalClearanceTolerance._Cast_InternalClearanceTolerance",
        ) -> "_2445.AxialInternalClearanceTolerance":
            from mastapy.system_model.part_model import _2445

            return self._parent._cast(_2445.AxialInternalClearanceTolerance)

        @property
        def radial_internal_clearance_tolerance(
            self: "InternalClearanceTolerance._Cast_InternalClearanceTolerance",
        ) -> "_2480.RadialInternalClearanceTolerance":
            from mastapy.system_model.part_model import _2480

            return self._parent._cast(_2480.RadialInternalClearanceTolerance)

        @property
        def internal_clearance_tolerance(
            self: "InternalClearanceTolerance._Cast_InternalClearanceTolerance",
        ) -> "InternalClearanceTolerance":
            return self._parent

        def __getattr__(
            self: "InternalClearanceTolerance._Cast_InternalClearanceTolerance",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InternalClearanceTolerance.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def clearance_class(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_InternalClearanceClass":
        """EnumWithSelectedValue[mastapy.bearings.tolerances.InternalClearanceClass]"""
        temp = self.wrapped.ClearanceClass

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_InternalClearanceClass.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @clearance_class.setter
    @enforce_parameter_types
    def clearance_class(self: Self, value: "_1909.InternalClearanceClass"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_InternalClearanceClass.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ClearanceClass = value

    @property
    def definition_option(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_BearingToleranceDefinitionOptions":
        """EnumWithSelectedValue[mastapy.bearings.tolerances.BearingToleranceDefinitionOptions]"""
        temp = self.wrapped.DefinitionOption

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_BearingToleranceDefinitionOptions.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @definition_option.setter
    @enforce_parameter_types
    def definition_option(self: Self, value: "_1911.BearingToleranceDefinitionOptions"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_BearingToleranceDefinitionOptions.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DefinitionOption = value

    @property
    def maximum(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Maximum

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum.setter
    @enforce_parameter_types
    def maximum(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Maximum = value

    @property
    def maximum_from_nominal(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumFromNominal

        if temp is None:
            return 0.0

        return temp

    @maximum_from_nominal.setter
    @enforce_parameter_types
    def maximum_from_nominal(self: Self, value: "float"):
        self.wrapped.MaximumFromNominal = float(value) if value is not None else 0.0

    @property
    def minimum(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Minimum

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum.setter
    @enforce_parameter_types
    def minimum(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Minimum = value

    @property
    def minimum_from_nominal(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumFromNominal

        if temp is None:
            return 0.0

        return temp

    @minimum_from_nominal.setter
    @enforce_parameter_types
    def minimum_from_nominal(self: Self, value: "float"):
        self.wrapped.MinimumFromNominal = float(value) if value is not None else 0.0

    @property
    def nominal(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Nominal

        if temp is None:
            return 0.0

        return temp

    @nominal.setter
    @enforce_parameter_types
    def nominal(self: Self, value: "float"):
        self.wrapped.Nominal = float(value) if value is not None else 0.0

    @property
    def specify_from_nominal(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyFromNominal

        if temp is None:
            return False

        return temp

    @specify_from_nominal.setter
    @enforce_parameter_types
    def specify_from_nominal(self: Self, value: "bool"):
        self.wrapped.SpecifyFromNominal = bool(value) if value is not None else False

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
    ) -> "InternalClearanceTolerance._Cast_InternalClearanceTolerance":
        return self._Cast_InternalClearanceTolerance(self)
