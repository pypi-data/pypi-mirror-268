from ...classes.StiComponentOptions import StiComponentOptions


class StiBandsOptions(StiComponentOptions):
    """A class which controls settings of the bands."""

### Properties

    @property
    def id(self) -> str:
        return super().id + '.bands'


### Options

    showReportTitleBand: bool = True
    """Gets or sets a visibility of the ReportTitleBand item in the bands menu of the designer."""

    showReportSummaryBand: bool = True
    """Gets or sets a visibility of the ReportSummaryBand item in the bands menu of the designer."""

    showPageHeaderBand: bool = True
    """Gets or sets a visibility of the PageHeaderBand item in the bands menu of the designer."""

    showPageFooterBand: bool = True
    """Gets or sets a visibility of the PageFooterBand item in the bands menu of the designer."""

    showGroupHeaderBand: bool = True
    """Gets or sets a visibility of the GroupHeaderBand item in the bands menu of the designer."""

    showGroupFooterBand: bool = True
    """Gets or sets a visibility of the GroupFooterBand item in the bands menu of the designer."""

    showHeaderBand: bool = True
    """Gets or sets a visibility of the HeaderBand item in the bands menu of the designer."""

    showFooterBand: bool = True
    """Gets or sets a visibility of the FooterBand item in the bands menu of the designer."""

    showColumnHeaderBand: bool = True
    """Gets or sets a visibility of the ColumnHeaderBand item in the bands menu of the designer."""

    showColumnFooterBand: bool = True
    """Gets or sets a visibility of the ColumnFooterBand item in the bands menu of the designer."""

    showDataBand: bool = True
    """Gets or sets a visibility of the DataBand item in the bands menu of the designer."""

    showHierarchicalBand: bool = True
    """Gets or sets a visibility of the HierarchicalBand item in the bands menu of the designer."""

    showChildBand: bool = True
    """Gets or sets a visibility of the ChildBand item in the bands menu of the designer."""

    showEmptyBand: bool = True
    """Gets or sets a visibility of the EmptyBand item in the bands menu of the designer."""

    showOverlayBand: bool = True
    """Gets or sets a visibility of the OverlayBand item in the bands menu of the designer."""

    showTable: bool = True
    """Gets or sets a visibility of the Table item in the bands menu of the designer."""

    showTableOfContents: bool = True
    """Gets or sets a visibility of the TableOfContents item in the Bands menu of the designer."""