__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "12/08/2019"

from typing import Optional

from Orange.widgets.widget import OWWidget, Input, Output

from darfix.core.process import FlashTask
from darfix import dtypes


class FlashWidgetOW(OWWidget):
    """
    Widget that creates a new dataset from a given one, and copies its data.
    """

    name = "flash"
    icon = "icons/flash.svg"
    want_main_area = False
    ewokstaskclass = FlashTask

    # Inputs
    class Inputs:
        dataset = Input("dataset", dtypes.OWSendDataset)

    # Outputs
    class Outputs:
        dataset = Output("dataset", dtypes.OWSendDataset)

    def __init__(self):
        super().__init__()

    @Inputs.dataset
    def setDataset(self, _input: Optional[dtypes.OWSendDataset]):
        if _input is not None:
            # Copy and send new dataset
            self.dataset, update = _input
            self.dataset[0]._updateDataset(self.dataset[0], self.dataset[1])
            owdataset = dtypes.OWDataset(self, *self.dataset[1:])
            senddataset = dtypes.OWSendDataset(owdataset)
            self.Outputs.dataset.send(senddataset)

    def _updateDataset(self, widget, dataset):
        owdataset = dtypes.OWDataset(self, dataset, *self.dataset[1:])
        senddataset = dtypes.OWSendDataset(owdataset, widget)
        self.Outputs.dataset.send(senddataset)

    def setVisible(self, visible):
        pass
