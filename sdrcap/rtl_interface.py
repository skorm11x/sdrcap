import os
import datetime
import time
import h5py
from rtlsdr import RtlSdr

class RTLSDRInterface:
    AVAILABLE_FILETYPES = ("csv", "hdf5")

    def __init__(
        self,
        sdr=None,
        center_freq: float = 100700000.0,
        sample_rate: float = 2.4e6,
        freq_correction: int = 60,
        gain: str = "auto",
        record_delay: int = 2,
        sample_window: int = 1024*256,
        stream: int = 0,
        filetype: str = "csv",
        output_dir: str = "outputs"
    ):
        if filetype not in self.AVAILABLE_FILETYPES:
            raise ValueError(f"Invalid file type: {filetype}. Must be one of {self.AVAILABLE_FILETYPES}.")

        self.center_freq = center_freq
        self.sample_rate = sample_rate
        self.freq_correction = freq_correction
        self.gain = gain
        self.record_delay = record_delay
        self.sample_window = sample_window
        self.stream = stream
        self.filetype = filetype
        self.output_dir = output_dir
        self.sdr = sdr if sdr is not None else self._setup_rtl_sdr()
        os.makedirs(self.output_dir, exist_ok=True)

    def _setup_rtl_sdr(self):
        sdr = RtlSdr()
        sdr.center_freq = self.center_freq
        sdr.freq_correction = self.freq_correction
        sdr.gain = self.gain
        return sdr

    def record_single_sample(self):

        if self.stream:
            if self.filetype == "csv":
                output_file_path = f"{self.output_dir}/stream.csv"
                if self.sdr is None:
                    self.sdr = self._setup_rtl_sdr()
                else:
                    samples = self.sdr.read_samples(self.sample_window)
                    with open(output_file_path, "w", encoding="utf-8") as out_file:
                        out_file.write("Real Value,Imaginary Value\n")
                        for sample in samples:
                            out_file.write(f"{sample.real},{sample.imag}\n")
        else:
            curr_time = datetime.datetime.now()
            filename = f"{self.output_dir}/{curr_time}-sample_window{self.sample_window}.{self.filetype}"
            if self.sdr is None:
                self.sdr = self._setup_rtl_sdr()
            else:
                samples = self.sdr.read_samples(self.sample_window)
                if self.filetype == "csv":
                    self._save_to_csv(samples=samples, filename=filename)
                elif self.filetype == "hdf5":
                    self._save_to_hdf5(samples=samples, filename=filename)

    def record_continuous_sample(self):
        if self.sdr is None:
            self.sdr = self._setup_rtl_sdr()
        while True:
            self.record_single_sample()
            time.sleep(int(self.record_delay))

    def _save_to_csv(self, samples, filename):
        with open(filename, "w", encoding="utf-8") as out_file:
            out_file.write("Real Value,Imaginary Value\n")
            for sample in samples:
                out_file.write(f"{sample.real},{sample.imag}\n")

    def _save_to_hdf5(self, samples, filename):
        with h5py.File(filename, 'w') as f:
            f.create_dataset("real", data=samples.real)
            f.create_dataset("imag", data=samples.imag)
            f.attrs["center_freq"] = self.center_freq
            f.attrs["sample_rate"] = self.sample_rate
            f.attrs["freq_correction"] = self.freq_correction
            f.attrs["gain"] = self.gain
        