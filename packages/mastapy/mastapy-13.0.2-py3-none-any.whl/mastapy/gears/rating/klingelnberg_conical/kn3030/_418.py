"""KlingelnbergConicalRateableMesh"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.rating import _370
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CONICAL_RATEABLE_MESH = python_net_import(
    "SMT.MastaAPI.Gears.Rating.KlingelnbergConical.KN3030",
    "KlingelnbergConicalRateableMesh",
)


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergConicalRateableMesh",)


Self = TypeVar("Self", bound="KlingelnbergConicalRateableMesh")


class KlingelnbergConicalRateableMesh(_370.RateableMesh):
    """KlingelnbergConicalRateableMesh

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CONICAL_RATEABLE_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_KlingelnbergConicalRateableMesh")

    class _Cast_KlingelnbergConicalRateableMesh:
        """Special nested class for casting KlingelnbergConicalRateableMesh to subclasses."""

        def __init__(
            self: "KlingelnbergConicalRateableMesh._Cast_KlingelnbergConicalRateableMesh",
            parent: "KlingelnbergConicalRateableMesh",
        ):
            self._parent = parent

        @property
        def rateable_mesh(
            self: "KlingelnbergConicalRateableMesh._Cast_KlingelnbergConicalRateableMesh",
        ) -> "_370.RateableMesh":
            return self._parent._cast(_370.RateableMesh)

        @property
        def klingelnberg_conical_rateable_mesh(
            self: "KlingelnbergConicalRateableMesh._Cast_KlingelnbergConicalRateableMesh",
        ) -> "KlingelnbergConicalRateableMesh":
            return self._parent

        def __getattr__(
            self: "KlingelnbergConicalRateableMesh._Cast_KlingelnbergConicalRateableMesh",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "KlingelnbergConicalRateableMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergConicalRateableMesh._Cast_KlingelnbergConicalRateableMesh":
        return self._Cast_KlingelnbergConicalRateableMesh(self)
