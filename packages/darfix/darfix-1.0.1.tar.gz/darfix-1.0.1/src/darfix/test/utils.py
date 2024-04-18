__authors__ = ["H.Payno", "J.Garriga"]
__license__ = "MIT"
__date__ = "14/10/2019"

import os
import h5py
import tempfile

import fabio
import numpy
import string

from silx.resources import ExternalResources
from silx.io.dictdump import dicttoh5
from silx.io.url import DataUrl

from darfix.core.dataset import Dataset


utilstest = ExternalResources(
    project="darfix",
    url_base="http://www.edna-site.org/pub/darfix/testimages",
    env_key="DATA_KEY",
    timeout=60,
)


def random_generator(size=4, chars=string.printable):
    """
    Returns a string with random characters.
    """
    return "".join(chars[numpy.random.choice(len(chars))] for x in range(size))


def createRandomEDFDataset(
    dims, nb_data_files=20, header=False, _dir=None, in_memory=True, num_dims=3
):
    """Simple creation of a dataset in _dir with the requested number of data
    files and dark files.

    :param tuple of int dims: dimensions of the files.
    :param int nb_data_files: Number of data files to create.
    :param bool header: If True, a random header is created for every frame.
    :param str or None _dir: Directory to save the temporary files.

    :return :class:`Dataset`: generated instance of :class:`Dataset`
    """
    if not isinstance(dims, tuple) and len(dims) == 2:
        raise TypeError("dims should be a tuple of two elements")
    if not isinstance(nb_data_files, int):
        raise TypeError(
            f"nb_data_files ({nb_data_files}) should be an int. Get {type(nb_data_files)} instead"
        )
    if not isinstance(_dir, (type(None), str)):
        raise TypeError(f"_dir shuld be none or a string. Get {type(_dir)} instead")

    if _dir is None:
        _dir = tempfile.mkdtemp()

    if os.path.isdir(_dir) is False:
        raise ValueError("%s is not a directory" % _dir)

    if header:
        counter_mne = "a b c d e f g h"
        motor_mne = "obpitch y z mainx ffz m obx"
        # Create headers
        header = []
        # Dimensions for reshaping
        a = sorted(numpy.random.rand(2))
        b = [numpy.random.rand()] * numpy.array([1, 1.2, 1.4, 1.6, 1.8])
        c = sorted(numpy.random.rand(2))
        motors = numpy.random.rand(7)
        for i in numpy.arange(nb_data_files):
            header.append({})
            header[i]["HeaderID"] = i
            header[i]["counter_mne"] = counter_mne
            header[i]["motor_mne"] = motor_mne
            header[i]["counter_pos"] = ""
            header[i]["motor_pos"] = ""
            for count in counter_mne:
                header[i]["counter_pos"] += str(numpy.random.rand(1)[0]) + " "
            for j, m in enumerate(motor_mne.split()):
                if m == "m":
                    header[i]["motor_pos"] += str(b[i % 5]) + " "
                elif m == "z" and num_dims > 1:
                    header[i]["motor_pos"] += (
                        str(a[int((i > 4 and i < 10) or i > 14)]) + " "
                    )
                elif m == "obpitch" and num_dims == 3:
                    header[i]["motor_pos"] += str(c[int(i > 9)]) + " "
                else:
                    header[i]["motor_pos"] += str(motors[j]) + " "

            data_file = os.path.join(_dir, "data_file%04i.edf" % i)
            image = fabio.edfimage.EdfImage(
                data=numpy.random.random(dims), header=header[i]
            )
            image.write(data_file)
    else:
        for index in range(nb_data_files):
            data_file = os.path.join(_dir, "data_file%04i.edf" % index)
            image = fabio.edfimage.EdfImage(data=numpy.random.random(dims))
            image.write(data_file)

    dataset = Dataset(_dir=_dir, in_memory=in_memory)
    return dataset


