"""VDI2736PlasticMetalRateableMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _496
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VDI2736_PLASTIC_METAL_RATEABLE_MESH = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.PlasticVDI2736",
    "VDI2736PlasticMetalRateableMesh",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.iso6336 import _526
    from mastapy.gears.rating.cylindrical import _474
    from mastapy.gears.rating import _370


__docformat__ = "restructuredtext en"
__all__ = ("VDI2736PlasticMetalRateableMesh",)


Self = TypeVar("Self", bound="VDI2736PlasticMetalRateableMesh")


class VDI2736PlasticMetalRateableMesh(_496.PlasticGearVDI2736AbstractRateableMesh):
    """VDI2736PlasticMetalRateableMesh

    This is a mastapy class.
    """

    TYPE = _VDI2736_PLASTIC_METAL_RATEABLE_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VDI2736PlasticMetalRateableMesh")

    class _Cast_VDI2736PlasticMetalRateableMesh:
        """Special nested class for casting VDI2736PlasticMetalRateableMesh to subclasses."""

        def __init__(
            self: "VDI2736PlasticMetalRateableMesh._Cast_VDI2736PlasticMetalRateableMesh",
            parent: "VDI2736PlasticMetalRateableMesh",
        ):
            self._parent = parent

        @property
        def plastic_gear_vdi2736_abstract_rateable_mesh(
            self: "VDI2736PlasticMetalRateableMesh._Cast_VDI2736PlasticMetalRateableMesh",
        ) -> "_496.PlasticGearVDI2736AbstractRateableMesh":
            return self._parent._cast(_496.PlasticGearVDI2736AbstractRateableMesh)

        @property
        def iso6336_rateable_mesh(
            self: "VDI2736PlasticMetalRateableMesh._Cast_VDI2736PlasticMetalRateableMesh",
        ) -> "_526.ISO6336RateableMesh":
            from mastapy.gears.rating.cylindrical.iso6336 import _526

            return self._parent._cast(_526.ISO6336RateableMesh)

        @property
        def cylindrical_rateable_mesh(
            self: "VDI2736PlasticMetalRateableMesh._Cast_VDI2736PlasticMetalRateableMesh",
        ) -> "_474.CylindricalRateableMesh":
            from mastapy.gears.rating.cylindrical import _474

            return self._parent._cast(_474.CylindricalRateableMesh)

        @property
        def rateable_mesh(
            self: "VDI2736PlasticMetalRateableMesh._Cast_VDI2736PlasticMetalRateableMesh",
        ) -> "_370.RateableMesh":
            from mastapy.gears.rating import _370

            return self._parent._cast(_370.RateableMesh)

        @property
        def vdi2736_plastic_metal_rateable_mesh(
            self: "VDI2736PlasticMetalRateableMesh._Cast_VDI2736PlasticMetalRateableMesh",
        ) -> "VDI2736PlasticMetalRateableMesh":
            return self._parent

        def __getattr__(
            self: "VDI2736PlasticMetalRateableMesh._Cast_VDI2736PlasticMetalRateableMesh",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VDI2736PlasticMetalRateableMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "VDI2736PlasticMetalRateableMesh._Cast_VDI2736PlasticMetalRateableMesh":
        return self._Cast_VDI2736PlasticMetalRateableMesh(self)
