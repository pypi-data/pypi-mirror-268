"""DynamicForceVector3DResult"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_FORCE_VECTOR_3D_RESULT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Reporting",
    "DynamicForceVector3DResult",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses.reporting import _5532


__docformat__ = "restructuredtext en"
__all__ = ("DynamicForceVector3DResult",)


Self = TypeVar("Self", bound="DynamicForceVector3DResult")


class DynamicForceVector3DResult(_0.APIBase):
    """DynamicForceVector3DResult

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_FORCE_VECTOR_3D_RESULT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicForceVector3DResult")

    class _Cast_DynamicForceVector3DResult:
        """Special nested class for casting DynamicForceVector3DResult to subclasses."""

        def __init__(
            self: "DynamicForceVector3DResult._Cast_DynamicForceVector3DResult",
            parent: "DynamicForceVector3DResult",
        ):
            self._parent = parent

        @property
        def dynamic_force_vector_3d_result(
            self: "DynamicForceVector3DResult._Cast_DynamicForceVector3DResult",
        ) -> "DynamicForceVector3DResult":
            return self._parent

        def __getattr__(
            self: "DynamicForceVector3DResult._Cast_DynamicForceVector3DResult",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicForceVector3DResult.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def magnitude(self: Self) -> "_5532.DynamicForceResultAtTime":
        """mastapy.system_model.analyses_and_results.mbd_analyses.reporting.DynamicForceResultAtTime

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Magnitude

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def magnitude_xy(self: Self) -> "_5532.DynamicForceResultAtTime":
        """mastapy.system_model.analyses_and_results.mbd_analyses.reporting.DynamicForceResultAtTime

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MagnitudeXY

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def x(self: Self) -> "_5532.DynamicForceResultAtTime":
        """mastapy.system_model.analyses_and_results.mbd_analyses.reporting.DynamicForceResultAtTime

        Note:
            This property is readonly.
        """
        temp = self.wrapped.X

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def y(self: Self) -> "_5532.DynamicForceResultAtTime":
        """mastapy.system_model.analyses_and_results.mbd_analyses.reporting.DynamicForceResultAtTime

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Y

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def z(self: Self) -> "_5532.DynamicForceResultAtTime":
        """mastapy.system_model.analyses_and_results.mbd_analyses.reporting.DynamicForceResultAtTime

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Z

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "DynamicForceVector3DResult._Cast_DynamicForceVector3DResult":
        return self._Cast_DynamicForceVector3DResult(self)
