"""BarMBD"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _136
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BAR_MBD = python_net_import("SMT.MastaAPI.NodalAnalysis.NodalEntities", "BarMBD")

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import _130, _132, _146, _147


__docformat__ = "restructuredtext en"
__all__ = ("BarMBD",)


Self = TypeVar("Self", bound="BarMBD")


class BarMBD(_136.ComponentNodalComposite):
    """BarMBD

    This is a mastapy class.
    """

    TYPE = _BAR_MBD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BarMBD")

    class _Cast_BarMBD:
        """Special nested class for casting BarMBD to subclasses."""

        def __init__(self: "BarMBD._Cast_BarMBD", parent: "BarMBD"):
            self._parent = parent

        @property
        def component_nodal_composite(
            self: "BarMBD._Cast_BarMBD",
        ) -> "_136.ComponentNodalComposite":
            return self._parent._cast(_136.ComponentNodalComposite)

        @property
        def nodal_composite(self: "BarMBD._Cast_BarMBD") -> "_146.NodalComposite":
            from mastapy.nodal_analysis.nodal_entities import _146

            return self._parent._cast(_146.NodalComposite)

        @property
        def nodal_entity(self: "BarMBD._Cast_BarMBD") -> "_147.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _147

            return self._parent._cast(_147.NodalEntity)

        @property
        def bar_elastic_mbd(self: "BarMBD._Cast_BarMBD") -> "_130.BarElasticMBD":
            from mastapy.nodal_analysis.nodal_entities import _130

            return self._parent._cast(_130.BarElasticMBD)

        @property
        def bar_rigid_mbd(self: "BarMBD._Cast_BarMBD") -> "_132.BarRigidMBD":
            from mastapy.nodal_analysis.nodal_entities import _132

            return self._parent._cast(_132.BarRigidMBD)

        @property
        def bar_mbd(self: "BarMBD._Cast_BarMBD") -> "BarMBD":
            return self._parent

        def __getattr__(self: "BarMBD._Cast_BarMBD", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BarMBD.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BarMBD._Cast_BarMBD":
        return self._Cast_BarMBD(self)
