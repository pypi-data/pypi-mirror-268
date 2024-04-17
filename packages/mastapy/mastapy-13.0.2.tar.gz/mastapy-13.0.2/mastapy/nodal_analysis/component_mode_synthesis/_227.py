"""CMSElementFaceGroup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.dev_tools_analyses import _183
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CMS_ELEMENT_FACE_GROUP = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis", "CMSElementFaceGroup"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.component_mode_synthesis import _228
    from mastapy.nodal_analysis.dev_tools_analyses import _185


__docformat__ = "restructuredtext en"
__all__ = ("CMSElementFaceGroup",)


Self = TypeVar("Self", bound="CMSElementFaceGroup")


class CMSElementFaceGroup(_183.ElementFaceGroup):
    """CMSElementFaceGroup

    This is a mastapy class.
    """

    TYPE = _CMS_ELEMENT_FACE_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CMSElementFaceGroup")

    class _Cast_CMSElementFaceGroup:
        """Special nested class for casting CMSElementFaceGroup to subclasses."""

        def __init__(
            self: "CMSElementFaceGroup._Cast_CMSElementFaceGroup",
            parent: "CMSElementFaceGroup",
        ):
            self._parent = parent

        @property
        def element_face_group(
            self: "CMSElementFaceGroup._Cast_CMSElementFaceGroup",
        ) -> "_183.ElementFaceGroup":
            return self._parent._cast(_183.ElementFaceGroup)

        @property
        def fe_entity_group(
            self: "CMSElementFaceGroup._Cast_CMSElementFaceGroup",
        ) -> "_185.FEEntityGroup":
            pass

            from mastapy.nodal_analysis.dev_tools_analyses import _185

            return self._parent._cast(_185.FEEntityGroup)

        @property
        def cms_element_face_group_of_all_free_faces(
            self: "CMSElementFaceGroup._Cast_CMSElementFaceGroup",
        ) -> "_228.CMSElementFaceGroupOfAllFreeFaces":
            from mastapy.nodal_analysis.component_mode_synthesis import _228

            return self._parent._cast(_228.CMSElementFaceGroupOfAllFreeFaces)

        @property
        def cms_element_face_group(
            self: "CMSElementFaceGroup._Cast_CMSElementFaceGroup",
        ) -> "CMSElementFaceGroup":
            return self._parent

        def __getattr__(
            self: "CMSElementFaceGroup._Cast_CMSElementFaceGroup", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CMSElementFaceGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def area(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Area

        if temp is None:
            return 0.0

        return temp

    def create_node_group(self: Self):
        """Method does not return."""
        self.wrapped.CreateNodeGroup()

    def populate_rms_values_cache(self: Self):
        """Method does not return."""
        self.wrapped.PopulateRMSValuesCache()

    @property
    def cast_to(self: Self) -> "CMSElementFaceGroup._Cast_CMSElementFaceGroup":
        return self._Cast_CMSElementFaceGroup(self)