def createRandomHDF5Dataset(
    dims,
    nb_data_frames=20,
    output_file=None,
    in_memory=True,
    num_dims=3,
    metadata=False,
):
    """Simple creation of a dataset in output_file with the requested number of data
    files and dark files.

    :param tuple of int dims: dimensions of the files.
    :param int nb_data_frames: Number of data files to create.
    :param str or None output_file: output HDF5 file
    :param in_memory: if True load the Dataset in memory
    :param int num_dims: number of dimensions of the dataset

    :return :class:`Dataset`: generated instance of :class:`Dataset`
    """
    if not isinstance(dims, tuple) and len(dims) == 2:
        raise TypeError("dims should be a tuple of two elements")
    if not isinstance(nb_data_frames, int):
        raise TypeError(
            f"nb_data_frames ({nb_data_frames}) should be an int. Get {type(nb_data_frames)} instead"
        )
    if not isinstance(output_file, (type(None), str)):
        raise TypeError(
            f"output_file shuld be none or a string. Get {type(output_file)} instead"
        )

    if output_file is None:
        output_file = os.path.join(str(tempfile.mkdtemp()), "darfix_dataset.hdf5")

    metadata_dict = {}
    if metadata:
        metadata_dict["obx"] = [numpy.random.rand(1)[0]] * nb_data_frames
        metadata_dict["mainx"] = [numpy.random.rand(1)[0]] * nb_data_frames
        metadata_dict["ffz"] = [numpy.random.rand(1)[0]] * nb_data_frames
        metadata_dict["y"] = [numpy.random.rand(1)[0]] * nb_data_frames

        # comes from createRandomEDFDataset. Don't know why those
        # values are making sense...
        a = sorted(numpy.random.rand(2))
        b = [numpy.random.rand()] * numpy.array([1, 1.2, 1.4, 1.6, 1.8])
        c = sorted(numpy.random.rand(2))
        metadata_dict["m"] = [b[i % 5] for i in range(nb_data_frames)]
        if num_dims > 1:
            metadata_dict["z"] = [
                a[int((i > 4 and i < 10) or i > 14)] for i in range(nb_data_frames)
            ]
        metadata_dict["obpitch"] = [c[int(i > 9)] for i in range(nb_data_frames)]

    data = numpy.random.random((nb_data_frames, *dims))
    dicttoh5(metadata_dict, output_file, h5path="1.1/instrument/positioners")
    with h5py.File(output_file, mode="a") as h5f:
        h5f["1.1/instrument/detector/data"] = data
    assert os.path.exists(output_file)

    dataset = Dataset(
        _dir=os.path.dirname(output_file),
        first_filename=DataUrl(
            file_path=output_file,
            data_path="1.1/instrument/detector/data",
            scheme="silx",
        ),
        in_memory=in_memory,
        isH5=True,
        metadata_url=DataUrl(
            file_path=output_file,
            data_path="1.1/instrument/positioners",
            scheme="silx",
        ),
    )
    return dataset


def createDataset(
    data, filter_data=False, header=None, _dir=None, in_memory=True, backend="hdf5"
):
    """
    Create a dataset from a configuration

    :param numpy.ndarray data: Images to form the data.
    :param numpy.ndarray dark_frames: Images to form the dark frames.
    :param bool filter_data: If True, the dataset created will divide the data
        between the ones with no intensity (or very low) and the others.
    :param Union[None,array_like] header: List with a header per frame. If None,
        no header is added.
    :param str or None _dir: Directory to save the temporary files.
    :param str backend: can be 'edf' or 'hdf5' according to the data format we want to save the dataset to

    :return :class:`Dataset`: generated instance of :class:`Dataset`.
    """
    assert type(_dir) in (type(None), str)
    assert len(data) > 0
    if header is not None:
        assert len(header) == len(data)

    if _dir is None:
        _dir = tempfile.mkdtemp()

    if backend == "hdf5":
        # handle HDF5 backend
        file_path = os.path.join(_dir, "darfix_dataset.hdf5")
        if header:
            # TODO: we might need to convert existing headers to a dict
            raise NotImplementedError
        else:
            metadata_url = None

        with h5py.File(file_path, mode="a") as h5f:
            h5f["1.1/instrument/detector/data"] = data

        dataset = Dataset(
            _dir=os.path.dirname(file_path),
            first_filename=DataUrl(
                file_path=file_path,
                data_path="1.1/instrument/detector/data",
                scheme="silx",
            ),
            in_memory=in_memory,
            isH5=True,
            metadata_url=metadata_url,
        )
    else:
        # handle EDF backend
        if os.path.isdir(_dir) is False:
            raise ValueError("%s is not a directory" % _dir)
        for index in range(len(data)):
            data_file = os.path.join(_dir, "data_file%04i.edf" % index)
            if header is not None:
                image = fabio.edfimage.EdfImage(data=data[index], header=header[index])
            else:
                image = fabio.edfimage.EdfImage(data=data[index])

            image.write(data_file)

        dataset = Dataset(_dir=_dir, in_memory=in_memory)

    return dataset
