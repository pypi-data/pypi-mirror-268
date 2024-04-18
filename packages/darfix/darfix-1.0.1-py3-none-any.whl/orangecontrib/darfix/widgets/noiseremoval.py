__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "11/12/2020"

from typing import Optional

import numpy

from Orange.widgets.settings import Setting
from Orange.widgets.widget import OWWidget, Input, Output
from silx.gui.colors import Colormap

from darfix.gui.noiseRemovalWidget import NoiseRemovalDialog
from darfix.core.process import NoiseRemoval
from darfix import dtypes


class NoiseRemovalWidgetOW(OWWidget):
    """
    Widget that computes the background substraction from a dataset
    """

    name = "noise removal"
    icon = "icons/noise_removal.png"
    want_main_area = False
    ewokstaskclass = NoiseRemoval

    # Inputs
    class Inputs:
        dataset = Input("dataset", dtypes.OWSendDataset)
        colormap = Input("colormap", Colormap)

    # Outputs
    class Outputs:
        dataset = Output("dataset", dtypes.OWSendDataset)
        colormap = Output("colormap", Colormap)

    # Settings
    method = Setting(str())
    background_type = Setting(str())
    kernel_size = Setting(str())
    bottom_threshold = Setting(str())
    top_threshold = Setting(str())
    chunks = Setting(list())
    step = Setting(str())
    mask = Setting(list())

    def __init__(self):
        super().__init__()

        self._widget = NoiseRemovalDialog(parent=self)
        self.controlArea.layout().addWidget(self._widget)
        self._widget.okSignal.connect(self._sendSignal)

    @Inputs.dataset
    def setDataset(self, _input: Optional[dtypes.OWSendDataset]):
        if _input is not None:
            dataset, update = _input
            self._widget.setDataset(dataset)
            if self.method:
                self._widget.mainWindow.method = self.method
            if self.background_type:
                self._widget.mainWindow.background = self.background_type
            if self.kernel_size:
                self._widget.mainWindow.size = self.kernel_size
            if self.bottom_threshold:
                self._widget.mainWindow.bottom_threshold = self.bottom_threshold
            if self.top_threshold:
                self._widget.mainWindow.top_threshold = self.top_threshold
            if self.step:
                self._widget.mainWindow.step = self.step
            if self.chunks:
                self._widget.mainWindow.chunks = self.chunks
            if self.mask:
                self._widget.mainWindow.mask = self.mask

            if update is None:
                self.show()
            elif update != self:
                owdataset = self._widget.getDataset(self)
                senddataset = dtypes.OWSendDataset(owdataset, update)
                self.Outputs.dataset.send(senddataset)

    @Inputs.colormap
    def setColormap(self, colormap):
        self._widget.mainWindow.setStackViewColormap(colormap)

    def _updateDataset(self, widget, dataset):
        self._widget.mainWindow._updateDataset(widget, dataset)

    def _sendSignal(self):
        """
        Function to emit the new dataset.
        """
        self.information()
        self.method = self._widget.mainWindow.method
        self.background_type = self._widget.mainWindow.background
        self.kernel_size = self._widget.mainWindow.size
        self.step = self._widget.mainWindow.step
        self.chunks = self._widget.mainWindow.chunks
        self.bottom_threshold = self._widget.mainWindow.bottom_threshold
        self.top_threshold = self._widget.mainWindow.top_threshold
        if isinstance(self._widget.mainWindow.mask, numpy.ndarray):
            self.mask = self._widget.mainWindow.mask.tolist()
        else:
            self.mask = self._widget.mainWindow.mask
        owdataset = self._widget.getDataset(self)
        senddataset = dtypes.OWSendDataset(owdataset)
        self.Outputs.dataset.send(senddataset)
        self.Outputs.colormap.send(self._widget.mainWindow.getStackViewColormap())
        self.close()
