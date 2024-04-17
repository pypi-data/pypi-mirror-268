"""ConicalRateableMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating import _370
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_RATEABLE_MESH = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Conical", "ConicalRateableMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.iso_10300 import _430
    from mastapy.gears.rating.hypoid.standards import _447
    from mastapy.gears.rating.bevel.standards import _567
    from mastapy.gears.rating.agma_gleason_conical import _571


__docformat__ = "restructuredtext en"
__all__ = ("ConicalRateableMesh",)


Self = TypeVar("Self", bound="ConicalRateableMesh")


class ConicalRateableMesh(_370.RateableMesh):
    """ConicalRateableMesh

    This is a mastapy class.
    """

    TYPE = _CONICAL_RATEABLE_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalRateableMesh")

    class _Cast_ConicalRateableMesh:
        """Special nested class for casting ConicalRateableMesh to subclasses."""

        def __init__(
            self: "ConicalRateableMesh._Cast_ConicalRateableMesh",
            parent: "ConicalRateableMesh",
        ):
            self._parent = parent

        @property
        def rateable_mesh(
            self: "ConicalRateableMesh._Cast_ConicalRateableMesh",
        ) -> "_370.RateableMesh":
            return self._parent._cast(_370.RateableMesh)

        @property
        def iso10300_rateable_mesh(
            self: "ConicalRateableMesh._Cast_ConicalRateableMesh",
        ) -> "_430.ISO10300RateableMesh":
            from mastapy.gears.rating.iso_10300 import _430

            return self._parent._cast(_430.ISO10300RateableMesh)

        @property
        def hypoid_rateable_mesh(
            self: "ConicalRateableMesh._Cast_ConicalRateableMesh",
        ) -> "_447.HypoidRateableMesh":
            from mastapy.gears.rating.hypoid.standards import _447

            return self._parent._cast(_447.HypoidRateableMesh)

        @property
        def spiral_bevel_rateable_mesh(
            self: "ConicalRateableMesh._Cast_ConicalRateableMesh",
        ) -> "_567.SpiralBevelRateableMesh":
            from mastapy.gears.rating.bevel.standards import _567

            return self._parent._cast(_567.SpiralBevelRateableMesh)

        @property
        def agma_gleason_conical_rateable_mesh(
            self: "ConicalRateableMesh._Cast_ConicalRateableMesh",
        ) -> "_571.AGMAGleasonConicalRateableMesh":
            from mastapy.gears.rating.agma_gleason_conical import _571

            return self._parent._cast(_571.AGMAGleasonConicalRateableMesh)

        @property
        def conical_rateable_mesh(
            self: "ConicalRateableMesh._Cast_ConicalRateableMesh",
        ) -> "ConicalRateableMesh":
            return self._parent

        def __getattr__(
            self: "ConicalRateableMesh._Cast_ConicalRateableMesh", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalRateableMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ConicalRateableMesh._Cast_ConicalRateableMesh":
        return self._Cast_ConicalRateableMesh(self)
