"""ElementFaceGroup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.dev_tools_analyses import _185
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_FACE_GROUP = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses", "ElementFaceGroup"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.component_mode_synthesis import _227, _228


__docformat__ = "restructuredtext en"
__all__ = ("ElementFaceGroup",)


Self = TypeVar("Self", bound="ElementFaceGroup")


class ElementFaceGroup(_185.FEEntityGroup["_1239.ElementFace"]):
    """ElementFaceGroup

    This is a mastapy class.
    """

    TYPE = _ELEMENT_FACE_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElementFaceGroup")

    class _Cast_ElementFaceGroup:
        """Special nested class for casting ElementFaceGroup to subclasses."""

        def __init__(
            self: "ElementFaceGroup._Cast_ElementFaceGroup", parent: "ElementFaceGroup"
        ):
            self._parent = parent

        @property
        def fe_entity_group(
            self: "ElementFaceGroup._Cast_ElementFaceGroup",
        ) -> "_185.FEEntityGroup":
            return self._parent._cast(_185.FEEntityGroup)

        @property
        def cms_element_face_group(
            self: "ElementFaceGroup._Cast_ElementFaceGroup",
        ) -> "_227.CMSElementFaceGroup":
            from mastapy.nodal_analysis.component_mode_synthesis import _227

            return self._parent._cast(_227.CMSElementFaceGroup)

        @property
        def cms_element_face_group_of_all_free_faces(
            self: "ElementFaceGroup._Cast_ElementFaceGroup",
        ) -> "_228.CMSElementFaceGroupOfAllFreeFaces":
            from mastapy.nodal_analysis.component_mode_synthesis import _228

            return self._parent._cast(_228.CMSElementFaceGroupOfAllFreeFaces)

        @property
        def element_face_group(
            self: "ElementFaceGroup._Cast_ElementFaceGroup",
        ) -> "ElementFaceGroup":
            return self._parent

        def __getattr__(self: "ElementFaceGroup._Cast_ElementFaceGroup", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElementFaceGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ElementFaceGroup._Cast_ElementFaceGroup":
        return self._Cast_ElementFaceGroup(self)
