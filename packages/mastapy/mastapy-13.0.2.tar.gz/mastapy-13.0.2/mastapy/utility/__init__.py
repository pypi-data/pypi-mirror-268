"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1584 import Command
    from ._1585 import AnalysisRunInformation
    from ._1586 import DispatcherHelper
    from ._1587 import EnvironmentSummary
    from ._1588 import ExternalFullFEFileOption
    from ._1589 import FileHistory
    from ._1590 import FileHistoryItem
    from ._1591 import FolderMonitor
    from ._1593 import IndependentReportablePropertiesBase
    from ._1594 import InputNamePrompter
    from ._1595 import IntegerRange
    from ._1596 import LoadCaseOverrideOption
    from ._1597 import MethodOutcome
    from ._1598 import MethodOutcomeWithResult
    from ._1599 import MKLVersion
    from ._1600 import NumberFormatInfoSummary
    from ._1601 import PerMachineSettings
    from ._1602 import PersistentSingleton
    from ._1603 import ProgramSettings
    from ._1604 import PushbulletSettings
    from ._1605 import RoundingMethods
    from ._1606 import SelectableFolder
    from ._1607 import SystemDirectory
    from ._1608 import SystemDirectoryPopulator
else:
    import_structure = {
        "_1584": ["Command"],
        "_1585": ["AnalysisRunInformation"],
        "_1586": ["DispatcherHelper"],
        "_1587": ["EnvironmentSummary"],
        "_1588": ["ExternalFullFEFileOption"],
        "_1589": ["FileHistory"],
        "_1590": ["FileHistoryItem"],
        "_1591": ["FolderMonitor"],
        "_1593": ["IndependentReportablePropertiesBase"],
        "_1594": ["InputNamePrompter"],
        "_1595": ["IntegerRange"],
        "_1596": ["LoadCaseOverrideOption"],
        "_1597": ["MethodOutcome"],
        "_1598": ["MethodOutcomeWithResult"],
        "_1599": ["MKLVersion"],
        "_1600": ["NumberFormatInfoSummary"],
        "_1601": ["PerMachineSettings"],
        "_1602": ["PersistentSingleton"],
        "_1603": ["ProgramSettings"],
        "_1604": ["PushbulletSettings"],
        "_1605": ["RoundingMethods"],
        "_1606": ["SelectableFolder"],
        "_1607": ["SystemDirectory"],
        "_1608": ["SystemDirectoryPopulator"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Command",
    "AnalysisRunInformation",
    "DispatcherHelper",
    "EnvironmentSummary",
    "ExternalFullFEFileOption",
    "FileHistory",
    "FileHistoryItem",
    "FolderMonitor",
    "IndependentReportablePropertiesBase",
    "InputNamePrompter",
    "IntegerRange",
    "LoadCaseOverrideOption",
    "MethodOutcome",
    "MethodOutcomeWithResult",
    "MKLVersion",
    "NumberFormatInfoSummary",
    "PerMachineSettings",
    "PersistentSingleton",
    "ProgramSettings",
    "PushbulletSettings",
    "RoundingMethods",
    "SelectableFolder",
    "SystemDirectory",
    "SystemDirectoryPopulator",
)
