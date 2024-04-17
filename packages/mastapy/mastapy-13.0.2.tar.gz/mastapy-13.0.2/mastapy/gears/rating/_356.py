"""AbstractGearMeshRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1222
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_MESH_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating", "AbstractGearMeshRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _363, _368
    from mastapy.gears.rating.zerol_bevel import _372
    from mastapy.gears.rating.worm import _376, _380
    from mastapy.gears.rating.straight_bevel import _398
    from mastapy.gears.rating.straight_bevel_diff import _401
    from mastapy.gears.rating.spiral_bevel import _405
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _408
    from mastapy.gears.rating.klingelnberg_hypoid import _411
    from mastapy.gears.rating.klingelnberg_conical import _414
    from mastapy.gears.rating.hypoid import _441
    from mastapy.gears.rating.face import _449, _450
    from mastapy.gears.rating.cylindrical import _461, _469
    from mastapy.gears.rating.conical import _542, _547
    from mastapy.gears.rating.concept import _552, _553
    from mastapy.gears.rating.bevel import _557
    from mastapy.gears.rating.agma_gleason_conical import _568


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearMeshRating",)


Self = TypeVar("Self", bound="AbstractGearMeshRating")


class AbstractGearMeshRating(_1222.AbstractGearMeshAnalysis):
    """AbstractGearMeshRating

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_MESH_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractGearMeshRating")

    class _Cast_AbstractGearMeshRating:
        """Special nested class for casting AbstractGearMeshRating to subclasses."""

        def __init__(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
            parent: "AbstractGearMeshRating",
        ):
            self._parent = parent

        @property
        def abstract_gear_mesh_analysis(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_1222.AbstractGearMeshAnalysis":
            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_363.GearMeshRating":
            from mastapy.gears.rating import _363

            return self._parent._cast(_363.GearMeshRating)

        @property
        def mesh_duty_cycle_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_368.MeshDutyCycleRating":
            from mastapy.gears.rating import _368

            return self._parent._cast(_368.MeshDutyCycleRating)

        @property
        def zerol_bevel_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_372.ZerolBevelGearMeshRating":
            from mastapy.gears.rating.zerol_bevel import _372

            return self._parent._cast(_372.ZerolBevelGearMeshRating)

        @property
        def worm_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_376.WormGearMeshRating":
            from mastapy.gears.rating.worm import _376

            return self._parent._cast(_376.WormGearMeshRating)

        @property
        def worm_mesh_duty_cycle_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_380.WormMeshDutyCycleRating":
            from mastapy.gears.rating.worm import _380

            return self._parent._cast(_380.WormMeshDutyCycleRating)

        @property
        def straight_bevel_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_398.StraightBevelGearMeshRating":
            from mastapy.gears.rating.straight_bevel import _398

            return self._parent._cast(_398.StraightBevelGearMeshRating)

        @property
        def straight_bevel_diff_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_401.StraightBevelDiffGearMeshRating":
            from mastapy.gears.rating.straight_bevel_diff import _401

            return self._parent._cast(_401.StraightBevelDiffGearMeshRating)

        @property
        def spiral_bevel_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_405.SpiralBevelGearMeshRating":
            from mastapy.gears.rating.spiral_bevel import _405

            return self._parent._cast(_405.SpiralBevelGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_408.KlingelnbergCycloPalloidSpiralBevelGearMeshRating":
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _408

            return self._parent._cast(
                _408.KlingelnbergCycloPalloidSpiralBevelGearMeshRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_411.KlingelnbergCycloPalloidHypoidGearMeshRating":
            from mastapy.gears.rating.klingelnberg_hypoid import _411

            return self._parent._cast(_411.KlingelnbergCycloPalloidHypoidGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_414.KlingelnbergCycloPalloidConicalGearMeshRating":
            from mastapy.gears.rating.klingelnberg_conical import _414

            return self._parent._cast(
                _414.KlingelnbergCycloPalloidConicalGearMeshRating
            )

        @property
        def hypoid_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_441.HypoidGearMeshRating":
            from mastapy.gears.rating.hypoid import _441

            return self._parent._cast(_441.HypoidGearMeshRating)

        @property
        def face_gear_mesh_duty_cycle_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_449.FaceGearMeshDutyCycleRating":
            from mastapy.gears.rating.face import _449

            return self._parent._cast(_449.FaceGearMeshDutyCycleRating)

        @property
        def face_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_450.FaceGearMeshRating":
            from mastapy.gears.rating.face import _450

            return self._parent._cast(_450.FaceGearMeshRating)

        @property
        def cylindrical_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_461.CylindricalGearMeshRating":
            from mastapy.gears.rating.cylindrical import _461

            return self._parent._cast(_461.CylindricalGearMeshRating)

        @property
        def cylindrical_mesh_duty_cycle_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_469.CylindricalMeshDutyCycleRating":
            from mastapy.gears.rating.cylindrical import _469

            return self._parent._cast(_469.CylindricalMeshDutyCycleRating)

        @property
        def conical_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_542.ConicalGearMeshRating":
            from mastapy.gears.rating.conical import _542

            return self._parent._cast(_542.ConicalGearMeshRating)

        @property
        def conical_mesh_duty_cycle_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_547.ConicalMeshDutyCycleRating":
            from mastapy.gears.rating.conical import _547

            return self._parent._cast(_547.ConicalMeshDutyCycleRating)

        @property
        def concept_gear_mesh_duty_cycle_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_552.ConceptGearMeshDutyCycleRating":
            from mastapy.gears.rating.concept import _552

            return self._parent._cast(_552.ConceptGearMeshDutyCycleRating)

        @property
        def concept_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_553.ConceptGearMeshRating":
            from mastapy.gears.rating.concept import _553

            return self._parent._cast(_553.ConceptGearMeshRating)

        @property
        def bevel_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_557.BevelGearMeshRating":
            from mastapy.gears.rating.bevel import _557

            return self._parent._cast(_557.BevelGearMeshRating)

        @property
        def agma_gleason_conical_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_568.AGMAGleasonConicalGearMeshRating":
            from mastapy.gears.rating.agma_gleason_conical import _568

            return self._parent._cast(_568.AGMAGleasonConicalGearMeshRating)

        @property
        def abstract_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "AbstractGearMeshRating":
            return self._parent

        def __getattr__(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractGearMeshRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mesh_efficiency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshEfficiency

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "AbstractGearMeshRating._Cast_AbstractGearMeshRating":
        return self._Cast_AbstractGearMeshRating(self)
