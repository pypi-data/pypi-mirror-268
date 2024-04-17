"""ISO6336MetalRateableMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.cylindrical.iso6336 import _526
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO6336_METAL_RATEABLE_MESH = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336", "ISO6336MetalRateableMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical import _474
    from mastapy.gears.rating import _370


__docformat__ = "restructuredtext en"
__all__ = ("ISO6336MetalRateableMesh",)


Self = TypeVar("Self", bound="ISO6336MetalRateableMesh")


class ISO6336MetalRateableMesh(_526.ISO6336RateableMesh):
    """ISO6336MetalRateableMesh

    This is a mastapy class.
    """

    TYPE = _ISO6336_METAL_RATEABLE_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO6336MetalRateableMesh")

    class _Cast_ISO6336MetalRateableMesh:
        """Special nested class for casting ISO6336MetalRateableMesh to subclasses."""

        def __init__(
            self: "ISO6336MetalRateableMesh._Cast_ISO6336MetalRateableMesh",
            parent: "ISO6336MetalRateableMesh",
        ):
            self._parent = parent

        @property
        def iso6336_rateable_mesh(
            self: "ISO6336MetalRateableMesh._Cast_ISO6336MetalRateableMesh",
        ) -> "_526.ISO6336RateableMesh":
            return self._parent._cast(_526.ISO6336RateableMesh)

        @property
        def cylindrical_rateable_mesh(
            self: "ISO6336MetalRateableMesh._Cast_ISO6336MetalRateableMesh",
        ) -> "_474.CylindricalRateableMesh":
            from mastapy.gears.rating.cylindrical import _474

            return self._parent._cast(_474.CylindricalRateableMesh)

        @property
        def rateable_mesh(
            self: "ISO6336MetalRateableMesh._Cast_ISO6336MetalRateableMesh",
        ) -> "_370.RateableMesh":
            from mastapy.gears.rating import _370

            return self._parent._cast(_370.RateableMesh)

        @property
        def iso6336_metal_rateable_mesh(
            self: "ISO6336MetalRateableMesh._Cast_ISO6336MetalRateableMesh",
        ) -> "ISO6336MetalRateableMesh":
            return self._parent

        def __getattr__(
            self: "ISO6336MetalRateableMesh._Cast_ISO6336MetalRateableMesh", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO6336MetalRateableMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ISO6336MetalRateableMesh._Cast_ISO6336MetalRateableMesh":
        return self._Cast_ISO6336MetalRateableMesh(self)
