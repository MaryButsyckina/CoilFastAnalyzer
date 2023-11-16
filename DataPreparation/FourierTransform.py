from scipy import fft
from abc import ABC, abstractmethod


class FourierTransform(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def transform(self):
        pass


class ScipyFFT(FourierTransform):
    def __init__(self, data):
        super(ScipyFFT).__init__(data)

    def transform(self):
        pass
