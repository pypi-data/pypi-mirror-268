"""DistributedRigidBarCoupling"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _145
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DISTRIBUTED_RIGID_BAR_COUPLING = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "DistributedRigidBarCoupling"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import _147


__docformat__ = "restructuredtext en"
__all__ = ("DistributedRigidBarCoupling",)


Self = TypeVar("Self", bound="DistributedRigidBarCoupling")


class DistributedRigidBarCoupling(_145.NodalComponent):
    """DistributedRigidBarCoupling

    This is a mastapy class.
    """

    TYPE = _DISTRIBUTED_RIGID_BAR_COUPLING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DistributedRigidBarCoupling")

    class _Cast_DistributedRigidBarCoupling:
        """Special nested class for casting DistributedRigidBarCoupling to subclasses."""

        def __init__(
            self: "DistributedRigidBarCoupling._Cast_DistributedRigidBarCoupling",
            parent: "DistributedRigidBarCoupling",
        ):
            self._parent = parent

        @property
        def nodal_component(
            self: "DistributedRigidBarCoupling._Cast_DistributedRigidBarCoupling",
        ) -> "_145.NodalComponent":
            return self._parent._cast(_145.NodalComponent)

        @property
        def nodal_entity(
            self: "DistributedRigidBarCoupling._Cast_DistributedRigidBarCoupling",
        ) -> "_147.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _147

            return self._parent._cast(_147.NodalEntity)

        @property
        def distributed_rigid_bar_coupling(
            self: "DistributedRigidBarCoupling._Cast_DistributedRigidBarCoupling",
        ) -> "DistributedRigidBarCoupling":
            return self._parent

        def __getattr__(
            self: "DistributedRigidBarCoupling._Cast_DistributedRigidBarCoupling",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DistributedRigidBarCoupling.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "DistributedRigidBarCoupling._Cast_DistributedRigidBarCoupling":
        return self._Cast_DistributedRigidBarCoupling(self)
