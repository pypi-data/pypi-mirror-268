"""ActiveGearSetDesignSelection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.configurations import _2626
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ACTIVE_GEAR_SET_DESIGN_SELECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ActiveGearSetDesignSelection"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2517


__docformat__ = "restructuredtext en"
__all__ = ("ActiveGearSetDesignSelection",)


Self = TypeVar("Self", bound="ActiveGearSetDesignSelection")


class ActiveGearSetDesignSelection(
    _2626.PartDetailSelection["_2539.GearSet", "_954.GearSetDesign"]
):
    """ActiveGearSetDesignSelection

    This is a mastapy class.
    """

    TYPE = _ACTIVE_GEAR_SET_DESIGN_SELECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ActiveGearSetDesignSelection")

    class _Cast_ActiveGearSetDesignSelection:
        """Special nested class for casting ActiveGearSetDesignSelection to subclasses."""

        def __init__(
            self: "ActiveGearSetDesignSelection._Cast_ActiveGearSetDesignSelection",
            parent: "ActiveGearSetDesignSelection",
        ):
            self._parent = parent

        @property
        def part_detail_selection(
            self: "ActiveGearSetDesignSelection._Cast_ActiveGearSetDesignSelection",
        ) -> "_2626.PartDetailSelection":
            return self._parent._cast(_2626.PartDetailSelection)

        @property
        def active_cylindrical_gear_set_design_selection(
            self: "ActiveGearSetDesignSelection._Cast_ActiveGearSetDesignSelection",
        ) -> "_2517.ActiveCylindricalGearSetDesignSelection":
            from mastapy.system_model.part_model.gears import _2517

            return self._parent._cast(_2517.ActiveCylindricalGearSetDesignSelection)

        @property
        def active_gear_set_design_selection(
            self: "ActiveGearSetDesignSelection._Cast_ActiveGearSetDesignSelection",
        ) -> "ActiveGearSetDesignSelection":
            return self._parent

        def __getattr__(
            self: "ActiveGearSetDesignSelection._Cast_ActiveGearSetDesignSelection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ActiveGearSetDesignSelection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ActiveGearSetDesignSelection._Cast_ActiveGearSetDesignSelection":
        return self._Cast_ActiveGearSetDesignSelection(self)
