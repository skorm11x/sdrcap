import h5py
import time
from datetime import datetime
import numpy as np
from .recorder import Recorder

class HDF5Recorder(Recorder):
    """_summary_

    Args:
        Recorder (_type_): _description_
    """
    
    def __init__(self, center_freq, sample_rate, freq_correction, gain):
        self.center_freq = center_freq
        self.sample_rate = sample_rate
        self.freq_correction = freq_correction
        self.gain = gain

    def save(self, samples, filename):
        """_summary_

        Args:
            samples (_type_): _description_
            filename (_type_): _description_
        """
        current_time = time.time()
        batch_timestamps = [
            datetime.utcfromtimestamp(current_time + (i / len(samples))).strftime('%Y-%m-%d %H:%M:%S.') + 
            f"{int(((current_time + (i / len(samples))) % 1) * 1_000_000):06d}"
            for i in range(len(samples))
        ]
        batch_timestamps = np.array(batch_timestamps, dtype='S26')  # Store as bytes with max length of 26

        with h5py.File(filename, 'a') as f:
            if "real" in f:
                real_data = f["real"]
                imag_data = f["imag"]
                timestamp_data = f["timestamps"]
                
                real_data.resize((real_data.shape[0] + len(samples),))
                imag_data.resize((imag_data.shape[0] + len(samples),))
                timestamp_data.resize((timestamp_data.shape[0] + len(samples),))
                
                real_data[-len(samples):] = samples.real
                imag_data[-len(samples):] = samples.imag
                timestamp_data[-len(samples):] = batch_timestamps

            else:
                f.create_dataset("real", data=samples.real, maxshape=(None,))
                f.create_dataset("imag", data=samples.imag, maxshape=(None,))
                f.create_dataset("timestamps", data=batch_timestamps, maxshape=(None,))
                
            if "center_freq" not in f.attrs:
                f.attrs["center_freq"] = self.center_freq
            if "sample_rate" not in f.attrs:
                f.attrs["sample_rate"] = self.sample_rate
            if "freq_correction" not in f.attrs:
                f.attrs["freq_correction"] = self.freq_correction
            if "gain" not in f.attrs:
                f.attrs["gain"] = self.gain