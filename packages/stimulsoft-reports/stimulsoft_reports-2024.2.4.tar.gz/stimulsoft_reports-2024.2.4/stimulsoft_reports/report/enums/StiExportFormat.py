from typing import Final


class StiExportFormat:

### Constants

    PDF: Final = 1
    XPS: Final = 2
    TEXT: Final = 11
    EXCEL: Final = 14
    WORD: Final = 15
    CSV: Final = 17
    IMAGE_SVG: Final = 28
    HTML: Final = 32
    ODS: Final = 33
    ODT: Final = 34
    POWERPOINT: Final = 35
    HTML5: Final = 36
    DOCUMENT : Final= 1000


### Private

    def __getFormatName(format: int) -> str:
        names = {value: name for name, value in vars(StiExportFormat).items() if name.isupper()}
        return names[format]


### Public

    def getFileExtension(format: int) -> str:
        """Returns the file extension for the selected export format."""

        if format == StiExportFormat.TEXT:
            return 'txt'

        if format == StiExportFormat.EXCEL:
            return 'xlsx'

        if format == StiExportFormat.WORD:
            return 'docx'

        if format == StiExportFormat.HTML or format == StiExportFormat.HTML5:
            return 'html'

        if format == StiExportFormat.POWERPOINT:
            return 'pptx'

        if format == StiExportFormat.DOCUMENT:
            return 'mdc'
            
        return StiExportFormat.__getFormatName(format).replace('IMAGE_', '').lower()

    def getMimeType(format: int) -> str:
        """Returns the mimetype for the selected export format."""

        if format == StiExportFormat.PDF:
            return 'application/pdf'

        if format == StiExportFormat.XPS:
            return 'application/vnd.ms-xpsdocument'

        if format == StiExportFormat.TEXT:
            return 'text/plain'

        if format == StiExportFormat.EXCEL:
            return 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

        if format == StiExportFormat.WORD:
            return 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'

        if format == StiExportFormat.CSV:
            return 'text/csv'

        if format == StiExportFormat.IMAGE_SVG:
            return 'image/svg+xml'

        if format == StiExportFormat.HTML or format == StiExportFormat.HTML5:
            return 'text/html'

        if format == StiExportFormat.ODS:
            return 'application/vnd.oasis.opendocument.spreadsheet'

        if format == StiExportFormat.ODT:
            return 'application/vnd.oasis.opendocument.text'

        if format == StiExportFormat.POWERPOINT:
            return 'application/vnd.ms-powerpoint'

        if format == StiExportFormat.DOCUMENT:
            return 'text/xml'

        return 'text/plain'

    def getFormatName(format: int) -> str:
        """Returns the name of the export format suitable for use in JavaScript code."""

        formatName = StiExportFormat.__getFormatName(format).lower().capitalize()
        return formatName.replace('_svg', 'Svg').replace('point', 'Point')