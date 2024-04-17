"""ConceptMeshLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.load_case import _878
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase.Concept", "ConceptMeshLoadCase"
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1228, _1222


__docformat__ = "restructuredtext en"
__all__ = ("ConceptMeshLoadCase",)


Self = TypeVar("Self", bound="ConceptMeshLoadCase")


class ConceptMeshLoadCase(_878.MeshLoadCase):
    """ConceptMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _CONCEPT_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptMeshLoadCase")

    class _Cast_ConceptMeshLoadCase:
        """Special nested class for casting ConceptMeshLoadCase to subclasses."""

        def __init__(
            self: "ConceptMeshLoadCase._Cast_ConceptMeshLoadCase",
            parent: "ConceptMeshLoadCase",
        ):
            self._parent = parent

        @property
        def mesh_load_case(
            self: "ConceptMeshLoadCase._Cast_ConceptMeshLoadCase",
        ) -> "_878.MeshLoadCase":
            return self._parent._cast(_878.MeshLoadCase)

        @property
        def gear_mesh_design_analysis(
            self: "ConceptMeshLoadCase._Cast_ConceptMeshLoadCase",
        ) -> "_1228.GearMeshDesignAnalysis":
            from mastapy.gears.analysis import _1228

            return self._parent._cast(_1228.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "ConceptMeshLoadCase._Cast_ConceptMeshLoadCase",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def concept_mesh_load_case(
            self: "ConceptMeshLoadCase._Cast_ConceptMeshLoadCase",
        ) -> "ConceptMeshLoadCase":
            return self._parent

        def __getattr__(
            self: "ConceptMeshLoadCase._Cast_ConceptMeshLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptMeshLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ConceptMeshLoadCase._Cast_ConceptMeshLoadCase":
        return self._Cast_ConceptMeshLoadCase(self)
