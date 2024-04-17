"""LineContactStiffnessEntity"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.nodal_analysis.nodal_entities import _128
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LINE_CONTACT_STIFFNESS_ENTITY = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "LineContactStiffnessEntity"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _79
    from mastapy.nodal_analysis.nodal_entities import _145, _147


__docformat__ = "restructuredtext en"
__all__ = ("LineContactStiffnessEntity",)


Self = TypeVar("Self", bound="LineContactStiffnessEntity")


class LineContactStiffnessEntity(_128.ArbitraryNodalComponent):
    """LineContactStiffnessEntity

    This is a mastapy class.
    """

    TYPE = _LINE_CONTACT_STIFFNESS_ENTITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LineContactStiffnessEntity")

    class _Cast_LineContactStiffnessEntity:
        """Special nested class for casting LineContactStiffnessEntity to subclasses."""

        def __init__(
            self: "LineContactStiffnessEntity._Cast_LineContactStiffnessEntity",
            parent: "LineContactStiffnessEntity",
        ):
            self._parent = parent

        @property
        def arbitrary_nodal_component(
            self: "LineContactStiffnessEntity._Cast_LineContactStiffnessEntity",
        ) -> "_128.ArbitraryNodalComponent":
            return self._parent._cast(_128.ArbitraryNodalComponent)

        @property
        def nodal_component(
            self: "LineContactStiffnessEntity._Cast_LineContactStiffnessEntity",
        ) -> "_145.NodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _145

            return self._parent._cast(_145.NodalComponent)

        @property
        def nodal_entity(
            self: "LineContactStiffnessEntity._Cast_LineContactStiffnessEntity",
        ) -> "_147.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _147

            return self._parent._cast(_147.NodalEntity)

        @property
        def line_contact_stiffness_entity(
            self: "LineContactStiffnessEntity._Cast_LineContactStiffnessEntity",
        ) -> "LineContactStiffnessEntity":
            return self._parent

        def __getattr__(
            self: "LineContactStiffnessEntity._Cast_LineContactStiffnessEntity",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LineContactStiffnessEntity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def stiffness_in_local_coordinate_system(self: Self) -> "_79.NodalMatrix":
        """mastapy.nodal_analysis.NodalMatrix

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessInLocalCoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "LineContactStiffnessEntity._Cast_LineContactStiffnessEntity":
        return self._Cast_LineContactStiffnessEntity(self)
