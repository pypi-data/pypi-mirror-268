__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "09/12/2021"

from typing import Optional

from Orange.widgets.widget import OWWidget, Input, Output
from Orange.widgets.settings import Setting

from darfix.gui.weakBeamWidget import WeakBeamWidget
from darfix.core.process import WeakBeam
from darfix import dtypes


class WeakBeamWidgetOW(OWWidget):
    """
    Widget that computes the background substraction from a dataset
    """

    name = "weak beam"
    icon = "icons/gaussian.png"
    want_main_area = False
    ewokstaskclass = WeakBeam

    # Inputs
    class Inputs:
        dataset = Input("dataset", tuple)

    # Outputs
    class Outputs:
        dataset = Output("dataset", tuple)

    nvalue = Setting(float(), schema_only=True)

    def __init__(self):
        super().__init__()

        self._widget = WeakBeamWidget(parent=self)
        self._widget.sigComputed.connect(self._sendSignal)
        self.controlArea.layout().addWidget(self._widget)

    @Inputs.dataset
    def setDataset(self, _input: Optional[dtypes.OWSendDataset]):
        if _input is not None:
            dataset, update = _input
            self._widget.setDataset(dataset)
            if self.nvalue:
                self._widget.nvalue = self.nvalue
            if update is None:
                self.open()
            elif update != self:
                owdataset = self._widget.getDataset(self)
                senddataset = dtypes.OWSendDataset(owdataset, update)
                self.Outputs.dataset.send(senddataset)

    def _updateDataset(self, widget, dataset):
        self._widget._updateDataset(widget, dataset)

    def _sendSignal(self):
        """
        Function to emit the new dataset.
        """
        self.nvalue = self._widget.nvalue
        owdataset = self._widget.getDataset(self)
        senddataset = dtypes.OWSendDataset(owdataset)
        self.Outputs.dataset.send(senddataset)
        self.close()
