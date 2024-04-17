"""VDI2736PlasticPlasticRateableMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _496
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VDI2736_PLASTIC_PLASTIC_RATEABLE_MESH = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.PlasticVDI2736",
    "VDI2736PlasticPlasticRateableMesh",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.iso6336 import _526
    from mastapy.gears.rating.cylindrical import _474
    from mastapy.gears.rating import _370


__docformat__ = "restructuredtext en"
__all__ = ("VDI2736PlasticPlasticRateableMesh",)


Self = TypeVar("Self", bound="VDI2736PlasticPlasticRateableMesh")


class VDI2736PlasticPlasticRateableMesh(_496.PlasticGearVDI2736AbstractRateableMesh):
    """VDI2736PlasticPlasticRateableMesh

    This is a mastapy class.
    """

    TYPE = _VDI2736_PLASTIC_PLASTIC_RATEABLE_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VDI2736PlasticPlasticRateableMesh")

    class _Cast_VDI2736PlasticPlasticRateableMesh:
        """Special nested class for casting VDI2736PlasticPlasticRateableMesh to subclasses."""

        def __init__(
            self: "VDI2736PlasticPlasticRateableMesh._Cast_VDI2736PlasticPlasticRateableMesh",
            parent: "VDI2736PlasticPlasticRateableMesh",
        ):
            self._parent = parent

        @property
        def plastic_gear_vdi2736_abstract_rateable_mesh(
            self: "VDI2736PlasticPlasticRateableMesh._Cast_VDI2736PlasticPlasticRateableMesh",
        ) -> "_496.PlasticGearVDI2736AbstractRateableMesh":
            return self._parent._cast(_496.PlasticGearVDI2736AbstractRateableMesh)

        @property
        def iso6336_rateable_mesh(
            self: "VDI2736PlasticPlasticRateableMesh._Cast_VDI2736PlasticPlasticRateableMesh",
        ) -> "_526.ISO6336RateableMesh":
            from mastapy.gears.rating.cylindrical.iso6336 import _526

            return self._parent._cast(_526.ISO6336RateableMesh)

        @property
        def cylindrical_rateable_mesh(
            self: "VDI2736PlasticPlasticRateableMesh._Cast_VDI2736PlasticPlasticRateableMesh",
        ) -> "_474.CylindricalRateableMesh":
            from mastapy.gears.rating.cylindrical import _474

            return self._parent._cast(_474.CylindricalRateableMesh)

        @property
        def rateable_mesh(
            self: "VDI2736PlasticPlasticRateableMesh._Cast_VDI2736PlasticPlasticRateableMesh",
        ) -> "_370.RateableMesh":
            from mastapy.gears.rating import _370

            return self._parent._cast(_370.RateableMesh)

        @property
        def vdi2736_plastic_plastic_rateable_mesh(
            self: "VDI2736PlasticPlasticRateableMesh._Cast_VDI2736PlasticPlasticRateableMesh",
        ) -> "VDI2736PlasticPlasticRateableMesh":
            return self._parent

        def __getattr__(
            self: "VDI2736PlasticPlasticRateableMesh._Cast_VDI2736PlasticPlasticRateableMesh",
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
        self: Self, instance_to_wrap: "VDI2736PlasticPlasticRateableMesh.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "VDI2736PlasticPlasticRateableMesh._Cast_VDI2736PlasticPlasticRateableMesh":
        return self._Cast_VDI2736PlasticPlasticRateableMesh(self)
