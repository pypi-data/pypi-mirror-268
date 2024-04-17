"""DesignEntityExcitationDescription"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_ENTITY_EXCITATION_DESCRIPTION = python_net_import(
    "SMT.MastaAPI.Utility.ModalAnalysis", "DesignEntityExcitationDescription"
)


__docformat__ = "restructuredtext en"
__all__ = ("DesignEntityExcitationDescription",)


Self = TypeVar("Self", bound="DesignEntityExcitationDescription")


class DesignEntityExcitationDescription(_0.APIBase):
    """DesignEntityExcitationDescription

    This is a mastapy class.
    """

    TYPE = _DESIGN_ENTITY_EXCITATION_DESCRIPTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DesignEntityExcitationDescription")

    class _Cast_DesignEntityExcitationDescription:
        """Special nested class for casting DesignEntityExcitationDescription to subclasses."""

        def __init__(
            self: "DesignEntityExcitationDescription._Cast_DesignEntityExcitationDescription",
            parent: "DesignEntityExcitationDescription",
        ):
            self._parent = parent

        @property
        def design_entity_excitation_description(
            self: "DesignEntityExcitationDescription._Cast_DesignEntityExcitationDescription",
        ) -> "DesignEntityExcitationDescription":
            return self._parent

        def __getattr__(
            self: "DesignEntityExcitationDescription._Cast_DesignEntityExcitationDescription",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "DesignEntityExcitationDescription.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitation_frequency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcitationFrequency

        if temp is None:
            return 0.0

        return temp

    @property
    def harmonic_index(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicIndex

        if temp is None:
            return 0

        return temp

    @property
    def order(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Order

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "DesignEntityExcitationDescription._Cast_DesignEntityExcitationDescription":
        return self._Cast_DesignEntityExcitationDescription(self)
