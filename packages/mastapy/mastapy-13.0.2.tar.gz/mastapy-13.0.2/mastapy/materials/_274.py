"""MaterialsSettings"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MATERIALS_SETTINGS = python_net_import("SMT.MastaAPI.Materials", "MaterialsSettings")


__docformat__ = "restructuredtext en"
__all__ = ("MaterialsSettings",)


Self = TypeVar("Self", bound="MaterialsSettings")


class MaterialsSettings(_0.APIBase):
    """MaterialsSettings

    This is a mastapy class.
    """

    TYPE = _MATERIALS_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MaterialsSettings")

    class _Cast_MaterialsSettings:
        """Special nested class for casting MaterialsSettings to subclasses."""

        def __init__(
            self: "MaterialsSettings._Cast_MaterialsSettings",
            parent: "MaterialsSettings",
        ):
            self._parent = parent

        @property
        def materials_settings(
            self: "MaterialsSettings._Cast_MaterialsSettings",
        ) -> "MaterialsSettings":
            return self._parent

        def __getattr__(self: "MaterialsSettings._Cast_MaterialsSettings", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MaterialsSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "MaterialsSettings._Cast_MaterialsSettings":
        return self._Cast_MaterialsSettings(self)
