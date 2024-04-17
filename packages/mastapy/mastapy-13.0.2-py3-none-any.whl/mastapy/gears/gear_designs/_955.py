"""SelectedDesignConstraintsCollection"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SELECTED_DESIGN_CONSTRAINTS_COLLECTION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns", "SelectedDesignConstraintsCollection"
)


__docformat__ = "restructuredtext en"
__all__ = ("SelectedDesignConstraintsCollection",)


Self = TypeVar("Self", bound="SelectedDesignConstraintsCollection")


class SelectedDesignConstraintsCollection(_0.APIBase):
    """SelectedDesignConstraintsCollection

    This is a mastapy class.
    """

    TYPE = _SELECTED_DESIGN_CONSTRAINTS_COLLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SelectedDesignConstraintsCollection")

    class _Cast_SelectedDesignConstraintsCollection:
        """Special nested class for casting SelectedDesignConstraintsCollection to subclasses."""

        def __init__(
            self: "SelectedDesignConstraintsCollection._Cast_SelectedDesignConstraintsCollection",
            parent: "SelectedDesignConstraintsCollection",
        ):
            self._parent = parent

        @property
        def selected_design_constraints_collection(
            self: "SelectedDesignConstraintsCollection._Cast_SelectedDesignConstraintsCollection",
        ) -> "SelectedDesignConstraintsCollection":
            return self._parent

        def __getattr__(
            self: "SelectedDesignConstraintsCollection._Cast_SelectedDesignConstraintsCollection",
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
        self: Self, instance_to_wrap: "SelectedDesignConstraintsCollection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "SelectedDesignConstraintsCollection._Cast_SelectedDesignConstraintsCollection"
    ):
        return self._Cast_SelectedDesignConstraintsCollection(self)
