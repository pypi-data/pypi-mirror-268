"""IWrapSMTType"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.python_net import python_net_import

_I_WRAP_SMT_TYPE = python_net_import("SMT.MastaAPIUtility.Scripting", "IWrapSMTType")


__docformat__ = "restructuredtext en"
__all__ = ("IWrapSMTType",)


Self = TypeVar("Self", bound="IWrapSMTType")


class IWrapSMTType:
    """This class is a public interface.
    The class body has intentionally been left empty.
    """
