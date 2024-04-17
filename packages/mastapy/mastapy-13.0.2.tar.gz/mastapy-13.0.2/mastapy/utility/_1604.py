"""PushbulletSettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.utility import _1601
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PUSHBULLET_SETTINGS = python_net_import("SMT.MastaAPI.Utility", "PushbulletSettings")

if TYPE_CHECKING:
    from mastapy.utility import _1602


__docformat__ = "restructuredtext en"
__all__ = ("PushbulletSettings",)


Self = TypeVar("Self", bound="PushbulletSettings")


class PushbulletSettings(_1601.PerMachineSettings):
    """PushbulletSettings

    This is a mastapy class.
    """

    TYPE = _PUSHBULLET_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PushbulletSettings")

    class _Cast_PushbulletSettings:
        """Special nested class for casting PushbulletSettings to subclasses."""

        def __init__(
            self: "PushbulletSettings._Cast_PushbulletSettings",
            parent: "PushbulletSettings",
        ):
            self._parent = parent

        @property
        def per_machine_settings(
            self: "PushbulletSettings._Cast_PushbulletSettings",
        ) -> "_1601.PerMachineSettings":
            return self._parent._cast(_1601.PerMachineSettings)

        @property
        def persistent_singleton(
            self: "PushbulletSettings._Cast_PushbulletSettings",
        ) -> "_1602.PersistentSingleton":
            from mastapy.utility import _1602

            return self._parent._cast(_1602.PersistentSingleton)

        @property
        def pushbullet_settings(
            self: "PushbulletSettings._Cast_PushbulletSettings",
        ) -> "PushbulletSettings":
            return self._parent

        def __getattr__(self: "PushbulletSettings._Cast_PushbulletSettings", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PushbulletSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def enable_pushbullet(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.EnablePushbullet

        if temp is None:
            return False

        return temp

    @enable_pushbullet.setter
    @enforce_parameter_types
    def enable_pushbullet(self: Self, value: "bool"):
        self.wrapped.EnablePushbullet = bool(value) if value is not None else False

    @property
    def pushbullet_token(self: Self) -> "str":
        """str"""
        temp = self.wrapped.PushbulletToken

        if temp is None:
            return ""

        return temp

    @pushbullet_token.setter
    @enforce_parameter_types
    def pushbullet_token(self: Self, value: "str"):
        self.wrapped.PushbulletToken = str(value) if value is not None else ""

    @property
    def send_progress_screenshot_interval_minutes(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.SendProgressScreenshotIntervalMinutes

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @send_progress_screenshot_interval_minutes.setter
    @enforce_parameter_types
    def send_progress_screenshot_interval_minutes(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.SendProgressScreenshotIntervalMinutes = value

    def generate_pushbullet_token(self: Self):
        """Method does not return."""
        self.wrapped.GeneratePushbulletToken()

    @property
    def cast_to(self: Self) -> "PushbulletSettings._Cast_PushbulletSettings":
        return self._Cast_PushbulletSettings(self)
