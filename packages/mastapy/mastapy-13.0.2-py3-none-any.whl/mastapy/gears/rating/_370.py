"""RateableMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RATEABLE_MESH = python_net_import("SMT.MastaAPI.Gears.Rating", "RateableMesh")

if TYPE_CHECKING:
    from mastapy.gears.rating.klingelnberg_conical.kn3030 import _418
    from mastapy.gears.rating.iso_10300 import _430
    from mastapy.gears.rating.hypoid.standards import _447
    from mastapy.gears.rating.cylindrical import _474
    from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _496, _501, _502, _503
    from mastapy.gears.rating.cylindrical.iso6336 import _525, _526
    from mastapy.gears.rating.cylindrical.agma import _539
    from mastapy.gears.rating.conical import _550
    from mastapy.gears.rating.bevel.standards import _567
    from mastapy.gears.rating.agma_gleason_conical import _571


__docformat__ = "restructuredtext en"
__all__ = ("RateableMesh",)


Self = TypeVar("Self", bound="RateableMesh")


class RateableMesh(_0.APIBase):
    """RateableMesh

    This is a mastapy class.
    """

    TYPE = _RATEABLE_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RateableMesh")

    class _Cast_RateableMesh:
        """Special nested class for casting RateableMesh to subclasses."""

        def __init__(self: "RateableMesh._Cast_RateableMesh", parent: "RateableMesh"):
            self._parent = parent

        @property
        def klingelnberg_conical_rateable_mesh(
            self: "RateableMesh._Cast_RateableMesh",
        ) -> "_418.KlingelnbergConicalRateableMesh":
            from mastapy.gears.rating.klingelnberg_conical.kn3030 import _418

            return self._parent._cast(_418.KlingelnbergConicalRateableMesh)

        @property
        def iso10300_rateable_mesh(
            self: "RateableMesh._Cast_RateableMesh",
        ) -> "_430.ISO10300RateableMesh":
            from mastapy.gears.rating.iso_10300 import _430

            return self._parent._cast(_430.ISO10300RateableMesh)

        @property
        def hypoid_rateable_mesh(
            self: "RateableMesh._Cast_RateableMesh",
        ) -> "_447.HypoidRateableMesh":
            from mastapy.gears.rating.hypoid.standards import _447

            return self._parent._cast(_447.HypoidRateableMesh)

        @property
        def cylindrical_rateable_mesh(
            self: "RateableMesh._Cast_RateableMesh",
        ) -> "_474.CylindricalRateableMesh":
            from mastapy.gears.rating.cylindrical import _474

            return self._parent._cast(_474.CylindricalRateableMesh)

        @property
        def plastic_gear_vdi2736_abstract_rateable_mesh(
            self: "RateableMesh._Cast_RateableMesh",
        ) -> "_496.PlasticGearVDI2736AbstractRateableMesh":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _496

            return self._parent._cast(_496.PlasticGearVDI2736AbstractRateableMesh)

        @property
        def vdi2736_metal_plastic_rateable_mesh(
            self: "RateableMesh._Cast_RateableMesh",
        ) -> "_501.VDI2736MetalPlasticRateableMesh":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _501

            return self._parent._cast(_501.VDI2736MetalPlasticRateableMesh)

        @property
        def vdi2736_plastic_metal_rateable_mesh(
            self: "RateableMesh._Cast_RateableMesh",
        ) -> "_502.VDI2736PlasticMetalRateableMesh":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _502

            return self._parent._cast(_502.VDI2736PlasticMetalRateableMesh)

        @property
        def vdi2736_plastic_plastic_rateable_mesh(
            self: "RateableMesh._Cast_RateableMesh",
        ) -> "_503.VDI2736PlasticPlasticRateableMesh":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _503

            return self._parent._cast(_503.VDI2736PlasticPlasticRateableMesh)

        @property
        def iso6336_metal_rateable_mesh(
            self: "RateableMesh._Cast_RateableMesh",
        ) -> "_525.ISO6336MetalRateableMesh":
            from mastapy.gears.rating.cylindrical.iso6336 import _525

            return self._parent._cast(_525.ISO6336MetalRateableMesh)

        @property
        def iso6336_rateable_mesh(
            self: "RateableMesh._Cast_RateableMesh",
        ) -> "_526.ISO6336RateableMesh":
            from mastapy.gears.rating.cylindrical.iso6336 import _526

            return self._parent._cast(_526.ISO6336RateableMesh)

        @property
        def agma2101_rateable_mesh(
            self: "RateableMesh._Cast_RateableMesh",
        ) -> "_539.AGMA2101RateableMesh":
            from mastapy.gears.rating.cylindrical.agma import _539

            return self._parent._cast(_539.AGMA2101RateableMesh)

        @property
        def conical_rateable_mesh(
            self: "RateableMesh._Cast_RateableMesh",
        ) -> "_550.ConicalRateableMesh":
            from mastapy.gears.rating.conical import _550

            return self._parent._cast(_550.ConicalRateableMesh)

        @property
        def spiral_bevel_rateable_mesh(
            self: "RateableMesh._Cast_RateableMesh",
        ) -> "_567.SpiralBevelRateableMesh":
            from mastapy.gears.rating.bevel.standards import _567

            return self._parent._cast(_567.SpiralBevelRateableMesh)

        @property
        def agma_gleason_conical_rateable_mesh(
            self: "RateableMesh._Cast_RateableMesh",
        ) -> "_571.AGMAGleasonConicalRateableMesh":
            from mastapy.gears.rating.agma_gleason_conical import _571

            return self._parent._cast(_571.AGMAGleasonConicalRateableMesh)

        @property
        def rateable_mesh(self: "RateableMesh._Cast_RateableMesh") -> "RateableMesh":
            return self._parent

        def __getattr__(self: "RateableMesh._Cast_RateableMesh", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RateableMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "RateableMesh._Cast_RateableMesh":
        return self._Cast_RateableMesh(self)
