"""BevelGearMeshAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7286
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "BevelGearMeshAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2310
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7293,
        _7384,
        _7390,
        _7393,
        _7412,
        _7314,
        _7342,
        _7348,
        _7316,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="BevelGearMeshAdvancedSystemDeflection")


class BevelGearMeshAdvancedSystemDeflection(
    _7286.AGMAGleasonConicalGearMeshAdvancedSystemDeflection
):
    """BevelGearMeshAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshAdvancedSystemDeflection"
    )

    class _Cast_BevelGearMeshAdvancedSystemDeflection:
        """Special nested class for casting BevelGearMeshAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
            parent: "BevelGearMeshAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7286.AGMAGleasonConicalGearMeshAdvancedSystemDeflection":
            return self._parent._cast(
                _7286.AGMAGleasonConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7314.ConicalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7314,
            )

            return self._parent._cast(_7314.ConicalGearMeshAdvancedSystemDeflection)

        @property
        def gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7342.GearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7342,
            )

            return self._parent._cast(_7342.GearMeshAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7348.InterMountableComponentConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7348,
            )

            return self._parent._cast(
                _7348.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7316.ConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7316,
            )

            return self._parent._cast(_7316.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7293.BevelDifferentialGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7293,
            )

            return self._parent._cast(
                _7293.BevelDifferentialGearMeshAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7384.SpiralBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7384,
            )

            return self._parent._cast(_7384.SpiralBevelGearMeshAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7390.StraightBevelDiffGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7390,
            )

            return self._parent._cast(
                _7390.StraightBevelDiffGearMeshAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7393.StraightBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7393,
            )

            return self._parent._cast(
                _7393.StraightBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "_7412.ZerolBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7412,
            )

            return self._parent._cast(_7412.ZerolBevelGearMeshAdvancedSystemDeflection)

        @property
        def bevel_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "BevelGearMeshAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "BevelGearMeshAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2310.BevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelGearMesh

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
    ) -> "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection":
        return self._Cast_BevelGearMeshAdvancedSystemDeflection(self)
