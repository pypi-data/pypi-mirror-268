import base64
import gzip
import os
import pathlib

from ..classes.StiComponent import StiComponent
from ..classes.StiHandler import StiHandler
from ..enums.StiComponentType import StiComponentType
from ..events.StiComponentEvent import StiComponentEvent
from .dictionary.StiDictionary import StiDictionary
from .enums.StiExportFormat import StiExportFormat
from .enums.StiRangeType import StiRangeType
from .StiPagesRange import StiPagesRange


class StiReport(StiComponent):

### Events

    onBeforeRender: StiComponentEvent = None
    """The event is invoked called before all actions related to report rendering."""

    onAfterRender: StiComponentEvent = None
    """The event is invoked called immediately after report rendering."""

    onPrepareVariables: StiComponentEvent = None
    """The event is invoked before rendering a report after preparing report variables."""

    onBeginProcessData: StiComponentEvent = None
    """The event is invoked before data request, which needed to render a report."""

    onEndProcessData: StiComponentEvent = None
    """The event is invoked after loading data before rendering a report."""


### Private

    __dictionary: StiDictionary = None
    __renderCalled: bool = False
    __printCalled: bool = False
    __exportCalled: bool = False
    __openAfterExport: bool = False

    __reportString: str = None
    __reportFile: str = None
    __documentString: str = None
    __documentFile: str = None
    __exportFile: str = None
    __exportFormat: str = None
    __pagesRange: str = None

    def __clearReport(self) -> None:
        self.__reportString = None
        self.__reportFile = None
        self.__documentString = None
        self.__documentFile = None
        self.__exportFile = None

    def __getAbsoluteFilePath(self, filePath: str) -> str:
        filePath = os.path.normpath(filePath.split('?')[0])
        pathInfo = pathlib.Path(filePath)
        if not pathInfo.is_file():
            filePath = os.getcwd() + filePath

        pathInfo = pathlib.Path(filePath)
        if pathInfo.is_file():
            return filePath
        
        return None


### Properties

    @property
    def componentType(self) -> str:
        return StiComponentType.REPORT

    @property
    def handler(self) -> StiHandler:
        return super().handler
    
    @handler.setter
    def handler(self, value: StiHandler):
        super(type(self), type(self)).handler.fset(self, value)
        if value != None:
            value.component = self
            value.onBeginProcessData = self.onBeginProcessData
            value.onEndProcessData = self.onEndProcessData
            value.onPrepareVariables = self.onPrepareVariables
    
    @property
    def dictionary(self) -> StiDictionary:
        """Manages variables and data for the report."""

        return self.__dictionary


### Protected

    def _getComponentHtml(self) -> str:
        result = ''

        result += self.license.getHtml()
        result += f'let {self.id} = new Stimulsoft.Report.StiReport();\n'
        
        result += self.onPrepareVariables.getHtml(True)
        result += self.onBeginProcessData.getHtml(True)
        result += self.onEndProcessData.getHtml()

        if self.__reportFile != None and len(self.__reportFile) > 0:
            result += f"{self.id}.loadFile('{self.__reportFile}');\n"

        elif self.__reportString != None and len(self.__reportString) > 0:
            result += f"{self.id}.loadPacked('{self.__reportString}');\n"

        elif self.__documentFile != None and len(self.__documentFile) > 0:
            result += f"{self.id}.loadDocumentFile('{self.__documentFile}');\n"

        elif self.__documentString != None and len(self.__documentString) > 0:
            result += f"{self.id}.loadPackedDocument('{self.__documentString}');\n"

        result += self.dictionary.getHtml()
        result += self.onBeforeRender.getHtml(internal = True)

        if self.__renderCalled:
            result += f'{self.id}.renderAsync(function () {{\n'
            result += self.onAfterRender.getHtml(internal = True)

        if self.__printCalled:
            pagesRangeId = ''
            if len(self.__pagesRange or '') > 0:
                pagesRange = StiPagesRange(StiRangeType.PAGES, self.__pagesRange)
                pagesRangeId = pagesRange.id
                result += pagesRange.getHtml()

            result += f'report.print({pagesRangeId});\n'

        if self.__exportCalled:
            exportFileExt = StiExportFormat.getFileExtension(self.__exportFormat)
            exportMimeType = StiExportFormat.getMimeType(self.__exportFormat)
            exportName = StiExportFormat.getFormatName(self.__exportFormat)

            result += 'report.exportDocumentAsync(function (data) {\n'
            result += \
                f"var blob = new Blob([new Uint8Array(data)], {{ type: '{exportMimeType}' }});\n" \
                'var fileURL = URL.createObjectURL(blob);\n' \
                'window.open(fileURL);\n' \
                if self.__openAfterExport else \
                f"Stimulsoft.System.StiObject.saveAs(data, '{self.__exportFile}.{exportFileExt}', '{exportMimeType}');\n"
            result += f'}}, Stimulsoft.Report.StiExportFormat.{exportName});\n'

        if self.__renderCalled:
            result += '});\n'

        return result
    

