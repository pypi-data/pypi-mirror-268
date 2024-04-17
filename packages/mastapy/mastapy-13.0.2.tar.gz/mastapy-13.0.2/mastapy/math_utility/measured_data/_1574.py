"""OnedimensionalFunctionLookupTable"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.math_utility.measured_data import _1573
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ONEDIMENSIONAL_FUNCTION_LOOKUP_TABLE = python_net_import(
    "SMT.MastaAPI.MathUtility.MeasuredData", "OnedimensionalFunctionLookupTable"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1542
    from mastapy.utility import _1593


__docformat__ = "restructuredtext en"
__all__ = ("OnedimensionalFunctionLookupTable",)


Self = TypeVar("Self", bound="OnedimensionalFunctionLookupTable")


class OnedimensionalFunctionLookupTable(
    _1573.LookupTableBase["OnedimensionalFunctionLookupTable"]
):
    """OnedimensionalFunctionLookupTable

    This is a mastapy class.
    """

    TYPE = _ONEDIMENSIONAL_FUNCTION_LOOKUP_TABLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OnedimensionalFunctionLookupTable")

    class _Cast_OnedimensionalFunctionLookupTable:
        """Special nested class for casting OnedimensionalFunctionLookupTable to subclasses."""

        def __init__(
            self: "OnedimensionalFunctionLookupTable._Cast_OnedimensionalFunctionLookupTable",
            parent: "OnedimensionalFunctionLookupTable",
        ):
            self._parent = parent

        @property
        def lookup_table_base(
            self: "OnedimensionalFunctionLookupTable._Cast_OnedimensionalFunctionLookupTable",
        ) -> "_1573.LookupTableBase":
            pass

            return self._parent._cast(_1573.LookupTableBase)

        @property
        def independent_reportable_properties_base(
            self: "OnedimensionalFunctionLookupTable._Cast_OnedimensionalFunctionLookupTable",
        ) -> "_1593.IndependentReportablePropertiesBase":
            pass

            from mastapy.utility import _1593

            return self._parent._cast(_1593.IndependentReportablePropertiesBase)

        @property
        def onedimensional_function_lookup_table(
            self: "OnedimensionalFunctionLookupTable._Cast_OnedimensionalFunctionLookupTable",
        ) -> "OnedimensionalFunctionLookupTable":
            return self._parent

        def __getattr__(
            self: "OnedimensionalFunctionLookupTable._Cast_OnedimensionalFunctionLookupTable",
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
        self: Self, instance_to_wrap: "OnedimensionalFunctionLookupTable.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def lookup_table(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.LookupTable

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @lookup_table.setter
    @enforce_parameter_types
    def lookup_table(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.LookupTable = value.wrapped

    @property
    def cast_to(
        self: Self,
    ) -> "OnedimensionalFunctionLookupTable._Cast_OnedimensionalFunctionLookupTable":
        return self._Cast_OnedimensionalFunctionLookupTable(self)
