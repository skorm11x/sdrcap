import time
from datetime import datetime
import numpy as np
from .recorder import Recorder

class CSVRecorder(Recorder):
    """_summary_

    Args:
        Recorder (_type_): _description_
    """

    def __init__(self):
        pass
    def save(self, samples, filename):
        """_summary_

        Args:
            samples (_type_): _description_
            filename (_type_): _description_
        """
        batch_start_time = time.time()
        with open(filename, "a", encoding="utf-8") as out_file:
            out_file.write("Real Value,Imaginary Value,TimeStamp\n")
            for i, sample in enumerate(samples):
                current_time = time.time()
                timestamp_seconds = current_time - batch_start_time
                timestamp = datetime.utcfromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S.') + f"{int((timestamp_seconds % 1) * 1_000_000):06d}"
                out_file.write(f"{sample.real},{sample.imag},{timestamp}\n")