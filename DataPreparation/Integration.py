from abc import ABC, abstractmethod


class Integral(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def integrate(self):
        pass


class BasicIntegral(Integral):
    def __init__(self, data):
        super(BasicIntegral).__init__(data)

    def integrate(self):
        integral = []
        partial_sum = 0
        for el in self.data:
            partial_sum += el
            integral.append(partial_sum)
        return integral