### Public

    def loadFile(self, filePath: str, load: bool = False) -> None:
        """Loading a report template from a file or URL address.
        :param filePath: The path to the file or the URL of the report template.
        :param load: Loading a report file on the server side."""
    
        self.__clearReport()
        pathInfo = pathlib.Path(filePath)
        self.__exportFile = pathInfo.stem
        if load:
            extension: str = pathInfo.suffix[1:].split('?')[0]
            filePath = self.__getAbsoluteFilePath(filePath)
            if filePath != None and extension == 'mrt':
                with open(filePath, mode='r', encoding='utf-8') as file:
                    self.__reportString = file.read()
                    gzipBytes = gzip.compress(self.__reportString.encode())
                    self.__reportString = base64.b64encode(gzipBytes).decode()
        else:
            self.__reportFile = filePath

    def load(self, data: str, fileName: str = 'Report') -> None:
        """Loading a report template from an XML or JSON string and send it as a packed string in Base64 format.
        :param data: Report template in XML or JSON format.
        :param fileName: The name of the report file to be used for saving and exporting."""

        self.__clearReport()
        self.__exportFile = fileName
        gzipBytes = gzip.compress(data.encode())
        self.__reportString = base64.b64encode(gzipBytes).decode()

    def loadPacked(self, data: str, fileName: str = 'Report') -> None:
        """Loading a report template from a packed string in Base64 format.
        :param data: Report template as a packed string in Base64 format.
        :param fileName: The name of the report file to be used for saving and exporting."""
    
        self.__clearReport()
        self.__exportFile = fileName
        self.__reportString = data
    
    def loadDocumentFile(self, filePath: str, load: str = False) -> None:
        """Load a rendered report from a file or URL address.
        :param filePath: The path to the file or the URL of the rendered report.
        :param load: Loading a report file on the server side."""

        self.__clearReport()
        pathInfo = pathlib.Path(filePath)
        self.__exportFile = pathInfo.stem
        if load:
            extension: str = pathInfo.suffix[1:].split('?')[0]
            filePath = self.__getAbsoluteFilePath(filePath)
            if filePath != None and extension == 'mdc':
                with open(filePath, mode='r', encoding='utf-8') as file:
                    self.__documentString = file.read()
                    gzipBytes = gzip.compress(self.__documentString.encode())
                    self.__documentString = base64.b64encode(gzipBytes).decode()
        else:
            self.__documentFile = filePath

    def loadDocument(self, data: str, fileName: str = 'Report') -> None:
        """Load a rendered report from an XML or JSON string and send it as a packed string in Base64 format.
        :param data: Rendered report in XML or JSON format.
        :param fileName: The name of the report file to be used for saving and exporting."""
    
        self.__clearReport()
        self.__exportFile = fileName
        gzipBytes = gzip.compress(data.encode())
        self.__documentString = base64.b64encode(gzipBytes).decode()

    def loadPackedDocument(self, data: str, fileName: str = 'Report') -> None:
        """Loading a rendered report from a packed string in Base64 format.
        :param data: Rendered report as a packed string in Base64 format.
        :param fileName: The name of the report file to be used for saving and exporting."""
    
        self.__clearReport()
        self.__exportFile = fileName
        self.__documentString = data

    def exportDocument(self, format: str, openAfterExport: bool = False) -> None:
        """Exporting the report to the specified format and saving it as a file on the client side.
        :param format: The type of the export. Is equal to one of the values of the StiExportFormat enumeration."""
    
        self.__exportCalled = True
        self.__openAfterExport = openAfterExport
        self.__exportFormat = format

    def render(self) -> None:
        """Building a report and calling a JavaScript callback function, if it is set."""
    
        self.__renderCalled = True

    def print(self, pagesRange: str | int = None) -> None:
        """Printing the rendered report. The browser print dialog will be called."""
    
        self.__printCalled = True
        self.__pagesRange = str(pagesRange)
    

### Constructor

    def __init__(self):
        super().__init__()

        self.id = 'report'
        
        self.__dictionary = StiDictionary(self)

        self.onBeginProcessData = StiComponentEvent(self, 'onBeginProcessData')
        self.onBeginProcessData += True
        
        self.onEndProcessData = StiComponentEvent(self, 'onEndProcessData')
        self.onPrepareVariables = StiComponentEvent(self, 'onPrepareVariables')
        self.onBeforeRender = StiComponentEvent(self, 'onBeforeRender')
        self.onAfterRender = StiComponentEvent(self, 'onAfterRender')
        
        self.handler = StiHandler()