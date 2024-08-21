"""
    An example on how you import and call the sdrcap.
"""

# import argparse
# from sdrcap import rtl_interface
from sdrcap import rtl_interface

# How to get arguments and pass them to the packaage as it expects then
# parser = argparse.ArgumentParser(description="Process radio parameters.")
# parser.add_argument(
#     "--center_freq", type=float, default=100700000.0, help="center frequency"
# )
# parser.add_argument(
#     "--record_delay",
#     default=2,
#     help="the time delay for window of writing csv file output",
# )
# args = parser.parse_args()
# assert isinstance(args, argparse.Namespace)


# rtl_interface.record_sdr()
sdr = rtl_interface.RTLSDRInterface(record_delay=0, filetype="hdf5")
sdr.record_continuous_sample()
