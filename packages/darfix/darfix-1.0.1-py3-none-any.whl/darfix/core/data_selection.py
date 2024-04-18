import os
import urllib.parse
import urllib.request
from typing import Iterable, Optional, Union
from darfix.core.dataset import Dataset
from silx.io.url import DataUrl


def load_process_data(
    filenames: Union[str, Iterable[str], DataUrl],
    root_dir: Optional[str] = None,
    in_memory: bool = True,
    dark_filename: Optional[Union[str, DataUrl]] = None,
    copy_files: bool = True,
    isH5: bool = False,
    title: str = "",
    metadata_url=None,
):
    """
    When `filenames` is a string, it will be treated as a file pattern.

    :param filenames: filenames to be loaded. If filenames is a str then consider it as a file pattern (for EDF files). If is an iterable consider a list of EDF files. If this is a DataUrl expected it readable by silx get_data function
    :param metadata_url: path to the scan metadata for HDF5 containing positioner information in order to load metadata for non-edf files
    """
    indices = li_indices = None
    root_dir_specified = bool(root_dir)

    if isinstance(filenames, DataUrl):
        assert filenames.file_path() not in (
            "",
            None,
        ), "no file_path provided to the DataUrl"
        if not root_dir_specified:
            root_dir = os.path.dirname(filenames.file_path())
        dataset = Dataset(
            _dir=root_dir,
            first_filename=filenames,
            in_memory=in_memory,
            copy_files=copy_files,
            isH5=isH5,
            title=title,
            metadata_url=metadata_url,
        )
    elif isinstance(filenames, str):
        if not root_dir_specified:
            root_dir = _get_root_dir(filenames)
        dataset = Dataset(
            _dir=root_dir,
            first_filename=filenames,
            in_memory=in_memory,
            copy_files=copy_files,
            isH5=isH5,
            title=title,
            metadata_url=metadata_url,
        )
    elif isinstance(filenames, Iterable):
        filenames = list(filenames)
        if not root_dir_specified:
            root_dir = _get_root_dir(filenames[0])
        dataset = Dataset(
            _dir=root_dir,
            filenames=filenames,
            in_memory=in_memory,
            copy_files=copy_files,
            isH5=isH5,
            title=title,
            metadata_url=metadata_url,
        )
    else:
        raise TypeError(f"filenames of type {type(filenames)} is not handle")

    if isinstance(dark_filename, str):
        dark_root_dir = os.path.join(dataset.dir, "dark")
        os.makedirs(dark_root_dir, exist_ok=True)
        bg_dataset = Dataset(
            _dir=dark_root_dir,
            first_filename=dark_filename,
            copy_files=False,
            isH5=isH5,
            metadata_url=None,
        )
    elif isinstance(dark_filename, DataUrl):
        assert dark_filename.file_path() not in (
            "",
            None,
        ), "no file_path provided to the DataUrl"
        dark_root_dir = os.path.join(dataset.dir, "dark")
        os.makedirs(dark_root_dir, exist_ok=True)
        bg_dataset = Dataset(
            _dir=dark_root_dir,
            first_filename=dark_filename,
            copy_files=False,
            isH5=isH5,
            metadata_url=None,
        )
    elif dark_filename is None:
        bg_dataset = None
    else:
        raise TypeError(f"dark_filename of type {type(dark_filename)} is not handle")

    return dataset, indices, li_indices, bg_dataset


def _get_root_dir(filename: str) -> str:
    url = urllib.parse.urlparse(filename, scheme="file")
    return os.path.dirname(urllib.request.url2pathname(url.path))
