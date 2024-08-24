""" Hardware interface for each SDR device 
    interface regardless of driver details
"""

from abc import ABC, abstractmethod

class HardwareInterface:
    """Abstract class defining methods for each sdr interface to implement"""

    @abstractmethod
    def record_single_sample(self):
        """Records a single sample, based off the SDR sample size and calls recorder."""

    @abstractmethod
    def start_recording_continuous_samples(self):
        """Starts a continuous, synchronous, stream of samples. Establishes recording start time."""
