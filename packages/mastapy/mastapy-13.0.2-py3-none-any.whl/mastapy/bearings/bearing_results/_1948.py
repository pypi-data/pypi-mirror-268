"""BearingStiffnessMatrixReporter"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_STIFFNESS_MATRIX_REPORTER = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "BearingStiffnessMatrixReporter"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results import _1972


__docformat__ = "restructuredtext en"
__all__ = ("BearingStiffnessMatrixReporter",)


Self = TypeVar("Self", bound="BearingStiffnessMatrixReporter")


class BearingStiffnessMatrixReporter(_0.APIBase):
    """BearingStiffnessMatrixReporter

    This is a mastapy class.
    """

    TYPE = _BEARING_STIFFNESS_MATRIX_REPORTER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingStiffnessMatrixReporter")

    class _Cast_BearingStiffnessMatrixReporter:
        """Special nested class for casting BearingStiffnessMatrixReporter to subclasses."""

        def __init__(
            self: "BearingStiffnessMatrixReporter._Cast_BearingStiffnessMatrixReporter",
            parent: "BearingStiffnessMatrixReporter",
        ):
            self._parent = parent

        @property
        def bearing_stiffness_matrix_reporter(
            self: "BearingStiffnessMatrixReporter._Cast_BearingStiffnessMatrixReporter",
        ) -> "BearingStiffnessMatrixReporter":
            return self._parent

        def __getattr__(
            self: "BearingStiffnessMatrixReporter._Cast_BearingStiffnessMatrixReporter",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingStiffnessMatrixReporter.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_stiffness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_radial_stiffness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumRadialStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_tilt_stiffness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_radial_stiffness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumRadialStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_tilt_stiffness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumTiltStiffness

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
    def radial_stiffness_variation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialStiffnessVariation

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_xx(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessXX

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_xy(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessXY

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_xz(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessXZ

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_x_theta_x(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessXThetaX

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_x_theta_y(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessXThetaY

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_x_theta_z(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessXThetaZ

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_yx(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessYX

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_yy(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessYY

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_yz(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessYZ

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_y_theta_x(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessYThetaX

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_y_theta_y(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessYThetaY

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_y_theta_z(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessYThetaZ

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_zx(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessZX

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_zy(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessZY

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_zz(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessZZ

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_z_theta_x(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessZThetaX

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_z_theta_y(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessZThetaY

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_z_theta_z(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessZThetaZ

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_theta_xx(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessThetaXX

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_theta_xy(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessThetaXY

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_theta_xz(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessThetaXZ

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_theta_x_theta_x(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessThetaXThetaX

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_theta_x_theta_y(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessThetaXThetaY

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_theta_x_theta_z(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessThetaXThetaZ

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_theta_yx(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessThetaYX

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_theta_yy(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessThetaYY

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_theta_yz(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessThetaYZ

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_theta_y_theta_x(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessThetaYThetaX

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_theta_y_theta_y(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessThetaYThetaY

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_theta_y_theta_z(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessThetaYThetaZ

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_theta_zx(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessThetaZX

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_theta_zy(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessThetaZY

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_theta_zz(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessThetaZZ

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_theta_z_theta_x(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessThetaZThetaX

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_theta_z_theta_y(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessThetaZThetaY

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_theta_z_theta_z(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessThetaZThetaZ

        if temp is None:
            return 0.0

        return temp

    @property
    def tilt_stiffness_variation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TiltStiffnessVariation

        if temp is None:
            return 0.0

        return temp

    @property
    def torsional_stiffness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorsionalStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def rows(self: Self) -> "List[_1972.StiffnessRow]":
        """List[mastapy.bearings.bearing_results.StiffnessRow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rows

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BearingStiffnessMatrixReporter._Cast_BearingStiffnessMatrixReporter":
        return self._Cast_BearingStiffnessMatrixReporter(self)
