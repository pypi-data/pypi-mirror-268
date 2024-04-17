"""MultiNodeFELink"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.fe.links import _2425
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MULTI_NODE_FE_LINK = python_net_import(
    "SMT.MastaAPI.SystemModel.FE.Links", "MultiNodeFELink"
)

if TYPE_CHECKING:
    from mastapy.system_model.fe.links import (
        _2426,
        _2428,
        _2429,
        _2430,
        _2431,
        _2433,
        _2434,
        _2435,
        _2436,
        _2437,
        _2438,
    )


__docformat__ = "restructuredtext en"
__all__ = ("MultiNodeFELink",)


Self = TypeVar("Self", bound="MultiNodeFELink")


class MultiNodeFELink(_2425.FELink):
    """MultiNodeFELink

    This is a mastapy class.
    """

    TYPE = _MULTI_NODE_FE_LINK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MultiNodeFELink")

    class _Cast_MultiNodeFELink:
        """Special nested class for casting MultiNodeFELink to subclasses."""

        def __init__(
            self: "MultiNodeFELink._Cast_MultiNodeFELink", parent: "MultiNodeFELink"
        ):
            self._parent = parent

        @property
        def fe_link(self: "MultiNodeFELink._Cast_MultiNodeFELink") -> "_2425.FELink":
            return self._parent._cast(_2425.FELink)

        @property
        def electric_machine_stator_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "_2426.ElectricMachineStatorFELink":
            from mastapy.system_model.fe.links import _2426

            return self._parent._cast(_2426.ElectricMachineStatorFELink)

        @property
        def gear_mesh_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "_2428.GearMeshFELink":
            from mastapy.system_model.fe.links import _2428

            return self._parent._cast(_2428.GearMeshFELink)

        @property
        def gear_with_duplicated_meshes_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "_2429.GearWithDuplicatedMeshesFELink":
            from mastapy.system_model.fe.links import _2429

            return self._parent._cast(_2429.GearWithDuplicatedMeshesFELink)

        @property
        def multi_angle_connection_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "_2430.MultiAngleConnectionFELink":
            from mastapy.system_model.fe.links import _2430

            return self._parent._cast(_2430.MultiAngleConnectionFELink)

        @property
        def multi_node_connector_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "_2431.MultiNodeConnectorFELink":
            from mastapy.system_model.fe.links import _2431

            return self._parent._cast(_2431.MultiNodeConnectorFELink)

        @property
        def planetary_connector_multi_node_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "_2433.PlanetaryConnectorMultiNodeFELink":
            from mastapy.system_model.fe.links import _2433

            return self._parent._cast(_2433.PlanetaryConnectorMultiNodeFELink)

        @property
        def planet_based_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "_2434.PlanetBasedFELink":
            from mastapy.system_model.fe.links import _2434

            return self._parent._cast(_2434.PlanetBasedFELink)

        @property
        def planet_carrier_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "_2435.PlanetCarrierFELink":
            from mastapy.system_model.fe.links import _2435

            return self._parent._cast(_2435.PlanetCarrierFELink)

        @property
        def point_load_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "_2436.PointLoadFELink":
            from mastapy.system_model.fe.links import _2436

            return self._parent._cast(_2436.PointLoadFELink)

        @property
        def rolling_ring_connection_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "_2437.RollingRingConnectionFELink":
            from mastapy.system_model.fe.links import _2437

            return self._parent._cast(_2437.RollingRingConnectionFELink)

        @property
        def shaft_hub_connection_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "_2438.ShaftHubConnectionFELink":
            from mastapy.system_model.fe.links import _2438

            return self._parent._cast(_2438.ShaftHubConnectionFELink)

        @property
        def multi_node_fe_link(
            self: "MultiNodeFELink._Cast_MultiNodeFELink",
        ) -> "MultiNodeFELink":
            return self._parent

        def __getattr__(self: "MultiNodeFELink._Cast_MultiNodeFELink", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MultiNodeFELink.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "MultiNodeFELink._Cast_MultiNodeFELink":
        return self._Cast_MultiNodeFELink(self)
