"""ActiveFESubstructureSelection"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.part_model.configurations import _2626
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ACTIVE_FE_SUBSTRUCTURE_SELECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Configurations", "ActiveFESubstructureSelection"
)


__docformat__ = "restructuredtext en"
__all__ = ("ActiveFESubstructureSelection",)


Self = TypeVar("Self", bound="ActiveFESubstructureSelection")


class ActiveFESubstructureSelection(
    _2626.PartDetailSelection["_2460.FEPart", "_2390.FESubstructure"]
):
    """ActiveFESubstructureSelection

    This is a mastapy class.
    """

    TYPE = _ACTIVE_FE_SUBSTRUCTURE_SELECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ActiveFESubstructureSelection")

    class _Cast_ActiveFESubstructureSelection:
        """Special nested class for casting ActiveFESubstructureSelection to subclasses."""

        def __init__(
            self: "ActiveFESubstructureSelection._Cast_ActiveFESubstructureSelection",
            parent: "ActiveFESubstructureSelection",
        ):
            self._parent = parent

        @property
        def part_detail_selection(
            self: "ActiveFESubstructureSelection._Cast_ActiveFESubstructureSelection",
        ) -> "_2626.PartDetailSelection":
            return self._parent._cast(_2626.PartDetailSelection)

        @property
        def active_fe_substructure_selection(
            self: "ActiveFESubstructureSelection._Cast_ActiveFESubstructureSelection",
        ) -> "ActiveFESubstructureSelection":
            return self._parent

        def __getattr__(
            self: "ActiveFESubstructureSelection._Cast_ActiveFESubstructureSelection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ActiveFESubstructureSelection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ActiveFESubstructureSelection._Cast_ActiveFESubstructureSelection":
        return self._Cast_ActiveFESubstructureSelection(self)
