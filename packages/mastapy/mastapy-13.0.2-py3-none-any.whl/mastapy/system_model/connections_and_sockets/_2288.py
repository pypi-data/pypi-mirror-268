"""InterMountableComponentConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.connections_and_sockets import _2279
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "InterMountableComponentConnection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2275, _2280, _2299
    from mastapy.system_model.connections_and_sockets.gears import (
        _2306,
        _2308,
        _2310,
        _2312,
        _2314,
        _2316,
        _2318,
        _2320,
        _2322,
        _2325,
        _2326,
        _2327,
        _2330,
        _2332,
        _2334,
        _2336,
        _2338,
    )
    from mastapy.system_model.connections_and_sockets.cycloidal import _2348
    from mastapy.system_model.connections_and_sockets.couplings import (
        _2349,
        _2351,
        _2353,
        _2355,
        _2357,
        _2359,
    )
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnection",)


Self = TypeVar("Self", bound="InterMountableComponentConnection")


class InterMountableComponentConnection(_2279.Connection):
    """InterMountableComponentConnection

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InterMountableComponentConnection")

    class _Cast_InterMountableComponentConnection:
        """Special nested class for casting InterMountableComponentConnection to subclasses."""

        def __init__(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
            parent: "InterMountableComponentConnection",
        ):
            self._parent = parent

        @property
        def connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2279.Connection":
            return self._parent._cast(_2279.Connection)

        @property
        def design_entity(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def belt_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2275.BeltConnection":
            from mastapy.system_model.connections_and_sockets import _2275

            return self._parent._cast(_2275.BeltConnection)

        @property
        def cvt_belt_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2280.CVTBeltConnection":
            from mastapy.system_model.connections_and_sockets import _2280

            return self._parent._cast(_2280.CVTBeltConnection)

        @property
        def rolling_ring_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2299.RollingRingConnection":
            from mastapy.system_model.connections_and_sockets import _2299

            return self._parent._cast(_2299.RollingRingConnection)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2306.AGMAGleasonConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2306

            return self._parent._cast(_2306.AGMAGleasonConicalGearMesh)

        @property
        def bevel_differential_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2308.BevelDifferentialGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2308

            return self._parent._cast(_2308.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2310.BevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2310

            return self._parent._cast(_2310.BevelGearMesh)

        @property
        def concept_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2312.ConceptGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2312

            return self._parent._cast(_2312.ConceptGearMesh)

        @property
        def conical_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2314.ConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2314

            return self._parent._cast(_2314.ConicalGearMesh)

        @property
        def cylindrical_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2316.CylindricalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2316

            return self._parent._cast(_2316.CylindricalGearMesh)

        @property
        def face_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2318.FaceGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2318

            return self._parent._cast(_2318.FaceGearMesh)

        @property
        def gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2320.GearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2320

            return self._parent._cast(_2320.GearMesh)

        @property
        def hypoid_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2322.HypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2322

            return self._parent._cast(_2322.HypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2325.KlingelnbergCycloPalloidConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2325

            return self._parent._cast(_2325.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2326.KlingelnbergCycloPalloidHypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2326

            return self._parent._cast(_2326.KlingelnbergCycloPalloidHypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2327.KlingelnbergCycloPalloidSpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2327

            return self._parent._cast(_2327.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        @property
        def spiral_bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2330.SpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2330

            return self._parent._cast(_2330.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2332.StraightBevelDiffGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2332

            return self._parent._cast(_2332.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2334.StraightBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2334

            return self._parent._cast(_2334.StraightBevelGearMesh)

        @property
        def worm_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2336.WormGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2336

            return self._parent._cast(_2336.WormGearMesh)

        @property
        def zerol_bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2338.ZerolBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2338

            return self._parent._cast(_2338.ZerolBevelGearMesh)

        @property
        def ring_pins_to_disc_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2348.RingPinsToDiscConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2348

            return self._parent._cast(_2348.RingPinsToDiscConnection)

        @property
        def clutch_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2349.ClutchConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2349

            return self._parent._cast(_2349.ClutchConnection)

        @property
        def concept_coupling_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2351.ConceptCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2351

            return self._parent._cast(_2351.ConceptCouplingConnection)

        @property
        def coupling_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2353.CouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2353

            return self._parent._cast(_2353.CouplingConnection)

        @property
        def part_to_part_shear_coupling_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2355.PartToPartShearCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2355

            return self._parent._cast(_2355.PartToPartShearCouplingConnection)

        @property
        def spring_damper_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2357.SpringDamperConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2357

            return self._parent._cast(_2357.SpringDamperConnection)

        @property
        def torque_converter_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2359.TorqueConverterConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2359

            return self._parent._cast(_2359.TorqueConverterConnection)

        @property
        def inter_mountable_component_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "InterMountableComponentConnection":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
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
        self: Self, instance_to_wrap: "InterMountableComponentConnection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_modal_damping_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AdditionalModalDampingRatio

        if temp is None:
            return 0.0

        return temp

    @additional_modal_damping_ratio.setter
    @enforce_parameter_types
    def additional_modal_damping_ratio(self: Self, value: "float"):
        self.wrapped.AdditionalModalDampingRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(
        self: Self,
    ) -> "InterMountableComponentConnection._Cast_InterMountableComponentConnection":
        return self._Cast_InterMountableComponentConnection(self)
