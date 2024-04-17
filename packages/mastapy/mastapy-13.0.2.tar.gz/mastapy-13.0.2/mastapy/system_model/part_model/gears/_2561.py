"""ZerolBevelGearSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2527
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ZerolBevelGearSet"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.zerol_bevel import _958
    from mastapy.system_model.part_model.gears import _2560, _2521, _2531, _2539
    from mastapy.system_model.connections_and_sockets.gears import _2338
    from mastapy.system_model.part_model import _2483, _2441, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSet",)


Self = TypeVar("Self", bound="ZerolBevelGearSet")


class ZerolBevelGearSet(_2527.BevelGearSet):
    """ZerolBevelGearSet

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearSet")

    class _Cast_ZerolBevelGearSet:
        """Special nested class for casting ZerolBevelGearSet to subclasses."""

        def __init__(
            self: "ZerolBevelGearSet._Cast_ZerolBevelGearSet",
            parent: "ZerolBevelGearSet",
        ):
            self._parent = parent

        @property
        def bevel_gear_set(
            self: "ZerolBevelGearSet._Cast_ZerolBevelGearSet",
        ) -> "_2527.BevelGearSet":
            return self._parent._cast(_2527.BevelGearSet)

        @property
        def agma_gleason_conical_gear_set(
            self: "ZerolBevelGearSet._Cast_ZerolBevelGearSet",
        ) -> "_2521.AGMAGleasonConicalGearSet":
            from mastapy.system_model.part_model.gears import _2521

            return self._parent._cast(_2521.AGMAGleasonConicalGearSet)

        @property
        def conical_gear_set(
            self: "ZerolBevelGearSet._Cast_ZerolBevelGearSet",
        ) -> "_2531.ConicalGearSet":
            from mastapy.system_model.part_model.gears import _2531

            return self._parent._cast(_2531.ConicalGearSet)

        @property
        def gear_set(
            self: "ZerolBevelGearSet._Cast_ZerolBevelGearSet",
        ) -> "_2539.GearSet":
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.GearSet)

        @property
        def specialised_assembly(
            self: "ZerolBevelGearSet._Cast_ZerolBevelGearSet",
        ) -> "_2483.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2483

            return self._parent._cast(_2483.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "ZerolBevelGearSet._Cast_ZerolBevelGearSet",
        ) -> "_2441.AbstractAssembly":
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.AbstractAssembly)

        @property
        def part(self: "ZerolBevelGearSet._Cast_ZerolBevelGearSet") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "ZerolBevelGearSet._Cast_ZerolBevelGearSet",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def zerol_bevel_gear_set(
            self: "ZerolBevelGearSet._Cast_ZerolBevelGearSet",
        ) -> "ZerolBevelGearSet":
            return self._parent

        def __getattr__(self: "ZerolBevelGearSet._Cast_ZerolBevelGearSet", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ZerolBevelGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_set_design(self: Self) -> "_958.ZerolBevelGearSetDesign":
        """mastapy.gears.gear_designs.zerol_bevel.ZerolBevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def zerol_bevel_gear_set_design(self: Self) -> "_958.ZerolBevelGearSetDesign":
        """mastapy.gears.gear_designs.zerol_bevel.ZerolBevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def zerol_bevel_gears(self: Self) -> "List[_2560.ZerolBevelGear]":
        """List[mastapy.system_model.part_model.gears.ZerolBevelGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes(self: Self) -> "List[_2338.ZerolBevelGearMesh]":
        """List[mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ZerolBevelGearSet._Cast_ZerolBevelGearSet":
        return self._Cast_ZerolBevelGearSet(self)
