from ...classes.StiComponentOptions import StiComponentOptions
from ...viewer.enums.StiWebUIIconSet import StiWebUIIconSet
from ..enums.StiDesignerTheme import StiDesignerTheme
from ..enums.StiFirstDayOfWeek import StiFirstDayOfWeek
from ..enums.StiInterfaceType import StiInterfaceType
from ..enums.StiPropertiesGridPosition import StiPropertiesGridPosition
from ..enums.StiReportUnitType import StiReportUnitType
from ..enums.StiWizardType import StiWizardType


class StiAppearanceOptions(StiComponentOptions):
    """A class which controls settings of the designer appearance."""

### Properties

    @property
    def id(self) -> str:
        return super().id + '.appearance'


### Protected

    _enums: list = [
        'defaultUnit', 'interfaceType', 'propertiesGridPosition', 'datePickerFirstDayOfWeek',
        'wizardTypeRunningAfterLoad', 'zoom', 'theme'
    ]


### Options

    theme: str = StiDesignerTheme.OFFICE_2022_WHITE_BLUE
    """Gets or sets the current visual theme which is used for drawing visual elements of the designer."""

    iconSet: str = StiWebUIIconSet.AUTO
    """ Gets or sets the current icon set for the viewer. """

    defaultUnit: str = StiReportUnitType.CENTIMETERS
    """Gets or sets a default value of unit in the designer."""

    interfaceType: str = StiInterfaceType.AUTO
    """Gets or sets the type of the designer interface."""

    showAnimation: bool = True
    """Gets or sets a value which indicates that animation is enabled."""

    showSaveDialog: bool = True
    """Gets or sets a visibility of the save dialog of the designer."""

    showTooltips: bool = True
    """Gets or sets a value which indicates that show or hide tooltips."""

    showTooltipsHelp: bool = True
    """Gets or sets a value which indicates that show or hide tooltips help icon."""

    showDialogsHelp: bool = True
    """Gets or sets a value which indicates that show or hide the help button in dialogs."""

    fullScreenMode: bool = False
    """Gets or sets a value which indicates that the designer is displayed in full screen mode."""

    maximizeAfterCreating: bool = False
    """Gets or sets a value which indicates that the designer will be maximized after creation."""

    showLocalization: bool = True
    """Gets or sets a visibility of the localization control of the designer."""

    allowChangeWindowTitle: bool = True
    """Allow the designer to change the window title."""

    showPropertiesGrid: bool = True
    """Gets or sets a visibility of the properties grid in the designer."""

    showReportTree: bool = True
    """Gets or sets a visibility of the report tree in the designer."""

    propertiesGridPosition: str = StiPropertiesGridPosition.LEFT
    """Gets or sets a position of the properties grid in the designer."""

    showSystemFonts: bool = True
    """Gets or sets a visibility of the system fonts in the fonts list."""

    datePickerFirstDayOfWeek: str = StiFirstDayOfWeek.AUTO
    """Gets or sets the first day of week in the date picker."""

    undoMaxLevel: int = 6
    """Gets or sets a maximum level of undo actions with the report. A large number of actions consume more memory on the server side."""

    wizardTypeRunningAfterLoad: str = StiWizardType.NONE
    """Gets or sets a value of the wizard type which should be run after designer starts."""

    allowWordWrapTextEditors: bool = True
    """Gets or sets a value which indicates that allows word wrap in the text editors."""

    zoom: int = 100
    """Gets or sets the report showing zoom. The default value is 100."""
