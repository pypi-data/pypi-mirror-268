"""DataPointForResponseOfANodeAtAFrequencyToAHarmonic"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy.math_utility import _1527
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATA_POINT_FOR_RESPONSE_OF_A_NODE_AT_A_FREQUENCY_TO_A_HARMONIC = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults",
    "DataPointForResponseOfANodeAtAFrequencyToAHarmonic",
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1512


__docformat__ = "restructuredtext en"
__all__ = ("DataPointForResponseOfANodeAtAFrequencyToAHarmonic",)


Self = TypeVar("Self", bound="DataPointForResponseOfANodeAtAFrequencyToAHarmonic")


class DataPointForResponseOfANodeAtAFrequencyToAHarmonic(_0.APIBase):
    """DataPointForResponseOfANodeAtAFrequencyToAHarmonic

    This is a mastapy class.
    """

    TYPE = _DATA_POINT_FOR_RESPONSE_OF_A_NODE_AT_A_FREQUENCY_TO_A_HARMONIC
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_DataPointForResponseOfANodeAtAFrequencyToAHarmonic"
    )

    class _Cast_DataPointForResponseOfANodeAtAFrequencyToAHarmonic:
        """Special nested class for casting DataPointForResponseOfANodeAtAFrequencyToAHarmonic to subclasses."""

        def __init__(
            self: "DataPointForResponseOfANodeAtAFrequencyToAHarmonic._Cast_DataPointForResponseOfANodeAtAFrequencyToAHarmonic",
            parent: "DataPointForResponseOfANodeAtAFrequencyToAHarmonic",
        ):
            self._parent = parent

        @property
        def data_point_for_response_of_a_node_at_a_frequency_to_a_harmonic(
            self: "DataPointForResponseOfANodeAtAFrequencyToAHarmonic._Cast_DataPointForResponseOfANodeAtAFrequencyToAHarmonic",
        ) -> "DataPointForResponseOfANodeAtAFrequencyToAHarmonic":
            return self._parent

        def __getattr__(
            self: "DataPointForResponseOfANodeAtAFrequencyToAHarmonic._Cast_DataPointForResponseOfANodeAtAFrequencyToAHarmonic",
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
        self: Self,
        instance_to_wrap: "DataPointForResponseOfANodeAtAFrequencyToAHarmonic.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_magnitude(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularMagnitude

        if temp is None:
            return 0.0

        return temp

    @property
    def angular_radial_magnitude(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularRadialMagnitude

        if temp is None:
            return 0.0

        return temp

    @property
    def frequency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Frequency

        if temp is None:
            return 0.0

        return temp

    @property
    def linear_magnitude(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearMagnitude

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_magnitude(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialMagnitude

        if temp is None:
            return 0.0

        return temp

    @property
    def speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @property
    def theta_x(self: Self) -> "complex":
        """complex

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThetaX

        if temp is None:
            return None

        value = conversion.pn_to_mp_complex(temp)

        if value is None:
            return None

        return value

    @property
    def theta_y(self: Self) -> "complex":
        """complex

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThetaY

        if temp is None:
            return None

        value = conversion.pn_to_mp_complex(temp)

        if value is None:
            return None

        return value

    @property
    def theta_z(self: Self) -> "complex":
        """complex

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThetaZ

        if temp is None:
            return None

        value = conversion.pn_to_mp_complex(temp)

        if value is None:
            return None

        return value

    @property
    def x(self: Self) -> "complex":
        """complex

        Note:
            This property is readonly.
        """
        temp = self.wrapped.X

        if temp is None:
            return None

        value = conversion.pn_to_mp_complex(temp)

        if value is None:
            return None

        return value

    @property
    def y(self: Self) -> "complex":
        """complex

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Y

        if temp is None:
            return None

        value = conversion.pn_to_mp_complex(temp)

        if value is None:
            return None

        return value

    @property
    def z(self: Self) -> "complex":
        """complex

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Z

        if temp is None:
            return None

        value = conversion.pn_to_mp_complex(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def get_scalar_result(
        self: Self,
        scalar_result: "_1512.DynamicsResponseScalarResult",
        complex_magnitude_method: "_1527.ComplexMagnitudeMethod" = _1527.ComplexMagnitudeMethod.PEAK_AMPLITUDE,
    ) -> "complex":
        """complex

        Args:
            scalar_result (mastapy.math_utility.DynamicsResponseScalarResult)
            complex_magnitude_method (mastapy.math_utility.ComplexMagnitudeMethod, optional)
        """
        scalar_result = conversion.mp_to_pn_enum(
            scalar_result, "SMT.MastaAPI.MathUtility.DynamicsResponseScalarResult"
        )
        complex_magnitude_method = conversion.mp_to_pn_enum(
            complex_magnitude_method, "SMT.MastaAPI.MathUtility.ComplexMagnitudeMethod"
        )
        return conversion.pn_to_mp_complex(
            self.wrapped.GetScalarResult(scalar_result, complex_magnitude_method)
        )

    @property
    def cast_to(
        self: Self,
    ) -> "DataPointForResponseOfANodeAtAFrequencyToAHarmonic._Cast_DataPointForResponseOfANodeAtAFrequencyToAHarmonic":
        return self._Cast_DataPointForResponseOfANodeAtAFrequencyToAHarmonic(self)
