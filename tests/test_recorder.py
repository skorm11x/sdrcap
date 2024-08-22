import unittest
import os
import tempfile
from datetime import datetime
import numpy as np
import h5py
from sdrcap.recorders.csv_recorder import CSVRecorder
from sdrcap.recorders.hdf5_recorder import HDF5Recorder

class TestRecorderMethods(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    def setUp(self):
        """_summary_
        """
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        """_summary_
        """
        for file in os.listdir(self.temp_dir):
            file_path = os.path.join(self.temp_dir, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        os.rmdir(self.temp_dir)

    def test_csv(self):
        """_summary_
        """
        csv = CSVRecorder()
        # Use dictionaries with 'real' and 'imaginary' keys
        samples = np.array([1.0 + 0.1j, 2.0 + 0.2j], dtype=np.complex64)
        filename = os.path.join(self.temp_dir, 'test.csv')
        csv.save(samples, filename)

        self.assertTrue(os.path.isfile(filename))

        with open(filename, 'r') as file:
            content = file.read()
            self.assertIn("Real Value,Imaginary Value,TimeStamp", content)

            import pandas as pd
            df = pd.read_csv(filename)
            self.assertEqual(len(df), len(samples))

            for idx, sample in enumerate(samples):
                real_value = df.loc[idx, 'Real Value']
                imag_value = df.loc[idx, 'Imaginary Value']
                
                self.assertAlmostEqual(real_value, sample.real, places=1)
                self.assertAlmostEqual(imag_value, sample.imag, places=1)

    def test_hdf5(self):
        """_summary_
        """
        hdf5 = HDF5Recorder(center_freq=100700000.0, sample_rate=2.4e6, freq_correction=60, gain="auto")
        samples = np.array([(1.0 + 1j * 0.1)], dtype=np.complex64)
        filename = os.path.join(self.temp_dir, 'test.hdf5')
        hdf5.save(samples, filename)


        self.assertTrue(os.path.isfile(filename))

        with h5py.File(filename, 'r') as f:
            self.assertTrue('real' in f)
            self.assertTrue('imag' in f)
            self.assertTrue('timestamps' in f)
            self.assertEqual(f.attrs['center_freq'], 100700000.0)
            self.assertEqual(f.attrs['sample_rate'], 2.4e6)
            self.assertEqual(f.attrs['freq_correction'], 60)
            self.assertEqual(f.attrs['gain'], 'auto')

if __name__ == '__main__':
    unittest.main()