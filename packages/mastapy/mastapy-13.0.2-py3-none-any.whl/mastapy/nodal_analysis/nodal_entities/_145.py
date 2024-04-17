"""NodalComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _147
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODAL_COMPONENT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "NodalComponent"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import (
        _128,
        _129,
        _134,
        _135,
        _138,
        _139,
        _141,
        _144,
        _148,
        _149,
        _151,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2811


__docformat__ = "restructuredtext en"
__all__ = ("NodalComponent",)


Self = TypeVar("Self", bound="NodalComponent")


class NodalComponent(_147.NodalEntity):
    """NodalComponent

    This is a mastapy class.
    """

    TYPE = _NODAL_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NodalComponent")

    class _Cast_NodalComponent:
        """Special nested class for casting NodalComponent to subclasses."""

        def __init__(
            self: "NodalComponent._Cast_NodalComponent", parent: "NodalComponent"
        ):
            self._parent = parent

        @property
        def nodal_entity(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_147.NodalEntity":
            return self._parent._cast(_147.NodalEntity)

        @property
        def arbitrary_nodal_component(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_128.ArbitraryNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _128

            return self._parent._cast(_128.ArbitraryNodalComponent)

        @property
        def bar(self: "NodalComponent._Cast_NodalComponent") -> "_129.Bar":
            from mastapy.nodal_analysis.nodal_entities import _129

            return self._parent._cast(_129.Bar)

        @property
        def bearing_axial_mounting_clearance(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_134.BearingAxialMountingClearance":
            from mastapy.nodal_analysis.nodal_entities import _134

            return self._parent._cast(_134.BearingAxialMountingClearance)

        @property
        def cms_nodal_component(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_135.CMSNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _135

            return self._parent._cast(_135.CMSNodalComponent)

        @property
        def distributed_rigid_bar_coupling(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_138.DistributedRigidBarCoupling":
            from mastapy.nodal_analysis.nodal_entities import _138

            return self._parent._cast(_138.DistributedRigidBarCoupling)

        @property
        def friction_nodal_component(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_139.FrictionNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _139

            return self._parent._cast(_139.FrictionNodalComponent)

        @property
        def gear_mesh_node_pair(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_141.GearMeshNodePair":
            from mastapy.nodal_analysis.nodal_entities import _141

            return self._parent._cast(_141.GearMeshNodePair)

        @property
        def line_contact_stiffness_entity(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_144.LineContactStiffnessEntity":
            from mastapy.nodal_analysis.nodal_entities import _144

            return self._parent._cast(_144.LineContactStiffnessEntity)

        @property
        def pid_control_nodal_component(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_148.PIDControlNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _148

            return self._parent._cast(_148.PIDControlNodalComponent)

        @property
        def rigid_bar(self: "NodalComponent._Cast_NodalComponent") -> "_149.RigidBar":
            from mastapy.nodal_analysis.nodal_entities import _149

            return self._parent._cast(_149.RigidBar)

        @property
        def surface_to_surface_contact_stiffness_entity(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_151.SurfaceToSurfaceContactStiffnessEntity":
            from mastapy.nodal_analysis.nodal_entities import _151

            return self._parent._cast(_151.SurfaceToSurfaceContactStiffnessEntity)

        @property
        def shaft_section_system_deflection(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_2811.ShaftSectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2811,
            )

            return self._parent._cast(_2811.ShaftSectionSystemDeflection)

        @property
        def nodal_component(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "NodalComponent":
            return self._parent

        def __getattr__(self: "NodalComponent._Cast_NodalComponent", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NodalComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "NodalComponent._Cast_NodalComponent":
        return self._Cast_NodalComponent(self)
