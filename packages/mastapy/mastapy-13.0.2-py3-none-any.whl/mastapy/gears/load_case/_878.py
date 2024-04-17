"""MeshLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1228
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MESH_LOAD_CASE = python_net_import("SMT.MastaAPI.Gears.LoadCase", "MeshLoadCase")

if TYPE_CHECKING:
    from mastapy.gears.load_case.worm import _881
    from mastapy.gears.load_case.face import _884
    from mastapy.gears.load_case.cylindrical import _887
    from mastapy.gears.load_case.conical import _890
    from mastapy.gears.load_case.concept import _893
    from mastapy.gears.load_case.bevel import _895
    from mastapy.gears.analysis import _1222


__docformat__ = "restructuredtext en"
__all__ = ("MeshLoadCase",)


Self = TypeVar("Self", bound="MeshLoadCase")


class MeshLoadCase(_1228.GearMeshDesignAnalysis):
    """MeshLoadCase

    This is a mastapy class.
    """

    TYPE = _MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MeshLoadCase")

    class _Cast_MeshLoadCase:
        """Special nested class for casting MeshLoadCase to subclasses."""

        def __init__(self: "MeshLoadCase._Cast_MeshLoadCase", parent: "MeshLoadCase"):
            self._parent = parent

        @property
        def gear_mesh_design_analysis(
            self: "MeshLoadCase._Cast_MeshLoadCase",
        ) -> "_1228.GearMeshDesignAnalysis":
            return self._parent._cast(_1228.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "MeshLoadCase._Cast_MeshLoadCase",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def worm_mesh_load_case(
            self: "MeshLoadCase._Cast_MeshLoadCase",
        ) -> "_881.WormMeshLoadCase":
            from mastapy.gears.load_case.worm import _881

            return self._parent._cast(_881.WormMeshLoadCase)

        @property
        def face_mesh_load_case(
            self: "MeshLoadCase._Cast_MeshLoadCase",
        ) -> "_884.FaceMeshLoadCase":
            from mastapy.gears.load_case.face import _884

            return self._parent._cast(_884.FaceMeshLoadCase)

        @property
        def cylindrical_mesh_load_case(
            self: "MeshLoadCase._Cast_MeshLoadCase",
        ) -> "_887.CylindricalMeshLoadCase":
            from mastapy.gears.load_case.cylindrical import _887

            return self._parent._cast(_887.CylindricalMeshLoadCase)

        @property
        def conical_mesh_load_case(
            self: "MeshLoadCase._Cast_MeshLoadCase",
        ) -> "_890.ConicalMeshLoadCase":
            from mastapy.gears.load_case.conical import _890

            return self._parent._cast(_890.ConicalMeshLoadCase)

        @property
        def concept_mesh_load_case(
            self: "MeshLoadCase._Cast_MeshLoadCase",
        ) -> "_893.ConceptMeshLoadCase":
            from mastapy.gears.load_case.concept import _893

            return self._parent._cast(_893.ConceptMeshLoadCase)

        @property
        def bevel_mesh_load_case(
            self: "MeshLoadCase._Cast_MeshLoadCase",
        ) -> "_895.BevelMeshLoadCase":
            from mastapy.gears.load_case.bevel import _895

            return self._parent._cast(_895.BevelMeshLoadCase)

        @property
        def mesh_load_case(self: "MeshLoadCase._Cast_MeshLoadCase") -> "MeshLoadCase":
            return self._parent

        def __getattr__(self: "MeshLoadCase._Cast_MeshLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MeshLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def driving_gear(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DrivingGear

        if temp is None:
            return ""

        return temp

    @property
    def gear_a_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearATorque

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_b_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def is_loaded(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsLoaded

        if temp is None:
            return False

        return temp

    @property
    def signed_gear_a_power(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SignedGearAPower

        if temp is None:
            return 0.0

        return temp

    @property
    def signed_gear_a_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SignedGearATorque

        if temp is None:
            return 0.0

        return temp

    @property
    def signed_gear_b_power(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SignedGearBPower

        if temp is None:
            return 0.0

        return temp

    @property
    def signed_gear_b_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SignedGearBTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "MeshLoadCase._Cast_MeshLoadCase":
        return self._Cast_MeshLoadCase(self)
