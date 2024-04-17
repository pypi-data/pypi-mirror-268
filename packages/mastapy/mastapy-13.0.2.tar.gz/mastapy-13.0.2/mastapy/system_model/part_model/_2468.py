"""LoadSharingSettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOAD_SHARING_SETTINGS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "LoadSharingSettings"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2467, _2444


__docformat__ = "restructuredtext en"
__all__ = ("LoadSharingSettings",)


Self = TypeVar("Self", bound="LoadSharingSettings")


class LoadSharingSettings(_0.APIBase):
    """LoadSharingSettings

    This is a mastapy class.
    """

    TYPE = _LOAD_SHARING_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadSharingSettings")

    class _Cast_LoadSharingSettings:
        """Special nested class for casting LoadSharingSettings to subclasses."""

        def __init__(
            self: "LoadSharingSettings._Cast_LoadSharingSettings",
            parent: "LoadSharingSettings",
        ):
            self._parent = parent

        @property
        def load_sharing_settings(
            self: "LoadSharingSettings._Cast_LoadSharingSettings",
        ) -> "LoadSharingSettings":
            return self._parent

        def __getattr__(
            self: "LoadSharingSettings._Cast_LoadSharingSettings", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadSharingSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetary_load_sharing(self: Self) -> "_2467.LoadSharingModes":
        """mastapy.system_model.part_model.LoadSharingModes"""
        temp = self.wrapped.PlanetaryLoadSharing

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.PartModel.LoadSharingModes"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.part_model._2467", "LoadSharingModes"
        )(value)

    @planetary_load_sharing.setter
    @enforce_parameter_types
    def planetary_load_sharing(self: Self, value: "_2467.LoadSharingModes"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.PartModel.LoadSharingModes"
        )
        self.wrapped.PlanetaryLoadSharing = value

    @property
    def planetary_load_sharing_agma_application_level(
        self: Self,
    ) -> "_2444.AGMALoadSharingTableApplicationLevel":
        """mastapy.system_model.part_model.AGMALoadSharingTableApplicationLevel"""
        temp = self.wrapped.PlanetaryLoadSharingAGMAApplicationLevel

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.PartModel.AGMALoadSharingTableApplicationLevel",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.part_model._2444",
            "AGMALoadSharingTableApplicationLevel",
        )(value)

    @planetary_load_sharing_agma_application_level.setter
    @enforce_parameter_types
    def planetary_load_sharing_agma_application_level(
        self: Self, value: "_2444.AGMALoadSharingTableApplicationLevel"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.PartModel.AGMALoadSharingTableApplicationLevel",
        )
        self.wrapped.PlanetaryLoadSharingAGMAApplicationLevel = value

    @property
    def cast_to(self: Self) -> "LoadSharingSettings._Cast_LoadSharingSettings":
        return self._Cast_LoadSharingSettings(self)
