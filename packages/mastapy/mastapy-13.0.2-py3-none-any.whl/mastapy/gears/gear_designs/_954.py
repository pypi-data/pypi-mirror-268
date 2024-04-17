"""GearSetDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.gears.gear_designs import _952
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_GEAR_SET_DESIGN = python_net_import("SMT.MastaAPI.Gears.GearDesigns", "GearSetDesign")

if TYPE_CHECKING:
    from mastapy.gears.fe_model import _1206
    from mastapy.gears import _331
    from mastapy.gears.gear_designs import _951
    from mastapy.gears.gear_designs.zerol_bevel import _958
    from mastapy.gears.gear_designs.worm import _963
    from mastapy.gears.gear_designs.straight_bevel import _967
    from mastapy.gears.gear_designs.straight_bevel_diff import _971
    from mastapy.gears.gear_designs.spiral_bevel import _975
    from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _979
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _983
    from mastapy.gears.gear_designs.klingelnberg_conical import _987
    from mastapy.gears.gear_designs.hypoid import _991
    from mastapy.gears.gear_designs.face import _999
    from mastapy.gears.gear_designs.cylindrical import _1032, _1045
    from mastapy.gears.gear_designs.conical import _1162
    from mastapy.gears.gear_designs.concept import _1184
    from mastapy.gears.gear_designs.bevel import _1188
    from mastapy.gears.gear_designs.agma_gleason_conical import _1201


__docformat__ = "restructuredtext en"
__all__ = ("GearSetDesign",)


Self = TypeVar("Self", bound="GearSetDesign")


class GearSetDesign(_952.GearDesignComponent):
    """GearSetDesign

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetDesign")

    class _Cast_GearSetDesign:
        """Special nested class for casting GearSetDesign to subclasses."""

        def __init__(
            self: "GearSetDesign._Cast_GearSetDesign", parent: "GearSetDesign"
        ):
            self._parent = parent

        @property
        def gear_design_component(
            self: "GearSetDesign._Cast_GearSetDesign",
        ) -> "_952.GearDesignComponent":
            return self._parent._cast(_952.GearDesignComponent)

        @property
        def zerol_bevel_gear_set_design(
            self: "GearSetDesign._Cast_GearSetDesign",
        ) -> "_958.ZerolBevelGearSetDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _958

            return self._parent._cast(_958.ZerolBevelGearSetDesign)

        @property
        def worm_gear_set_design(
            self: "GearSetDesign._Cast_GearSetDesign",
        ) -> "_963.WormGearSetDesign":
            from mastapy.gears.gear_designs.worm import _963

            return self._parent._cast(_963.WormGearSetDesign)

        @property
        def straight_bevel_gear_set_design(
            self: "GearSetDesign._Cast_GearSetDesign",
        ) -> "_967.StraightBevelGearSetDesign":
            from mastapy.gears.gear_designs.straight_bevel import _967

            return self._parent._cast(_967.StraightBevelGearSetDesign)

        @property
        def straight_bevel_diff_gear_set_design(
            self: "GearSetDesign._Cast_GearSetDesign",
        ) -> "_971.StraightBevelDiffGearSetDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _971

            return self._parent._cast(_971.StraightBevelDiffGearSetDesign)

        @property
        def spiral_bevel_gear_set_design(
            self: "GearSetDesign._Cast_GearSetDesign",
        ) -> "_975.SpiralBevelGearSetDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _975

            return self._parent._cast(_975.SpiralBevelGearSetDesign)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(
            self: "GearSetDesign._Cast_GearSetDesign",
        ) -> "_979.KlingelnbergCycloPalloidSpiralBevelGearSetDesign":
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _979

            return self._parent._cast(
                _979.KlingelnbergCycloPalloidSpiralBevelGearSetDesign
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_design(
            self: "GearSetDesign._Cast_GearSetDesign",
        ) -> "_983.KlingelnbergCycloPalloidHypoidGearSetDesign":
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _983

            return self._parent._cast(_983.KlingelnbergCycloPalloidHypoidGearSetDesign)

        @property
        def klingelnberg_conical_gear_set_design(
            self: "GearSetDesign._Cast_GearSetDesign",
        ) -> "_987.KlingelnbergConicalGearSetDesign":
            from mastapy.gears.gear_designs.klingelnberg_conical import _987

            return self._parent._cast(_987.KlingelnbergConicalGearSetDesign)

        @property
        def hypoid_gear_set_design(
            self: "GearSetDesign._Cast_GearSetDesign",
        ) -> "_991.HypoidGearSetDesign":
            from mastapy.gears.gear_designs.hypoid import _991

            return self._parent._cast(_991.HypoidGearSetDesign)

        @property
        def face_gear_set_design(
            self: "GearSetDesign._Cast_GearSetDesign",
        ) -> "_999.FaceGearSetDesign":
            from mastapy.gears.gear_designs.face import _999

            return self._parent._cast(_999.FaceGearSetDesign)

        @property
        def cylindrical_gear_set_design(
            self: "GearSetDesign._Cast_GearSetDesign",
        ) -> "_1032.CylindricalGearSetDesign":
            from mastapy.gears.gear_designs.cylindrical import _1032

            return self._parent._cast(_1032.CylindricalGearSetDesign)

        @property
        def cylindrical_planetary_gear_set_design(
            self: "GearSetDesign._Cast_GearSetDesign",
        ) -> "_1045.CylindricalPlanetaryGearSetDesign":
            from mastapy.gears.gear_designs.cylindrical import _1045

            return self._parent._cast(_1045.CylindricalPlanetaryGearSetDesign)

        @property
        def conical_gear_set_design(
            self: "GearSetDesign._Cast_GearSetDesign",
        ) -> "_1162.ConicalGearSetDesign":
            from mastapy.gears.gear_designs.conical import _1162

            return self._parent._cast(_1162.ConicalGearSetDesign)

        @property
        def concept_gear_set_design(
            self: "GearSetDesign._Cast_GearSetDesign",
        ) -> "_1184.ConceptGearSetDesign":
            from mastapy.gears.gear_designs.concept import _1184

            return self._parent._cast(_1184.ConceptGearSetDesign)

        @property
        def bevel_gear_set_design(
            self: "GearSetDesign._Cast_GearSetDesign",
        ) -> "_1188.BevelGearSetDesign":
            from mastapy.gears.gear_designs.bevel import _1188

            return self._parent._cast(_1188.BevelGearSetDesign)

        @property
        def agma_gleason_conical_gear_set_design(
            self: "GearSetDesign._Cast_GearSetDesign",
        ) -> "_1201.AGMAGleasonConicalGearSetDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1201

            return self._parent._cast(_1201.AGMAGleasonConicalGearSetDesign)

        @property
        def gear_set_design(
            self: "GearSetDesign._Cast_GearSetDesign",
        ) -> "GearSetDesign":
            return self._parent

        def __getattr__(self: "GearSetDesign._Cast_GearSetDesign", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetDesign.TYPE"):
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
    def fe_model(self: Self) -> "str":
        """str"""
        temp = self.wrapped.FEModel.SelectedItemName

        if temp is None:
            return ""

        return temp

    @fe_model.setter
    @enforce_parameter_types
    def fe_model(self: Self, value: "str"):
        self.wrapped.FEModel.SetSelectedItem(str(value) if value is not None else "")

    @property
    def gear_set_drawing(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetDrawing

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def has_errors_or_warnings(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasErrorsOrWarnings

        if temp is None:
            return False

        return temp

    @property
    def largest_mesh_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LargestMeshRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def largest_number_of_teeth(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LargestNumberOfTeeth

        if temp is None:
            return 0

        return temp

    @property
    def long_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LongName

        if temp is None:
            return ""

        return temp

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
    def name_including_tooth_numbers(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NameIncludingToothNumbers

        if temp is None:
            return ""

        return temp

    @property
    def required_safety_factor_for_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RequiredSafetyFactorForBending

        if temp is None:
            return 0.0

        return temp

    @property
    def required_safety_factor_for_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RequiredSafetyFactorForContact

        if temp is None:
            return 0.0

        return temp

    @property
    def required_safety_factor_for_static_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RequiredSafetyFactorForStaticBending

        if temp is None:
            return 0.0

        return temp

    @property
    def required_safety_factor_for_static_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RequiredSafetyFactorForStaticContact

        if temp is None:
            return 0.0

        return temp

    @property
    def smallest_number_of_teeth(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SmallestNumberOfTeeth

        if temp is None:
            return 0

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
    def active_ltcafe_model(self: Self) -> "_1206.GearSetFEModel":
        """mastapy.gears.fe_model.GearSetFEModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveLTCAFEModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def tifffe_model(self: Self) -> "_1206.GearSetFEModel":
        """mastapy.gears.fe_model.GearSetFEModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TIFFFEModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def transmission_properties_gears(self: Self) -> "_331.GearSetDesignGroup":
        """mastapy.gears.GearSetDesignGroup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransmissionPropertiesGears

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(self: Self) -> "List[_951.GearDesign]":
        """List[mastapy.gears.gear_designs.GearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def ltcafe_models(self: Self) -> "List[_1206.GearSetFEModel]":
        """List[mastapy.gears.fe_model.GearSetFEModel]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LTCAFEModels

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def create_new_fe_model(self: Self):
        """Method does not return."""
        self.wrapped.CreateNewFEModel()

    def create_new_tifffe_model(self: Self):
        """Method does not return."""
        self.wrapped.CreateNewTIFFFEModel()

    @enforce_parameter_types
    def copy(self: Self, include_fe: "bool" = False) -> "GearSetDesign":
        """mastapy.gears.gear_designs.GearSetDesign

        Args:
            include_fe (bool, optional)
        """
        include_fe = bool(include_fe)
        method_result = self.wrapped.Copy(include_fe if include_fe else False)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "GearSetDesign._Cast_GearSetDesign":
        return self._Cast_GearSetDesign(self)
