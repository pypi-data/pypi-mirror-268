"""HypoidRateableMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.agma_gleason_conical import _571
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_RATEABLE_MESH = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Hypoid.Standards", "HypoidRateableMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.conical import _550
    from mastapy.gears.rating import _370


__docformat__ = "restructuredtext en"
__all__ = ("HypoidRateableMesh",)


Self = TypeVar("Self", bound="HypoidRateableMesh")


class HypoidRateableMesh(_571.AGMAGleasonConicalRateableMesh):
    """HypoidRateableMesh

    This is a mastapy class.
    """

    TYPE = _HYPOID_RATEABLE_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidRateableMesh")

    class _Cast_HypoidRateableMesh:
        """Special nested class for casting HypoidRateableMesh to subclasses."""

        def __init__(
            self: "HypoidRateableMesh._Cast_HypoidRateableMesh",
            parent: "HypoidRateableMesh",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_rateable_mesh(
            self: "HypoidRateableMesh._Cast_HypoidRateableMesh",
        ) -> "_571.AGMAGleasonConicalRateableMesh":
            return self._parent._cast(_571.AGMAGleasonConicalRateableMesh)

        @property
        def conical_rateable_mesh(
            self: "HypoidRateableMesh._Cast_HypoidRateableMesh",
        ) -> "_550.ConicalRateableMesh":
            from mastapy.gears.rating.conical import _550

            return self._parent._cast(_550.ConicalRateableMesh)

        @property
        def rateable_mesh(
            self: "HypoidRateableMesh._Cast_HypoidRateableMesh",
        ) -> "_370.RateableMesh":
            from mastapy.gears.rating import _370

            return self._parent._cast(_370.RateableMesh)

        @property
        def hypoid_rateable_mesh(
            self: "HypoidRateableMesh._Cast_HypoidRateableMesh",
        ) -> "HypoidRateableMesh":
            return self._parent

        def __getattr__(self: "HypoidRateableMesh._Cast_HypoidRateableMesh", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidRateableMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "HypoidRateableMesh._Cast_HypoidRateableMesh":
        return self._Cast_HypoidRateableMesh(self)
