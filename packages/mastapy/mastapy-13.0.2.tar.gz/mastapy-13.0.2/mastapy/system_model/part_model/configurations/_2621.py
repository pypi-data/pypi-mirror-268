"""ActiveShaftDesignSelection"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.part_model.configurations import _2626
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ACTIVE_SHAFT_DESIGN_SELECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Configurations", "ActiveShaftDesignSelection"
)


__docformat__ = "restructuredtext en"
__all__ = ("ActiveShaftDesignSelection",)


Self = TypeVar("Self", bound="ActiveShaftDesignSelection")


class ActiveShaftDesignSelection(
    _2626.PartDetailSelection["_2489.Shaft", "_43.SimpleShaftDefinition"]
):
    """ActiveShaftDesignSelection

    This is a mastapy class.
    """

    TYPE = _ACTIVE_SHAFT_DESIGN_SELECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ActiveShaftDesignSelection")

    class _Cast_ActiveShaftDesignSelection:
        """Special nested class for casting ActiveShaftDesignSelection to subclasses."""

        def __init__(
            self: "ActiveShaftDesignSelection._Cast_ActiveShaftDesignSelection",
            parent: "ActiveShaftDesignSelection",
        ):
            self._parent = parent

        @property
        def part_detail_selection(
            self: "ActiveShaftDesignSelection._Cast_ActiveShaftDesignSelection",
        ) -> "_2626.PartDetailSelection":
            return self._parent._cast(_2626.PartDetailSelection)

        @property
        def active_shaft_design_selection(
            self: "ActiveShaftDesignSelection._Cast_ActiveShaftDesignSelection",
        ) -> "ActiveShaftDesignSelection":
            return self._parent

        def __getattr__(
            self: "ActiveShaftDesignSelection._Cast_ActiveShaftDesignSelection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ActiveShaftDesignSelection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ActiveShaftDesignSelection._Cast_ActiveShaftDesignSelection":
        return self._Cast_ActiveShaftDesignSelection(self)
