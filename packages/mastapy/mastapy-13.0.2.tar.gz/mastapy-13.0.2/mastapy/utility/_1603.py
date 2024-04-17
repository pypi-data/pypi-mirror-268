"""ProgramSettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Any, Union, Tuple
from enum import Enum

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.utility import _1601
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PROGRAM_SETTINGS = python_net_import("SMT.MastaAPI.Utility", "ProgramSettings")

if TYPE_CHECKING:
    from mastapy.utility import _1602


__docformat__ = "restructuredtext en"
__all__ = ("ProgramSettings",)


Self = TypeVar("Self", bound="ProgramSettings")


class ProgramSettings(_1601.PerMachineSettings):
    """ProgramSettings

    This is a mastapy class.
    """

    TYPE = _PROGRAM_SETTINGS

    class CheckForNewerVersionOption(Enum):
        """CheckForNewerVersionOption is a nested enum."""

        @classmethod
        def type_(cls):
            return _PROGRAM_SETTINGS.CheckForNewerVersionOption

        ASK_ON_STARTUP = 0
        YES = 1
        NO = 2

    def __enum_setattr(self: Self, attr: str, value: Any):
        raise AttributeError("Cannot set the attributes of an Enum.") from None

    def __enum_delattr(self: Self, attr: str):
        raise AttributeError("Cannot delete the attributes of an Enum.") from None

    CheckForNewerVersionOption.__setattr__ = __enum_setattr
    CheckForNewerVersionOption.__delattr__ = __enum_delattr
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ProgramSettings")

    class _Cast_ProgramSettings:
        """Special nested class for casting ProgramSettings to subclasses."""

        def __init__(
            self: "ProgramSettings._Cast_ProgramSettings", parent: "ProgramSettings"
        ):
            self._parent = parent

        @property
        def per_machine_settings(
            self: "ProgramSettings._Cast_ProgramSettings",
        ) -> "_1601.PerMachineSettings":
            return self._parent._cast(_1601.PerMachineSettings)

        @property
        def persistent_singleton(
            self: "ProgramSettings._Cast_ProgramSettings",
        ) -> "_1602.PersistentSingleton":
            from mastapy.utility import _1602

            return self._parent._cast(_1602.PersistentSingleton)

        @property
        def program_settings(
            self: "ProgramSettings._Cast_ProgramSettings",
        ) -> "ProgramSettings":
            return self._parent

        def __getattr__(self: "ProgramSettings._Cast_ProgramSettings", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ProgramSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_dcad_guide_model_autosave_size_limit(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TwoDCADGuideModelAutosaveSizeLimit

        if temp is None:
            return 0.0

        return temp

    @two_dcad_guide_model_autosave_size_limit.setter
    @enforce_parameter_types
    def two_dcad_guide_model_autosave_size_limit(self: Self, value: "float"):
        self.wrapped.TwoDCADGuideModelAutosaveSizeLimit = (
            float(value) if value is not None else 0.0
        )

    @property
    def allow_multithreading(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.AllowMultithreading

        if temp is None:
            return False

        return temp

    @allow_multithreading.setter
    @enforce_parameter_types
    def allow_multithreading(self: Self, value: "bool"):
        self.wrapped.AllowMultithreading = bool(value) if value is not None else False

    @property
    def ask_for_part_names_in_the_2d_view(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.AskForPartNamesInThe2DView

        if temp is None:
            return False

        return temp

    @ask_for_part_names_in_the_2d_view.setter
    @enforce_parameter_types
    def ask_for_part_names_in_the_2d_view(self: Self, value: "bool"):
        self.wrapped.AskForPartNamesInThe2DView = (
            bool(value) if value is not None else False
        )

    @property
    def auto_return_licences_inactivity_interval_minutes(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.AutoReturnLicencesInactivityIntervalMinutes

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @auto_return_licences_inactivity_interval_minutes.setter
    @enforce_parameter_types
    def auto_return_licences_inactivity_interval_minutes(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.AutoReturnLicencesInactivityIntervalMinutes = value

    @property
    def autosave_directory(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AutosaveDirectory

        if temp is None:
            return ""

        return temp

    @property
    def autosave_interval_minutes(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.AutosaveIntervalMinutes

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @autosave_interval_minutes.setter
    @enforce_parameter_types
    def autosave_interval_minutes(self: Self, value: "Union[int, Tuple[int, bool]]"):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.AutosaveIntervalMinutes = value

    @property
    def check_for_new_version_on_startup(
        self: Self,
    ) -> "ProgramSettings.CheckForNewerVersionOption":
        """mastapy.utility.ProgramSettings.CheckForNewerVersionOption"""
        temp = self.wrapped.CheckForNewVersionOnStartup

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.ProgramSettings+CheckForNewerVersionOption"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility.ProgramSettings.ProgramSettings",
            "CheckForNewerVersionOption",
        )(value)

    @check_for_new_version_on_startup.setter
    @enforce_parameter_types
    def check_for_new_version_on_startup(
        self: Self, value: "ProgramSettings.CheckForNewerVersionOption"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.ProgramSettings+CheckForNewerVersionOption"
        )
        self.wrapped.CheckForNewVersionOnStartup = value

    @property
    def confirm_exit(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ConfirmExit

        if temp is None:
            return False

        return temp

    @confirm_exit.setter
    @enforce_parameter_types
    def confirm_exit(self: Self, value: "bool"):
        self.wrapped.ConfirmExit = bool(value) if value is not None else False

    @property
    def eigenvalue_tolerance(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.EigenvalueTolerance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @eigenvalue_tolerance.setter
    @enforce_parameter_types
    def eigenvalue_tolerance(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.EigenvalueTolerance = value

    @property
    def font_size(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FontSize

        if temp is None:
            return 0.0

        return temp

    @font_size.setter
    @enforce_parameter_types
    def font_size(self: Self, value: "float"):
        self.wrapped.FontSize = float(value) if value is not None else 0.0

    @property
    def include_overridable_property_source_information(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeOverridablePropertySourceInformation

        if temp is None:
            return False

        return temp

    @include_overridable_property_source_information.setter
    @enforce_parameter_types
    def include_overridable_property_source_information(self: Self, value: "bool"):
        self.wrapped.IncludeOverridablePropertySourceInformation = (
            bool(value) if value is not None else False
        )

    @property
    def log_steps(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.LogSteps

        if temp is None:
            return False

        return temp

    @log_steps.setter
    @enforce_parameter_types
    def log_steps(self: Self, value: "bool"):
        self.wrapped.LogSteps = bool(value) if value is not None else False

    @property
    def maximum_number_of_files_to_store_in_history(self: Self) -> "int":
        """int"""
        temp = self.wrapped.MaximumNumberOfFilesToStoreInHistory

        if temp is None:
            return 0

        return temp

    @maximum_number_of_files_to_store_in_history.setter
    @enforce_parameter_types
    def maximum_number_of_files_to_store_in_history(self: Self, value: "int"):
        self.wrapped.MaximumNumberOfFilesToStoreInHistory = (
            int(value) if value is not None else 0
        )

    @property
    def maximum_number_of_threads_for_large_operations(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.MaximumNumberOfThreadsForLargeOperations

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @maximum_number_of_threads_for_large_operations.setter
    @enforce_parameter_types
    def maximum_number_of_threads_for_large_operations(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.MaximumNumberOfThreadsForLargeOperations = value

    @property
    def maximum_number_of_threads_for_mathematically_intensive_operations(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.MaximumNumberOfThreadsForMathematicallyIntensiveOperations

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @maximum_number_of_threads_for_mathematically_intensive_operations.setter
    @enforce_parameter_types
    def maximum_number_of_threads_for_mathematically_intensive_operations(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.MaximumNumberOfThreadsForMathematicallyIntensiveOperations = value

    @property
    def maximum_number_of_undo_items(self: Self) -> "int":
        """int"""
        temp = self.wrapped.MaximumNumberOfUndoItems

        if temp is None:
            return 0

        return temp

    @maximum_number_of_undo_items.setter
    @enforce_parameter_types
    def maximum_number_of_undo_items(self: Self, value: "int"):
        self.wrapped.MaximumNumberOfUndoItems = int(value) if value is not None else 0

    @property
    def mode_shape_tolerance(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ModeShapeTolerance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @mode_shape_tolerance.setter
    @enforce_parameter_types
    def mode_shape_tolerance(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ModeShapeTolerance = value

    @property
    def number_of_cpu_cores(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfCPUCores

        if temp is None:
            return 0

        return temp

    @property
    def number_of_cpu_threads(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfCPUThreads

        if temp is None:
            return 0

        return temp

    @property
    def number_of_connections_to_show_when_multi_selecting(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfConnectionsToShowWhenMultiSelecting

        if temp is None:
            return 0

        return temp

    @number_of_connections_to_show_when_multi_selecting.setter
    @enforce_parameter_types
    def number_of_connections_to_show_when_multi_selecting(self: Self, value: "int"):
        self.wrapped.NumberOfConnectionsToShowWhenMultiSelecting = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_days_of_advance_warning_for_expiring_features(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfDaysOfAdvanceWarningForExpiringFeatures

        if temp is None:
            return 0

        return temp

    @number_of_days_of_advance_warning_for_expiring_features.setter
    @enforce_parameter_types
    def number_of_days_of_advance_warning_for_expiring_features(
        self: Self, value: "int"
    ):
        self.wrapped.NumberOfDaysOfAdvanceWarningForExpiringFeatures = (
            int(value) if value is not None else 0
        )

    @property
    def override_font(self: Self) -> "str":
        """str"""
        temp = self.wrapped.OverrideFont

        if temp is None:
            return ""

        return temp

    @override_font.setter
    @enforce_parameter_types
    def override_font(self: Self, value: "str"):
        self.wrapped.OverrideFont = str(value) if value is not None else ""

    @property
    def show_drawing_numbers_in_tree_view(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowDrawingNumbersInTreeView

        if temp is None:
            return False

        return temp

    @show_drawing_numbers_in_tree_view.setter
    @enforce_parameter_types
    def show_drawing_numbers_in_tree_view(self: Self, value: "bool"):
        self.wrapped.ShowDrawingNumbersInTreeView = (
            bool(value) if value is not None else False
        )

    @property
    def show_number_of_teeth_with_gear_set_names(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowNumberOfTeethWithGearSetNames

        if temp is None:
            return False

        return temp

    @show_number_of_teeth_with_gear_set_names.setter
    @enforce_parameter_types
    def show_number_of_teeth_with_gear_set_names(self: Self, value: "bool"):
        self.wrapped.ShowNumberOfTeethWithGearSetNames = (
            bool(value) if value is not None else False
        )

    @property
    def show_user_interface_hints(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowUserInterfaceHints

        if temp is None:
            return False

        return temp

    @show_user_interface_hints.setter
    @enforce_parameter_types
    def show_user_interface_hints(self: Self, value: "bool"):
        self.wrapped.ShowUserInterfaceHints = (
            bool(value) if value is not None else False
        )

    @property
    def use_background_saving(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseBackgroundSaving

        if temp is None:
            return False

        return temp

    @use_background_saving.setter
    @enforce_parameter_types
    def use_background_saving(self: Self, value: "bool"):
        self.wrapped.UseBackgroundSaving = bool(value) if value is not None else False

    @property
    def use_compression_for_masta_files(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseCompressionForMASTAFiles

        if temp is None:
            return False

        return temp

    @use_compression_for_masta_files.setter
    @enforce_parameter_types
    def use_compression_for_masta_files(self: Self, value: "bool"):
        self.wrapped.UseCompressionForMASTAFiles = (
            bool(value) if value is not None else False
        )

    @property
    def use_default_autosave_directory(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseDefaultAutosaveDirectory

        if temp is None:
            return False

        return temp

    @use_default_autosave_directory.setter
    @enforce_parameter_types
    def use_default_autosave_directory(self: Self, value: "bool"):
        self.wrapped.UseDefaultAutosaveDirectory = (
            bool(value) if value is not None else False
        )

    @property
    def use_standard_dialog_for_file_open(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseStandardDialogForFileOpen

        if temp is None:
            return False

        return temp

    @use_standard_dialog_for_file_open.setter
    @enforce_parameter_types
    def use_standard_dialog_for_file_open(self: Self, value: "bool"):
        self.wrapped.UseStandardDialogForFileOpen = (
            bool(value) if value is not None else False
        )

    @property
    def use_standard_dialog_for_file_save(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseStandardDialogForFileSave

        if temp is None:
            return False

        return temp

    @use_standard_dialog_for_file_save.setter
    @enforce_parameter_types
    def use_standard_dialog_for_file_save(self: Self, value: "bool"):
        self.wrapped.UseStandardDialogForFileSave = (
            bool(value) if value is not None else False
        )

    @property
    def user_name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.UserName

        if temp is None:
            return ""

        return temp

    @user_name.setter
    @enforce_parameter_types
    def user_name(self: Self, value: "str"):
        self.wrapped.UserName = str(value) if value is not None else ""

    @property
    def user_defined_autosave_directory(self: Self) -> "str":
        """str"""
        temp = self.wrapped.UserDefinedAutosaveDirectory

        if temp is None:
            return ""

        return temp

    @user_defined_autosave_directory.setter
    @enforce_parameter_types
    def user_defined_autosave_directory(self: Self, value: "str"):
        self.wrapped.UserDefinedAutosaveDirectory = (
            str(value) if value is not None else ""
        )

    def clear_mru_entries(self: Self):
        """Method does not return."""
        self.wrapped.ClearMRUEntries()

    def select_autosave_directory(self: Self):
        """Method does not return."""
        self.wrapped.SelectAutosaveDirectory()

    @property
    def cast_to(self: Self) -> "ProgramSettings._Cast_ProgramSettings":
        return self._Cast_ProgramSettings(self)
