from ...classes.StiComponentOptions import StiComponentOptions
from ..enums.StiChartRenderType import StiChartRenderType
from ..enums.StiContentAlignment import StiContentAlignment
from ..enums.StiFirstDayOfWeek import StiFirstDayOfWeek
from ..enums.StiHtmlExportMode import StiHtmlExportMode
from ..enums.StiInterfaceType import StiInterfaceType
from ..enums.StiParametersPanelPosition import StiParametersPanelPosition
from ..enums.StiViewerTheme import StiViewerTheme
from ..enums.StiWebUIIconSet import StiWebUIIconSet


class StiAppearanceOptions(StiComponentOptions):
    """A class which controls settings of the viewer appearance."""
    
### Properties

    @property
    def id(self) -> str:
        return super().id + '.appearance'


### Protected

    _enums: list = [
        'pageAlignment', 'parametersPanelPosition', 'interfaceType', 'chartRenderType', 'reportDisplayMode',
        'datePickerFirstDayOfWeek', 'theme', 'iconSet'
    ]


### Options

    theme: str = StiViewerTheme.OFFICE_2022_WHITE_BLUE
    """Gets or sets the current visual theme which is used for drawing visual elements of the viewer."""

    iconSet: str = StiWebUIIconSet.AUTO
    """ Gets or sets the current icon set for the viewer. """

    backgroundColor: str = 'white'
    """Gets or sets the background color of the viewer."""

    pageBorderColor: str = 'gray'
    """Gets or sets a color of the report page border."""

    rightToLeft: bool = False
    """Gets or sets a value which controls of output objects in the right to left mode."""

    fullScreenMode: bool = False
    """Gets or sets a value which indicates which indicates that the viewer is displayed in full screen mode."""

    scrollbarsMode: bool = False
    """Gets or sets a value which indicates that the viewer will show the report area with scrollbars."""

    openLinksWindow: str = '_blank'
    """Gets or sets a browser window to open links from the report."""

    openExportedReportWindow: str = '_blank'
    """Gets or sets a browser window to open the exported report."""

    showTooltips: bool = True
    """Gets or sets a value which indicates that show or hide tooltips."""

    showTooltipsHelp: bool = True
    """Gets or sets a value which indicates that show or hide the help link in tooltips."""

    showDialogsHelp: bool = True
    """Gets or sets a value which indicates that show or hide the help button in dialogs."""

    pageAlignment: str = StiContentAlignment.DEFAULT
    """Gets or sets the alignment of the viewer page."""

    showPageShadow: bool = False
    """Gets or sets a value which indicates that the shadow of the page will be displayed in the viewer."""

    bookmarksPrint: bool = False
    """Gets or sets a value which allows printing report bookmarks."""

    bookmarksTreeWidth: int = 180
    """Gets or sets a width of the bookmarks tree in the viewer."""

    parametersPanelPosition: str = StiParametersPanelPosition.FROM_REPORT
    """Gets or sets a position of the parameters panel."""

    parametersPanelMaxHeight: int = 300
    """Gets or sets a max height of parameters panel in the viewer."""

    parametersPanelColumnsCount: int = 2
    """Gets or sets a count columns in parameters panel."""

    parametersPanelDateFormat: str = ''
    """Gets or sets a date format for datetime parameters in parameters panel. The default is the client browser date format."""

    parametersPanelSortDataItems: bool = False
    """Gets or sets a value which indicates that variable items will be sorted."""

    interfaceType: str = StiInterfaceType.AUTO
    """Gets or sets the type of the viewer interface."""

    chartRenderType: str = StiChartRenderType.ANIMATED_VECTOR
    """Gets or sets the type of the chart in the viewer."""

    reportDisplayMode: str = StiHtmlExportMode.FROM_REPORT
    """Gets or sets a method how the viewer will show a report."""

    datePickerFirstDayOfWeek: str = StiFirstDayOfWeek.AUTO
    """Gets or sets the first day of week in the date picker"""

    datePickerIncludeCurrentDayForRanges: bool = False
    """Gets or sets a value, which indicates that the current day will be included in the ranges of the date picker."""

    allowTouchZoom: bool = True
    """Gets or sets a value which allows touch zoom in the viewer."""

    allowMobileMode: bool = True
    """Gets or sets a value which indicates that allows mobile mode of the viewer interface."""

    combineReportPages: bool = False
    """Gets or sets a value which indicates that if a report contains several pages, then they will be combined in preview."""
