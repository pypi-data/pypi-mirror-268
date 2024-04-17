"""ConcentricConnectionNodalComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _154
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCENTRIC_CONNECTION_NODAL_COMPONENT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "ConcentricConnectionNodalComponent"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import _152, _153, _136, _146, _147


__docformat__ = "restructuredtext en"
__all__ = ("ConcentricConnectionNodalComponent",)


Self = TypeVar("Self", bound="ConcentricConnectionNodalComponent")


class ConcentricConnectionNodalComponent(_154.TwoBodyConnectionNodalComponent):
    """ConcentricConnectionNodalComponent

    This is a mastapy class.
    """

    TYPE = _CONCENTRIC_CONNECTION_NODAL_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConcentricConnectionNodalComponent")

    class _Cast_ConcentricConnectionNodalComponent:
        """Special nested class for casting ConcentricConnectionNodalComponent to subclasses."""

        def __init__(
            self: "ConcentricConnectionNodalComponent._Cast_ConcentricConnectionNodalComponent",
            parent: "ConcentricConnectionNodalComponent",
        ):
            self._parent = parent

        @property
        def two_body_connection_nodal_component(
            self: "ConcentricConnectionNodalComponent._Cast_ConcentricConnectionNodalComponent",
        ) -> "_154.TwoBodyConnectionNodalComponent":
            return self._parent._cast(_154.TwoBodyConnectionNodalComponent)

        @property
        def component_nodal_composite(
            self: "ConcentricConnectionNodalComponent._Cast_ConcentricConnectionNodalComponent",
        ) -> "_136.ComponentNodalComposite":
            from mastapy.nodal_analysis.nodal_entities import _136

            return self._parent._cast(_136.ComponentNodalComposite)

        @property
        def nodal_composite(
            self: "ConcentricConnectionNodalComponent._Cast_ConcentricConnectionNodalComponent",
        ) -> "_146.NodalComposite":
            from mastapy.nodal_analysis.nodal_entities import _146

            return self._parent._cast(_146.NodalComposite)

        @property
        def nodal_entity(
            self: "ConcentricConnectionNodalComponent._Cast_ConcentricConnectionNodalComponent",
        ) -> "_147.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _147

            return self._parent._cast(_147.NodalEntity)

        @property
        def torsional_friction_node_pair(
            self: "ConcentricConnectionNodalComponent._Cast_ConcentricConnectionNodalComponent",
        ) -> "_152.TorsionalFrictionNodePair":
            from mastapy.nodal_analysis.nodal_entities import _152

            return self._parent._cast(_152.TorsionalFrictionNodePair)

        @property
        def torsional_friction_node_pair_simple_locked_stiffness(
            self: "ConcentricConnectionNodalComponent._Cast_ConcentricConnectionNodalComponent",
        ) -> "_153.TorsionalFrictionNodePairSimpleLockedStiffness":
            from mastapy.nodal_analysis.nodal_entities import _153

            return self._parent._cast(
                _153.TorsionalFrictionNodePairSimpleLockedStiffness
            )

        @property
        def concentric_connection_nodal_component(
            self: "ConcentricConnectionNodalComponent._Cast_ConcentricConnectionNodalComponent",
        ) -> "ConcentricConnectionNodalComponent":
            return self._parent

        def __getattr__(
            self: "ConcentricConnectionNodalComponent._Cast_ConcentricConnectionNodalComponent",
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
        self: Self, instance_to_wrap: "ConcentricConnectionNodalComponent.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConcentricConnectionNodalComponent._Cast_ConcentricConnectionNodalComponent":
        return self._Cast_ConcentricConnectionNodalComponent(self)
