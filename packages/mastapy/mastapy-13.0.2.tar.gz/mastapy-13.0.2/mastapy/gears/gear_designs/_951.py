"""GearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.gear_designs import _952
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_DESIGN = python_net_import("SMT.MastaAPI.Gears.GearDesigns", "GearDesign")

if TYPE_CHECKING:
    from mastapy.gears.fe_model import _1203
    from mastapy.gears.gear_designs.zerol_bevel import _956
    from mastapy.gears.gear_designs.worm import _960, _961, _964
    from mastapy.gears.gear_designs.straight_bevel import _965
    from mastapy.gears.gear_designs.straight_bevel_diff import _969
    from mastapy.gears.gear_designs.spiral_bevel import _973
    from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _977
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _981
    from mastapy.gears.gear_designs.klingelnberg_conical import _985
    from mastapy.gears.gear_designs.hypoid import _989
    from mastapy.gears.gear_designs.face import _993, _998, _1001
    from mastapy.gears.gear_designs.cylindrical import _1016, _1046
    from mastapy.gears.gear_designs.conical import _1160
    from mastapy.gears.gear_designs.concept import _1182
    from mastapy.gears.gear_designs.bevel import _1186
    from mastapy.gears.gear_designs.agma_gleason_conical import _1199


__docformat__ = "restructuredtext en"
__all__ = ("GearDesign",)


Self = TypeVar("Self", bound="GearDesign")


class GearDesign(_952.GearDesignComponent):
    """GearDesign

    This is a mastapy class.
    """

    TYPE = _GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearDesign")

    class _Cast_GearDesign:
        """Special nested class for casting GearDesign to subclasses."""

        def __init__(self: "GearDesign._Cast_GearDesign", parent: "GearDesign"):
            self._parent = parent

        @property
        def gear_design_component(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_952.GearDesignComponent":
            return self._parent._cast(_952.GearDesignComponent)

        @property
        def zerol_bevel_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_956.ZerolBevelGearDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _956

            return self._parent._cast(_956.ZerolBevelGearDesign)

        @property
        def worm_design(self: "GearDesign._Cast_GearDesign") -> "_960.WormDesign":
            from mastapy.gears.gear_designs.worm import _960

            return self._parent._cast(_960.WormDesign)

        @property
        def worm_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_961.WormGearDesign":
            from mastapy.gears.gear_designs.worm import _961

            return self._parent._cast(_961.WormGearDesign)

        @property
        def worm_wheel_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_964.WormWheelDesign":
            from mastapy.gears.gear_designs.worm import _964

            return self._parent._cast(_964.WormWheelDesign)

        @property
        def straight_bevel_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_965.StraightBevelGearDesign":
            from mastapy.gears.gear_designs.straight_bevel import _965

            return self._parent._cast(_965.StraightBevelGearDesign)

        @property
        def straight_bevel_diff_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_969.StraightBevelDiffGearDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _969

            return self._parent._cast(_969.StraightBevelDiffGearDesign)

        @property
        def spiral_bevel_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_973.SpiralBevelGearDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _973

            return self._parent._cast(_973.SpiralBevelGearDesign)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_977.KlingelnbergCycloPalloidSpiralBevelGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _977

            return self._parent._cast(
                _977.KlingelnbergCycloPalloidSpiralBevelGearDesign
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_981.KlingelnbergCycloPalloidHypoidGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _981

            return self._parent._cast(_981.KlingelnbergCycloPalloidHypoidGearDesign)

        @property
        def klingelnberg_conical_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_985.KlingelnbergConicalGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_conical import _985

            return self._parent._cast(_985.KlingelnbergConicalGearDesign)

        @property
        def hypoid_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_989.HypoidGearDesign":
            from mastapy.gears.gear_designs.hypoid import _989

            return self._parent._cast(_989.HypoidGearDesign)

        @property
        def face_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_993.FaceGearDesign":
            from mastapy.gears.gear_designs.face import _993

            return self._parent._cast(_993.FaceGearDesign)

        @property
        def face_gear_pinion_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_998.FaceGearPinionDesign":
            from mastapy.gears.gear_designs.face import _998

            return self._parent._cast(_998.FaceGearPinionDesign)

        @property
        def face_gear_wheel_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_1001.FaceGearWheelDesign":
            from mastapy.gears.gear_designs.face import _1001

            return self._parent._cast(_1001.FaceGearWheelDesign)

        @property
        def cylindrical_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_1016.CylindricalGearDesign":
            from mastapy.gears.gear_designs.cylindrical import _1016

            return self._parent._cast(_1016.CylindricalGearDesign)

        @property
        def cylindrical_planet_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_1046.CylindricalPlanetGearDesign":
            from mastapy.gears.gear_designs.cylindrical import _1046

            return self._parent._cast(_1046.CylindricalPlanetGearDesign)

        @property
        def conical_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_1160.ConicalGearDesign":
            from mastapy.gears.gear_designs.conical import _1160

            return self._parent._cast(_1160.ConicalGearDesign)

        @property
        def concept_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_1182.ConceptGearDesign":
            from mastapy.gears.gear_designs.concept import _1182

            return self._parent._cast(_1182.ConceptGearDesign)

        @property
        def bevel_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_1186.BevelGearDesign":
            from mastapy.gears.gear_designs.bevel import _1186

            return self._parent._cast(_1186.BevelGearDesign)

        @property
        def agma_gleason_conical_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_1199.AGMAGleasonConicalGearDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1199

            return self._parent._cast(_1199.AGMAGleasonConicalGearDesign)

        @property
        def gear_design(self: "GearDesign._Cast_GearDesign") -> "GearDesign":
            return self._parent

        def __getattr__(self: "GearDesign._Cast_GearDesign", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def absolute_shaft_inner_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AbsoluteShaftInnerDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @face_width.setter
    @enforce_parameter_types
    def face_width(self: Self, value: "float"):
        self.wrapped.FaceWidth = float(value) if value is not None else 0.0

    @property
    def mass(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Mass

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def names_of_meshing_gears(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NamesOfMeshingGears

        if temp is None:
            return ""

        return temp

    @property
    def number_of_teeth(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfTeeth

        if temp is None:
            return 0

        return temp

    @number_of_teeth.setter
    @enforce_parameter_types
    def number_of_teeth(self: Self, value: "int"):
        self.wrapped.NumberOfTeeth = int(value) if value is not None else 0

    @property
    def number_of_teeth_maintaining_ratio(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfTeethMaintainingRatio

        if temp is None:
            return 0

        return temp

    @number_of_teeth_maintaining_ratio.setter
    @enforce_parameter_types
    def number_of_teeth_maintaining_ratio(self: Self, value: "int"):
        self.wrapped.NumberOfTeethMaintainingRatio = (
            int(value) if value is not None else 0
        )

    @property
    def shaft_inner_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftInnerDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def shaft_outer_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftOuterDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def tifffe_model(self: Self) -> "_1203.GearFEModel":
        """mastapy.gears.fe_model.GearFEModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TIFFFEModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearDesign._Cast_GearDesign":
        return self._Cast_GearDesign(self)
