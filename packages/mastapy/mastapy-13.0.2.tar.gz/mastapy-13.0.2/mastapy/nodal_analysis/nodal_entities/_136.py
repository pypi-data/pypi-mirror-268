"""ComponentNodalComposite"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _146
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_NODAL_COMPOSITE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "ComponentNodalComposite"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import (
        _130,
        _131,
        _132,
        _137,
        _142,
        _150,
        _152,
        _153,
        _154,
        _147,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ComponentNodalComposite",)


Self = TypeVar("Self", bound="ComponentNodalComposite")


class ComponentNodalComposite(_146.NodalComposite):
    """ComponentNodalComposite

    This is a mastapy class.
    """

    TYPE = _COMPONENT_NODAL_COMPOSITE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentNodalComposite")

    class _Cast_ComponentNodalComposite:
        """Special nested class for casting ComponentNodalComposite to subclasses."""

        def __init__(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
            parent: "ComponentNodalComposite",
        ):
            self._parent = parent

        @property
        def nodal_composite(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "_146.NodalComposite":
            return self._parent._cast(_146.NodalComposite)

        @property
        def nodal_entity(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "_147.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _147

            return self._parent._cast(_147.NodalEntity)

        @property
        def bar_elastic_mbd(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "_130.BarElasticMBD":
            from mastapy.nodal_analysis.nodal_entities import _130

            return self._parent._cast(_130.BarElasticMBD)

        @property
        def bar_mbd(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "_131.BarMBD":
            from mastapy.nodal_analysis.nodal_entities import _131

            return self._parent._cast(_131.BarMBD)

        @property
        def bar_rigid_mbd(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "_132.BarRigidMBD":
            from mastapy.nodal_analysis.nodal_entities import _132

            return self._parent._cast(_132.BarRigidMBD)

        @property
        def concentric_connection_nodal_component(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "_137.ConcentricConnectionNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _137

            return self._parent._cast(_137.ConcentricConnectionNodalComponent)

        @property
        def gear_mesh_point_on_flank_contact(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "_142.GearMeshPointOnFlankContact":
            from mastapy.nodal_analysis.nodal_entities import _142

            return self._parent._cast(_142.GearMeshPointOnFlankContact)

        @property
        def simple_bar(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "_150.SimpleBar":
            from mastapy.nodal_analysis.nodal_entities import _150

            return self._parent._cast(_150.SimpleBar)

        @property
        def torsional_friction_node_pair(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "_152.TorsionalFrictionNodePair":
            from mastapy.nodal_analysis.nodal_entities import _152

            return self._parent._cast(_152.TorsionalFrictionNodePair)

        @property
        def torsional_friction_node_pair_simple_locked_stiffness(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "_153.TorsionalFrictionNodePairSimpleLockedStiffness":
            from mastapy.nodal_analysis.nodal_entities import _153

            return self._parent._cast(
                _153.TorsionalFrictionNodePairSimpleLockedStiffness
            )

        @property
        def two_body_connection_nodal_component(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "_154.TwoBodyConnectionNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _154

            return self._parent._cast(_154.TwoBodyConnectionNodalComponent)

        @property
        def component_nodal_composite(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "ComponentNodalComposite":
            return self._parent

        def __getattr__(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentNodalComposite.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ComponentNodalComposite._Cast_ComponentNodalComposite":
        return self._Cast_ComponentNodalComposite(self)
