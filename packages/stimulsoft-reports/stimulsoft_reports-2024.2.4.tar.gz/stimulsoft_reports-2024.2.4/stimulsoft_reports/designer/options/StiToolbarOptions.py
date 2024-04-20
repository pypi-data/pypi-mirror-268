from ...classes.StiComponentOptions import StiComponentOptions


class StiToolbarOptions(StiComponentOptions):
    """A class which controls settings of the designer toolbar."""

### Properties

    @property
    def id(self) -> str:
        return super().id + '.toolbar'


### Options

    visible: bool = True
    """Gets or sets a value which indicates that toolbar will be shown in the designer."""

    showPreviewButton: bool = True
    """Gets or sets a visibility of the preview button in the toolbar of the designer."""

    showSaveButton: bool = False
    """Gets or sets a visibility of the save button in the toolbar of the designer."""

    showAboutButton: bool = False
    """Gets or sets a visibility of the about button in the toolbar of the designer."""

    showFileMenu: bool = True
    """Gets or sets a visibility of the file menu of the designer."""

    showFileMenuNew: bool = True
    """Gets or sets a visibility of the item New in the file menu."""

    showFileMenuOpen: bool = True
    """Gets or sets a visibility of the item Open in the file menu."""

    showFileMenuSave: bool = True
    """Gets or sets a visibility of the item Save in the file menu."""

    showFileMenuSaveAs: bool = True
    """Gets or sets a visibility of the item Save As in the file menu."""

    showFileMenuClose: bool = True
    """Gets or sets a visibility of the item Close in the file menu."""

    showFileMenuExit: bool = False
    """Gets or sets a visibility of the item Exit in the file menu."""

    showFileMenuReportSetup: bool = True
    """Gets or sets a visibility of the item Report Setup in the file menu."""

    showFileMenuOptions: bool = True
    """Gets or sets a visibility of the item Options in the file menu."""

    showFileMenuInfo: bool = True
    """Gets or sets a visibility of the item Info in the file menu."""

    showFileMenuAbout: bool = True
    """Gets or sets a visibility of the item About in the file menu."""

    showFileMenuNewReport: bool = True
    """Gets or sets a visibility of the new report button in the file menu."""

    showFileMenuNewDashboard: bool = True
    """Gets or sets a visibility of the new dashboard button in the file menu."""

    showSetupToolboxButton: bool = True
    """Gets or sets a visibility of the setup toolbox button in the designer."""

    showNewPageButton: bool = True
    """Gets or sets a visibility of the new page button in the designer."""

    showNewDashboardButton: bool = True
    """Gets or sets a visibility of the new dashboard button in the designer."""