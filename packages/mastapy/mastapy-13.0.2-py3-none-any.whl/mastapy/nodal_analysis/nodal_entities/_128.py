"""ArbitraryNodalComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _145
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ARBITRARY_NODAL_COMPONENT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "ArbitraryNodalComponent"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import _134, _135, _141, _144, _151, _147


__docformat__ = "restructuredtext en"
__all__ = ("ArbitraryNodalComponent",)


Self = TypeVar("Self", bound="ArbitraryNodalComponent")


class ArbitraryNodalComponent(_145.NodalComponent):
    """ArbitraryNodalComponent

    This is a mastapy class.
    """

    TYPE = _ARBITRARY_NODAL_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ArbitraryNodalComponent")

    class _Cast_ArbitraryNodalComponent:
        """Special nested class for casting ArbitraryNodalComponent to subclasses."""

        def __init__(
            self: "ArbitraryNodalComponent._Cast_ArbitraryNodalComponent",
            parent: "ArbitraryNodalComponent",
        ):
            self._parent = parent

        @property
        def nodal_component(
            self: "ArbitraryNodalComponent._Cast_ArbitraryNodalComponent",
        ) -> "_145.NodalComponent":
            return self._parent._cast(_145.NodalComponent)

        @property
        def nodal_entity(
            self: "ArbitraryNodalComponent._Cast_ArbitraryNodalComponent",
        ) -> "_147.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _147

            return self._parent._cast(_147.NodalEntity)

        @property
        def bearing_axial_mounting_clearance(
            self: "ArbitraryNodalComponent._Cast_ArbitraryNodalComponent",
        ) -> "_134.BearingAxialMountingClearance":
            from mastapy.nodal_analysis.nodal_entities import _134

            return self._parent._cast(_134.BearingAxialMountingClearance)

        @property
        def cms_nodal_component(
            self: "ArbitraryNodalComponent._Cast_ArbitraryNodalComponent",
        ) -> "_135.CMSNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _135

            return self._parent._cast(_135.CMSNodalComponent)

        @property
        def gear_mesh_node_pair(
            self: "ArbitraryNodalComponent._Cast_ArbitraryNodalComponent",
        ) -> "_141.GearMeshNodePair":
            from mastapy.nodal_analysis.nodal_entities import _141

            return self._parent._cast(_141.GearMeshNodePair)

        @property
        def line_contact_stiffness_entity(
            self: "ArbitraryNodalComponent._Cast_ArbitraryNodalComponent",
        ) -> "_144.LineContactStiffnessEntity":
            from mastapy.nodal_analysis.nodal_entities import _144

            return self._parent._cast(_144.LineContactStiffnessEntity)

        @property
        def surface_to_surface_contact_stiffness_entity(
            self: "ArbitraryNodalComponent._Cast_ArbitraryNodalComponent",
        ) -> "_151.SurfaceToSurfaceContactStiffnessEntity":
            from mastapy.nodal_analysis.nodal_entities import _151

            return self._parent._cast(_151.SurfaceToSurfaceContactStiffnessEntity)

        @property
        def arbitrary_nodal_component(
            self: "ArbitraryNodalComponent._Cast_ArbitraryNodalComponent",
        ) -> "ArbitraryNodalComponent":
            return self._parent

        def __getattr__(
            self: "ArbitraryNodalComponent._Cast_ArbitraryNodalComponent", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ArbitraryNodalComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ArbitraryNodalComponent._Cast_ArbitraryNodalComponent":
        return self._Cast_ArbitraryNodalComponent(self)
