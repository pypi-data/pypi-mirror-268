from ...classes.StiComponentOptions import StiComponentOptions


class StiDashboardElementsOptions(StiComponentOptions):
    """A class which controls settings of the dashboardElements."""

### Properties

    @property
    def id(self) -> str:
        return super().id + '.dashboardElements'


### Options

    showTableElement: bool = True
    """Gets or sets a visibility of the TableElement item in the designer."""

    showCardsElement: bool = True
    """Gets or sets a visibility of the CardsElement item in the designer."""

    showChartElement: bool = True
    """Gets or sets a visibility of the ChartElement item in the designer."""

    showGaugeElement: bool = True
    """Gets or sets a visibility of the GaugeElement item in the designer."""

    howPivotTableElement: bool = True
    """Gets or sets a visibility of the PivotTableElement item in the designer."""

    showIndicatorElement: bool = True
    """Gets or sets a visibility of the IndicatorElement item in the designer."""

    showProgressElement: bool = True
    """Gets or sets a visibility of the ProgressElement item in the designer."""

    showRegionMapElement: bool = True
    """Gets or sets a visibility of the RegionMapElement item in the designer."""

    showOnlineMapElement: bool = True
    """Gets or sets a visibility of the OnlineMapElement item in the designer."""

    showImageElement: bool = True
    """Gets or sets a visibility of the ImageElement item in the designer."""

    showTextElement: bool = True
    """Gets or sets a visibility of the TextElement item in the designer."""

    showPanelElement: bool = True
    """Gets or sets a visibility of the PanelElement item in the designer."""

    showShapeElement: bool = True
    """Gets or sets a visibility of the ShapeElement item in the designer."""

    showButtonElement: bool = True
    """Gets or sets a visibility of the ButtonElement item in the designer."""

    showListBoxElement: bool = True
    """Gets or sets a visibility of the ListBoxElement item in the designer."""

    showComboBoxElement: bool = True
    """Gets or sets a visibility of the ComboBoxElement item in the designer."""

    showTreeViewElement: bool = True
    """Gets or sets a visibility of the TreeViewElement item in the designer."""

    showTreeViewBoxElement: bool = True
    """Gets or sets a visibility of the TreeViewBoxElement item in the designer."""

    showDatePickerElement: bool = True
    """Gets or sets a visibility of the DatePickerElement item in the designer."""