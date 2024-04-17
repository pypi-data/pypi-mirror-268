"""ElementFaceGroupWithSelection"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.fe import _2384
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_FACE_GROUP_WITH_SELECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "ElementFaceGroupWithSelection"
)


__docformat__ = "restructuredtext en"
__all__ = ("ElementFaceGroupWithSelection",)


Self = TypeVar("Self", bound="ElementFaceGroupWithSelection")


class ElementFaceGroupWithSelection(
    _2384.FEEntityGroupWithSelection["_227.CMSElementFaceGroup", "_1239.ElementFace"]
):
    """ElementFaceGroupWithSelection

    This is a mastapy class.
    """

    TYPE = _ELEMENT_FACE_GROUP_WITH_SELECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElementFaceGroupWithSelection")

    class _Cast_ElementFaceGroupWithSelection:
        """Special nested class for casting ElementFaceGroupWithSelection to subclasses."""

        def __init__(
            self: "ElementFaceGroupWithSelection._Cast_ElementFaceGroupWithSelection",
            parent: "ElementFaceGroupWithSelection",
        ):
            self._parent = parent

        @property
        def fe_entity_group_with_selection(
            self: "ElementFaceGroupWithSelection._Cast_ElementFaceGroupWithSelection",
        ) -> "_2384.FEEntityGroupWithSelection":
            return self._parent._cast(_2384.FEEntityGroupWithSelection)

        @property
        def element_face_group_with_selection(
            self: "ElementFaceGroupWithSelection._Cast_ElementFaceGroupWithSelection",
        ) -> "ElementFaceGroupWithSelection":
            return self._parent

        def __getattr__(
            self: "ElementFaceGroupWithSelection._Cast_ElementFaceGroupWithSelection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElementFaceGroupWithSelection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElementFaceGroupWithSelection._Cast_ElementFaceGroupWithSelection":
        return self._Cast_ElementFaceGroupWithSelection(self)
