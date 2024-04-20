import copy

from stimulsoft_data_adapters.events.StiEventArgs import StiEventArgs


class StiReportEventArgs(StiEventArgs):

    __report: object = None

    @property
    def report(self) -> object:
        """The current report object as a JSON object."""

        return self.__report
    
    @report.setter
    def report(self, value: object):
        self.__report = copy.deepcopy(value)
    
    fileName: str = None
    """The name of the report file to save."""

    isWizardUsed: bool = None
    """A flag indicating that the wizard was used when creating the report."""

    autoSave: bool = None
    """A flag indicating that the report was saved automatically."""

    printAction: str = None
    """The current print type of the report. StiPrintAction enum."""
