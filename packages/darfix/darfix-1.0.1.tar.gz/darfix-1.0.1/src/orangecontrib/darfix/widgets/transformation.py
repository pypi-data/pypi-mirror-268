__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "10/08/2021"

from typing import Optional

from silx.gui import qt
from Orange.widgets.settings import Setting
from Orange.widgets.widget import OWWidget, Input, Output

from darfix.gui.magnificationWidget import MagnificationWidget
from darfix.gui.rsmWidget import RSMWidget
from darfix.core.process import Transformation
from darfix import dtypes


class TransformationWidgetOW(OWWidget):
    """
    Widget that computes the background substraction from a dataset
    """

    name = "transformation"
    icon = "icons/axes.png"
    want_main_area = False
    ewokstaskclass = Transformation

    # Inputs
    class Inputs:
        dataset = Input("dataset", dtypes.OWSendDataset)

    # Outputs
    class Outputs:
        dataset = Output("dataset", dtypes.OWSendDataset)

    magnification = Setting(float(), schema_only=True)
    pixelSize = Setting(str(), schema_only=True)
    kind = Setting(bool(), schema_only=True)
    rotate = Setting(bool(), schema_only=True)
    orientation = Setting(int(), schema_only=True)

    def __init__(self):
        super().__init__()
        qt.QLocale.setDefault(qt.QLocale("en_US"))
        self._widget = None
        self._methodCB = qt.QComboBox(self)
        self.controlArea.layout().addWidget(self._methodCB)
        self._methodCB.currentTextChanged.connect(self._changeTransformationWidget)

    @Inputs.dataset
    def setDataset(self, _input: Optional[dtypes.OWSendDataset]):
        if _input is not None:
            dataset, update = _input

            ndim = dataset[1].dims.ndim
            if ndim == 0:
                msg = qt.QMessageBox()
                msg.setIcon(qt.QMessageBox.Warning)
                msg.setText(
                    "This widget has to be used before selecting any region of \
                                interest and after selecting the dimensions"
                )
                msg.exec_()
                return

            self._dataset = dataset
            self._changeDimensions(ndim)
            self._widget.setDataset(self._dataset)

            if update is None:
                self.open()
            elif update != self._widget:
                owdataset = self._widget.getDataset(self)
                senddataset = dtypes.OWSendDataset(owdataset, update)
                self.Outputs.dataset.send(senddataset)

    def _updateDataset(self, widget, dataset):
        self._widget._updateDataset(widget, dataset)
        if widget != self:
            owdataset = self._widget.getDataset(self)
            senddataset = dtypes.OWSendDataset(owdataset, widget)
            self.Outputs.dataset.send(senddataset)

    def _changeDimensions(self, ndim: int) -> None:
        """The possible transformations depend on the number of dimensions (one or two)."""
        if ndim == 1:
            transformations = ["Magnification", "RSM"]
        elif ndim == 2:
            transformations = ["Magnification"]
        else:
            raise ValueError(ndim)
        current_items = [
            self._methodCB.itemText(i) for i in range(self._methodCB.count())
        ]
        if transformations == current_items:
            return

        self._methodCB.currentTextChanged.disconnect(self._changeTransformationWidget)
        try:
            method = self._methodCB.currentText()
            self._methodCB.clear()
            self._methodCB.addItems(transformations)
            try:
                idx = transformations.index(method)
            except ValueError:
                idx = 0
            self._methodCB.setCurrentIndex(idx)

            method = transformations[idx]
            self._changeTransformationWidget(method, force=True)
        finally:
            self._methodCB.currentTextChanged.connect(self._changeTransformationWidget)

    def _changeTransformationWidget(self, method: str, force: bool = False) -> None:
        """
        Change the widget displayed on the window
        """
        if not force and method == self._currentMethod():
            return
        if self._widget:
            self.controlArea.layout().removeWidget(self._widget)
            self._widget.hide()
        if method == "RSM":
            self._widget = RSMWidget(parent=self)
            if self.pixelSize:
                self._widget.pixelSize = self.pixelSize
                self._widget.rotate = self.rotate
        elif method == "Magnification":
            self._widget = MagnificationWidget(parent=self)
            if self.magnification:
                self._widget.magnification = self.magnification
                self._widget.orientation = self.orientation
        else:
            return
        self._widget.sigComputed.connect(self._sendSignal)
        self.controlArea.layout().addWidget(self._widget)
        self._widget.show()

    def _sendSignal(self) -> None:
        """
        Emits the signal with the new dataset.
        """
        method = self._methodCB.currentText()
        if method == "Magnification":
            self.magnification = self._widget.magnification
            self.kind = False
            self.orientation = self._widget.orientation
        elif method == "RSM":
            self.pixelSize = self._widget.pixelSize
            self.rotate = self._widget.rotate
            self.kind = True
        self.close()
        owdataset = self._widget.getDataset(self)
        senddataset = dtypes.OWSendDataset(owdataset)
        self.Outputs.dataset.send(senddataset)

    def _currentMethod(self) -> Optional[str]:
        if isinstance(self._widget, MagnificationWidget):
            return "Magnification"
        if isinstance(self._widget, RSMWidget):
            return "RSM"
        return None
