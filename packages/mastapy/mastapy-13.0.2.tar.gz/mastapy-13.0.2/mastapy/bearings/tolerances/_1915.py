"""InterferenceDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.bearings.tolerances import _1908
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTERFERENCE_DETAIL = python_net_import(
    "SMT.MastaAPI.Bearings.Tolerances", "InterferenceDetail"
)

if TYPE_CHECKING:
    from mastapy.materials import _272
    from mastapy.bearings.tolerances import _1918, _1921, _1927


__docformat__ = "restructuredtext en"
__all__ = ("InterferenceDetail",)


Self = TypeVar("Self", bound="InterferenceDetail")


class InterferenceDetail(_1908.BearingConnectionComponent):
    """InterferenceDetail

    This is a mastapy class.
    """

    TYPE = _INTERFERENCE_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InterferenceDetail")

    class _Cast_InterferenceDetail:
        """Special nested class for casting InterferenceDetail to subclasses."""

        def __init__(
            self: "InterferenceDetail._Cast_InterferenceDetail",
            parent: "InterferenceDetail",
        ):
            self._parent = parent

        @property
        def bearing_connection_component(
            self: "InterferenceDetail._Cast_InterferenceDetail",
        ) -> "_1908.BearingConnectionComponent":
            return self._parent._cast(_1908.BearingConnectionComponent)

        @property
        def mounting_sleeve_diameter_detail(
            self: "InterferenceDetail._Cast_InterferenceDetail",
        ) -> "_1918.MountingSleeveDiameterDetail":
            from mastapy.bearings.tolerances import _1918

            return self._parent._cast(_1918.MountingSleeveDiameterDetail)

        @property
        def race_detail(
            self: "InterferenceDetail._Cast_InterferenceDetail",
        ) -> "_1921.RaceDetail":
            from mastapy.bearings.tolerances import _1921

            return self._parent._cast(_1921.RaceDetail)

        @property
        def support_detail(
            self: "InterferenceDetail._Cast_InterferenceDetail",
        ) -> "_1927.SupportDetail":
            from mastapy.bearings.tolerances import _1927

            return self._parent._cast(_1927.SupportDetail)

        @property
        def interference_detail(
            self: "InterferenceDetail._Cast_InterferenceDetail",
        ) -> "InterferenceDetail":
            return self._parent

        def __getattr__(self: "InterferenceDetail._Cast_InterferenceDetail", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InterferenceDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def diameter_tolerance_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DiameterToleranceFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @diameter_tolerance_factor.setter
    @enforce_parameter_types
    def diameter_tolerance_factor(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DiameterToleranceFactor = value

    @property
    def temperature(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Temperature

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @temperature.setter
    @enforce_parameter_types
    def temperature(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Temperature = value

    @property
    def material(self: Self) -> "_272.Material":
        """mastapy.materials.Material

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Material

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "InterferenceDetail._Cast_InterferenceDetail":
        return self._Cast_InterferenceDetail(self)
