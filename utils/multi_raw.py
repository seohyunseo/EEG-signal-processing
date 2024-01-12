import mne
import numpy as np

def set_multiple_raw(data, channel_names, sample_rate):
    n_channels = len(channel_names)

    # Get dimensions of the data
    time, channels, trials = data.shape

    raws = []
    for trial in range(trials):
        # Initialize an info structure
        sample_rate = sample_rate
        info = mne.create_info(
            ch_names=channel_names, 
            sfreq=sample_rate, 
            ch_types=['eeg']*n_channels)

        info.set_montage('standard_1020')

        # Create an MNE Raw object
        raw = mne.io.RawArray(np.transpose(data[:,:,trial]), info)
        raws.append(raw)
    return raws