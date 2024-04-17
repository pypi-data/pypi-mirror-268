"""NodalComposite"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _147
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODAL_COMPOSITE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "NodalComposite"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import (
        _130,
        _131,
        _132,
        _136,
        _137,
        _140,
        _142,
        _143,
        _150,
        _152,
        _153,
        _154,
    )


__docformat__ = "restructuredtext en"
__all__ = ("NodalComposite",)


Self = TypeVar("Self", bound="NodalComposite")


class NodalComposite(_147.NodalEntity):
    """NodalComposite

    This is a mastapy class.
    """

    TYPE = _NODAL_COMPOSITE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NodalComposite")

    class _Cast_NodalComposite:
        """Special nested class for casting NodalComposite to subclasses."""

        def __init__(
            self: "NodalComposite._Cast_NodalComposite", parent: "NodalComposite"
        ):
            self._parent = parent

        @property
        def nodal_entity(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "_147.NodalEntity":
            return self._parent._cast(_147.NodalEntity)

        @property
        def bar_elastic_mbd(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "_130.BarElasticMBD":
            from mastapy.nodal_analysis.nodal_entities import _130

            return self._parent._cast(_130.BarElasticMBD)

        @property
        def bar_mbd(self: "NodalComposite._Cast_NodalComposite") -> "_131.BarMBD":
            from mastapy.nodal_analysis.nodal_entities import _131

            return self._parent._cast(_131.BarMBD)

        @property
        def bar_rigid_mbd(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "_132.BarRigidMBD":
            from mastapy.nodal_analysis.nodal_entities import _132

            return self._parent._cast(_132.BarRigidMBD)

        @property
        def component_nodal_composite(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "_136.ComponentNodalComposite":
            from mastapy.nodal_analysis.nodal_entities import _136

            return self._parent._cast(_136.ComponentNodalComposite)

        @property
        def concentric_connection_nodal_component(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "_137.ConcentricConnectionNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _137

            return self._parent._cast(_137.ConcentricConnectionNodalComponent)

        @property
        def gear_mesh_nodal_component(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "_140.GearMeshNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _140

            return self._parent._cast(_140.GearMeshNodalComponent)

        @property
        def gear_mesh_point_on_flank_contact(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "_142.GearMeshPointOnFlankContact":
            from mastapy.nodal_analysis.nodal_entities import _142

            return self._parent._cast(_142.GearMeshPointOnFlankContact)

        @property
        def gear_mesh_single_flank_contact(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "_143.GearMeshSingleFlankContact":
            from mastapy.nodal_analysis.nodal_entities import _143

            return self._parent._cast(_143.GearMeshSingleFlankContact)

        @property
        def simple_bar(self: "NodalComposite._Cast_NodalComposite") -> "_150.SimpleBar":
            from mastapy.nodal_analysis.nodal_entities import _150

            return self._parent._cast(_150.SimpleBar)

        @property
        def torsional_friction_node_pair(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "_152.TorsionalFrictionNodePair":
            from mastapy.nodal_analysis.nodal_entities import _152

            return self._parent._cast(_152.TorsionalFrictionNodePair)

        @property
        def torsional_friction_node_pair_simple_locked_stiffness(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "_153.TorsionalFrictionNodePairSimpleLockedStiffness":
            from mastapy.nodal_analysis.nodal_entities import _153

            return self._parent._cast(
                _153.TorsionalFrictionNodePairSimpleLockedStiffness
            )

        @property
        def two_body_connection_nodal_component(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "_154.TwoBodyConnectionNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _154

            return self._parent._cast(_154.TwoBodyConnectionNodalComponent)

        @property
        def nodal_composite(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "NodalComposite":
            return self._parent

        def __getattr__(self: "NodalComposite._Cast_NodalComposite", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NodalComposite.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "NodalComposite._Cast_NodalComposite":
        return self._Cast_NodalComposite(self)
