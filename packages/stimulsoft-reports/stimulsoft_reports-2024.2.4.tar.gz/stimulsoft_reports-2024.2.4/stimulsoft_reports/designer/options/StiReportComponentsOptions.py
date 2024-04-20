from ...classes.StiComponentOptions import StiComponentOptions


class StiReportComponentsOptions(StiComponentOptions):
    """A class which controls settings of the components."""

### Properties

    @property
    def id(self) -> str:
        return super().id + '.components'


### Options

    showText: bool = True
    """Gets or sets a visibility of the Text item in the components menu of the designer."""

    showTextInCells: bool = True
    """Gets or sets a visibility of the TextInCells item in the components menu of the designer."""

    showRichText: bool = False
    """Gets or sets a visibility of the RichText item in the components menu of the designer."""

    showImage: bool = True
    """Gets or sets a visibility of the Image item in the components menu of the designer."""

    showBarCode: bool = True
    """Gets or sets a visibility of the BarCode item in the components menu of the designer."""

    showShape: bool = True
    """Gets or sets a visibility of the Shape item in the components menu of the designer."""

    showPanel: bool = True
    """Gets or sets a visibility of the Panel item in the components menu of the designer."""

    showClone: bool = True
    """Gets or sets a visibility of the Clone item in the components menu of the designer."""

    showCheckBox: bool = True
    """Gets or sets a visibility of the CheckBox item in the components menu of the designer."""

    showSubReport: bool = True
    """Gets or sets a visibility of the SubReport item in the components menu of the designer."""

    showZipCode: bool = False
    """Gets or sets a visibility of the ZipCode item in the components menu of the designer."""

    showChart: bool = True
    """Gets or sets a visibility of the Chart item in the components menu of the designer."""

    showGauge: bool = True
    """Gets or sets a visibility of the Gauge item in the components menu of the designer."""

    showSparkline: bool = True
    """Gets or sets a visibility of the Sparkline item in the components menu of the designer."""

    showMathFormula: bool = False
    """Gets or sets a visibility of the MathFormula item in the Components menu of the designer."""

    showMap: bool = True
    """Gets or sets a visibility of the Map item in the Components menu of the designer."""