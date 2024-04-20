from __future__ import annotations

import typing

from stimulsoft_data_adapters.events.StiEvent import StiEvent
from stimulsoft_data_adapters.events.StiEventArgs import StiEventArgs

from ..classes.StiFileResult import StiFileResult
from ..classes.StiJavaScript import StiJavaScript
from ..classes.StiLicense import StiLicense
from ..classes.StiRequest import StiRequest
from ..classes.StiResponse import StiResponse
from ..classes.StiResult import StiResult
from ..enums.StiComponentType import StiComponentType
from ..enums.StiDataType import StiDataType
from ..enums.StiHtmlMode import StiHtmlMode

if typing.TYPE_CHECKING:
    from .StiHandler import StiHandler


class StiComponent:

### Fields
    
    id: str = None


### Private
    
    __handler: StiHandler = None
    __htmlRendered: bool = False
    __processRequestResult: bool = None
    __javascript: StiJavaScript = None
    __license: StiLicense = None


### Properties

    @property
    def componentType(self) -> str:
        return None
    
    @property
    def htmlRendered(self) -> str:
        return self.__htmlRendered

    @property
    def handler(self) -> StiHandler:
        return self.__handler
    
    @handler.setter
    def handler(self, value: StiHandler):
        if value != None:
            self.__handler = value

    @property
    def request(self) -> StiRequest:
        return self.handler.request if self.handler != None else None

    @property
    def javascript(self) -> StiJavaScript:
        """Controls the deployment of all designer JavaScripts."""

        return self.__javascript
    
    @property
    def license(self) -> StiLicense:
        """Applies the product license key in various formats."""

        return self.__license
    
    @license.setter
    def license(self, value: StiLicense):
        self.__license = value


### Protected

    def _getComponentHtml(self) -> str:
        return ''
    
    def _getDefaultEventResult(self, event: StiEvent, args: StiEventArgs) -> StiResult | None:
        if len(event) > 0:
            result = event(args)
            if result == None or result == True:
                return StiResult.getSuccess()
            if result == False:
                return StiResult.getError(f'An error occurred while processing the {self.request.event} event.')
            if isinstance(result, StiResult):
                return result
            return StiResult.getSuccess(str(result))
        
        return None


### Public: Request

    def processRequest(self, request: object = None, query: dict | str = None, body: bytes | str = None) -> bool:
        self.__processRequestResult = self.handler.processRequest(request, query, body)
        return self.__processRequestResult
    
    def getEventResult(self) -> StiResult:
        return None
    
    def getResponse(self) -> StiResponse:
        if self.__processRequestResult == False:
            html = self.getHtml(StiHtmlMode.HTML_PAGE)
            result = StiFileResult(html, StiDataType.HTML)
            return StiResponse(self.handler, result)

        self.__processRequestResult = None
        return self.handler.getResponse()
    
    def getFrameworkResponse(self, handler = None) -> object:
        """
        Returns a response intended for one of the supported frameworks.
        """
        
        return self.getResponse().getFrameworkResponse(handler)


### Public

    def getHtml(self, mode = StiHtmlMode.HTML_SCRIPTS) -> str:
        """Get the HTML representation of the component."""

        result = ''

        if mode == StiHtmlMode.HTML_PAGE:
            result += '<!DOCTYPE html>\n<html>\n<head>\n'
            result += self.javascript.getHtml()
            result += '</head>\n<body onload="start()">\n'

        if mode == StiHtmlMode.HTML_SCRIPTS or mode == StiHtmlMode.HTML_PAGE:
            if self.componentType == StiComponentType.VIEWER or self.componentType == StiComponentType.DESIGNER:
                result += f'<div id="{self.id}Content"></div>\n'

            result += '<script type="text/javascript">\n'

        if mode == StiHtmlMode.HTML_PAGE:
            result += 'function start() {\n'

        result += self._getComponentHtml()

        if mode == StiHtmlMode.HTML_PAGE:
            result += '}\n'

        if mode == StiHtmlMode.HTML_SCRIPTS or mode == StiHtmlMode.HTML_PAGE:
            result += '</script>\n'

        if mode == StiHtmlMode.HTML_PAGE:
            result += '</body>\n</html>'

        self.__htmlRendered = True
        return result
    
    
### Constructor

    def __init__(self):
        self.__javascript = StiJavaScript(self)
        self.__license = StiLicense()