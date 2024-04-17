"""VDI2736MetalPlasticRateableMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _496
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VDI2736_METAL_PLASTIC_RATEABLE_MESH = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.PlasticVDI2736",
    "VDI2736MetalPlasticRateableMesh",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.iso6336 import _526
    from mastapy.gears.rating.cylindrical import _474
    from mastapy.gears.rating import _370


__docformat__ = "restructuredtext en"
__all__ = ("VDI2736MetalPlasticRateableMesh",)


Self = TypeVar("Self", bound="VDI2736MetalPlasticRateableMesh")


class VDI2736MetalPlasticRateableMesh(_496.PlasticGearVDI2736AbstractRateableMesh):
    """VDI2736MetalPlasticRateableMesh

    This is a mastapy class.
    """

    TYPE = _VDI2736_METAL_PLASTIC_RATEABLE_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VDI2736MetalPlasticRateableMesh")

    class _Cast_VDI2736MetalPlasticRateableMesh:
        """Special nested class for casting VDI2736MetalPlasticRateableMesh to subclasses."""

        def __init__(
            self: "VDI2736MetalPlasticRateableMesh._Cast_VDI2736MetalPlasticRateableMesh",
            parent: "VDI2736MetalPlasticRateableMesh",
        ):
            self._parent = parent

        @property
        def plastic_gear_vdi2736_abstract_rateable_mesh(
            self: "VDI2736MetalPlasticRateableMesh._Cast_VDI2736MetalPlasticRateableMesh",
        ) -> "_496.PlasticGearVDI2736AbstractRateableMesh":
            return self._parent._cast(_496.PlasticGearVDI2736AbstractRateableMesh)

        @property
        def iso6336_rateable_mesh(
            self: "VDI2736MetalPlasticRateableMesh._Cast_VDI2736MetalPlasticRateableMesh",
        ) -> "_526.ISO6336RateableMesh":
            from mastapy.gears.rating.cylindrical.iso6336 import _526

            return self._parent._cast(_526.ISO6336RateableMesh)

        @property
        def cylindrical_rateable_mesh(
            self: "VDI2736MetalPlasticRateableMesh._Cast_VDI2736MetalPlasticRateableMesh",
        ) -> "_474.CylindricalRateableMesh":
            from mastapy.gears.rating.cylindrical import _474

            return self._parent._cast(_474.CylindricalRateableMesh)

        @property
        def rateable_mesh(
            self: "VDI2736MetalPlasticRateableMesh._Cast_VDI2736MetalPlasticRateableMesh",
        ) -> "_370.RateableMesh":
            from mastapy.gears.rating import _370

            return self._parent._cast(_370.RateableMesh)

        @property
        def vdi2736_metal_plastic_rateable_mesh(
            self: "VDI2736MetalPlasticRateableMesh._Cast_VDI2736MetalPlasticRateableMesh",
        ) -> "VDI2736MetalPlasticRateableMesh":
            return self._parent

        def __getattr__(
            self: "VDI2736MetalPlasticRateableMesh._Cast_VDI2736MetalPlasticRateableMesh",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VDI2736MetalPlasticRateableMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "VDI2736MetalPlasticRateableMesh._Cast_VDI2736MetalPlasticRateableMesh":
        return self._Cast_VDI2736MetalPlasticRateableMesh(self)
