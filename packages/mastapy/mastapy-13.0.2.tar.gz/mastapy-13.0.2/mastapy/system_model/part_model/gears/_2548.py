"""KlingelnbergCycloPalloidSpiralBevelGearSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2544
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears",
    "KlingelnbergCycloPalloidSpiralBevelGearSet",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _979
    from mastapy.system_model.part_model.gears import _2547, _2531, _2539
    from mastapy.system_model.connections_and_sockets.gears import _2327
    from mastapy.system_model.part_model import _2483, _2441, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSet",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelGearSet")


class KlingelnbergCycloPalloidSpiralBevelGearSet(
    _2544.KlingelnbergCycloPalloidConicalGearSet
):
    """KlingelnbergCycloPalloidSpiralBevelGearSet

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSet"
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSet:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSet to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSet._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSet",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSet._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet",
        ) -> "_2544.KlingelnbergCycloPalloidConicalGearSet":
            return self._parent._cast(_2544.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def conical_gear_set(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSet._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet",
        ) -> "_2531.ConicalGearSet":
            from mastapy.system_model.part_model.gears import _2531

            return self._parent._cast(_2531.ConicalGearSet)

        @property
        def gear_set(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSet._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet",
        ) -> "_2539.GearSet":
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.GearSet)

        @property
        def specialised_assembly(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSet._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet",
        ) -> "_2483.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2483

            return self._parent._cast(_2483.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSet._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet",
        ) -> "_2441.AbstractAssembly":
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.AbstractAssembly)

        @property
        def part(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSet._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet",
        ) -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSet._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSet._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSet":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSet._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet",
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
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def klingelnberg_conical_gear_set_design(
        self: Self,
    ) -> "_979.KlingelnbergCycloPalloidSpiralBevelGearSetDesign":
        """mastapy.gears.gear_designs.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(
        self: Self,
    ) -> "_979.KlingelnbergCycloPalloidSpiralBevelGearSetDesign":
        """mastapy.gears.gear_designs.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears(
        self: Self,
    ) -> "List[_2547.KlingelnbergCycloPalloidSpiralBevelGear]":
        """List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes(
        self: Self,
    ) -> "List[_2327.KlingelnbergCycloPalloidSpiralBevelGearMesh]":
        """List[mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSet._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet(self)
