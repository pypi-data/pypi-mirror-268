"""CrossedRollerBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_designs.rolling import _2169
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CROSSED_ROLLER_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "CrossedRollerBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2172
    from mastapy.bearings.bearing_designs import _2138, _2141, _2137


__docformat__ = "restructuredtext en"
__all__ = ("CrossedRollerBearing",)


Self = TypeVar("Self", bound="CrossedRollerBearing")


class CrossedRollerBearing(_2169.RollerBearing):
    """CrossedRollerBearing

    This is a mastapy class.
    """

    TYPE = _CROSSED_ROLLER_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CrossedRollerBearing")

    class _Cast_CrossedRollerBearing:
        """Special nested class for casting CrossedRollerBearing to subclasses."""

        def __init__(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing",
            parent: "CrossedRollerBearing",
        ):
            self._parent = parent

        @property
        def roller_bearing(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing",
        ) -> "_2169.RollerBearing":
            return self._parent._cast(_2169.RollerBearing)

        @property
        def rolling_bearing(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing",
        ) -> "_2172.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2172

            return self._parent._cast(_2172.RollingBearing)

        @property
        def detailed_bearing(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing",
        ) -> "_2138.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2138

            return self._parent._cast(_2138.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing",
        ) -> "_2141.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2141

            return self._parent._cast(_2141.NonLinearBearing)

        @property
        def bearing_design(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing",
        ) -> "_2137.BearingDesign":
            from mastapy.bearings.bearing_designs import _2137

            return self._parent._cast(_2137.BearingDesign)

        @property
        def crossed_roller_bearing(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing",
        ) -> "CrossedRollerBearing":
            return self._parent

        def __getattr__(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CrossedRollerBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CrossedRollerBearing._Cast_CrossedRollerBearing":
        return self._Cast_CrossedRollerBearing(self)
