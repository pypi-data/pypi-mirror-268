"""BearingAxialMountingClearance"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _128
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_AXIAL_MOUNTING_CLEARANCE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "BearingAxialMountingClearance"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import _145, _147


__docformat__ = "restructuredtext en"
__all__ = ("BearingAxialMountingClearance",)


Self = TypeVar("Self", bound="BearingAxialMountingClearance")


class BearingAxialMountingClearance(_128.ArbitraryNodalComponent):
    """BearingAxialMountingClearance

    This is a mastapy class.
    """

    TYPE = _BEARING_AXIAL_MOUNTING_CLEARANCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingAxialMountingClearance")

    class _Cast_BearingAxialMountingClearance:
        """Special nested class for casting BearingAxialMountingClearance to subclasses."""

        def __init__(
            self: "BearingAxialMountingClearance._Cast_BearingAxialMountingClearance",
            parent: "BearingAxialMountingClearance",
        ):
            self._parent = parent

        @property
        def arbitrary_nodal_component(
            self: "BearingAxialMountingClearance._Cast_BearingAxialMountingClearance",
        ) -> "_128.ArbitraryNodalComponent":
            return self._parent._cast(_128.ArbitraryNodalComponent)

        @property
        def nodal_component(
            self: "BearingAxialMountingClearance._Cast_BearingAxialMountingClearance",
        ) -> "_145.NodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _145

            return self._parent._cast(_145.NodalComponent)

        @property
        def nodal_entity(
            self: "BearingAxialMountingClearance._Cast_BearingAxialMountingClearance",
        ) -> "_147.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _147

            return self._parent._cast(_147.NodalEntity)

        @property
        def bearing_axial_mounting_clearance(
            self: "BearingAxialMountingClearance._Cast_BearingAxialMountingClearance",
        ) -> "BearingAxialMountingClearance":
            return self._parent

        def __getattr__(
            self: "BearingAxialMountingClearance._Cast_BearingAxialMountingClearance",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingAxialMountingClearance.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BearingAxialMountingClearance._Cast_BearingAxialMountingClearance":
        return self._Cast_BearingAxialMountingClearance(self)
