import os
import h5py
import numpy
from silx.io.url import DataUrl
from darfix.core.data_selection import load_process_data


def test_load_process_data_hdf5(tmp_path):
    """test load_process_data function with HDF5 dataset"""
    raw_data_dir = tmp_path / "raw_data"
    raw_data_dir.mkdir()

    raw_data_file = os.path.join(raw_data_dir, "raw.hdf5")
    with h5py.File(raw_data_file, mode="w") as h5f:
        h5f["/path/to/data"] = numpy.arange(0, 100 * 100 * 20).reshape(20, 100, 100)

    raw_dark_file = os.path.join(raw_data_dir, "dark.hdf5")
    with h5py.File(raw_dark_file, mode="w") as h5f:
        h5f["/path/to/dark"] = numpy.arange(100 * 100).reshape(1, 100, 100)

    load_process_data(
        filenames=DataUrl(
            file_path=raw_data_file,
            data_path="/path/to/data",
            scheme="silx",
        ).path(),
        root_dir=raw_data_dir,
        in_memory=True,
        dark_filename=DataUrl(
            file_path=raw_dark_file,
            data_path="/path/to/dark",
            scheme="silx",
        ),
        copy_files=False,
        isH5=True,
    )
