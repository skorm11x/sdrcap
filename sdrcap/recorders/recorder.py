from abc import ABC, abstractmethod

class Recorder(ABC):
    def __init__(self, filename: str):
        self.filename = filename

    @abstractmethod
    def save(self, samples, filename):
        pass