"""ScriptingSetup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility import _1601
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SCRIPTING_SETUP = python_net_import("SMT.MastaAPI.Utility.Scripting", "ScriptingSetup")

if TYPE_CHECKING:
    from mastapy.utility import _1602


__docformat__ = "restructuredtext en"
__all__ = ("ScriptingSetup",)


Self = TypeVar("Self", bound="ScriptingSetup")


class ScriptingSetup(_1601.PerMachineSettings):
    """ScriptingSetup

    This is a mastapy class.
    """

    TYPE = _SCRIPTING_SETUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ScriptingSetup")

    class _Cast_ScriptingSetup:
        """Special nested class for casting ScriptingSetup to subclasses."""

        def __init__(
            self: "ScriptingSetup._Cast_ScriptingSetup", parent: "ScriptingSetup"
        ):
            self._parent = parent

        @property
        def per_machine_settings(
            self: "ScriptingSetup._Cast_ScriptingSetup",
        ) -> "_1601.PerMachineSettings":
            return self._parent._cast(_1601.PerMachineSettings)

        @property
        def persistent_singleton(
            self: "ScriptingSetup._Cast_ScriptingSetup",
        ) -> "_1602.PersistentSingleton":
            from mastapy.utility import _1602

            return self._parent._cast(_1602.PersistentSingleton)

        @property
        def scripting_setup(
            self: "ScriptingSetup._Cast_ScriptingSetup",
        ) -> "ScriptingSetup":
            return self._parent

        def __getattr__(self: "ScriptingSetup._Cast_ScriptingSetup", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ScriptingSetup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def display_python_property_hints(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.DisplayPythonPropertyHints

        if temp is None:
            return False

        return temp

    @display_python_property_hints.setter
    @enforce_parameter_types
    def display_python_property_hints(self: Self, value: "bool"):
        self.wrapped.DisplayPythonPropertyHints = (
            bool(value) if value is not None else False
        )

    @property
    def image_height(self: Self) -> "int":
        """int"""
        temp = self.wrapped.ImageHeight

        if temp is None:
            return 0

        return temp

    @image_height.setter
    @enforce_parameter_types
    def image_height(self: Self, value: "int"):
        self.wrapped.ImageHeight = int(value) if value is not None else 0

    @property
    def image_width(self: Self) -> "int":
        """int"""
        temp = self.wrapped.ImageWidth

        if temp is None:
            return 0

        return temp

    @image_width.setter
    @enforce_parameter_types
    def image_width(self: Self, value: "int"):
        self.wrapped.ImageWidth = int(value) if value is not None else 0

    @property
    def load_scripted_properties_when_opening_masta(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.LoadScriptedPropertiesWhenOpeningMASTA

        if temp is None:
            return False

        return temp

    @load_scripted_properties_when_opening_masta.setter
    @enforce_parameter_types
    def load_scripted_properties_when_opening_masta(self: Self, value: "bool"):
        self.wrapped.LoadScriptedPropertiesWhenOpeningMASTA = (
            bool(value) if value is not None else False
        )

    @property
    def mastapy_version(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MastapyVersion

        if temp is None:
            return ""

        return temp

    @property
    def python_exe_path(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PythonExePath

        if temp is None:
            return ""

        return temp

    @property
    def python_home_directory(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PythonHomeDirectory

        if temp is None:
            return ""

        return temp

    @property
    def python_install_directory(self: Self) -> "str":
        """str"""
        temp = self.wrapped.PythonInstallDirectory

        if temp is None:
            return ""

        return temp

    @python_install_directory.setter
    @enforce_parameter_types
    def python_install_directory(self: Self, value: "str"):
        self.wrapped.PythonInstallDirectory = str(value) if value is not None else ""

    @property
    def python_remote_host(self: Self) -> "str":
        """str"""
        temp = self.wrapped.PythonRemoteHost

        if temp is None:
            return ""

        return temp

    @python_remote_host.setter
    @enforce_parameter_types
    def python_remote_host(self: Self, value: "str"):
        self.wrapped.PythonRemoteHost = str(value) if value is not None else ""

    @property
    def python_remote_port(self: Self) -> "int":
        """int"""
        temp = self.wrapped.PythonRemotePort

        if temp is None:
            return 0

        return temp

    @python_remote_port.setter
    @enforce_parameter_types
    def python_remote_port(self: Self, value: "int"):
        self.wrapped.PythonRemotePort = int(value) if value is not None else 0

    @property
    def python_remote_timeout_s(self: Self) -> "int":
        """int"""
        temp = self.wrapped.PythonRemoteTimeoutS

        if temp is None:
            return 0

        return temp

    @python_remote_timeout_s.setter
    @enforce_parameter_types
    def python_remote_timeout_s(self: Self, value: "int"):
        self.wrapped.PythonRemoteTimeoutS = int(value) if value is not None else 0

    @property
    def run_scripts_in_separate_threads(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.RunScriptsInSeparateThreads

        if temp is None:
            return False

        return temp

    @run_scripts_in_separate_threads.setter
    @enforce_parameter_types
    def run_scripts_in_separate_threads(self: Self, value: "bool"):
        self.wrapped.RunScriptsInSeparateThreads = (
            bool(value) if value is not None else False
        )

    @property
    def use_default_net_solution_directory(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseDefaultNETSolutionDirectory

        if temp is None:
            return False

        return temp

    @use_default_net_solution_directory.setter
    @enforce_parameter_types
    def use_default_net_solution_directory(self: Self, value: "bool"):
        self.wrapped.UseDefaultNETSolutionDirectory = (
            bool(value) if value is not None else False
        )

    @property
    def use_default_plugin_directory(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseDefaultPluginDirectory

        if temp is None:
            return False

        return temp

    @use_default_plugin_directory.setter
    @enforce_parameter_types
    def use_default_plugin_directory(self: Self, value: "bool"):
        self.wrapped.UseDefaultPluginDirectory = (
            bool(value) if value is not None else False
        )

    @property
    def use_default_python_scripts_directory(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseDefaultPythonScriptsDirectory

        if temp is None:
            return False

        return temp

    @use_default_python_scripts_directory.setter
    @enforce_parameter_types
    def use_default_python_scripts_directory(self: Self, value: "bool"):
        self.wrapped.UseDefaultPythonScriptsDirectory = (
            bool(value) if value is not None else False
        )

    @property
    def use_default_visual_studio_code_directory(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseDefaultVisualStudioCodeDirectory

        if temp is None:
            return False

        return temp

    @use_default_visual_studio_code_directory.setter
    @enforce_parameter_types
    def use_default_visual_studio_code_directory(self: Self, value: "bool"):
        self.wrapped.UseDefaultVisualStudioCodeDirectory = (
            bool(value) if value is not None else False
        )

    @property
    def visual_studio_code_directory(self: Self) -> "str":
        """str"""
        temp = self.wrapped.VisualStudioCodeDirectory

        if temp is None:
            return ""

        return temp

    @visual_studio_code_directory.setter
    @enforce_parameter_types
    def visual_studio_code_directory(self: Self, value: "str"):
        self.wrapped.VisualStudioCodeDirectory = str(value) if value is not None else ""

    def add_existing_net_solution(self: Self):
        """Method does not return."""
        self.wrapped.AddExistingNETSolution()

    def restore_api_packages(self: Self):
        """Method does not return."""
        self.wrapped.RestoreAPIPackages()

    def select_net_solution_directory(self: Self):
        """Method does not return."""
        self.wrapped.SelectNETSolutionDirectory()

    def select_plugin_directory(self: Self):
        """Method does not return."""
        self.wrapped.SelectPluginDirectory()

    def select_python_install_directory(self: Self):
        """Method does not return."""
        self.wrapped.SelectPythonInstallDirectory()

    def select_python_scripts_directory(self: Self):
        """Method does not return."""
        self.wrapped.SelectPythonScriptsDirectory()

    def select_visual_studio_code_directory(self: Self):
        """Method does not return."""
        self.wrapped.SelectVisualStudioCodeDirectory()

    @property
    def cast_to(self: Self) -> "ScriptingSetup._Cast_ScriptingSetup":
        return self._Cast_ScriptingSetup(self)
