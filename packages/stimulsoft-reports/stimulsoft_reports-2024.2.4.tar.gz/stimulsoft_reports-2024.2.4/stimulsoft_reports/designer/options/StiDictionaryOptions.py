from ...classes.StiComponentOptions import StiComponentOptions
from ..enums.StiDesignerPermissions import StiDesignerPermissions
from ..enums.StiNewReportDictionary import StiNewReportDictionary
from ..enums.StiUseAliases import StiUseAliases


class StiDictionaryOptions(StiComponentOptions):
    """A class which controls settings of the dictionary."""

### Properties

    @property
    def id(self) -> str:
        return super().id + '.dictionary'


### Protected

    _enums: list = [
        'useAliases', 'newReportDictionary', 'dataSourcesPermissions', 'dataConnectionsPermissions', 'dataColumnsPermissions',
        'dataRelationsPermissions', 'businessObjectsPermissions', 'variablesPermissions', 'resourcesPermissions'
    ]


### Options

    showDictionary: bool = True
    """Gets or sets a visibility of the dictionary in the designer."""

    showAdaptersInNewConnectionForm: bool = True
    """Gets or sets a visibility of the other category in the new connection form."""

    newReportDictionary: str = StiNewReportDictionary.AUTO
    """Gets or sets a value which indicates what to do with the dictionary when creating a new report in the designer."""

    useAliases: str = StiUseAliases.AUTO
    """Gets or sets a value which indicates that using aliases in the dictionary."""

    showDictionaryContextMenuProperties: bool = True
    """Gets or sets a visibility of the Properties item in the dictionary context menu."""

    dataSourcesPermissions: str = StiDesignerPermissions.ALL
    """Gets or sets a value of permissions for datasources in the designer."""

    dataConnectionsPermissions: str = StiDesignerPermissions.ALL
    """Gets or sets a value of connections for datasources in the designer."""

    dataColumnsPermissions: str = StiDesignerPermissions.ALL
    """Gets or sets a value of connections for columns in the designer."""

    dataRelationsPermissions: str = StiDesignerPermissions.ALL
    """Gets or sets a value of connections for relations in the designer."""

    businessObjectsPermissions: str = StiDesignerPermissions.ALL
    """Gets or sets a value of connections for business objects in the designer."""

    variablesPermissions: str = StiDesignerPermissions.ALL
    """Gets or sets a value of connections for variables in the designer."""

    resourcesPermissions: str = StiDesignerPermissions.ALL
    """Gets or sets a value of connections for resources in the designer."""