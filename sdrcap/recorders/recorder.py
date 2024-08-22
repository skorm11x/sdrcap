from abc import ABC, abstractmethod

class Recorder(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_
    """
    def __init__(self, filename: str):
        self.filename = filename

    @abstractmethod
    def save(self, samples, filename):
        """_summary_

        Args:
            samples (_type_): _description_
            filename (_type_): _description_
        """
        pass