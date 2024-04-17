"""InterMountableComponentConnectionLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6858
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "InterMountableComponentConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2288
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6823,
        _6829,
        _6832,
        _6837,
        _6841,
        _6847,
        _6851,
        _6855,
        _6860,
        _6863,
        _6872,
        _6894,
        _6901,
        _6915,
        _6922,
        _6925,
        _6928,
        _6938,
        _6953,
        _6955,
        _6963,
        _6965,
        _6969,
        _6972,
        _6981,
        _6992,
        _6995,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionLoadCase",)


Self = TypeVar("Self", bound="InterMountableComponentConnectionLoadCase")


class InterMountableComponentConnectionLoadCase(_6858.ConnectionLoadCase):
    """InterMountableComponentConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_InterMountableComponentConnectionLoadCase"
    )

    class _Cast_InterMountableComponentConnectionLoadCase:
        """Special nested class for casting InterMountableComponentConnectionLoadCase to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
            parent: "InterMountableComponentConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6858.ConnectionLoadCase":
            return self._parent._cast(_6858.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6823.AGMAGleasonConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6823

            return self._parent._cast(_6823.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def belt_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6829.BeltConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6829

            return self._parent._cast(_6829.BeltConnectionLoadCase)

        @property
        def bevel_differential_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6832.BevelDifferentialGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6832

            return self._parent._cast(_6832.BevelDifferentialGearMeshLoadCase)

        @property
        def bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6837.BevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.BevelGearMeshLoadCase)

        @property
        def clutch_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6841.ClutchConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6841

            return self._parent._cast(_6841.ClutchConnectionLoadCase)

        @property
        def concept_coupling_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6847.ConceptCouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6847

            return self._parent._cast(_6847.ConceptCouplingConnectionLoadCase)

        @property
        def concept_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6851.ConceptGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6851

            return self._parent._cast(_6851.ConceptGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6855.ConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6855

            return self._parent._cast(_6855.ConicalGearMeshLoadCase)

        @property
        def coupling_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6860.CouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6860

            return self._parent._cast(_6860.CouplingConnectionLoadCase)

        @property
        def cvt_belt_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6863.CVTBeltConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6863

            return self._parent._cast(_6863.CVTBeltConnectionLoadCase)

        @property
        def cylindrical_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6872.CylindricalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6872

            return self._parent._cast(_6872.CylindricalGearMeshLoadCase)

        @property
        def face_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6894.FaceGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6894

            return self._parent._cast(_6894.FaceGearMeshLoadCase)

        @property
        def gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6901.GearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6901

            return self._parent._cast(_6901.GearMeshLoadCase)

        @property
        def hypoid_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6915.HypoidGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6915

            return self._parent._cast(_6915.HypoidGearMeshLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6922.KlingelnbergCycloPalloidConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6922

            return self._parent._cast(
                _6922.KlingelnbergCycloPalloidConicalGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6925.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6925

            return self._parent._cast(
                _6925.KlingelnbergCycloPalloidHypoidGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6928.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(
                _6928.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
            )

        @property
        def part_to_part_shear_coupling_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6938.PartToPartShearCouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6938

            return self._parent._cast(_6938.PartToPartShearCouplingConnectionLoadCase)

        @property
        def ring_pins_to_disc_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6953.RingPinsToDiscConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6953

            return self._parent._cast(_6953.RingPinsToDiscConnectionLoadCase)

        @property
        def rolling_ring_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6955.RollingRingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.RollingRingConnectionLoadCase)

        @property
        def spiral_bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6963.SpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6963

            return self._parent._cast(_6963.SpiralBevelGearMeshLoadCase)

        @property
        def spring_damper_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6965.SpringDamperConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6965

            return self._parent._cast(_6965.SpringDamperConnectionLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6969.StraightBevelDiffGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6969

            return self._parent._cast(_6969.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6972.StraightBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6972

            return self._parent._cast(_6972.StraightBevelGearMeshLoadCase)

        @property
        def torque_converter_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6981.TorqueConverterConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6981

            return self._parent._cast(_6981.TorqueConverterConnectionLoadCase)

        @property
        def worm_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6992.WormGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6992

            return self._parent._cast(_6992.WormGearMeshLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6995.ZerolBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6995

            return self._parent._cast(_6995.ZerolBevelGearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "InterMountableComponentConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
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
        self: Self, instance_to_wrap: "InterMountableComponentConnectionLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_modal_damping_ratio(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AdditionalModalDampingRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @additional_modal_damping_ratio.setter
    @enforce_parameter_types
    def additional_modal_damping_ratio(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AdditionalModalDampingRatio = value

    @property
    def connection_design(self: Self) -> "_2288.InterMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.InterMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase":
        return self._Cast_InterMountableComponentConnectionLoadCase(self)
