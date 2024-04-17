"""LinkComponentAxialPositionErrorReporter"""

from __future__ import annotations

from typing import TypeVar

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LINK_COMPONENT_AXIAL_POSITION_ERROR_REPORTER = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "LinkComponentAxialPositionErrorReporter"
)


__docformat__ = "restructuredtext en"
__all__ = ("LinkComponentAxialPositionErrorReporter",)


Self = TypeVar("Self", bound="LinkComponentAxialPositionErrorReporter")


class LinkComponentAxialPositionErrorReporter(_0.APIBase):
    """LinkComponentAxialPositionErrorReporter

    This is a mastapy class.
    """

    TYPE = _LINK_COMPONENT_AXIAL_POSITION_ERROR_REPORTER
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LinkComponentAxialPositionErrorReporter"
    )

    class _Cast_LinkComponentAxialPositionErrorReporter:
        """Special nested class for casting LinkComponentAxialPositionErrorReporter to subclasses."""

        def __init__(
            self: "LinkComponentAxialPositionErrorReporter._Cast_LinkComponentAxialPositionErrorReporter",
            parent: "LinkComponentAxialPositionErrorReporter",
        ):
            self._parent = parent

        @property
        def link_component_axial_position_error_reporter(
            self: "LinkComponentAxialPositionErrorReporter._Cast_LinkComponentAxialPositionErrorReporter",
        ) -> "LinkComponentAxialPositionErrorReporter":
            return self._parent

        def __getattr__(
            self: "LinkComponentAxialPositionErrorReporter._Cast_LinkComponentAxialPositionErrorReporter",
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
        self: Self, instance_to_wrap: "LinkComponentAxialPositionErrorReporter.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def error_in_location_on_axis(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ErrorInLocationOnAxis

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def expected_location_on_component_axis(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExpectedLocationOnComponentAxis

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def location_on_component_axis_from_fe_nodes(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LocationOnComponentAxisFromFENodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "LinkComponentAxialPositionErrorReporter._Cast_LinkComponentAxialPositionErrorReporter":
        return self._Cast_LinkComponentAxialPositionErrorReporter(self)
