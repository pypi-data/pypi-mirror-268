import json

from stimulsoft_data_adapters.classes.StiBaseRequest import StiBaseRequest


class StiRequest(StiBaseRequest):

### Fields

    sender: object = None
    data: str = None
    fileName: str = None
    action: str = None
    printAction: str = None
    format: str = None
    formatName: str = None
    settings: object = None
    variables: str = None
    isWizardUsed: bool = None
    report: str = None
    autoSave: bool = None


### Protected

    def _setField(self, name, value):
        if name == 'report' or name == 'settings':
            setattr(self, name, json.loads(value) if value != None else None)
        else:
            super()._setField(name, value)


### Properties

    """def checkRequestParams(self, obj: object):
        if (not obj.event is None and (obj.command == StiDataCommand.TEST_CONNECTION or StiDataCommand.EXECUTE_QUERY)):
            self.event = StiEventType.BEGIN_PROCESS_DATA

        if (obj.report):
            self.report = obj.report
            self.reportJson = json_encode(self.report)

        return StiResult.success(None, self)"""