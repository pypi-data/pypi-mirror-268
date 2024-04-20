from ...classes.StiComponentOptions import StiComponentOptions
from ..enums.StiContentAlignment import StiContentAlignment
from ..enums.StiPrintDestination import StiPrintDestination
from ..enums.StiShowMenuMode import StiShowMenuMode
from ..enums.StiToolbarDisplayMode import StiToolbarDisplayMode
from ..enums.StiWebViewMode import StiWebViewMode


class StiToolbarOptions(StiComponentOptions):
    """A class which controls settings of the viewer toolbar."""

### Properties

    @property
    def id(self) -> str:
        return super().id + '.toolbar'


### Protected

    _enums: list = [
        'displayMode', 'alignment', 'printDestination', 'viewMode', 'zoom', 'showMenuMode'
    ]


### Options

    visible: bool = True
    """Gets or sets a value which indicates that toolbar will be shown in the viewer."""

    displayMode: str = StiToolbarDisplayMode.SIMPLE
    """Gets or sets the display mode of the toolbar - simple or separated into upper and lower parts."""

    backgroundColor: str = 'transparent'
    """Gets or sets a color of the toolbar background. The default value is the theme color."""

    borderColor: str = 'transparent'
    """Gets or sets a color of the toolbar border. The default value is the theme color."""

    fontColor: str = 'transparent'
    """Gets or sets a color of the toolbar texts."""

    fontFamily: str = 'Arial'
    """Gets or sets a value which indicates which font family will be used for drawing texts in the viewer."""

    alignment: str = StiContentAlignment.DEFAULT
    """Gets or sets the alignment of the viewer toolbar."""

    showButtonCaptions: bool = True
    """Gets or sets a value which allows displaying or hiding toolbar buttons captions."""

    showPrintButton: bool = True
    """Gets or sets a visibility of the Print button in the toolbar of the viewer."""

    showOpenButton: bool = True
    """Gets or sets a visibility of the Open button in the toolbar of the viewer."""

    showSaveButton: bool = True
    """Gets or sets a visibility of the Save button in the toolbar of the viewer."""

    showSendEmailButton: bool = False
    """Gets or sets a visibility of the Send Email button in the toolbar of the viewer."""

    showFindButton: bool = True
    """Gets or sets a visibility of the Find button in the toolbar of the viewer."""

    showBookmarksButton: bool = True
    """Gets or sets a visibility of the Bookmarks button in the toolbar of the viewer."""

    showParametersButton: bool = True
    """Gets or sets a visibility of the Parameters button in the toolbar of the viewer."""

    showResourcesButton: bool = True
    """Gets or sets a visibility of the Resources button in the toolbar of the viewer."""

    showEditorButton: bool = True
    """Gets or sets a visibility of the Editor button in the toolbar of the viewer."""

    showFullScreenButton: bool = True
    """Gets or sets a visibility of the Full Screen button in the toolbar of the viewer."""

    showRefreshButton: bool = True
    """Gets or sets a visibility of the Refresh button in the toolbar of the viewer."""

    showFirstPageButton: bool = True
    """Gets or sets a visibility of the First Page button in the toolbar of the viewer."""

    showPreviousPageButton: bool = True
    """Gets or sets a visibility of the Prev Page button in the toolbar of the viewer."""

    showCurrentPageControl: bool = True
    """Gets or sets a visibility of the current page control in the toolbar of the viewer."""

    showNextPageButton: bool = True
    """Gets or sets a visibility of the Next Page button in the toolbar of the viewer."""

    showLastPageButton: bool = True
    """Gets or sets a visibility of the Last Page button in the toolbar of the viewer."""

    showZoomButton: bool = True
    """Gets or sets a visibility of the Zoom control in the toolbar of the viewer."""

    showViewModeButton: bool = True
    """Gets or sets a visibility of the View Mode button in the toolbar of the viewer."""

    showDesignButton: bool = False
    """Gets or sets a visibility of the Design button in the toolbar of the viewer."""

    showAboutButton: bool = True
    """Gets or sets a visibility of the About button in the toolbar of the viewer."""

    showPinToolbarButton: bool = True
    """Gets or sets a visibility of the Pin button in the toolbar of the viewer in mobile mode."""

    printDestination: str = StiPrintDestination.DEFAULT
    """Gets or sets the default mode of the report print destination."""

    viewMode: str = StiWebViewMode.SINGLE_PAGE
    """Gets or sets the mode of showing a report in the viewer - one page or the whole report."""

    zoom: int = 100
    """Gets or sets the report showing zoom. The default value is 100."""

    menuAnimation: bool = True
    """Gets or sets a value which indicates that menu animation is enabled."""

    showMenuMode: str = StiShowMenuMode.CLICK
    """Gets or sets the mode that shows menu of the viewer."""

    autoHide: bool = False
    """Gets or sets a value which allows automatically hide the viewer toolbar in mobile mode."""