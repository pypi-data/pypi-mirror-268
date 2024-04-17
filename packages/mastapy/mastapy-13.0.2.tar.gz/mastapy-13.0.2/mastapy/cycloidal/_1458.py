"""ContactSpecification"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal import conversion
from mastapy._math.vector_2d import Vector2D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONTACT_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.Cycloidal", "ContactSpecification"
)


__docformat__ = "restructuredtext en"
__all__ = ("ContactSpecification",)


Self = TypeVar("Self", bound="ContactSpecification")


class ContactSpecification(_0.APIBase):
    """ContactSpecification

    This is a mastapy class.
    """

    TYPE = _CONTACT_SPECIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ContactSpecification")

    class _Cast_ContactSpecification:
        """Special nested class for casting ContactSpecification to subclasses."""

        def __init__(
            self: "ContactSpecification._Cast_ContactSpecification",
            parent: "ContactSpecification",
        ):
            self._parent = parent

        @property
        def contact_specification(
            self: "ContactSpecification._Cast_ContactSpecification",
        ) -> "ContactSpecification":
            return self._parent

        def __getattr__(
            self: "ContactSpecification._Cast_ContactSpecification", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ContactSpecification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Clearance

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def contact_line_direction(self: Self) -> "Vector2D":
        """Vector2D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactLineDirection

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)

        if value is None:
            return None

        return value

    @property
    def contact_line_point_1(self: Self) -> "Vector2D":
        """Vector2D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactLinePoint1

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)

        if value is None:
            return None

        return value

    @property
    def contact_line_point_2(self: Self) -> "Vector2D":
        """Vector2D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactLinePoint2

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)

        if value is None:
            return None

        return value

    @property
    def contact_point(self: Self) -> "Vector2D":
        """Vector2D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactPoint

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)

        if value is None:
            return None

        return value

    @property
    def estimate_contact_point(self: Self) -> "Vector2D":
        """Vector2D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EstimateContactPoint

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ContactSpecification._Cast_ContactSpecification":
        return self._Cast_ContactSpecification(self)
