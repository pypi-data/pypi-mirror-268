"""ActiveFESubstructureSelectionGroup"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.part_model.configurations import _2625
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ACTIVE_FE_SUBSTRUCTURE_SELECTION_GROUP = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Configurations",
    "ActiveFESubstructureSelectionGroup",
)


__docformat__ = "restructuredtext en"
__all__ = ("ActiveFESubstructureSelectionGroup",)


Self = TypeVar("Self", bound="ActiveFESubstructureSelectionGroup")


class ActiveFESubstructureSelectionGroup(
    _2625.PartDetailConfiguration[
        "_2619.ActiveFESubstructureSelection", "_2460.FEPart", "_2390.FESubstructure"
    ]
):
    """ActiveFESubstructureSelectionGroup

    This is a mastapy class.
    """

    TYPE = _ACTIVE_FE_SUBSTRUCTURE_SELECTION_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ActiveFESubstructureSelectionGroup")

    class _Cast_ActiveFESubstructureSelectionGroup:
        """Special nested class for casting ActiveFESubstructureSelectionGroup to subclasses."""

        def __init__(
            self: "ActiveFESubstructureSelectionGroup._Cast_ActiveFESubstructureSelectionGroup",
            parent: "ActiveFESubstructureSelectionGroup",
        ):
            self._parent = parent

        @property
        def part_detail_configuration(
            self: "ActiveFESubstructureSelectionGroup._Cast_ActiveFESubstructureSelectionGroup",
        ) -> "_2625.PartDetailConfiguration":
            return self._parent._cast(_2625.PartDetailConfiguration)

        @property
        def active_fe_substructure_selection_group(
            self: "ActiveFESubstructureSelectionGroup._Cast_ActiveFESubstructureSelectionGroup",
        ) -> "ActiveFESubstructureSelectionGroup":
            return self._parent

        def __getattr__(
            self: "ActiveFESubstructureSelectionGroup._Cast_ActiveFESubstructureSelectionGroup",
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
        self: Self, instance_to_wrap: "ActiveFESubstructureSelectionGroup.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ActiveFESubstructureSelectionGroup._Cast_ActiveFESubstructureSelectionGroup":
        return self._Cast_ActiveFESubstructureSelectionGroup(self)
