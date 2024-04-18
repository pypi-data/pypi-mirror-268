__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "12/08/2019"


import copy
from typing import Optional

from Orange.widgets.widget import OWWidget, Input, Output

from darfix.core.process import DataCopy
from darfix import dtypes


class DataCopyWidgetOW(OWWidget):
    """
    Widget that creates a new dataset from a given one, and copies its data.
    """

    name = "data copy"
    icon = "icons/copy.svg"
    want_main_area = False
    ewokstaskclass = DataCopy

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
            dataset, update = _input
            if not update:
                self.cp_dataset = copy.deepcopy(dataset[1:])
                owdataset = dtypes.OWDataset(self, *self.cp_dataset)
                senddataset = dtypes.OWSendDataset(owdataset)
                self.Outputs.dataset.send(senddataset)

    def _updateDataset(self, widget, dataset):
        owdataset = dtypes.OWDataset(self, dataset, *self.cp_dataset[1:])
        senddataset = dtypes.OWSendDataset(owdataset, widget)
        self.Outputs.dataset.send(senddataset)

    def setVisible(self, visible):
        pass
