import os
import datetime
import time
from rtlsdr import RtlSdr
from sdrcap.recorders.hdf5_recorder import HDF5Recorder
from sdrcap.recorders.csv_recorder import CSVRecorder

class RTLSDRInterface:
    """_summary_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    AVAILABLE_FILETYPES = ("csv", "hdf5")

    def __init__(self, sdr=None, center_freq=100700000.0, sample_rate=2.4e6, 
                 freq_correction=60, gain="auto", record_delay=2, 
                 sample_window=1024*256, filetype="csv", 
                 output_dir="outputs"):
        if filetype not in self.AVAILABLE_FILETYPES:
            raise ValueError(f"Invalid file type: {filetype}. Must be one of {self.AVAILABLE_FILETYPES}.")

        self.center_freq = center_freq
        self.sample_rate = sample_rate
        self.freq_correction = freq_correction
        self.gain = gain
        self.record_delay = record_delay
        self.sample_window = sample_window
        self.filetype = filetype
        self.output_dir = output_dir
        self.sdr = sdr if sdr is not None else self._setup_rtl_sdr()
        os.makedirs(self.output_dir, exist_ok=True)

        if self.filetype == "hdf5":
            self.recorder = HDF5Recorder(
                center_freq=self.center_freq,
                sample_rate=self.sample_rate,
                freq_correction=self.freq_correction,
                gain=self.gain
            )
        elif self.filetype == "csv":
            self.recorder = CSVRecorder()

    def _setup_rtl_sdr(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        sdr = RtlSdr()
        sdr.center_freq = self.center_freq
        sdr.freq_correction = self.freq_correction
        sdr.gain = self.gain
        return sdr

    def record_single_sample(self, recording_name=None):
        """_summary_

        Args:
            recording_name (_type_, optional): _description_. Defaults to None.
        """
        if recording_name != None:
            filename = f"{self.output_dir}/{recording_name}-sample_window{self.sample_window}.{self.filetype}"
        else:
            filename = f"{self.output_dir}/sample_window{self.sample_window}.{self.filetype}"
        if self.sdr is None:
            self.sdr = self._setup_rtl_sdr()
        else:
            samples = self.sdr.read_samples(self.sample_window)
            self.recorder.save(samples=samples, filename=filename)

    def record_continuous_sample(self):
        """_summary_
        """
        start_record_time = datetime.datetime.now().timestamp()
        if self.sdr is None:
            self.sdr = self._setup_rtl_sdr()
        while True:
            self.record_single_sample(recording_name=start_record_time)
            time.sleep(int(self.record_delay))