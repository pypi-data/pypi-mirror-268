"""IHaveAllSettings"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.python_net import python_net_import

_I_HAVE_ALL_SETTINGS = python_net_import("SMT.MastaAPI.Utility", "IHaveAllSettings")


__docformat__ = "restructuredtext en"
__all__ = ("IHaveAllSettings",)


Self = TypeVar("Self", bound="IHaveAllSettings")


class IHaveAllSettings:
    """This class is a public interface.
    The class body has intentionally been left empty.
    """
