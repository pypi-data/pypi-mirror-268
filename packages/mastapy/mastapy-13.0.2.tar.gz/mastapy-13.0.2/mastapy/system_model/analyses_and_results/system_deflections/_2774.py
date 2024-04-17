"""InformationForContactAtPointAlongFaceWidth"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INFORMATION_FOR_CONTACT_AT_POINT_ALONG_FACE_WIDTH = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "InformationForContactAtPointAlongFaceWidth",
)


__docformat__ = "restructuredtext en"
__all__ = ("InformationForContactAtPointAlongFaceWidth",)


Self = TypeVar("Self", bound="InformationForContactAtPointAlongFaceWidth")


class InformationForContactAtPointAlongFaceWidth(_0.APIBase):
    """InformationForContactAtPointAlongFaceWidth

    This is a mastapy class.
    """

    TYPE = _INFORMATION_FOR_CONTACT_AT_POINT_ALONG_FACE_WIDTH
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_InformationForContactAtPointAlongFaceWidth"
    )

    class _Cast_InformationForContactAtPointAlongFaceWidth:
        """Special nested class for casting InformationForContactAtPointAlongFaceWidth to subclasses."""

        def __init__(
            self: "InformationForContactAtPointAlongFaceWidth._Cast_InformationForContactAtPointAlongFaceWidth",
            parent: "InformationForContactAtPointAlongFaceWidth",
        ):
            self._parent = parent

        @property
        def information_for_contact_at_point_along_face_width(
            self: "InformationForContactAtPointAlongFaceWidth._Cast_InformationForContactAtPointAlongFaceWidth",
        ) -> "InformationForContactAtPointAlongFaceWidth":
            return self._parent

        def __getattr__(
            self: "InformationForContactAtPointAlongFaceWidth._Cast_InformationForContactAtPointAlongFaceWidth",
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
        self: Self, instance_to_wrap: "InformationForContactAtPointAlongFaceWidth.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def force_per_unit_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForcePerUnitLength

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_per_unit_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessPerUnitLength

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_penetration(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfacePenetration

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "InformationForContactAtPointAlongFaceWidth._Cast_InformationForContactAtPointAlongFaceWidth":
        return self._Cast_InformationForContactAtPointAlongFaceWidth(self)
