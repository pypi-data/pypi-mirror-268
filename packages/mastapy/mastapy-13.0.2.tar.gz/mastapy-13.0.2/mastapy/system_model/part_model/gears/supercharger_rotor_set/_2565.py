"""RotorSetDataInputFileOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility_gui import _1855
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROTOR_SET_DATA_INPUT_FILE_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears.SuperchargerRotorSet",
    "RotorSetDataInputFileOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("RotorSetDataInputFileOptions",)


Self = TypeVar("Self", bound="RotorSetDataInputFileOptions")


class RotorSetDataInputFileOptions(_1855.DataInputFileOptions):
    """RotorSetDataInputFileOptions

    This is a mastapy class.
    """

    TYPE = _ROTOR_SET_DATA_INPUT_FILE_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RotorSetDataInputFileOptions")

    class _Cast_RotorSetDataInputFileOptions:
        """Special nested class for casting RotorSetDataInputFileOptions to subclasses."""

        def __init__(
            self: "RotorSetDataInputFileOptions._Cast_RotorSetDataInputFileOptions",
            parent: "RotorSetDataInputFileOptions",
        ):
            self._parent = parent

        @property
        def data_input_file_options(
            self: "RotorSetDataInputFileOptions._Cast_RotorSetDataInputFileOptions",
        ) -> "_1855.DataInputFileOptions":
            return self._parent._cast(_1855.DataInputFileOptions)

        @property
        def rotor_set_data_input_file_options(
            self: "RotorSetDataInputFileOptions._Cast_RotorSetDataInputFileOptions",
        ) -> "RotorSetDataInputFileOptions":
            return self._parent

        def __getattr__(
            self: "RotorSetDataInputFileOptions._Cast_RotorSetDataInputFileOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RotorSetDataInputFileOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "RotorSetDataInputFileOptions._Cast_RotorSetDataInputFileOptions":
        return self._Cast_RotorSetDataInputFileOptions(self)
