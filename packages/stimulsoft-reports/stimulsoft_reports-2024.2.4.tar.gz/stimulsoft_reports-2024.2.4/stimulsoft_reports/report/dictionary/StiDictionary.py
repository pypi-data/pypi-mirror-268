from __future__ import annotations

import typing

from ...classes.StiComponent import StiComponent
from .StiVariable import StiVariable

if typing.TYPE_CHECKING:
    from ..StiReport import StiReport


class StiDictionary(StiComponent):

    report: StiReport = None
    variables: list[StiVariable] = None

    def getHtml(self):
        """Get the HTML representation of the component."""

        result: str = ''
        for variable in self.variables:
            result += variable.getHtml()
            result += f'{self.report.id}.dictionary.variables.add({variable.id});\n'

        return result

    def __init__(self, report: StiReport):
        self.report = report
        self.variables = []
