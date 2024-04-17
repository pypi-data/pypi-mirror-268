"""GearWithDuplicatedMeshesFELink"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.fe.links import _2434
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_WITH_DUPLICATED_MESHES_FE_LINK = python_net_import(
    "SMT.MastaAPI.SystemModel.FE.Links", "GearWithDuplicatedMeshesFELink"
)

if TYPE_CHECKING:
    from mastapy.system_model.fe.links import _2432, _2425


__docformat__ = "restructuredtext en"
__all__ = ("GearWithDuplicatedMeshesFELink",)


Self = TypeVar("Self", bound="GearWithDuplicatedMeshesFELink")


class GearWithDuplicatedMeshesFELink(_2434.PlanetBasedFELink):
    """GearWithDuplicatedMeshesFELink

    This is a mastapy class.
    """

    TYPE = _GEAR_WITH_DUPLICATED_MESHES_FE_LINK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearWithDuplicatedMeshesFELink")

    class _Cast_GearWithDuplicatedMeshesFELink:
        """Special nested class for casting GearWithDuplicatedMeshesFELink to subclasses."""

        def __init__(
            self: "GearWithDuplicatedMeshesFELink._Cast_GearWithDuplicatedMeshesFELink",
            parent: "GearWithDuplicatedMeshesFELink",
        ):
            self._parent = parent

        @property
        def planet_based_fe_link(
            self: "GearWithDuplicatedMeshesFELink._Cast_GearWithDuplicatedMeshesFELink",
        ) -> "_2434.PlanetBasedFELink":
            return self._parent._cast(_2434.PlanetBasedFELink)

        @property
        def multi_node_fe_link(
            self: "GearWithDuplicatedMeshesFELink._Cast_GearWithDuplicatedMeshesFELink",
        ) -> "_2432.MultiNodeFELink":
            from mastapy.system_model.fe.links import _2432

            return self._parent._cast(_2432.MultiNodeFELink)

        @property
        def fe_link(
            self: "GearWithDuplicatedMeshesFELink._Cast_GearWithDuplicatedMeshesFELink",
        ) -> "_2425.FELink":
            from mastapy.system_model.fe.links import _2425

            return self._parent._cast(_2425.FELink)

        @property
        def gear_with_duplicated_meshes_fe_link(
            self: "GearWithDuplicatedMeshesFELink._Cast_GearWithDuplicatedMeshesFELink",
        ) -> "GearWithDuplicatedMeshesFELink":
            return self._parent

        def __getattr__(
            self: "GearWithDuplicatedMeshesFELink._Cast_GearWithDuplicatedMeshesFELink",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearWithDuplicatedMeshesFELink.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GearWithDuplicatedMeshesFELink._Cast_GearWithDuplicatedMeshesFELink":
        return self._Cast_GearWithDuplicatedMeshesFELink(self)
