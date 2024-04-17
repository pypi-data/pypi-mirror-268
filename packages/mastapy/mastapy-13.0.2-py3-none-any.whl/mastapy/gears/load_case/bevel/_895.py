"""BevelMeshLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.load_case.conical import _890
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase.Bevel", "BevelMeshLoadCase"
)

if TYPE_CHECKING:
    from mastapy.gears.load_case import _878
    from mastapy.gears.analysis import _1228, _1222


__docformat__ = "restructuredtext en"
__all__ = ("BevelMeshLoadCase",)


Self = TypeVar("Self", bound="BevelMeshLoadCase")


class BevelMeshLoadCase(_890.ConicalMeshLoadCase):
    """BevelMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelMeshLoadCase")

    class _Cast_BevelMeshLoadCase:
        """Special nested class for casting BevelMeshLoadCase to subclasses."""

        def __init__(
            self: "BevelMeshLoadCase._Cast_BevelMeshLoadCase",
            parent: "BevelMeshLoadCase",
        ):
            self._parent = parent

        @property
        def conical_mesh_load_case(
            self: "BevelMeshLoadCase._Cast_BevelMeshLoadCase",
        ) -> "_890.ConicalMeshLoadCase":
            return self._parent._cast(_890.ConicalMeshLoadCase)

        @property
        def mesh_load_case(
            self: "BevelMeshLoadCase._Cast_BevelMeshLoadCase",
        ) -> "_878.MeshLoadCase":
            from mastapy.gears.load_case import _878

            return self._parent._cast(_878.MeshLoadCase)

        @property
        def gear_mesh_design_analysis(
            self: "BevelMeshLoadCase._Cast_BevelMeshLoadCase",
        ) -> "_1228.GearMeshDesignAnalysis":
            from mastapy.gears.analysis import _1228

            return self._parent._cast(_1228.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "BevelMeshLoadCase._Cast_BevelMeshLoadCase",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def bevel_mesh_load_case(
            self: "BevelMeshLoadCase._Cast_BevelMeshLoadCase",
        ) -> "BevelMeshLoadCase":
            return self._parent

        def __getattr__(self: "BevelMeshLoadCase._Cast_BevelMeshLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelMeshLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BevelMeshLoadCase._Cast_BevelMeshLoadCase":
        return self._Cast_BevelMeshLoadCase(self)
