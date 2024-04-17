"""TaskProgress"""

from __future__ import annotations

from typing import TypeVar, Any, List, Callable, Iterable

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.class_property import classproperty
from mastapy._internal.python_net import python_net_import
from mastapy import _7561
from mastapy._internal.cast_exception import CastException

_STRING = python_net_import("System", "String")
_ACTION = python_net_import("System", "Action")
_TASK_PROGRESS = python_net_import("SMT.MastaAPIUtility", "TaskProgress")


__docformat__ = "restructuredtext en"
__all__ = ("TaskProgress",)


Self = TypeVar("Self", bound="TaskProgress")


class TaskProgress(_7561.MarshalByRefObjectPermanent):
    """TaskProgress

    This is a mastapy class.
    """

    TYPE = _TASK_PROGRESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TaskProgress")

    class _Cast_TaskProgress:
        """Special nested class for casting TaskProgress to subclasses."""

        def __init__(self: "TaskProgress._Cast_TaskProgress", parent: "TaskProgress"):
            self._parent = parent

        @property
        def task_progress(self: "TaskProgress._Cast_TaskProgress") -> "TaskProgress":
            return self._parent

        def __getattr__(self: "TaskProgress._Cast_TaskProgress", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TaskProgress.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def title(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Title

        if temp is None:
            return ""

        return temp

    @property
    def status(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Status

        if temp is None:
            return ""

        return temp

    @status.setter
    @enforce_parameter_types
    def status(self: Self, value: "str"):
        self.wrapped.Status = str(value) if value is not None else ""

    @property
    def number_of_items(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfItems

        if temp is None:
            return 0

        return temp

    @property
    def show_progress(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowProgress

        if temp is None:
            return False

        return temp

    @show_progress.setter
    @enforce_parameter_types
    def show_progress(self: Self, value: "bool"):
        self.wrapped.ShowProgress = bool(value) if value is not None else False

    @property
    def show_completion_status(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowCompletionStatus

        if temp is None:
            return False

        return temp

    @show_completion_status.setter
    @enforce_parameter_types
    def show_completion_status(self: Self, value: "bool"):
        self.wrapped.ShowCompletionStatus = bool(value) if value is not None else False

    @property
    def can_cancel(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CanCancel

        if temp is None:
            return False

        return temp

    @can_cancel.setter
    @enforce_parameter_types
    def can_cancel(self: Self, value: "bool"):
        self.wrapped.CanCancel = bool(value) if value is not None else False

    @property
    def additional_string_to_add_to_title(self: Self) -> "str":
        """str"""
        temp = self.wrapped.AdditionalStringToAddToTitle

        if temp is None:
            return ""

        return temp

    @additional_string_to_add_to_title.setter
    @enforce_parameter_types
    def additional_string_to_add_to_title(self: Self, value: "str"):
        self.wrapped.AdditionalStringToAddToTitle = (
            str(value) if value is not None else ""
        )

    @property
    def is_progress_tree_cell_expanded(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsProgressTreeCellExpanded

        if temp is None:
            return False

        return temp

    @is_progress_tree_cell_expanded.setter
    @enforce_parameter_types
    def is_progress_tree_cell_expanded(self: Self, value: "bool"):
        self.wrapped.IsProgressTreeCellExpanded = (
            bool(value) if value is not None else False
        )

    @property
    def parent(self: Self) -> "TaskProgress":
        """mastapy.TaskProgress

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Parent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @classproperty
    def null_task_progress(cls) -> "TaskProgress":
        """mastapy.TaskProgress"""
        temp = TaskProgress.TYPE.NullTaskProgress

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @classproperty
    def null(cls) -> "TaskProgress":
        """mastapy.TaskProgress"""
        temp = TaskProgress.TYPE.Null

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def child_tasks(self: Self) -> "List[TaskProgress]":
        """List[mastapy.TaskProgress]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ChildTasks

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def is_aborting(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsAborting

        if temp is None:
            return False

        return temp

    @property
    def fraction_complete(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FractionComplete

        if temp is None:
            return 0.0

        return temp

    @fraction_complete.setter
    @enforce_parameter_types
    def fraction_complete(self: Self, value: "float"):
        self.wrapped.FractionComplete = float(value) if value is not None else 0.0

    @property
    def additional_status_string(self: Self) -> "str":
        """str"""
        temp = self.wrapped.AdditionalStatusString

        if temp is None:
            return ""

        return temp

    @additional_status_string.setter
    @enforce_parameter_types
    def additional_status_string(self: Self, value: "str"):
        self.wrapped.AdditionalStatusString = str(value) if value is not None else ""

    @property
    def top_parent(self: Self) -> "TaskProgress":
        """mastapy.TaskProgress

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TopParent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def add_progress_status_updated(self: Self, value: "Callable[[str], None]"):
        """Method does not return.

        Args:
            value (Callable[[str], None])
        """
        self.wrapped.add_ProgressStatusUpdated(value)

    @enforce_parameter_types
    def remove_progress_status_updated(self: Self, value: "Callable[[str], None]"):
        """Method does not return.

        Args:
            value (Callable[[str], None])
        """
        self.wrapped.remove_ProgressStatusUpdated(value)

    @enforce_parameter_types
    def add_progress_incremented(self: Self, value: "Callable[[float], None]"):
        """Method does not return.

        Args:
            value (Callable[[float], None])
        """
        self.wrapped.add_ProgressIncremented(value)

    @enforce_parameter_types
    def remove_progress_incremented(self: Self, value: "Callable[[float], None]"):
        """Method does not return.

        Args:
            value (Callable[[float], None])
        """
        self.wrapped.remove_ProgressIncremented(value)

    def abort(self: Self):
        """Method does not return."""
        self.wrapped.Abort()

    @enforce_parameter_types
    def continue_with_progress(
        self: Self,
        status_update: "str",
        perform_analysis: "Callable[[TaskProgress], None]",
    ) -> "TaskProgress":
        """mastapy.TaskProgress

        Args:
            status_update (str)
            perform_analysis (Callable[[mastapy.TaskProgress], None])
        """
        status_update = str(status_update)
        method_result = self.wrapped.ContinueWith.Overloads[
            _STRING, _ACTION[_TASK_PROGRESS]
        ](status_update if status_update else "", perform_analysis)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def continue_with(
        self: Self, status_update: "str", perform_analysis: "Callable[..., None]"
    ) -> "TaskProgress":
        """mastapy.TaskProgress

        Args:
            status_update (str)
            perform_analysis (Callable[..., None])
        """
        status_update = str(status_update)
        method_result = self.wrapped.ContinueWith.Overloads[_STRING, _ACTION](
            status_update if status_update else "", perform_analysis
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def get_all_errors(self: Self) -> "Iterable[str]":
        """Iterable[str]"""
        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.GetAllErrors(), str)

    @enforce_parameter_types
    def increment_progress(self: Self, inc: "int" = 1):
        """Method does not return.

        Args:
            inc (int, optional)
        """
        inc = int(inc)
        self.wrapped.IncrementProgress(inc if inc else 0)

    @enforce_parameter_types
    def update_status_with_increment(self: Self, new_status: "str"):
        """Method does not return.

        Args:
            new_status (str)
        """
        new_status = str(new_status)
        self.wrapped.UpdateStatusWithIncrement(new_status if new_status else "")

    @enforce_parameter_types
    def add_error(self: Self, error: "str"):
        """Method does not return.

        Args:
            error (str)
        """
        error = str(error)
        self.wrapped.AddError(error if error else "")

    def complete(self: Self):
        """Method does not return."""
        self.wrapped.Complete()

    @enforce_parameter_types
    def subdivide(self: Self, number_of_items: "int") -> "TaskProgress":
        """mastapy.TaskProgress

        Args:
            number_of_items (int)
        """
        number_of_items = int(number_of_items)
        method_result = self.wrapped.Subdivide(
            number_of_items if number_of_items else 0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def create_new_task(
        self: Self,
        title: "str",
        number_of_items: "int",
        show_progress: "bool" = True,
        show_eta: "bool" = False,
        manual_increment: "bool" = False,
    ) -> "TaskProgress":
        """mastapy.TaskProgress

        Args:
            title (str)
            number_of_items (int)
            show_progress (bool, optional)
            show_eta (bool, optional)
            manual_increment (bool, optional)
        """
        title = str(title)
        number_of_items = int(number_of_items)
        show_progress = bool(show_progress)
        show_eta = bool(show_eta)
        manual_increment = bool(manual_increment)
        method_result = self.wrapped.CreateNewTask(
            title if title else "",
            number_of_items if number_of_items else 0,
            show_progress if show_progress else False,
            show_eta if show_eta else False,
            manual_increment if manual_increment else False,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def dispose(self: Self):
        """Method does not return."""
        self.wrapped.Dispose()

    def to_string(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.ToString()
        return method_result

    def __enter__(self: Self):
        return self

    def __exit__(self: Self, exception_type: Any, exception_value: Any, traceback: Any):
        self.dispose()

    @property
    def cast_to(self: Self) -> "TaskProgress._Cast_TaskProgress":
        return self._Cast_TaskProgress(self)
