"""GearDesignComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Any, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_DESIGN_COMPONENT = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns", "GearDesignComponent"
)

if TYPE_CHECKING:
    from mastapy.utility.scripting import _1748
    from mastapy.gears.gear_designs import _951, _953, _954
    from mastapy.gears.gear_designs.zerol_bevel import _956, _957, _958, _959
    from mastapy.gears.gear_designs.worm import _960, _961, _962, _963, _964
    from mastapy.gears.gear_designs.straight_bevel import _965, _966, _967, _968
    from mastapy.gears.gear_designs.straight_bevel_diff import _969, _970, _971, _972
    from mastapy.gears.gear_designs.spiral_bevel import _973, _974, _975, _976
    from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import (
        _977,
        _978,
        _979,
        _980,
    )
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _981, _982, _983, _984
    from mastapy.gears.gear_designs.klingelnberg_conical import _985, _986, _987, _988
    from mastapy.gears.gear_designs.hypoid import _989, _990, _991, _992
    from mastapy.gears.gear_designs.face import _993, _995, _998, _999, _1001
    from mastapy.gears.gear_designs.cylindrical import _1016, _1022, _1032, _1045, _1046
    from mastapy.gears.gear_designs.conical import _1160, _1161, _1162, _1165
    from mastapy.gears.gear_designs.concept import _1182, _1183, _1184
    from mastapy.gears.gear_designs.bevel import _1186, _1187, _1188, _1189
    from mastapy.gears.gear_designs.agma_gleason_conical import (
        _1199,
        _1200,
        _1201,
        _1202,
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearDesignComponent",)


Self = TypeVar("Self", bound="GearDesignComponent")


class GearDesignComponent(_0.APIBase):
    """GearDesignComponent

    This is a mastapy class.
    """

    TYPE = _GEAR_DESIGN_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearDesignComponent")

    class _Cast_GearDesignComponent:
        """Special nested class for casting GearDesignComponent to subclasses."""

        def __init__(
            self: "GearDesignComponent._Cast_GearDesignComponent",
            parent: "GearDesignComponent",
        ):
            self._parent = parent

        @property
        def gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_951.GearDesign":
            from mastapy.gears.gear_designs import _951

            return self._parent._cast(_951.GearDesign)

        @property
        def gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_953.GearMeshDesign":
            from mastapy.gears.gear_designs import _953

            return self._parent._cast(_953.GearMeshDesign)

        @property
        def gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_954.GearSetDesign":
            from mastapy.gears.gear_designs import _954

            return self._parent._cast(_954.GearSetDesign)

        @property
        def zerol_bevel_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_956.ZerolBevelGearDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _956

            return self._parent._cast(_956.ZerolBevelGearDesign)

        @property
        def zerol_bevel_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_957.ZerolBevelGearMeshDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _957

            return self._parent._cast(_957.ZerolBevelGearMeshDesign)

        @property
        def zerol_bevel_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_958.ZerolBevelGearSetDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _958

            return self._parent._cast(_958.ZerolBevelGearSetDesign)

        @property
        def zerol_bevel_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_959.ZerolBevelMeshedGearDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _959

            return self._parent._cast(_959.ZerolBevelMeshedGearDesign)

        @property
        def worm_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_960.WormDesign":
            from mastapy.gears.gear_designs.worm import _960

            return self._parent._cast(_960.WormDesign)

        @property
        def worm_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_961.WormGearDesign":
            from mastapy.gears.gear_designs.worm import _961

            return self._parent._cast(_961.WormGearDesign)

        @property
        def worm_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_962.WormGearMeshDesign":
            from mastapy.gears.gear_designs.worm import _962

            return self._parent._cast(_962.WormGearMeshDesign)

        @property
        def worm_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_963.WormGearSetDesign":
            from mastapy.gears.gear_designs.worm import _963

            return self._parent._cast(_963.WormGearSetDesign)

        @property
        def worm_wheel_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_964.WormWheelDesign":
            from mastapy.gears.gear_designs.worm import _964

            return self._parent._cast(_964.WormWheelDesign)

        @property
        def straight_bevel_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_965.StraightBevelGearDesign":
            from mastapy.gears.gear_designs.straight_bevel import _965

            return self._parent._cast(_965.StraightBevelGearDesign)

        @property
        def straight_bevel_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_966.StraightBevelGearMeshDesign":
            from mastapy.gears.gear_designs.straight_bevel import _966

            return self._parent._cast(_966.StraightBevelGearMeshDesign)

        @property
        def straight_bevel_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_967.StraightBevelGearSetDesign":
            from mastapy.gears.gear_designs.straight_bevel import _967

            return self._parent._cast(_967.StraightBevelGearSetDesign)

        @property
        def straight_bevel_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_968.StraightBevelMeshedGearDesign":
            from mastapy.gears.gear_designs.straight_bevel import _968

            return self._parent._cast(_968.StraightBevelMeshedGearDesign)

        @property
        def straight_bevel_diff_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_969.StraightBevelDiffGearDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _969

            return self._parent._cast(_969.StraightBevelDiffGearDesign)

        @property
        def straight_bevel_diff_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_970.StraightBevelDiffGearMeshDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _970

            return self._parent._cast(_970.StraightBevelDiffGearMeshDesign)

        @property
        def straight_bevel_diff_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_971.StraightBevelDiffGearSetDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _971

            return self._parent._cast(_971.StraightBevelDiffGearSetDesign)

        @property
        def straight_bevel_diff_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_972.StraightBevelDiffMeshedGearDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _972

            return self._parent._cast(_972.StraightBevelDiffMeshedGearDesign)

        @property
        def spiral_bevel_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_973.SpiralBevelGearDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _973

            return self._parent._cast(_973.SpiralBevelGearDesign)

        @property
        def spiral_bevel_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_974.SpiralBevelGearMeshDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _974

            return self._parent._cast(_974.SpiralBevelGearMeshDesign)

        @property
        def spiral_bevel_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_975.SpiralBevelGearSetDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _975

            return self._parent._cast(_975.SpiralBevelGearSetDesign)

        @property
        def spiral_bevel_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_976.SpiralBevelMeshedGearDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _976

            return self._parent._cast(_976.SpiralBevelMeshedGearDesign)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_977.KlingelnbergCycloPalloidSpiralBevelGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _977

            return self._parent._cast(
                _977.KlingelnbergCycloPalloidSpiralBevelGearDesign
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_978.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign":
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _978

            return self._parent._cast(
                _978.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_979.KlingelnbergCycloPalloidSpiralBevelGearSetDesign":
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _979

            return self._parent._cast(
                _979.KlingelnbergCycloPalloidSpiralBevelGearSetDesign
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_980.KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _980

            return self._parent._cast(
                _980.KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_981.KlingelnbergCycloPalloidHypoidGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _981

            return self._parent._cast(_981.KlingelnbergCycloPalloidHypoidGearDesign)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_982.KlingelnbergCycloPalloidHypoidGearMeshDesign":
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _982

            return self._parent._cast(_982.KlingelnbergCycloPalloidHypoidGearMeshDesign)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_983.KlingelnbergCycloPalloidHypoidGearSetDesign":
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _983

            return self._parent._cast(_983.KlingelnbergCycloPalloidHypoidGearSetDesign)

        @property
        def klingelnberg_cyclo_palloid_hypoid_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_984.KlingelnbergCycloPalloidHypoidMeshedGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _984

            return self._parent._cast(
                _984.KlingelnbergCycloPalloidHypoidMeshedGearDesign
            )

        @property
        def klingelnberg_conical_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_985.KlingelnbergConicalGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_conical import _985

            return self._parent._cast(_985.KlingelnbergConicalGearDesign)

        @property
        def klingelnberg_conical_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_986.KlingelnbergConicalGearMeshDesign":
            from mastapy.gears.gear_designs.klingelnberg_conical import _986

            return self._parent._cast(_986.KlingelnbergConicalGearMeshDesign)

        @property
        def klingelnberg_conical_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_987.KlingelnbergConicalGearSetDesign":
            from mastapy.gears.gear_designs.klingelnberg_conical import _987

            return self._parent._cast(_987.KlingelnbergConicalGearSetDesign)

        @property
        def klingelnberg_conical_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_988.KlingelnbergConicalMeshedGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_conical import _988

            return self._parent._cast(_988.KlingelnbergConicalMeshedGearDesign)

        @property
        def hypoid_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_989.HypoidGearDesign":
            from mastapy.gears.gear_designs.hypoid import _989

            return self._parent._cast(_989.HypoidGearDesign)

        @property
        def hypoid_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_990.HypoidGearMeshDesign":
            from mastapy.gears.gear_designs.hypoid import _990

            return self._parent._cast(_990.HypoidGearMeshDesign)

        @property
        def hypoid_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_991.HypoidGearSetDesign":
            from mastapy.gears.gear_designs.hypoid import _991

            return self._parent._cast(_991.HypoidGearSetDesign)

        @property
        def hypoid_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_992.HypoidMeshedGearDesign":
            from mastapy.gears.gear_designs.hypoid import _992

            return self._parent._cast(_992.HypoidMeshedGearDesign)

        @property
        def face_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_993.FaceGearDesign":
            from mastapy.gears.gear_designs.face import _993

            return self._parent._cast(_993.FaceGearDesign)

        @property
        def face_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_995.FaceGearMeshDesign":
            from mastapy.gears.gear_designs.face import _995

            return self._parent._cast(_995.FaceGearMeshDesign)

        @property
        def face_gear_pinion_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_998.FaceGearPinionDesign":
            from mastapy.gears.gear_designs.face import _998

            return self._parent._cast(_998.FaceGearPinionDesign)

        @property
        def face_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_999.FaceGearSetDesign":
            from mastapy.gears.gear_designs.face import _999

            return self._parent._cast(_999.FaceGearSetDesign)

        @property
        def face_gear_wheel_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1001.FaceGearWheelDesign":
            from mastapy.gears.gear_designs.face import _1001

            return self._parent._cast(_1001.FaceGearWheelDesign)

        @property
        def cylindrical_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1016.CylindricalGearDesign":
            from mastapy.gears.gear_designs.cylindrical import _1016

            return self._parent._cast(_1016.CylindricalGearDesign)

        @property
        def cylindrical_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1022.CylindricalGearMeshDesign":
            from mastapy.gears.gear_designs.cylindrical import _1022

            return self._parent._cast(_1022.CylindricalGearMeshDesign)

        @property
        def cylindrical_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1032.CylindricalGearSetDesign":
            from mastapy.gears.gear_designs.cylindrical import _1032

            return self._parent._cast(_1032.CylindricalGearSetDesign)

        @property
        def cylindrical_planetary_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1045.CylindricalPlanetaryGearSetDesign":
            from mastapy.gears.gear_designs.cylindrical import _1045

            return self._parent._cast(_1045.CylindricalPlanetaryGearSetDesign)

        @property
        def cylindrical_planet_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1046.CylindricalPlanetGearDesign":
            from mastapy.gears.gear_designs.cylindrical import _1046

            return self._parent._cast(_1046.CylindricalPlanetGearDesign)

        @property
        def conical_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1160.ConicalGearDesign":
            from mastapy.gears.gear_designs.conical import _1160

            return self._parent._cast(_1160.ConicalGearDesign)

        @property
        def conical_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1161.ConicalGearMeshDesign":
            from mastapy.gears.gear_designs.conical import _1161

            return self._parent._cast(_1161.ConicalGearMeshDesign)

        @property
        def conical_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1162.ConicalGearSetDesign":
            from mastapy.gears.gear_designs.conical import _1162

            return self._parent._cast(_1162.ConicalGearSetDesign)

        @property
        def conical_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1165.ConicalMeshedGearDesign":
            from mastapy.gears.gear_designs.conical import _1165

            return self._parent._cast(_1165.ConicalMeshedGearDesign)

        @property
        def concept_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1182.ConceptGearDesign":
            from mastapy.gears.gear_designs.concept import _1182

            return self._parent._cast(_1182.ConceptGearDesign)

        @property
        def concept_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1183.ConceptGearMeshDesign":
            from mastapy.gears.gear_designs.concept import _1183

            return self._parent._cast(_1183.ConceptGearMeshDesign)

        @property
        def concept_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1184.ConceptGearSetDesign":
            from mastapy.gears.gear_designs.concept import _1184

            return self._parent._cast(_1184.ConceptGearSetDesign)

        @property
        def bevel_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1186.BevelGearDesign":
            from mastapy.gears.gear_designs.bevel import _1186

            return self._parent._cast(_1186.BevelGearDesign)

        @property
        def bevel_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1187.BevelGearMeshDesign":
            from mastapy.gears.gear_designs.bevel import _1187

            return self._parent._cast(_1187.BevelGearMeshDesign)

        @property
        def bevel_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1188.BevelGearSetDesign":
            from mastapy.gears.gear_designs.bevel import _1188

            return self._parent._cast(_1188.BevelGearSetDesign)

        @property
        def bevel_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1189.BevelMeshedGearDesign":
            from mastapy.gears.gear_designs.bevel import _1189

            return self._parent._cast(_1189.BevelMeshedGearDesign)

        @property
        def agma_gleason_conical_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1199.AGMAGleasonConicalGearDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1199

            return self._parent._cast(_1199.AGMAGleasonConicalGearDesign)

        @property
        def agma_gleason_conical_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1200.AGMAGleasonConicalGearMeshDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1200

            return self._parent._cast(_1200.AGMAGleasonConicalGearMeshDesign)

        @property
        def agma_gleason_conical_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1201.AGMAGleasonConicalGearSetDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1201

            return self._parent._cast(_1201.AGMAGleasonConicalGearSetDesign)

        @property
        def agma_gleason_conical_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "_1202.AGMAGleasonConicalMeshedGearDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1202

            return self._parent._cast(_1202.AGMAGleasonConicalMeshedGearDesign)

        @property
        def gear_design_component(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "GearDesignComponent":
            return self._parent

        def __getattr__(
            self: "GearDesignComponent._Cast_GearDesignComponent", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearDesignComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def user_specified_data(self: Self) -> "_1748.UserSpecifiedData":
        """mastapy.utility.scripting.UserSpecifiedData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserSpecifiedData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    def dispose(self: Self):
        """Method does not return."""
        self.wrapped.Dispose()

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    def __enter__(self: Self):
        return self

    def __exit__(self: Self, exception_type: Any, exception_value: Any, traceback: Any):
        self.dispose()

    @property
    def cast_to(self: Self) -> "GearDesignComponent._Cast_GearDesignComponent":
        return self._Cast_GearDesignComponent(self)
