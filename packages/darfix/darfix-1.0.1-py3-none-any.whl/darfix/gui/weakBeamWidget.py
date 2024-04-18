__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "09/03/2023"

import numpy

from silx.gui import qt
from silx.gui.colors import Colormap
from silx.gui.plot import Plot2D

import darfix
from darfix import dtypes
from darfix.gui.utils import missing_dataset_msg

from .operationThread import OperationThread


class WeakBeamWidget(qt.QMainWindow):
    """
    Widget to recover weak beam to obtain dislocations.
    """

    sigComputed = qt.Signal()

    def __init__(self, parent=None):
        qt.QMainWindow.__init__(self, parent)

        self._nvalue = 1
        self._dataset = None
        self.indices = None
        self.bg_indices = None
        self.bg_dataset = None

        widget = qt.QWidget()
        layout = qt.QGridLayout()

        self._nLE = qt.QLineEdit("1")
        validator = qt.QDoubleValidator()
        self._nLE.setValidator(validator)
        _buttons = qt.QDialogButtonBox(parent=self)
        self._okB = _buttons.addButton(_buttons.Ok)
        self._applyB = _buttons.addButton(_buttons.Apply)

        self._applyB.clicked.connect(self._applyThresholding)
        self._okB.clicked.connect(self.apply)

        self._plot = Plot2D()
        self._plot.setDefaultColormap(
            Colormap(
                name=darfix.config.DEFAULT_COLORMAP_NAME,
                normalization=darfix.config.DEFAULT_COLORMAP_NORM,
            )
        )
        layout.addWidget(
            qt.QLabel("Increase/decrease threshold std by a value of : "), 0, 0
        )
        layout.addWidget(self._nLE, 0, 1)
        layout.addWidget(self._plot, 1, 0, 1, 2)
        layout.addWidget(_buttons, 2, 0, 1, 2)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    @property
    def nvalue(self):
        return self._nvalue

    @nvalue.setter
    def nvalue(self, nvalue):
        self._nvalue = nvalue
        self._nLE.setText(str(nvalue))

    def setDataset(self, owdataset: dtypes.OWDataset) -> None:
        self.parent = owdataset.parent
        self._dataset = owdataset.dataset
        self.indices = owdataset.indices
        self.bg_indices = owdataset.bg_indices
        self.bg_dataset = owdataset.bg_dataset
        self._thread = OperationThread(self, self._dataset.recover_weak_beam)

    def getDataset(self, parent) -> dtypes.OWDataset:
        if self._dataset is None:
            missing_dataset_msg()
            return None
        return dtypes.OWDataset(
            parent, self._dataset, self.indices, self.bg_indices, self.bg_dataset
        )

    def _applyThresholding(self):
        if self._dataset is None:
            missing_dataset_msg()
            return
        self._applyB.setEnabled(False)
        self._okB.setEnabled(False)
        self._nvalue = float(self._nLE.text())
        self._thread.setArgs(self.nvalue, self.indices)
        self._thread.finished.connect(self._updateData)
        self._thread.start()

    def _updateData(self):
        self._thread.finished.disconnect(self._updateData)
        self._applyB.setEnabled(True)
        self._okB.setEnabled(True)
        if self._thread.data is not None:
            self._dataset = self._thread.data
            self._com = self._dataset.apply_moments(indices=self.indices)[0][0]
            if self._dataset.transformation is None:
                self._plot.addImage(self._com, xlabel="pixels", ylabel="pixels")
                return
            if self._dataset.transformation.rotate:
                self._com = numpy.rot90(self._com, 3)
            self._plot.addImage(
                self._com,
                origin=self._dataset.transformation.origin,
                scale=self._dataset.transformation.scale,
                xlabel=self._dataset.transformation.label,
                ylabel=self._dataset.transformation.label,
            )

    def apply(self):
        self.sigComputed.emit()
