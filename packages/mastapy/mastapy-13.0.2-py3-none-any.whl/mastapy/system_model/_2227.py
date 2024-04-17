"""RelativeComponentAlignment"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RELATIVE_COMPONENT_ALIGNMENT = python_net_import(
    "SMT.MastaAPI.SystemModel", "RelativeComponentAlignment"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1498
    from mastapy.system_model import _2228
    from mastapy.system_model.part_model import _2451


__docformat__ = "restructuredtext en"
__all__ = ("RelativeComponentAlignment",)


Self = TypeVar("Self", bound="RelativeComponentAlignment")
T = TypeVar("T", bound="_2451.Component")


class RelativeComponentAlignment(_0.APIBase, Generic[T]):
    """RelativeComponentAlignment

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _RELATIVE_COMPONENT_ALIGNMENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RelativeComponentAlignment")

    class _Cast_RelativeComponentAlignment:
        """Special nested class for casting RelativeComponentAlignment to subclasses."""

        def __init__(
            self: "RelativeComponentAlignment._Cast_RelativeComponentAlignment",
            parent: "RelativeComponentAlignment",
        ):
            self._parent = parent

        @property
        def relative_component_alignment(
            self: "RelativeComponentAlignment._Cast_RelativeComponentAlignment",
        ) -> "RelativeComponentAlignment":
            return self._parent

        def __getattr__(
            self: "RelativeComponentAlignment._Cast_RelativeComponentAlignment",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RelativeComponentAlignment.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def alignment_axis(self: Self) -> "_1498.AlignmentAxis":
        """mastapy.math_utility.AlignmentAxis"""
        temp = self.wrapped.AlignmentAxis

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.MathUtility.AlignmentAxis")

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.math_utility._1498", "AlignmentAxis"
        )(value)

    @alignment_axis.setter
    @enforce_parameter_types
    def alignment_axis(self: Self, value: "_1498.AlignmentAxis"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.MathUtility.AlignmentAxis"
        )
        self.wrapped.AlignmentAxis = value

    @property
    def axial_offset(self: Self) -> "_2228.RelativeOffsetOption":
        """mastapy.system_model.RelativeOffsetOption"""
        temp = self.wrapped.AxialOffset

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.RelativeOffsetOption"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model._2228", "RelativeOffsetOption"
        )(value)

    @axial_offset.setter
    @enforce_parameter_types
    def axial_offset(self: Self, value: "_2228.RelativeOffsetOption"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.RelativeOffsetOption"
        )
        self.wrapped.AxialOffset = value

    @property
    def rotation_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotationAngle

        if temp is None:
            return 0.0

        return temp

    @rotation_angle.setter
    @enforce_parameter_types
    def rotation_angle(self: Self, value: "float"):
        self.wrapped.RotationAngle = float(value) if value is not None else 0.0

    @property
    def specified_offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpecifiedOffset

        if temp is None:
            return 0.0

        return temp

    @specified_offset.setter
    @enforce_parameter_types
    def specified_offset(self: Self, value: "float"):
        self.wrapped.SpecifiedOffset = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "RelativeComponentAlignment._Cast_RelativeComponentAlignment":
        return self._Cast_RelativeComponentAlignment(self)
