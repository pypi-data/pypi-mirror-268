"""KlingelnbergCycloPalloidHypoidGearSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2544
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidHypoidGearSet"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _983
    from mastapy.system_model.part_model.gears import _2545, _2531, _2539
    from mastapy.system_model.connections_and_sockets.gears import _2326
    from mastapy.system_model.part_model import _2483, _2441, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSet",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearSet")


class KlingelnbergCycloPalloidHypoidGearSet(
    _2544.KlingelnbergCycloPalloidConicalGearSet
):
    """KlingelnbergCycloPalloidHypoidGearSet

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearSet"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSet:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSet to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSet._Cast_KlingelnbergCycloPalloidHypoidGearSet",
            parent: "KlingelnbergCycloPalloidHypoidGearSet",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(
            self: "KlingelnbergCycloPalloidHypoidGearSet._Cast_KlingelnbergCycloPalloidHypoidGearSet",
        ) -> "_2544.KlingelnbergCycloPalloidConicalGearSet":
            return self._parent._cast(_2544.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def conical_gear_set(
            self: "KlingelnbergCycloPalloidHypoidGearSet._Cast_KlingelnbergCycloPalloidHypoidGearSet",
        ) -> "_2531.ConicalGearSet":
            from mastapy.system_model.part_model.gears import _2531

            return self._parent._cast(_2531.ConicalGearSet)

        @property
        def gear_set(
            self: "KlingelnbergCycloPalloidHypoidGearSet._Cast_KlingelnbergCycloPalloidHypoidGearSet",
        ) -> "_2539.GearSet":
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.GearSet)

        @property
        def specialised_assembly(
            self: "KlingelnbergCycloPalloidHypoidGearSet._Cast_KlingelnbergCycloPalloidHypoidGearSet",
        ) -> "_2483.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2483

            return self._parent._cast(_2483.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "KlingelnbergCycloPalloidHypoidGearSet._Cast_KlingelnbergCycloPalloidHypoidGearSet",
        ) -> "_2441.AbstractAssembly":
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.AbstractAssembly)

        @property
        def part(
            self: "KlingelnbergCycloPalloidHypoidGearSet._Cast_KlingelnbergCycloPalloidHypoidGearSet",
        ) -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "KlingelnbergCycloPalloidHypoidGearSet._Cast_KlingelnbergCycloPalloidHypoidGearSet",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(
            self: "KlingelnbergCycloPalloidHypoidGearSet._Cast_KlingelnbergCycloPalloidHypoidGearSet",
        ) -> "KlingelnbergCycloPalloidHypoidGearSet":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSet._Cast_KlingelnbergCycloPalloidHypoidGearSet",
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
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSet.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def klingelnberg_conical_gear_set_design(
        self: Self,
    ) -> "_983.KlingelnbergCycloPalloidHypoidGearSetDesign":
        """mastapy.gears.gear_designs.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_design(
        self: Self,
    ) -> "_983.KlingelnbergCycloPalloidHypoidGearSetDesign":
        """mastapy.gears.gear_designs.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears(
        self: Self,
    ) -> "List[_2545.KlingelnbergCycloPalloidHypoidGear]":
        """List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes(
        self: Self,
    ) -> "List[_2326.KlingelnbergCycloPalloidHypoidGearMesh]":
        """List[mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSet._Cast_KlingelnbergCycloPalloidHypoidGearSet":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSet(self)
