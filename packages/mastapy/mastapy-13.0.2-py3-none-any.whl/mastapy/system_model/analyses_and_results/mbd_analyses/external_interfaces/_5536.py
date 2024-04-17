"""DynamicExternalInterfaceOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_EXTERNAL_INTERFACE_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.ExternalInterfaces",
    "DynamicExternalInterfaceOptions",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5455


__docformat__ = "restructuredtext en"
__all__ = ("DynamicExternalInterfaceOptions",)


Self = TypeVar("Self", bound="DynamicExternalInterfaceOptions")


class DynamicExternalInterfaceOptions(_0.APIBase):
    """DynamicExternalInterfaceOptions

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_EXTERNAL_INTERFACE_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicExternalInterfaceOptions")

    class _Cast_DynamicExternalInterfaceOptions:
        """Special nested class for casting DynamicExternalInterfaceOptions to subclasses."""

        def __init__(
            self: "DynamicExternalInterfaceOptions._Cast_DynamicExternalInterfaceOptions",
            parent: "DynamicExternalInterfaceOptions",
        ):
            self._parent = parent

        @property
        def dynamic_external_interface_options(
            self: "DynamicExternalInterfaceOptions._Cast_DynamicExternalInterfaceOptions",
        ) -> "DynamicExternalInterfaceOptions":
            return self._parent

        def __getattr__(
            self: "DynamicExternalInterfaceOptions._Cast_DynamicExternalInterfaceOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicExternalInterfaceOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def generate_load_case(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.GenerateLoadCase

        if temp is None:
            return False

        return temp

    @generate_load_case.setter
    @enforce_parameter_types
    def generate_load_case(self: Self, value: "bool"):
        self.wrapped.GenerateLoadCase = bool(value) if value is not None else False

    @property
    def input_signal_filter_level(self: Self) -> "_5455.InputSignalFilterLevel":
        """mastapy.system_model.analyses_and_results.mbd_analyses.InputSignalFilterLevel"""
        temp = self.wrapped.InputSignalFilterLevel

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.InputSignalFilterLevel",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.mbd_analyses._5455",
            "InputSignalFilterLevel",
        )(value)

    @input_signal_filter_level.setter
    @enforce_parameter_types
    def input_signal_filter_level(self: Self, value: "_5455.InputSignalFilterLevel"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.InputSignalFilterLevel",
        )
        self.wrapped.InputSignalFilterLevel = value

    @property
    def path_of_saved_file(self: Self) -> "str":
        """str"""
        temp = self.wrapped.PathOfSavedFile

        if temp is None:
            return ""

        return temp

    @path_of_saved_file.setter
    @enforce_parameter_types
    def path_of_saved_file(self: Self, value: "str"):
        self.wrapped.PathOfSavedFile = str(value) if value is not None else ""

    @property
    def sample_time(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SampleTime

        if temp is None:
            return 0.0

        return temp

    @sample_time.setter
    @enforce_parameter_types
    def sample_time(self: Self, value: "float"):
        self.wrapped.SampleTime = float(value) if value is not None else 0.0

    @property
    def save_results(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SaveResults

        if temp is None:
            return False

        return temp

    @save_results.setter
    @enforce_parameter_types
    def save_results(self: Self, value: "bool"):
        self.wrapped.SaveResults = bool(value) if value is not None else False

    @property
    def cast_to(
        self: Self,
    ) -> "DynamicExternalInterfaceOptions._Cast_DynamicExternalInterfaceOptions":
        return self._Cast_DynamicExternalInterfaceOptions(self)
