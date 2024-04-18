__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "09/12/2021"

from typing import Optional

from Orange.widgets.widget import OWWidget, Input, Output
from Orange.widgets.settings import Setting

from darfix.gui.binningWidget import BinningWidget
from darfix import dtypes


class BinningWidgetOW(OWWidget):
    """
    Widget that computes the background substraction from a dataset
    """

    name = "binning"
    icon = "icons/resize.png"
    want_main_area = False
    # ewokstaskclass = Binning

    # Inputs
    class Inputs:
        dataset = Input("dataset", dtypes.OWSendDataset)

    # Outputs
    class Outputs:
        dataset = Output("dataset", dtypes.OWSendDataset)

    scale = Setting(float(), schema_only=True)

    def __init__(self):
        super().__init__()

        self._widget = BinningWidget(parent=self)
        self._widget.sigComputed.connect(self._sendSignal)
        self.controlArea.layout().addWidget(self._widget)

    @Inputs.dataset
    def setDataset(self, _input: Optional[dtypes.OWSendDataset]):
        if _input is not None:
            dataset, update = _input
            self._widget.setDataset(dataset)

            if update is None:
                self.open()
            elif update != self:
                owdataset = self._widget.getDataset(self)
                senddataset = dtypes.OWSendDataset(owdataset, update)
                self.Outputs.dataset.send(senddataset)

            if self.scale:
                self._widget.scale = self.scale

    def _updateDataset(self, widget, dataset):
        self._widget._updateDataset(widget, dataset)

    def _sendSignal(self):
        """
        Function to emit the new dataset.
        """
        self.scale = self._widget.scale
        owdataset = self._widget.getDataset(self)
        senddataset = dtypes.OWSendDataset(owdataset)
        self.Outputs.dataset.send(senddataset)
        self.close()
