from datetime import datetime

from stimulsoft_data_adapters.classes.StiBaseHandler import StiBaseHandler
from stimulsoft_data_adapters.enums.StiDatabaseType import StiDatabaseType
from stimulsoft_data_adapters.events.StiEvent import StiEvent

from ..classes.StiComponent import StiComponent
from ..enums.StiEventType import StiEventType
from .StiRequest import StiRequest
from .StiResponse import StiResponse
from .StiResult import StiResult


class StiHandler(StiBaseHandler):
    
    component: StiComponent = None
    request: StiRequest = None
    timeout: int = 30
    encryptData: bool = True
    escapeQueryParameters: bool = True
    passQueryParametersToReport: bool = False


### Private

    def __getJavaScriptValue(self, value) -> str:
        if value == None: return ''
        if type(value) == list: return str(value)
        if type(value) == str: return f"'{value}'"
        return str(value).lower()

    def __getJavaScript(self, data: bytes) -> bytes:
        csrf_token = None
        script = data.decode()
        script = script.replace('{databases}', self.__getJavaScriptValue(StiDatabaseType.getTypes()))
        script = script.replace('{csrf_token}', '' if csrf_token == None else csrf_token)
        script = script.replace('{url}', self.__getJavaScriptValue(self.url or ''))
        script = script.replace('{timeout}', self.__getJavaScriptValue(self.timeout))
        script = script.replace('{encryptData}', self.__getJavaScriptValue(self.encryptData))
        script = script.replace('{passQueryParametersToReport}', self.__getJavaScriptValue(self.passQueryParametersToReport))
        script = script.replace('{checkDataAdaptersVersion}', self.__getJavaScriptValue(self.checkDataAdaptersVersion))
        script = script.replace('{escapeQueryParameters}', self.__getJavaScriptValue(self.escapeQueryParameters))
        return script.encode()
    
    def __getPrepareVariablesResult(self) -> StiResult:
        if len(self.onPrepareVariables) > 0:
            from ..events.StiVariablesEventArgs import StiVariablesEventArgs
            from ..report.enums.StiVariableType import StiVariableType
            
            args = StiVariablesEventArgs(self.request)
            self.onPrepareVariables(args)

            result = StiResult.getSuccess()
            result.handlerVersion = self.version
            result.variables = list()
            for variableName in args.variables:
                variable = args.variables[variableName]
                variableChanged = True
                for variableOriginal in self.request.variables:
                    valueOriginal = variableOriginal['value']
                    if variableOriginal['name'] == variableName:
                        if variable.typeName[-5:] == 'Range' and type(variable.value) == dict:
                            value = variable.value
                            variableChanged = value.get('from') != valueOriginal.get('from') or value.get('to') != valueOriginal.get('to')
                        elif variable.typeName[-4:] == 'List' and type(variable.value) == list:
                            value = variable.value
                            variableChanged = len(value) != len(valueOriginal) or len(value) != sum([1 for i, j in zip(value, valueOriginal) if i == j])
                        else:
                            variableChanged = variableOriginal['value'] != variable.value
                        break
                if variableChanged:
                    if variable.typeName == StiVariableType.DATETIME and type(variable.value) == datetime:
                        variable.value = variable.value.strftime('%Y-%m-%d %H:%M:%S')
                    result.variables.append({ 'name': variable.name, 'type': variable.typeName, 'value': variable.value })
        else:
            result = StiResult.getError('The handler for the \'onPrepareVariables\' event is not specified.')

        return result
    

### Events

    onPrepareVariables: StiEvent = None
    """The event is invoked before rendering a report after preparing report variables."""


### Protected

    def _createRequest(self):
        return StiRequest()
    
    def _checkEvent(self):
        events = [getattr(StiEventType, field) for field in dir(StiEventType) if not callable(getattr(StiEventType, field)) and not field.startswith('_')]
        if self.request.event in events:
            return True

        return False
    
    def _checkCommand(self):
        if self.request.event == 'BeginProcessData':
            return super()._checkCommand()
        
        return True


### Public

    def getResponse(self) -> StiResponse:
        return StiResponse(self)
    
    def getResult(self):
        """
        The result of executing an event handler request. 
        The result contains a collection of data, message about the result of the command execution, and other technical information.
        """

        if self.request.event == StiEventType.GET_RESOURCE:
            try:
                from stimulsoft_dashboards.resources.StiResourcesHelper import StiResourcesHelper
            except Exception as e:
                from ..resources.StiResourcesHelper import StiResourcesHelper
            
            result = StiResourcesHelper.getResult(self.request.data)
            if result.success and self.request.data == 'stimulsoft.handler.js':
                result.data = self.__getJavaScript(result.data)
                result.handlerVersion = self.version

            return result
        
        if self.request.event == StiEventType.PREPARE_VARIABLES:
            return self.__getPrepareVariablesResult()
        
        if self.component != None:
            result = self.component.getEventResult()
            if result != None:
                result.handlerVersion = self.version
                return result
        
        return super().getResult()


### Constructor

    def __init__(self, url: str = None, timeout: int = 30):
        super().__init__(url)
        self.onBeginProcessData += True
        self.timeout = timeout

        self.onPrepareVariables = StiEvent(self, "onPrepareVariables")
