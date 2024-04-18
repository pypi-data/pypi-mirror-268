from typing import NamedTuple, Optional

import numpy
from Orange.widgets.widget import OWWidget
from silx.gui import qt

from darfix.core.dataset import Dataset as DarfixDataset


class Dataset(NamedTuple):
    """Darfix dataset with indices and background"""

    dataset: DarfixDataset  # Darfix dataset object that holds the image stack
    indices: Optional[numpy.ndarray] = (
        None  # Image stack indices to be taking into account?
    )
    bg_indices: Optional[numpy.ndarray] = (
        None  # Dark image stack indices to be taking into account?
    )
    bg_dataset: Optional[DarfixDataset] = (
        None  # Darfix dataset object that holds the dark image stack
    )


class OWDataset(NamedTuple):
    """Darfix dataset with indices and background and associated Orange widget"""

    parent: OWWidget  # Orange widget corresponding to an ewoks task
    dataset: DarfixDataset  # Darfix dataset object that holds the image stack
    indices: Optional[numpy.ndarray] = (
        None  # Image stack indices to be taking into account?
    )
    bg_indices: Optional[numpy.ndarray] = (
        None  # Dark image stack indices to be taking into account?
    )
    bg_dataset: Optional[DarfixDataset] = (
        None  # Darfix dataset object that holds the dark image stack
    )


class OWSendDataset(NamedTuple):
    """Object send between Orange widgets"""

    dataset: OWDataset  # Resulting dataset with associated widget
    update: Optional[qt.QWidget] = None  # ???
