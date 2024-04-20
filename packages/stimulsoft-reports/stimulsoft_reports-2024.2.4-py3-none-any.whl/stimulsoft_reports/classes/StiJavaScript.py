from __future__ import annotations

import typing

from ..enums.StiComponentType import StiComponentType

if typing.TYPE_CHECKING:
    from .StiComponent import StiComponent


class StiJavaScript:

### Private

    __component: StiComponent = None


### Options

    usePacked: bool = False
    reportsSet: bool = True
    reportsChart: bool = True
    reportsExport: bool = True
    reportsImportXlsx: bool = True
    reportsMaps: bool = True
    blocklyEditor: bool = True


### Public

    def getHtml(self) -> str:
        """Get the HTML representation of the component."""

        try:
            dashboards = True
            from stimulsoft_dashboards.report.StiDashboard import StiDashboard
        except Exception as e:
            dashboards = False

        extension = 'pack.js' if (self.usePacked) else 'js'
        scripts: list = []
        if self.reportsSet:
            scripts.append(f'stimulsoft.reports.{extension}')
        else:
            scripts.append(f'stimulsoft.reports.engine.{extension}')
            if self.reportsChart:
                scripts.append(f'stimulsoft.reports.chart.{extension}')
            if self.reportsExport:
                scripts.append(f'stimulsoft.reports.export.{extension}')
            if self.reportsMaps:
                scripts.append(f'stimulsoft.reports.maps.{extension}')
            if self.reportsImportXlsx:
                scripts.append(f'stimulsoft.reports.import.xlsx.{extension}')


        if dashboards:
            scripts.append(f'stimulsoft.dashboards.{extension}')

        if self.__component.componentType == StiComponentType.VIEWER or self.__component.componentType == StiComponentType.DESIGNER:
            scripts.append(f'stimulsoft.viewer.{extension}')

        if self.__component.componentType == StiComponentType.DESIGNER:
            scripts.append(f'stimulsoft.designer.{extension}')

            if self.blocklyEditor:
                scripts.append(f'stimulsoft.blockly.editor.{extension}')

        scripts.append('stimulsoft.handler.js')

        url = self.__component.handler.url
        return '\n'.join([f'<script src="{url}?sti_event=GetResource&sti_data={name}" type="text/javascript"></script>' for name in scripts])
    

### Constructor

    def __init__(self, component: StiComponent):
        self.__component = component
