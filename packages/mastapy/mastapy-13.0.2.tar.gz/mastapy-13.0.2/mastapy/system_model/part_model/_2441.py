"""AbstractAssembly"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.part_model import _2475
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractAssembly"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2451, _2440, _2450, _2461, _2481, _2483
    from mastapy.system_model.part_model.gears import (
        _2521,
        _2523,
        _2527,
        _2529,
        _2531,
        _2533,
        _2536,
        _2539,
        _2542,
        _2544,
        _2546,
        _2548,
        _2549,
        _2551,
        _2553,
        _2555,
        _2559,
        _2561,
    )
    from mastapy.system_model.part_model.cycloidal import _2575
    from mastapy.system_model.part_model.couplings import (
        _2583,
        _2585,
        _2588,
        _2591,
        _2594,
        _2596,
        _2605,
        _2608,
        _2610,
        _2615,
    )
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssembly",)


Self = TypeVar("Self", bound="AbstractAssembly")


class AbstractAssembly(_2475.Part):
    """AbstractAssembly

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssembly")

    class _Cast_AbstractAssembly:
        """Special nested class for casting AbstractAssembly to subclasses."""

        def __init__(
            self: "AbstractAssembly._Cast_AbstractAssembly", parent: "AbstractAssembly"
        ):
            self._parent = parent

        @property
        def part(self: "AbstractAssembly._Cast_AbstractAssembly") -> "_2475.Part":
            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def assembly(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2440.Assembly":
            from mastapy.system_model.part_model import _2440

            return self._parent._cast(_2440.Assembly)

        @property
        def bolted_joint(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2450.BoltedJoint":
            from mastapy.system_model.part_model import _2450

            return self._parent._cast(_2450.BoltedJoint)

        @property
        def flexible_pin_assembly(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2461.FlexiblePinAssembly":
            from mastapy.system_model.part_model import _2461

            return self._parent._cast(_2461.FlexiblePinAssembly)

        @property
        def root_assembly(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2481.RootAssembly":
            from mastapy.system_model.part_model import _2481

            return self._parent._cast(_2481.RootAssembly)

        @property
        def specialised_assembly(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2483.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2483

            return self._parent._cast(_2483.SpecialisedAssembly)

        @property
        def agma_gleason_conical_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2521.AGMAGleasonConicalGearSet":
            from mastapy.system_model.part_model.gears import _2521

            return self._parent._cast(_2521.AGMAGleasonConicalGearSet)

        @property
        def bevel_differential_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2523.BevelDifferentialGearSet":
            from mastapy.system_model.part_model.gears import _2523

            return self._parent._cast(_2523.BevelDifferentialGearSet)

        @property
        def bevel_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2527.BevelGearSet":
            from mastapy.system_model.part_model.gears import _2527

            return self._parent._cast(_2527.BevelGearSet)

        @property
        def concept_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2529.ConceptGearSet":
            from mastapy.system_model.part_model.gears import _2529

            return self._parent._cast(_2529.ConceptGearSet)

        @property
        def conical_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2531.ConicalGearSet":
            from mastapy.system_model.part_model.gears import _2531

            return self._parent._cast(_2531.ConicalGearSet)

        @property
        def cylindrical_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2533.CylindricalGearSet":
            from mastapy.system_model.part_model.gears import _2533

            return self._parent._cast(_2533.CylindricalGearSet)

        @property
        def face_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2536.FaceGearSet":
            from mastapy.system_model.part_model.gears import _2536

            return self._parent._cast(_2536.FaceGearSet)

        @property
        def gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2539.GearSet":
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.GearSet)

        @property
        def hypoid_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2542.HypoidGearSet":
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.HypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2544.KlingelnbergCycloPalloidConicalGearSet":
            from mastapy.system_model.part_model.gears import _2544

            return self._parent._cast(_2544.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2546.KlingelnbergCycloPalloidHypoidGearSet":
            from mastapy.system_model.part_model.gears import _2546

            return self._parent._cast(_2546.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2548.KlingelnbergCycloPalloidSpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2548

            return self._parent._cast(_2548.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def planetary_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2549.PlanetaryGearSet":
            from mastapy.system_model.part_model.gears import _2549

            return self._parent._cast(_2549.PlanetaryGearSet)

        @property
        def spiral_bevel_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2551.SpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2551

            return self._parent._cast(_2551.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2553.StraightBevelDiffGearSet":
            from mastapy.system_model.part_model.gears import _2553

            return self._parent._cast(_2553.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2555.StraightBevelGearSet":
            from mastapy.system_model.part_model.gears import _2555

            return self._parent._cast(_2555.StraightBevelGearSet)

        @property
        def worm_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2559.WormGearSet":
            from mastapy.system_model.part_model.gears import _2559

            return self._parent._cast(_2559.WormGearSet)

        @property
        def zerol_bevel_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2561.ZerolBevelGearSet":
            from mastapy.system_model.part_model.gears import _2561

            return self._parent._cast(_2561.ZerolBevelGearSet)

        @property
        def cycloidal_assembly(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2575.CycloidalAssembly":
            from mastapy.system_model.part_model.cycloidal import _2575

            return self._parent._cast(_2575.CycloidalAssembly)

        @property
        def belt_drive(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2583.BeltDrive":
            from mastapy.system_model.part_model.couplings import _2583

            return self._parent._cast(_2583.BeltDrive)

        @property
        def clutch(self: "AbstractAssembly._Cast_AbstractAssembly") -> "_2585.Clutch":
            from mastapy.system_model.part_model.couplings import _2585

            return self._parent._cast(_2585.Clutch)

        @property
        def concept_coupling(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2588.ConceptCoupling":
            from mastapy.system_model.part_model.couplings import _2588

            return self._parent._cast(_2588.ConceptCoupling)

        @property
        def coupling(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2591.Coupling":
            from mastapy.system_model.part_model.couplings import _2591

            return self._parent._cast(_2591.Coupling)

        @property
        def cvt(self: "AbstractAssembly._Cast_AbstractAssembly") -> "_2594.CVT":
            from mastapy.system_model.part_model.couplings import _2594

            return self._parent._cast(_2594.CVT)

        @property
        def part_to_part_shear_coupling(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2596.PartToPartShearCoupling":
            from mastapy.system_model.part_model.couplings import _2596

            return self._parent._cast(_2596.PartToPartShearCoupling)

        @property
        def rolling_ring_assembly(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2605.RollingRingAssembly":
            from mastapy.system_model.part_model.couplings import _2605

            return self._parent._cast(_2605.RollingRingAssembly)

        @property
        def spring_damper(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2608.SpringDamper":
            from mastapy.system_model.part_model.couplings import _2608

            return self._parent._cast(_2608.SpringDamper)

        @property
        def synchroniser(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2610.Synchroniser":
            from mastapy.system_model.part_model.couplings import _2610

            return self._parent._cast(_2610.Synchroniser)

        @property
        def torque_converter(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "_2615.TorqueConverter":
            from mastapy.system_model.part_model.couplings import _2615

            return self._parent._cast(_2615.TorqueConverter)

        @property
        def abstract_assembly(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "AbstractAssembly":
            return self._parent

        def __getattr__(self: "AbstractAssembly._Cast_AbstractAssembly", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractAssembly.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mass_of_assembly(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassOfAssembly

        if temp is None:
            return 0.0

        return temp

    @property
    def components_with_unknown_mass_properties(self: Self) -> "List[_2451.Component]":
        """List[mastapy.system_model.part_model.Component]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentsWithUnknownMassProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def components_with_zero_mass_properties(self: Self) -> "List[_2451.Component]":
        """List[mastapy.system_model.part_model.Component]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentsWithZeroMassProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "AbstractAssembly._Cast_AbstractAssembly":
        return self._Cast_AbstractAssembly(self)
