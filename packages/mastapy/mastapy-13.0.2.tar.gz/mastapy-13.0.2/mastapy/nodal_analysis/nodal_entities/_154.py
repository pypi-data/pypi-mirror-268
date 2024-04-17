"""TwoBodyConnectionNodalComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _136
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TWO_BODY_CONNECTION_NODAL_COMPONENT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "TwoBodyConnectionNodalComponent"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import (
        _137,
        _142,
        _150,
        _152,
        _153,
        _146,
        _147,
    )


__docformat__ = "restructuredtext en"
__all__ = ("TwoBodyConnectionNodalComponent",)


Self = TypeVar("Self", bound="TwoBodyConnectionNodalComponent")


class TwoBodyConnectionNodalComponent(_136.ComponentNodalComposite):
    """TwoBodyConnectionNodalComponent

    This is a mastapy class.
    """

    TYPE = _TWO_BODY_CONNECTION_NODAL_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TwoBodyConnectionNodalComponent")

    class _Cast_TwoBodyConnectionNodalComponent:
        """Special nested class for casting TwoBodyConnectionNodalComponent to subclasses."""

        def __init__(
            self: "TwoBodyConnectionNodalComponent._Cast_TwoBodyConnectionNodalComponent",
            parent: "TwoBodyConnectionNodalComponent",
        ):
            self._parent = parent

        @property
        def component_nodal_composite(
            self: "TwoBodyConnectionNodalComponent._Cast_TwoBodyConnectionNodalComponent",
        ) -> "_136.ComponentNodalComposite":
            return self._parent._cast(_136.ComponentNodalComposite)

        @property
        def nodal_composite(
            self: "TwoBodyConnectionNodalComponent._Cast_TwoBodyConnectionNodalComponent",
        ) -> "_146.NodalComposite":
            from mastapy.nodal_analysis.nodal_entities import _146

            return self._parent._cast(_146.NodalComposite)

        @property
        def nodal_entity(
            self: "TwoBodyConnectionNodalComponent._Cast_TwoBodyConnectionNodalComponent",
        ) -> "_147.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _147

            return self._parent._cast(_147.NodalEntity)

        @property
        def concentric_connection_nodal_component(
            self: "TwoBodyConnectionNodalComponent._Cast_TwoBodyConnectionNodalComponent",
        ) -> "_137.ConcentricConnectionNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _137

            return self._parent._cast(_137.ConcentricConnectionNodalComponent)

        @property
        def gear_mesh_point_on_flank_contact(
            self: "TwoBodyConnectionNodalComponent._Cast_TwoBodyConnectionNodalComponent",
        ) -> "_142.GearMeshPointOnFlankContact":
            from mastapy.nodal_analysis.nodal_entities import _142

            return self._parent._cast(_142.GearMeshPointOnFlankContact)

        @property
        def simple_bar(
            self: "TwoBodyConnectionNodalComponent._Cast_TwoBodyConnectionNodalComponent",
        ) -> "_150.SimpleBar":
            from mastapy.nodal_analysis.nodal_entities import _150

            return self._parent._cast(_150.SimpleBar)

        @property
        def torsional_friction_node_pair(
            self: "TwoBodyConnectionNodalComponent._Cast_TwoBodyConnectionNodalComponent",
        ) -> "_152.TorsionalFrictionNodePair":
            from mastapy.nodal_analysis.nodal_entities import _152

            return self._parent._cast(_152.TorsionalFrictionNodePair)

        @property
        def torsional_friction_node_pair_simple_locked_stiffness(
            self: "TwoBodyConnectionNodalComponent._Cast_TwoBodyConnectionNodalComponent",
        ) -> "_153.TorsionalFrictionNodePairSimpleLockedStiffness":
            from mastapy.nodal_analysis.nodal_entities import _153

            return self._parent._cast(
                _153.TorsionalFrictionNodePairSimpleLockedStiffness
            )

        @property
        def two_body_connection_nodal_component(
            self: "TwoBodyConnectionNodalComponent._Cast_TwoBodyConnectionNodalComponent",
        ) -> "TwoBodyConnectionNodalComponent":
            return self._parent

        def __getattr__(
            self: "TwoBodyConnectionNodalComponent._Cast_TwoBodyConnectionNodalComponent",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TwoBodyConnectionNodalComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "TwoBodyConnectionNodalComponent._Cast_TwoBodyConnectionNodalComponent":
        return self._Cast_TwoBodyConnectionNodalComponent(self)
