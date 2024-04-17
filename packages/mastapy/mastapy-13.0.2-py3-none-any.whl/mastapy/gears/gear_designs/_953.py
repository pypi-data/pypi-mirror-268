"""GearMeshDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.gear_designs import _952
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns", "GearMeshDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs import _951
    from mastapy.gears.gear_designs.zerol_bevel import _957
    from mastapy.gears.gear_designs.worm import _962
    from mastapy.gears.gear_designs.straight_bevel import _966
    from mastapy.gears.gear_designs.straight_bevel_diff import _970
    from mastapy.gears.gear_designs.spiral_bevel import _974
    from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _978
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _982
    from mastapy.gears.gear_designs.klingelnberg_conical import _986
    from mastapy.gears.gear_designs.hypoid import _990
    from mastapy.gears.gear_designs.face import _995
    from mastapy.gears.gear_designs.cylindrical import _1022
    from mastapy.gears.gear_designs.conical import _1161
    from mastapy.gears.gear_designs.concept import _1183
    from mastapy.gears.gear_designs.bevel import _1187
    from mastapy.gears.gear_designs.agma_gleason_conical import _1200


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshDesign",)


Self = TypeVar("Self", bound="GearMeshDesign")


class GearMeshDesign(_952.GearDesignComponent):
    """GearMeshDesign

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshDesign")

    class _Cast_GearMeshDesign:
        """Special nested class for casting GearMeshDesign to subclasses."""

        def __init__(
            self: "GearMeshDesign._Cast_GearMeshDesign", parent: "GearMeshDesign"
        ):
            self._parent = parent

        @property
        def gear_design_component(
            self: "GearMeshDesign._Cast_GearMeshDesign",
        ) -> "_952.GearDesignComponent":
            return self._parent._cast(_952.GearDesignComponent)

        @property
        def zerol_bevel_gear_mesh_design(
            self: "GearMeshDesign._Cast_GearMeshDesign",
        ) -> "_957.ZerolBevelGearMeshDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _957

            return self._parent._cast(_957.ZerolBevelGearMeshDesign)

        @property
        def worm_gear_mesh_design(
            self: "GearMeshDesign._Cast_GearMeshDesign",
        ) -> "_962.WormGearMeshDesign":
            from mastapy.gears.gear_designs.worm import _962

            return self._parent._cast(_962.WormGearMeshDesign)

        @property
        def straight_bevel_gear_mesh_design(
            self: "GearMeshDesign._Cast_GearMeshDesign",
        ) -> "_966.StraightBevelGearMeshDesign":
            from mastapy.gears.gear_designs.straight_bevel import _966

            return self._parent._cast(_966.StraightBevelGearMeshDesign)

        @property
        def straight_bevel_diff_gear_mesh_design(
            self: "GearMeshDesign._Cast_GearMeshDesign",
        ) -> "_970.StraightBevelDiffGearMeshDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _970

            return self._parent._cast(_970.StraightBevelDiffGearMeshDesign)

        @property
        def spiral_bevel_gear_mesh_design(
            self: "GearMeshDesign._Cast_GearMeshDesign",
        ) -> "_974.SpiralBevelGearMeshDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _974

            return self._parent._cast(_974.SpiralBevelGearMeshDesign)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_design(
            self: "GearMeshDesign._Cast_GearMeshDesign",
        ) -> "_978.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign":
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _978

            return self._parent._cast(
                _978.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_design(
            self: "GearMeshDesign._Cast_GearMeshDesign",
        ) -> "_982.KlingelnbergCycloPalloidHypoidGearMeshDesign":
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _982

            return self._parent._cast(_982.KlingelnbergCycloPalloidHypoidGearMeshDesign)

        @property
        def klingelnberg_conical_gear_mesh_design(
            self: "GearMeshDesign._Cast_GearMeshDesign",
        ) -> "_986.KlingelnbergConicalGearMeshDesign":
            from mastapy.gears.gear_designs.klingelnberg_conical import _986

            return self._parent._cast(_986.KlingelnbergConicalGearMeshDesign)

        @property
        def hypoid_gear_mesh_design(
            self: "GearMeshDesign._Cast_GearMeshDesign",
        ) -> "_990.HypoidGearMeshDesign":
            from mastapy.gears.gear_designs.hypoid import _990

            return self._parent._cast(_990.HypoidGearMeshDesign)

        @property
        def face_gear_mesh_design(
            self: "GearMeshDesign._Cast_GearMeshDesign",
        ) -> "_995.FaceGearMeshDesign":
            from mastapy.gears.gear_designs.face import _995

            return self._parent._cast(_995.FaceGearMeshDesign)

        @property
        def cylindrical_gear_mesh_design(
            self: "GearMeshDesign._Cast_GearMeshDesign",
        ) -> "_1022.CylindricalGearMeshDesign":
            from mastapy.gears.gear_designs.cylindrical import _1022

            return self._parent._cast(_1022.CylindricalGearMeshDesign)

        @property
        def conical_gear_mesh_design(
            self: "GearMeshDesign._Cast_GearMeshDesign",
        ) -> "_1161.ConicalGearMeshDesign":
            from mastapy.gears.gear_designs.conical import _1161

            return self._parent._cast(_1161.ConicalGearMeshDesign)

        @property
        def concept_gear_mesh_design(
            self: "GearMeshDesign._Cast_GearMeshDesign",
        ) -> "_1183.ConceptGearMeshDesign":
            from mastapy.gears.gear_designs.concept import _1183

            return self._parent._cast(_1183.ConceptGearMeshDesign)

        @property
        def bevel_gear_mesh_design(
            self: "GearMeshDesign._Cast_GearMeshDesign",
        ) -> "_1187.BevelGearMeshDesign":
            from mastapy.gears.gear_designs.bevel import _1187

            return self._parent._cast(_1187.BevelGearMeshDesign)

        @property
        def agma_gleason_conical_gear_mesh_design(
            self: "GearMeshDesign._Cast_GearMeshDesign",
        ) -> "_1200.AGMAGleasonConicalGearMeshDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1200

            return self._parent._cast(_1200.AGMAGleasonConicalGearMeshDesign)

        @property
        def gear_mesh_design(
            self: "GearMeshDesign._Cast_GearMeshDesign",
        ) -> "GearMeshDesign":
            return self._parent

        def __getattr__(self: "GearMeshDesign._Cast_GearMeshDesign", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_contact_ratio_rating_for_nvh(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialContactRatioRatingForNVH

        if temp is None:
            return 0.0

        return temp

    @property
    def has_hunting_ratio(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasHuntingRatio

        if temp is None:
            return False

        return temp

    @property
    def highest_common_factor_of_teeth_numbers(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HighestCommonFactorOfTeethNumbers

        if temp is None:
            return 0

        return temp

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def speed_ratio_a_to_b(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpeedRatioAToB

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_ratio_a_to_b(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueRatioAToB

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_contact_ratio_rating_for_nvh(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseContactRatioRatingForNVH

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_and_axial_contact_ratio_rating_for_nvh(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseAndAxialContactRatioRatingForNVH

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_a(self: Self) -> "_951.GearDesign":
        """mastapy.gears.gear_designs.GearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b(self: Self) -> "_951.GearDesign":
        """mastapy.gears.gear_designs.GearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearMeshDesign._Cast_GearMeshDesign":
        return self._Cast_GearMeshDesign(self)
