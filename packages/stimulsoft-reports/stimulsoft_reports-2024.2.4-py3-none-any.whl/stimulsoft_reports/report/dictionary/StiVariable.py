from ..enums.StiVariableType import StiVariableType


class StiVariable:
    
    name: str = None
    """The name of the variable."""

    typeName: str = None
    """The type of the variable. Is equal to one of the values of the StiVariableType enumeration."""

    value: object = None
    """The value of the variable. The type of object depends on the type of variable."""

    def getHtml(self) -> str:
        """Get the HTML representation of the component."""
        
        return f"let {self.name} = new Stimulsoft.Report.Dictionary.StiVariable" \
            f"('', '{self.name}', '{self.name}', '', Stimulsoft.System.{self.typeName}, '{self.value}');\n"

    def __init__(self, name: str, typeName: str = StiVariableType.STRING, value: str = ''):
        self.name = name
        self.typeName = typeName
        self.value = value