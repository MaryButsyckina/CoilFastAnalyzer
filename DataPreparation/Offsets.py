from abc import ABC, abstractmethod


class OffsetSubtraction(ABC):
    def __init__(self, signal, offset):
        self.average = None
        self.signal = signal
        self.offset = offset

    @abstractmethod
    def find_average_offset(self):
        pass

    @abstractmethod
    def subtract_offset(self):
        pass

    @abstractmethod
    def run(self):
        pass


class BasicOffsetSubtraction(OffsetSubtraction):
    def __init__(self, signal, offset):
        super(BasicOffsetSubtraction, self).__init__(signal, offset)

    def find_bad_data(self):
        exp = []
        indexes = []

        for i, el in enumerate(self.offset):
            exp.append(0)
            if el < 1:
                while el < 1:
                    el *= 10
                    exp[-1] += 1
            else:
                while el > 1:
                    el /= 10
                    exp[-1] += 1

            if exp[-1] < 6:
                indexes.append(i)

        self.offset = list(filter(lambda k: self.offset.index(k) not in indexes, self.offset))

        return self.offset

    def find_average_offset(self):
        self.average = sum(self.offset) / len(self.offset)
        return self.average

    def subtract_offset(self):
        for i in range(len(self.signal)):
            self.signal[i] -= self.average
        return self.signal

    def run(self):
        self.find_bad_data()
        self.find_average_offset()
        self.subtract_offset()
        return self.signal


class PreciseOffsetSubtraction(OffsetSubtraction):
    def __init__(self, signal, offset):
        super(PreciseOffsetSubtraction, self).__init__(signal, offset)

    def find_average_offset(self):
        pass

    def subtract_offset(self):
        pass

    def run(self):
        pass
