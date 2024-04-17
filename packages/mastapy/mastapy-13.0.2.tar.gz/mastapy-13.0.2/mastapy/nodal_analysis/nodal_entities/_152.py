"""TorsionalFrictionNodePair"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _137
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORSIONAL_FRICTION_NODE_PAIR = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "TorsionalFrictionNodePair"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import _153, _154, _136, _146, _147


__docformat__ = "restructuredtext en"
__all__ = ("TorsionalFrictionNodePair",)


Self = TypeVar("Self", bound="TorsionalFrictionNodePair")


class TorsionalFrictionNodePair(_137.ConcentricConnectionNodalComponent):
    """TorsionalFrictionNodePair

    This is a mastapy class.
    """

    TYPE = _TORSIONAL_FRICTION_NODE_PAIR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorsionalFrictionNodePair")

    class _Cast_TorsionalFrictionNodePair:
        """Special nested class for casting TorsionalFrictionNodePair to subclasses."""

        def __init__(
            self: "TorsionalFrictionNodePair._Cast_TorsionalFrictionNodePair",
            parent: "TorsionalFrictionNodePair",
        ):
            self._parent = parent

        @property
        def concentric_connection_nodal_component(
            self: "TorsionalFrictionNodePair._Cast_TorsionalFrictionNodePair",
        ) -> "_137.ConcentricConnectionNodalComponent":
            return self._parent._cast(_137.ConcentricConnectionNodalComponent)

        @property
        def two_body_connection_nodal_component(
            self: "TorsionalFrictionNodePair._Cast_TorsionalFrictionNodePair",
        ) -> "_154.TwoBodyConnectionNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _154

            return self._parent._cast(_154.TwoBodyConnectionNodalComponent)

        @property
        def component_nodal_composite(
            self: "TorsionalFrictionNodePair._Cast_TorsionalFrictionNodePair",
        ) -> "_136.ComponentNodalComposite":
            from mastapy.nodal_analysis.nodal_entities import _136

            return self._parent._cast(_136.ComponentNodalComposite)

        @property
        def nodal_composite(
            self: "TorsionalFrictionNodePair._Cast_TorsionalFrictionNodePair",
        ) -> "_146.NodalComposite":
            from mastapy.nodal_analysis.nodal_entities import _146

            return self._parent._cast(_146.NodalComposite)

        @property
        def nodal_entity(
            self: "TorsionalFrictionNodePair._Cast_TorsionalFrictionNodePair",
        ) -> "_147.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _147

            return self._parent._cast(_147.NodalEntity)

        @property
        def torsional_friction_node_pair_simple_locked_stiffness(
            self: "TorsionalFrictionNodePair._Cast_TorsionalFrictionNodePair",
        ) -> "_153.TorsionalFrictionNodePairSimpleLockedStiffness":
            from mastapy.nodal_analysis.nodal_entities import _153

            return self._parent._cast(
                _153.TorsionalFrictionNodePairSimpleLockedStiffness
            )

        @property
        def torsional_friction_node_pair(
            self: "TorsionalFrictionNodePair._Cast_TorsionalFrictionNodePair",
        ) -> "TorsionalFrictionNodePair":
            return self._parent

        def __getattr__(
            self: "TorsionalFrictionNodePair._Cast_TorsionalFrictionNodePair", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorsionalFrictionNodePair.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "TorsionalFrictionNodePair._Cast_TorsionalFrictionNodePair":
        return self._Cast_TorsionalFrictionNodePair(self)
