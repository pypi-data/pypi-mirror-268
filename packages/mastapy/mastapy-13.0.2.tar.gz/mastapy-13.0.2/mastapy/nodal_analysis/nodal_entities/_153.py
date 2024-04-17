"""TorsionalFrictionNodePairSimpleLockedStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _152
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORSIONAL_FRICTION_NODE_PAIR_SIMPLE_LOCKED_STIFFNESS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities",
    "TorsionalFrictionNodePairSimpleLockedStiffness",
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import _137, _154, _136, _146, _147


__docformat__ = "restructuredtext en"
__all__ = ("TorsionalFrictionNodePairSimpleLockedStiffness",)


Self = TypeVar("Self", bound="TorsionalFrictionNodePairSimpleLockedStiffness")


class TorsionalFrictionNodePairSimpleLockedStiffness(_152.TorsionalFrictionNodePair):
    """TorsionalFrictionNodePairSimpleLockedStiffness

    This is a mastapy class.
    """

    TYPE = _TORSIONAL_FRICTION_NODE_PAIR_SIMPLE_LOCKED_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorsionalFrictionNodePairSimpleLockedStiffness"
    )

    class _Cast_TorsionalFrictionNodePairSimpleLockedStiffness:
        """Special nested class for casting TorsionalFrictionNodePairSimpleLockedStiffness to subclasses."""

        def __init__(
            self: "TorsionalFrictionNodePairSimpleLockedStiffness._Cast_TorsionalFrictionNodePairSimpleLockedStiffness",
            parent: "TorsionalFrictionNodePairSimpleLockedStiffness",
        ):
            self._parent = parent

        @property
        def torsional_friction_node_pair(
            self: "TorsionalFrictionNodePairSimpleLockedStiffness._Cast_TorsionalFrictionNodePairSimpleLockedStiffness",
        ) -> "_152.TorsionalFrictionNodePair":
            return self._parent._cast(_152.TorsionalFrictionNodePair)

        @property
        def concentric_connection_nodal_component(
            self: "TorsionalFrictionNodePairSimpleLockedStiffness._Cast_TorsionalFrictionNodePairSimpleLockedStiffness",
        ) -> "_137.ConcentricConnectionNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _137

            return self._parent._cast(_137.ConcentricConnectionNodalComponent)

        @property
        def two_body_connection_nodal_component(
            self: "TorsionalFrictionNodePairSimpleLockedStiffness._Cast_TorsionalFrictionNodePairSimpleLockedStiffness",
        ) -> "_154.TwoBodyConnectionNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _154

            return self._parent._cast(_154.TwoBodyConnectionNodalComponent)

        @property
        def component_nodal_composite(
            self: "TorsionalFrictionNodePairSimpleLockedStiffness._Cast_TorsionalFrictionNodePairSimpleLockedStiffness",
        ) -> "_136.ComponentNodalComposite":
            from mastapy.nodal_analysis.nodal_entities import _136

            return self._parent._cast(_136.ComponentNodalComposite)

        @property
        def nodal_composite(
            self: "TorsionalFrictionNodePairSimpleLockedStiffness._Cast_TorsionalFrictionNodePairSimpleLockedStiffness",
        ) -> "_146.NodalComposite":
            from mastapy.nodal_analysis.nodal_entities import _146

            return self._parent._cast(_146.NodalComposite)

        @property
        def nodal_entity(
            self: "TorsionalFrictionNodePairSimpleLockedStiffness._Cast_TorsionalFrictionNodePairSimpleLockedStiffness",
        ) -> "_147.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _147

            return self._parent._cast(_147.NodalEntity)

        @property
        def torsional_friction_node_pair_simple_locked_stiffness(
            self: "TorsionalFrictionNodePairSimpleLockedStiffness._Cast_TorsionalFrictionNodePairSimpleLockedStiffness",
        ) -> "TorsionalFrictionNodePairSimpleLockedStiffness":
            return self._parent

        def __getattr__(
            self: "TorsionalFrictionNodePairSimpleLockedStiffness._Cast_TorsionalFrictionNodePairSimpleLockedStiffness",
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
        self: Self,
        instance_to_wrap: "TorsionalFrictionNodePairSimpleLockedStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "TorsionalFrictionNodePairSimpleLockedStiffness._Cast_TorsionalFrictionNodePairSimpleLockedStiffness":
        return self._Cast_TorsionalFrictionNodePairSimpleLockedStiffness(self)
