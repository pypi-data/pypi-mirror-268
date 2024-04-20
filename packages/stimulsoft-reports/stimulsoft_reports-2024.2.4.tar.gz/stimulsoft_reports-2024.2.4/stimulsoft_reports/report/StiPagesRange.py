from ..classes.StiComponent import StiComponent
from .enums.StiRangeType import StiRangeType


class StiPagesRange(StiComponent):
    
    rangeType = StiRangeType.ALL
    pageRanges = ''
    currentPage = 0

    def getHtml(self) -> str:
        """Get the HTML representation of the component."""
    
        result = f'let {self.id} = new Stimulsoft.Report.StiPagesRange();\n'
        if self.rangeType != StiRangeType.ALL:
            result += f'{self.id}.rangeType = {self.rangeType};\n'

            if len(self.pageRanges or '') > 0:
                result += f"{self.id}.pageRanges = '{self.pageRanges}';\n"

            if self.currentPage > 0:
                result += f'{self.id}.currentPage = {self.currentPage};\n'

        self._htmlRendered = True
        return result

    def __init__(self, rangeType: str = StiRangeType.ALL, pageRanges: str = '', currentPage: int = 0) -> None:
        self.id = 'pagesRange'
        self.rangeType = rangeType
        self.pageRanges = pageRanges
        self.currentPage = currentPage