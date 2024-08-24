"""
    This module contains the hardware interface files for various SDR devices.

    Each hardware interface is it's own class and inherits from hardware_interface
    abstract class for a more uniform API across SDR devices.

    Each hardware interface has its own private setup functions and parameters.
"""
__version__ = "0.0.1"
AVAILABLE_FILETYPES = ("csv", "hdf5")
AVAILABLE_SDR_DEVICES = ("rtl")
