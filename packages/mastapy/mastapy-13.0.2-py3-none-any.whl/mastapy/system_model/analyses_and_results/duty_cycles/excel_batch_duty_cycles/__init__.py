"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6545 import ExcelBatchDutyCycleCreator
    from ._6546 import ExcelBatchDutyCycleSpectraCreatorDetails
    from ._6547 import ExcelFileDetails
    from ._6548 import ExcelSheet
    from ._6549 import ExcelSheetDesignStateSelector
    from ._6550 import MASTAFileDetails
else:
    import_structure = {
        "_6545": ["ExcelBatchDutyCycleCreator"],
        "_6546": ["ExcelBatchDutyCycleSpectraCreatorDetails"],
        "_6547": ["ExcelFileDetails"],
        "_6548": ["ExcelSheet"],
        "_6549": ["ExcelSheetDesignStateSelector"],
        "_6550": ["MASTAFileDetails"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ExcelBatchDutyCycleCreator",
    "ExcelBatchDutyCycleSpectraCreatorDetails",
    "ExcelFileDetails",
    "ExcelSheet",
    "ExcelSheetDesignStateSelector",
    "MASTAFileDetails",
)
