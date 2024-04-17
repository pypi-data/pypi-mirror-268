"""GeometryModellerSettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal import constructor
from mastapy.utility import _1601
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEOMETRY_MODELLER_SETTINGS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.GeometryModellerLink", "GeometryModellerSettings"
)

if TYPE_CHECKING:
    from mastapy.utility import _1597, _1602


__docformat__ = "restructuredtext en"
__all__ = ("GeometryModellerSettings",)


Self = TypeVar("Self", bound="GeometryModellerSettings")


class GeometryModellerSettings(_1601.PerMachineSettings):
    """GeometryModellerSettings

    This is a mastapy class.
    """

    TYPE = _GEOMETRY_MODELLER_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GeometryModellerSettings")

    class _Cast_GeometryModellerSettings:
        """Special nested class for casting GeometryModellerSettings to subclasses."""

        def __init__(
            self: "GeometryModellerSettings._Cast_GeometryModellerSettings",
            parent: "GeometryModellerSettings",
        ):
            self._parent = parent

        @property
        def per_machine_settings(
            self: "GeometryModellerSettings._Cast_GeometryModellerSettings",
        ) -> "_1601.PerMachineSettings":
            return self._parent._cast(_1601.PerMachineSettings)

        @property
        def persistent_singleton(
            self: "GeometryModellerSettings._Cast_GeometryModellerSettings",
        ) -> "_1602.PersistentSingleton":
            from mastapy.utility import _1602

            return self._parent._cast(_1602.PersistentSingleton)

        @property
        def geometry_modeller_settings(
            self: "GeometryModellerSettings._Cast_GeometryModellerSettings",
        ) -> "GeometryModellerSettings":
            return self._parent

        def __getattr__(
            self: "GeometryModellerSettings._Cast_GeometryModellerSettings", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GeometryModellerSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def auto_detected_geometry_modeller_path(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.AutoDetectedGeometryModellerPath

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @auto_detected_geometry_modeller_path.setter
    @enforce_parameter_types
    def auto_detected_geometry_modeller_path(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.AutoDetectedGeometryModellerPath = value

    @property
    def disable_intel_mkl_internal_multithreading(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.DisableIntelMKLInternalMultithreading

        if temp is None:
            return False

        return temp

    @disable_intel_mkl_internal_multithreading.setter
    @enforce_parameter_types
    def disable_intel_mkl_internal_multithreading(self: Self, value: "bool"):
        self.wrapped.DisableIntelMKLInternalMultithreading = (
            bool(value) if value is not None else False
        )

    @property
    def folder_path(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FolderPath

        if temp is None:
            return ""

        return temp

    @property
    def geometry_modeller_arguments(self: Self) -> "str":
        """str"""
        temp = self.wrapped.GeometryModellerArguments

        if temp is None:
            return ""

        return temp

    @geometry_modeller_arguments.setter
    @enforce_parameter_types
    def geometry_modeller_arguments(self: Self, value: "str"):
        self.wrapped.GeometryModellerArguments = str(value) if value is not None else ""

    @property
    def hide_geometry_modeller_instead_of_closing(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.HideGeometryModellerInsteadOfClosing

        if temp is None:
            return False

        return temp

    @hide_geometry_modeller_instead_of_closing.setter
    @enforce_parameter_types
    def hide_geometry_modeller_instead_of_closing(self: Self, value: "bool"):
        self.wrapped.HideGeometryModellerInsteadOfClosing = (
            bool(value) if value is not None else False
        )

    @property
    def no_licence_for_geometry_modeller(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NoLicenceForGeometryModeller

        if temp is None:
            return ""

        return temp

    @property
    def show_message_when_hiding_geometry_modeller(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowMessageWhenHidingGeometryModeller

        if temp is None:
            return False

        return temp

    @show_message_when_hiding_geometry_modeller.setter
    @enforce_parameter_types
    def show_message_when_hiding_geometry_modeller(self: Self, value: "bool"):
        self.wrapped.ShowMessageWhenHidingGeometryModeller = (
            bool(value) if value is not None else False
        )

    @property
    def use_auto_detected_geometry_modeller_path(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseAutoDetectedGeometryModellerPath

        if temp is None:
            return False

        return temp

    @use_auto_detected_geometry_modeller_path.setter
    @enforce_parameter_types
    def use_auto_detected_geometry_modeller_path(self: Self, value: "bool"):
        self.wrapped.UseAutoDetectedGeometryModellerPath = (
            bool(value) if value is not None else False
        )

    @property
    def is_geometry_modeller_connected(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsGeometryModellerConnected

        if temp is None:
            return False

        return temp

    @enforce_parameter_types
    def launch_geometry_modeller(
        self: Self, file_path: "str" = "None"
    ) -> "_1597.MethodOutcome":
        """mastapy.utility.MethodOutcome

        Args:
            file_path (str, optional)
        """
        file_path = str(file_path)
        method_result = self.wrapped.LaunchGeometryModeller(
            file_path if file_path else ""
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def select_folder_path(self: Self, path: "str"):
        """Method does not return.

        Args:
            path (str)
        """
        path = str(path)
        self.wrapped.SelectFolderPath(path if path else "")

    @property
    def cast_to(
        self: Self,
    ) -> "GeometryModellerSettings._Cast_GeometryModellerSettings":
        return self._Cast_GeometryModellerSettings(self)
