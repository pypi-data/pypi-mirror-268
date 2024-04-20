from typing import Final


class StiEventType:
    GET_RESOURCE: Final = 'GetResource'
    PREPARE_VARIABLES: Final = 'PrepareVariables'
    BEGIN_PROCESS_DATA: Final = 'BeginProcessData'
    CREATE_REPORT: Final = 'CreateReport'
    OPEN_REPORT: Final = 'OpenReport'
    OPENED_REPORT: Final = 'OpenedReport'
    SAVE_REPORT: Final = 'SaveReport'
    SAVE_AS_REPORT: Final = 'SaveAsReport'
    PRINT_REPORT: Final = 'PrintReport'
    BEGIN_EXPORT_REPORT: Final = 'BeginExportReport'
    END_EXPORT_REPORT: Final = 'EndExportReport'
    EMAIL_REPORT: Final = 'EmailReport'
    INTERACTION: Final = 'Interaction'
    DESIGN_REPORT: Final = 'DesignReport'
    PREVIEW_REPORT: Final = 'PreviewReport'
    EXIT: Final = 'Exit'