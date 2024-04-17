"""PlasticGearVDI2736AbstractRateableMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.cylindrical.iso6336 import _526
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLASTIC_GEAR_VDI2736_ABSTRACT_RATEABLE_MESH = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.PlasticVDI2736",
    "PlasticGearVDI2736AbstractRateableMesh",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _501, _502, _503
    from mastapy.gears.rating.cylindrical import _474
    from mastapy.gears.rating import _370


__docformat__ = "restructuredtext en"
__all__ = ("PlasticGearVDI2736AbstractRateableMesh",)


Self = TypeVar("Self", bound="PlasticGearVDI2736AbstractRateableMesh")


class PlasticGearVDI2736AbstractRateableMesh(_526.ISO6336RateableMesh):
    """PlasticGearVDI2736AbstractRateableMesh

    This is a mastapy class.
    """

    TYPE = _PLASTIC_GEAR_VDI2736_ABSTRACT_RATEABLE_MESH
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlasticGearVDI2736AbstractRateableMesh"
    )

    class _Cast_PlasticGearVDI2736AbstractRateableMesh:
        """Special nested class for casting PlasticGearVDI2736AbstractRateableMesh to subclasses."""

        def __init__(
            self: "PlasticGearVDI2736AbstractRateableMesh._Cast_PlasticGearVDI2736AbstractRateableMesh",
            parent: "PlasticGearVDI2736AbstractRateableMesh",
        ):
            self._parent = parent

        @property
        def iso6336_rateable_mesh(
            self: "PlasticGearVDI2736AbstractRateableMesh._Cast_PlasticGearVDI2736AbstractRateableMesh",
        ) -> "_526.ISO6336RateableMesh":
            return self._parent._cast(_526.ISO6336RateableMesh)

        @property
        def cylindrical_rateable_mesh(
            self: "PlasticGearVDI2736AbstractRateableMesh._Cast_PlasticGearVDI2736AbstractRateableMesh",
        ) -> "_474.CylindricalRateableMesh":
            from mastapy.gears.rating.cylindrical import _474

            return self._parent._cast(_474.CylindricalRateableMesh)

        @property
        def rateable_mesh(
            self: "PlasticGearVDI2736AbstractRateableMesh._Cast_PlasticGearVDI2736AbstractRateableMesh",
        ) -> "_370.RateableMesh":
            from mastapy.gears.rating import _370

            return self._parent._cast(_370.RateableMesh)

        @property
        def vdi2736_metal_plastic_rateable_mesh(
            self: "PlasticGearVDI2736AbstractRateableMesh._Cast_PlasticGearVDI2736AbstractRateableMesh",
        ) -> "_501.VDI2736MetalPlasticRateableMesh":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _501

            return self._parent._cast(_501.VDI2736MetalPlasticRateableMesh)

        @property
        def vdi2736_plastic_metal_rateable_mesh(
            self: "PlasticGearVDI2736AbstractRateableMesh._Cast_PlasticGearVDI2736AbstractRateableMesh",
        ) -> "_502.VDI2736PlasticMetalRateableMesh":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _502

            return self._parent._cast(_502.VDI2736PlasticMetalRateableMesh)

        @property
        def vdi2736_plastic_plastic_rateable_mesh(
            self: "PlasticGearVDI2736AbstractRateableMesh._Cast_PlasticGearVDI2736AbstractRateableMesh",
        ) -> "_503.VDI2736PlasticPlasticRateableMesh":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _503

            return self._parent._cast(_503.VDI2736PlasticPlasticRateableMesh)

        @property
        def plastic_gear_vdi2736_abstract_rateable_mesh(
            self: "PlasticGearVDI2736AbstractRateableMesh._Cast_PlasticGearVDI2736AbstractRateableMesh",
        ) -> "PlasticGearVDI2736AbstractRateableMesh":
            return self._parent

        def __getattr__(
            self: "PlasticGearVDI2736AbstractRateableMesh._Cast_PlasticGearVDI2736AbstractRateableMesh",
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
        self: Self, instance_to_wrap: "PlasticGearVDI2736AbstractRateableMesh.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PlasticGearVDI2736AbstractRateableMesh._Cast_PlasticGearVDI2736AbstractRateableMesh":
        return self._Cast_PlasticGearVDI2736AbstractRateableMesh(self)
