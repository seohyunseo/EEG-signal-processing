import mne
import numpy as np
from scipy import signal

class EEGPreProcessor:
    def __init__(self, raws, montage='standard_1020'):
        self.raws = raws
        self.n_trials = len(self.raws)
        self.montage = montage
        self.channel_names = ['F3', 'F1', 'Fz', 'F2', 'F4', 'FC5', 'FC3', 
                              'FC1', 'FCz', 'FC2', 'FC4', 'FC6', 'C5', 'C3', 
                              'C1', 'Cz', 'C2', 'C4', 'C6', 'CP5', 'CP3', 
                              'CP1', 'CPz', 'CP2', 'CP4', 'CP6', 'O1', 'O2']
        

    def rereference(self, idx, reference):
        self.raws[idx].set_eeg_reference(reference)
        
    def bandpass_filter(self, idx, b_freq):
        self.raws[idx].filter(l_freq=b_freq[0], h_freq=b_freq[1])
        
    # Function for removing the power line noise
    def remove_powerline_noise(self, idx, p_freq):
        # Convert mne raw data into numpy array for using scipy function
        raw_array = self.raws[idx].get_data()

        fs = self.raws[idx].info["sfreq"] # Get sample frequency
        
        q = 30.0  # Quality factor for the notch filter
        f0 = p_freq  # Normalize frequency to Nyquist frequency
        b, a = signal.iirnotch(f0, Q=q, fs=fs)
        raw_notch = signal.filtfilt(b, a, raw_array)

        # Convert numpy array data into mne raw data for data analysis
        info = mne.create_info(ch_names=self.channel_names, sfreq=1000, ch_types='eeg')
        info.set_montage('standard_1020')
        raw_notch = mne.io.RawArray(raw_notch, info)

        self.raws[idx] = raw_notch
    
    def resampling(self, idx, s_freq):
        self.raws[idx].resample(s_freq)

    def preprocess(self, b_freq=[0.01, 50.0], s_freq=1000, p_freq=60, reference='average'):
        
        for idx in range(self.n_trials): 
            
            self.resampling(idx=idx, s_freq=s_freq) 
            self.raws[idx].resample(s_freq)
        
            self.remove_powerline_noise(idx=idx, p_freq=p_freq)           


            self.rereference(idx=idx, reference=reference)
            
            self.bandpass_filter(idx=idx, b_freq=b_freq)
            

        return self.raws
