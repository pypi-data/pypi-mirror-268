"""CycloidalDiscModificationsSpecification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_MODIFICATIONS_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.Cycloidal", "CycloidalDiscModificationsSpecification"
)

if TYPE_CHECKING:
    from mastapy.cycloidal import _1459, _1466
    from mastapy.math_utility import _1542


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscModificationsSpecification",)


Self = TypeVar("Self", bound="CycloidalDiscModificationsSpecification")


class CycloidalDiscModificationsSpecification(_0.APIBase):
    """CycloidalDiscModificationsSpecification

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_MODIFICATIONS_SPECIFICATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscModificationsSpecification"
    )

    class _Cast_CycloidalDiscModificationsSpecification:
        """Special nested class for casting CycloidalDiscModificationsSpecification to subclasses."""

        def __init__(
            self: "CycloidalDiscModificationsSpecification._Cast_CycloidalDiscModificationsSpecification",
            parent: "CycloidalDiscModificationsSpecification",
        ):
            self._parent = parent

        @property
        def cycloidal_disc_modifications_specification(
            self: "CycloidalDiscModificationsSpecification._Cast_CycloidalDiscModificationsSpecification",
        ) -> "CycloidalDiscModificationsSpecification":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscModificationsSpecification._Cast_CycloidalDiscModificationsSpecification",
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
        self: Self, instance_to_wrap: "CycloidalDiscModificationsSpecification.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_offset_modification(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AngularOffsetModification

        if temp is None:
            return 0.0

        return temp

    @angular_offset_modification.setter
    @enforce_parameter_types
    def angular_offset_modification(self: Self, value: "float"):
        self.wrapped.AngularOffsetModification = (
            float(value) if value is not None else 0.0
        )

    @property
    def coefficient_for_logarithmic_crowning(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CoefficientForLogarithmicCrowning

        if temp is None:
            return 0.0

        return temp

    @coefficient_for_logarithmic_crowning.setter
    @enforce_parameter_types
    def coefficient_for_logarithmic_crowning(self: Self, value: "float"):
        self.wrapped.CoefficientForLogarithmicCrowning = (
            float(value) if value is not None else 0.0
        )

    @property
    def crowning_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CrowningRadius

        if temp is None:
            return 0.0

        return temp

    @crowning_radius.setter
    @enforce_parameter_types
    def crowning_radius(self: Self, value: "float"):
        self.wrapped.CrowningRadius = float(value) if value is not None else 0.0

    @property
    def crowning_specification_method(
        self: Self,
    ) -> "_1459.CrowningSpecificationMethod":
        """mastapy.cycloidal.CrowningSpecificationMethod"""
        temp = self.wrapped.CrowningSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Cycloidal.CrowningSpecificationMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.cycloidal._1459", "CrowningSpecificationMethod"
        )(value)

    @crowning_specification_method.setter
    @enforce_parameter_types
    def crowning_specification_method(
        self: Self, value: "_1459.CrowningSpecificationMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Cycloidal.CrowningSpecificationMethod"
        )
        self.wrapped.CrowningSpecificationMethod = value

    @property
    def direction_of_measured_modifications(
        self: Self,
    ) -> "_1466.DirectionOfMeasuredModifications":
        """mastapy.cycloidal.DirectionOfMeasuredModifications"""
        temp = self.wrapped.DirectionOfMeasuredModifications

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Cycloidal.DirectionOfMeasuredModifications"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.cycloidal._1466", "DirectionOfMeasuredModifications"
        )(value)

    @direction_of_measured_modifications.setter
    @enforce_parameter_types
    def direction_of_measured_modifications(
        self: Self, value: "_1466.DirectionOfMeasuredModifications"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Cycloidal.DirectionOfMeasuredModifications"
        )
        self.wrapped.DirectionOfMeasuredModifications = value

    @property
    def distance_to_where_crowning_starts_from_lobe_centre(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DistanceToWhereCrowningStartsFromLobeCentre

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @distance_to_where_crowning_starts_from_lobe_centre.setter
    @enforce_parameter_types
    def distance_to_where_crowning_starts_from_lobe_centre(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DistanceToWhereCrowningStartsFromLobeCentre = value

    @property
    def generating_wheel_centre_circle_diameter_modification(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GeneratingWheelCentreCircleDiameterModification

        if temp is None:
            return 0.0

        return temp

    @generating_wheel_centre_circle_diameter_modification.setter
    @enforce_parameter_types
    def generating_wheel_centre_circle_diameter_modification(
        self: Self, value: "float"
    ):
        self.wrapped.GeneratingWheelCentreCircleDiameterModification = (
            float(value) if value is not None else 0.0
        )

    @property
    def generating_wheel_diameter_modification(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GeneratingWheelDiameterModification

        if temp is None:
            return 0.0

        return temp

    @generating_wheel_diameter_modification.setter
    @enforce_parameter_types
    def generating_wheel_diameter_modification(self: Self, value: "float"):
        self.wrapped.GeneratingWheelDiameterModification = (
            float(value) if value is not None else 0.0
        )

    @property
    def measured_profile_modification(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.MeasuredProfileModification

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @measured_profile_modification.setter
    @enforce_parameter_types
    def measured_profile_modification(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.MeasuredProfileModification = value.wrapped

    @property
    def specify_measured_profile_modification(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyMeasuredProfileModification

        if temp is None:
            return False

        return temp

    @specify_measured_profile_modification.setter
    @enforce_parameter_types
    def specify_measured_profile_modification(self: Self, value: "bool"):
        self.wrapped.SpecifyMeasuredProfileModification = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscModificationsSpecification._Cast_CycloidalDiscModificationsSpecification":
        return self._Cast_CycloidalDiscModificationsSpecification(self)
