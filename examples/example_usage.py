"""
    An example on how you import and call the sdrcap.
"""

from sdrcap import rtl_interface

sdr = rtl_interface.RTLSDRInterface(record_delay=0, filetype="csv")
# sdr = rtl_interface.RTLSDRInterface(record_delay=0, filetype="hdf5")
sdr.start_recording_continuous_samples()
