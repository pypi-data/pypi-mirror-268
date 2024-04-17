"""ConicalMeshLoadDistributionAtRotation"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.ltca import _845
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_LOAD_DISTRIBUTION_AT_ROTATION = python_net_import(
    "SMT.MastaAPI.Gears.LTCA.Conical", "ConicalMeshLoadDistributionAtRotation"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshLoadDistributionAtRotation",)


Self = TypeVar("Self", bound="ConicalMeshLoadDistributionAtRotation")


class ConicalMeshLoadDistributionAtRotation(_845.GearMeshLoadDistributionAtRotation):
    """ConicalMeshLoadDistributionAtRotation

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_LOAD_DISTRIBUTION_AT_ROTATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalMeshLoadDistributionAtRotation"
    )

    class _Cast_ConicalMeshLoadDistributionAtRotation:
        """Special nested class for casting ConicalMeshLoadDistributionAtRotation to subclasses."""

        def __init__(
            self: "ConicalMeshLoadDistributionAtRotation._Cast_ConicalMeshLoadDistributionAtRotation",
            parent: "ConicalMeshLoadDistributionAtRotation",
        ):
            self._parent = parent

        @property
        def gear_mesh_load_distribution_at_rotation(
            self: "ConicalMeshLoadDistributionAtRotation._Cast_ConicalMeshLoadDistributionAtRotation",
        ) -> "_845.GearMeshLoadDistributionAtRotation":
            return self._parent._cast(_845.GearMeshLoadDistributionAtRotation)

        @property
        def conical_mesh_load_distribution_at_rotation(
            self: "ConicalMeshLoadDistributionAtRotation._Cast_ConicalMeshLoadDistributionAtRotation",
        ) -> "ConicalMeshLoadDistributionAtRotation":
            return self._parent

        def __getattr__(
            self: "ConicalMeshLoadDistributionAtRotation._Cast_ConicalMeshLoadDistributionAtRotation",
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
        self: Self, instance_to_wrap: "ConicalMeshLoadDistributionAtRotation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalMeshLoadDistributionAtRotation._Cast_ConicalMeshLoadDistributionAtRotation":
        return self._Cast_ConicalMeshLoadDistributionAtRotation(self)
