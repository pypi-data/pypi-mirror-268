"""SurfaceToSurfaceContactStiffnessEntity"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.nodal_analysis.nodal_entities import _128
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SURFACE_TO_SURFACE_CONTACT_STIFFNESS_ENTITY = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "SurfaceToSurfaceContactStiffnessEntity"
)

if TYPE_CHECKING:
    from mastapy.math_utility.stiffness_calculators import _1545
    from mastapy.nodal_analysis.nodal_entities import _145, _147


__docformat__ = "restructuredtext en"
__all__ = ("SurfaceToSurfaceContactStiffnessEntity",)


Self = TypeVar("Self", bound="SurfaceToSurfaceContactStiffnessEntity")


class SurfaceToSurfaceContactStiffnessEntity(_128.ArbitraryNodalComponent):
    """SurfaceToSurfaceContactStiffnessEntity

    This is a mastapy class.
    """

    TYPE = _SURFACE_TO_SURFACE_CONTACT_STIFFNESS_ENTITY
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SurfaceToSurfaceContactStiffnessEntity"
    )

    class _Cast_SurfaceToSurfaceContactStiffnessEntity:
        """Special nested class for casting SurfaceToSurfaceContactStiffnessEntity to subclasses."""

        def __init__(
            self: "SurfaceToSurfaceContactStiffnessEntity._Cast_SurfaceToSurfaceContactStiffnessEntity",
            parent: "SurfaceToSurfaceContactStiffnessEntity",
        ):
            self._parent = parent

        @property
        def arbitrary_nodal_component(
            self: "SurfaceToSurfaceContactStiffnessEntity._Cast_SurfaceToSurfaceContactStiffnessEntity",
        ) -> "_128.ArbitraryNodalComponent":
            return self._parent._cast(_128.ArbitraryNodalComponent)

        @property
        def nodal_component(
            self: "SurfaceToSurfaceContactStiffnessEntity._Cast_SurfaceToSurfaceContactStiffnessEntity",
        ) -> "_145.NodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _145

            return self._parent._cast(_145.NodalComponent)

        @property
        def nodal_entity(
            self: "SurfaceToSurfaceContactStiffnessEntity._Cast_SurfaceToSurfaceContactStiffnessEntity",
        ) -> "_147.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _147

            return self._parent._cast(_147.NodalEntity)

        @property
        def surface_to_surface_contact_stiffness_entity(
            self: "SurfaceToSurfaceContactStiffnessEntity._Cast_SurfaceToSurfaceContactStiffnessEntity",
        ) -> "SurfaceToSurfaceContactStiffnessEntity":
            return self._parent

        def __getattr__(
            self: "SurfaceToSurfaceContactStiffnessEntity._Cast_SurfaceToSurfaceContactStiffnessEntity",
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
        self: Self, instance_to_wrap: "SurfaceToSurfaceContactStiffnessEntity.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact(self: Self) -> "_1545.SurfaceToSurfaceContact":
        """mastapy.math_utility.stiffness_calculators.SurfaceToSurfaceContact

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Contact

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SurfaceToSurfaceContactStiffnessEntity._Cast_SurfaceToSurfaceContactStiffnessEntity":
        return self._Cast_SurfaceToSurfaceContactStiffnessEntity(self)
