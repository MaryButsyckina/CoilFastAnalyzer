from scipy import fft
from abc import ABC, abstractmethod


class FourierTransform(ABC):
    def __init__(self, data, n_harms=15, start_harm=1):
        self.data = data
        self.start_harm = start_harm
        self.stop_harm = start_harm + n_harms

    @abstractmethod
    def transform(self):
        pass


class ScipyFFT(FourierTransform):
    def __init__(self, data):
        super(ScipyFFT).__init__(data)

    def transform(self):
        fft_data = fft.rfft(self.data)
        return fft_data.imag/64[self.start_harm:self.stop_harm], \
               fft_data.real/64[self.start_harm:self.stop_harm]
