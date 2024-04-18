import os
import pytest
import uuid
from .utils import createRandomEDFDataset, createRandomHDF5Dataset


@pytest.fixture(scope="function")
def edf_dataset(tmp_path):
    output_dir = tmp_path / str(uuid.uuid1())
    output_dir.mkdir()
    yield createRandomEDFDataset(
        dims=(100, 100), nb_data_files=3, header=True, _dir=output_dir
    )


@pytest.fixture(scope="function")
def hdf5_dataset(tmp_path):
    output_file = os.path.join(tmp_path, str(uuid.uuid1()) + ".hdf5")
    yield createRandomHDF5Dataset(
        dims=(100, 100), nb_data_frames=3, metadata=True, output_file=output_file
    )


@pytest.fixture(scope="function")
def datasets(tmp_path):
    output_dir = tmp_path / str(uuid.uuid1())
    output_dir.mkdir()

    # create edf Dataset
    edf_folder = tmp_path / "edf_dataset"
    edf_folder.mkdir()
    yield createRandomEDFDataset(
        dims=(100, 100), nb_data_files=3, header=True, _dir=str(edf_folder)
    )

    # create HDF5 Dataset
    output_file = os.path.join(tmp_path, str(uuid.uuid1()) + ".hdf5")
    yield createRandomHDF5Dataset(
        dims=(100, 100), nb_data_frames=3, metadata=True, output_file=output_file
    )
