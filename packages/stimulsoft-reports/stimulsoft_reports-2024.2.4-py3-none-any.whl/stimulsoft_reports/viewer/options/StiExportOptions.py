from ...classes.StiComponentOptions import StiComponentOptions


class StiExportOptions(StiComponentOptions):
    """A class which controls the export options."""
    
### Properties

    @property
    def id(self) -> str:
        return super().id + '.exports'


### Options

    storeExportSettings: bool = True
    """Gets or sets a value which allows store the export settings in the cookies."""

    showExportDialog: bool = True
    """Gets or sets a value which allows to display the export dialog, or to export with the default settings."""

    showExportToDocument: bool = True
    """Gets or sets a value which indicates that the user can save the report from the viewer to the report document file."""

    showExportToPdf: bool = True
    """Gets or sets a value which indicates that the user can save the report from the viewer to the PDF format."""

    showExportToXps: bool = True
    """Gets or sets a value which indicates that the user can save the report from the viewer to the Xps format."""

    showExportToPowerPoint: bool = True
    """Gets or sets a value which indicates that the user can save the report from the viewer to the HTML format."""

    showExportToHtml: bool = True
    """Gets or sets a value which indicates that the user can save the report from the viewer to the HTML format."""

    showExportToHtml5: bool = True
    """Gets or sets a value which indicates that the user can save the report from the viewer to the HTML5 format."""

    showExportToText: bool = True
    """Gets or sets a value which indicates that the user can save the report from the viewer to the Text format."""

    showExportToWord: bool = True
    """Gets or sets a value which indicates that the user can save the report from the viewer to the Word 2007-2024 format."""

    showExportToOpenDocumentWriter: bool = True
    """Gets or sets a value which indicates that the user can save the report from the viewer to the Open Document Text format."""

    showExportToExcel: bool = True
    """Gets or sets a value which indicates that the user can save the report from the viewer to the Excel 2007-2024 format."""

    showExportToOpenDocumentCalc: bool = True
    """Gets or sets a value which indicates that the user can save the report from the viewer to the Open Document Calc format."""

    showExportToCsv: bool = True
    """Gets or sets a value which indicates that the user can save the report from the viewer to the CSV format."""

    showExportToJson: bool = False
    """Gets or sets a value which indicates that the user can save the report from the viewer to the Json format."""

    showExportToImageSvg: bool = True
    """Gets or sets a value which indicates that the user can save the report from the viewer to the SVG format."""