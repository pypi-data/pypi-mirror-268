"""ActiveShaftDesignSelectionGroup"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.part_model.configurations import _2625
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ACTIVE_SHAFT_DESIGN_SELECTION_GROUP = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Configurations",
    "ActiveShaftDesignSelectionGroup",
)


__docformat__ = "restructuredtext en"
__all__ = ("ActiveShaftDesignSelectionGroup",)


Self = TypeVar("Self", bound="ActiveShaftDesignSelectionGroup")


class ActiveShaftDesignSelectionGroup(
    _2625.PartDetailConfiguration[
        "_2621.ActiveShaftDesignSelection", "_2489.Shaft", "_43.SimpleShaftDefinition"
    ]
):
    """ActiveShaftDesignSelectionGroup

    This is a mastapy class.
    """

    TYPE = _ACTIVE_SHAFT_DESIGN_SELECTION_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ActiveShaftDesignSelectionGroup")

    class _Cast_ActiveShaftDesignSelectionGroup:
        """Special nested class for casting ActiveShaftDesignSelectionGroup to subclasses."""

        def __init__(
            self: "ActiveShaftDesignSelectionGroup._Cast_ActiveShaftDesignSelectionGroup",
            parent: "ActiveShaftDesignSelectionGroup",
        ):
            self._parent = parent

        @property
        def part_detail_configuration(
            self: "ActiveShaftDesignSelectionGroup._Cast_ActiveShaftDesignSelectionGroup",
        ) -> "_2625.PartDetailConfiguration":
            return self._parent._cast(_2625.PartDetailConfiguration)

        @property
        def active_shaft_design_selection_group(
            self: "ActiveShaftDesignSelectionGroup._Cast_ActiveShaftDesignSelectionGroup",
        ) -> "ActiveShaftDesignSelectionGroup":
            return self._parent

        def __getattr__(
            self: "ActiveShaftDesignSelectionGroup._Cast_ActiveShaftDesignSelectionGroup",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ActiveShaftDesignSelectionGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ActiveShaftDesignSelectionGroup._Cast_ActiveShaftDesignSelectionGroup":
        return self._Cast_ActiveShaftDesignSelectionGroup(self)
