"""CylindricalRateableMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating import _370
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_RATEABLE_MESH = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "CylindricalRateableMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _496, _501, _502, _503
    from mastapy.gears.rating.cylindrical.iso6336 import _525, _526
    from mastapy.gears.rating.cylindrical.agma import _539


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalRateableMesh",)


Self = TypeVar("Self", bound="CylindricalRateableMesh")


class CylindricalRateableMesh(_370.RateableMesh):
    """CylindricalRateableMesh

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_RATEABLE_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalRateableMesh")

    class _Cast_CylindricalRateableMesh:
        """Special nested class for casting CylindricalRateableMesh to subclasses."""

        def __init__(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
            parent: "CylindricalRateableMesh",
        ):
            self._parent = parent

        @property
        def rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ) -> "_370.RateableMesh":
            return self._parent._cast(_370.RateableMesh)

        @property
        def plastic_gear_vdi2736_abstract_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ) -> "_496.PlasticGearVDI2736AbstractRateableMesh":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _496

            return self._parent._cast(_496.PlasticGearVDI2736AbstractRateableMesh)

        @property
        def vdi2736_metal_plastic_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ) -> "_501.VDI2736MetalPlasticRateableMesh":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _501

            return self._parent._cast(_501.VDI2736MetalPlasticRateableMesh)

        @property
        def vdi2736_plastic_metal_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ) -> "_502.VDI2736PlasticMetalRateableMesh":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _502

            return self._parent._cast(_502.VDI2736PlasticMetalRateableMesh)

        @property
        def vdi2736_plastic_plastic_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ) -> "_503.VDI2736PlasticPlasticRateableMesh":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _503

            return self._parent._cast(_503.VDI2736PlasticPlasticRateableMesh)

        @property
        def iso6336_metal_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ) -> "_525.ISO6336MetalRateableMesh":
            from mastapy.gears.rating.cylindrical.iso6336 import _525

            return self._parent._cast(_525.ISO6336MetalRateableMesh)

        @property
        def iso6336_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ) -> "_526.ISO6336RateableMesh":
            from mastapy.gears.rating.cylindrical.iso6336 import _526

            return self._parent._cast(_526.ISO6336RateableMesh)

        @property
        def agma2101_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ) -> "_539.AGMA2101RateableMesh":
            from mastapy.gears.rating.cylindrical.agma import _539

            return self._parent._cast(_539.AGMA2101RateableMesh)

        @property
        def cylindrical_rateable_mesh(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh",
        ) -> "CylindricalRateableMesh":
            return self._parent

        def __getattr__(
            self: "CylindricalRateableMesh._Cast_CylindricalRateableMesh", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalRateableMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CylindricalRateableMesh._Cast_CylindricalRateableMesh":
        return self._Cast_CylindricalRateableMesh(self)
