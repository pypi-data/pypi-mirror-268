import fabio
import glob
import h5py
import numpy
from silx.io import fabioh5

# filenames = sorted(glob.glob("/scisoft/darfix/datasets/55min/HRRSM_2x_s4-100um_noCDTF/*"))
# output_hdf5_file = "/scisoft/darfix/datasets/55min/hdf5_cast/HRRSM_2x_s4-100um_noCDTF.hdf5"
filenames = sorted(
    glob.glob("/home/payno/Documents/dev/diffraction/darfix/data_test/ouput/*")
)
output_hdf5_file = "//home/payno/Documents/dev/diffraction/darfix/data_test/test.hdf5"

positioners_output_data_path = "1.1/instrument/positioners"
detector_output_data_path = "1.1/instrument/my_detector/data"

with fabio.open_series(
    # first_filename=first_filename,
    filenames=filenames,
) as series:
    frames = []
    metadata = {}
    motor_mne = counter_mne = None
    for i_frame, frame in enumerate(series.frames()):
        frames.append(frame.data)
        filename = frame.file_container.filename
        fabio_reader = fabioh5.EdfFabioReader(file_name=filename)

        if i_frame == 0:
            # init all metadata and get motor_mne
            motor_mne = frame.header["motor_mne"].split(" ")
            for motor in motor_mne:
                metadata[motor] = [
                    fabio_reader.get_value(fabio_reader.POSITIONER, motor)[0],
                ]

        else:
            for motor in motor_mne:
                metadata[motor].append(
                    fabio_reader.get_value(fabio_reader.POSITIONER, motor)[0]
                )


with h5py.File(output_hdf5_file, mode="w") as h5f:
    h5f[detector_output_data_path] = numpy.asarray(frames)
    for pos_name, pos_values in metadata.items():
        h5f[f"{positioners_output_data_path}/{pos_name}"] = numpy.asarray(pos_values)
