from __future__ import annotations

import base64
import copy
import typing

from stimulsoft_data_adapters.events.StiEventArgs import StiEventArgs

from ..report.enums.StiExportFormat import StiExportFormat

if typing.TYPE_CHECKING:
    from ..viewer.enums.StiExportAction import StiExportAction


class StiExportEventArgs(StiEventArgs):

    __action: int = None

    @property
    def action(self) -> int:
        """The current action for which the report was exported. StiExportAction enum."""

        return StiExportAction.EXPORT_REPORT if self.__action == None or self.__action == 0 else self.__action
    
    @action.setter
    def action(self, value: int):
        self.__action = value

    __format: int = None

    @property
    def format(self) -> int:
        """The current export format of the report. StiExportFormat enum."""

        return self.__format
    
    @format.setter
    def format(self, value: int):
        self.__format = value
        self.__fileExtension = StiExportFormat.getFileExtension(value)
        self.__mimeType = StiExportFormat.getMimeType(value)

    formatName: str = None
    """String name of the current export format of the report."""

    __settings: object = None

    @property
    def settings(self) -> object:
        """The object of all settings for the current report export."""

        return self.__settings
    
    @settings.setter
    def settings(self, value: object):
        self.__settings = copy.deepcopy(value)

    fileName: str = None
    """The file name of the exported report."""

    openAfterExport: bool = None
    """The flag indicates that the report will be exported in a new browser tab (True), or the file will be saved (False)."""

    __fileExtension: str = None

    @property
    def fileExtension(self) -> str:
        """File extension for the current report export."""

        return self.__fileExtension

    __mimeType: str = None

    @property
    def mimeType(self) -> str:
        """MIME type for the current report export."""

        return self.__mimeType

    __data: bytes = None

    @property
    def data(self) -> bytes:
        """The byte data of the exported report."""

        return self.__data
    
    @data.setter
    def data(self, value: str):
        if value != None:
            self.__data = base64.b64decode(value)