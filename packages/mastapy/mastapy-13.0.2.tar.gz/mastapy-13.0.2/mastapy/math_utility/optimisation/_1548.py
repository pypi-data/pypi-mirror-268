"""InputSetter"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Generic

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INPUT_SETTER = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation", "InputSetter"
)

if TYPE_CHECKING:
    from mastapy.math_utility.optimisation import _1554


__docformat__ = "restructuredtext en"
__all__ = ("InputSetter",)


Self = TypeVar("Self", bound="InputSetter")
T = TypeVar("T")


class InputSetter(_0.APIBase, Generic[T]):
    """InputSetter

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _INPUT_SETTER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InputSetter")

    class _Cast_InputSetter:
        """Special nested class for casting InputSetter to subclasses."""

        def __init__(self: "InputSetter._Cast_InputSetter", parent: "InputSetter"):
            self._parent = parent

        @property
        def input_setter(self: "InputSetter._Cast_InputSetter") -> "InputSetter":
            return self._parent

        def __getattr__(self: "InputSetter._Cast_InputSetter", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InputSetter.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fix_this_property(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.FixThisProperty

        if temp is None:
            return False

        return temp

    @fix_this_property.setter
    @enforce_parameter_types
    def fix_this_property(self: Self, value: "bool"):
        self.wrapped.FixThisProperty = bool(value) if value is not None else False

    @property
    def last_path_object_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LastPathObjectName

        if temp is None:
            return ""

        return temp

    @property
    def value(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Value

        if temp is None:
            return 0.0

        return temp

    @property
    def candidate(self: Self) -> "T":
        """T

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Candidate

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def optimiser_input(self: Self) -> "_1554.ParetoOptimisationInput":
        """mastapy.math_utility.optimisation.ParetoOptimisationInput

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OptimiserInput

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
    def cast_to(self: Self) -> "InputSetter._Cast_InputSetter":
        return self._Cast_InputSetter(self)
