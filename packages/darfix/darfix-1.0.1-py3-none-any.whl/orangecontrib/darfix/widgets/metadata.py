__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "08/04/2020"

from typing import Optional

from Orange.widgets.widget import OWWidget, Input

from darfix.gui.metadataWidget import MetadataWidget
from darfix.core.process import MetadataTask
from darfix import dtypes


class MetadataWidgetOW(OWWidget):
    """
    Widget to select the data to be used in the dataset.
    """

    name = "metadata"
    icon = "icons/metadata.svg"
    want_main_area = False
    ewokstaskclass = MetadataTask

    # Inputs
    class Inputs:
        dataset = Input("dataset", dtypes.OWSendDataset)

    def __init__(self):
        super().__init__()

        self._widget = MetadataWidget()
        self.controlArea.layout().addWidget(self._widget)

    @Inputs.dataset
    def setDataset(self, _input: Optional[dtypes.OWSendDataset]):
        if _input:
            dataset, _ = _input
            if dataset:
                self._widget.setDataset(dataset)
            else:
                self._widget.clearTable()
