from __future__ import annotations

from stimulsoft_data_adapters.classes.StiBaseResult import StiBaseResult


class StiResult(StiBaseResult):
    """
    The result of executing an event handler request. 
    The result contains a collection of data, message about the result of the command execution, and other technical information.
    """

### Abstract

    fileName: str
    variables: list
    settings: dict
    report: object

    
### Public

    def getSuccess(notice: str = None) -> StiResult:
        """Creates a successful result."""
        
        result: StiResult = StiBaseResult.getSuccess(notice)
        result.__class__ = StiResult
        return result
    
    def getError(notice: str) -> StiResult:
        """Creates an error result."""

        result: StiResult = StiBaseResult.getError(notice)
        result.__class__ = StiResult
        return result