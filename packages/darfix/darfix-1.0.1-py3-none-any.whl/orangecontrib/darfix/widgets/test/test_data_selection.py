import os
import h5py
import numpy

from silx.io.url import DataUrl
from ewoksorange.tests.conftest import qtapp  # noqa F401
from orangecontrib.darfix.widgets.dataselection import DataSelectionWidgetOW


def test_DataSelectionWidgetOW(
    tmp_path,
    qtapp,  # noqa F811
):
    raw_data_dir = tmp_path / "raw_data"
    raw_data_dir.mkdir()

    raw_data_file = os.path.join(raw_data_dir, "raw.hdf5")
    with h5py.File(raw_data_file, mode="w") as h5f:
        h5f["/path/to/data"] = numpy.arange(0, 100 * 100 * 20).reshape(20, 100, 100)
    raw_data_url = DataUrl(
        file_path=raw_data_file,
        data_path="/path/to/data",
    )

    raw_dark_file = os.path.join(raw_data_dir, "dark.hdf5")
    with h5py.File(raw_dark_file, mode="w") as h5f:
        h5f["/path/to/dark"] = numpy.arange(100 * 100).reshape(1, 100, 100)
    dark_data_url = DataUrl(
        file_path=raw_dark_file,
        data_path="/path/to/dark",
    )

    widget = DataSelectionWidgetOW()
    widget._widget._ish5CB.setChecked(True)

    qtapp.processEvents()
    widget._widget._rawFilenameData.setFilename(raw_data_url.path())
    widget._widget._darkFilenameData.setFilename(dark_data_url.path())

    widget._getDataset()
    widget._thread.wait()
    assert widget._thread.data is not None
