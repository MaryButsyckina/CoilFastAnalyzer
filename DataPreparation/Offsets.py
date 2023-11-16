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

    def find_average_offset(self):
        pass

    def subtract_offset(self):
        pass

    def run(self):
        pass


class PreciseOffsetSubtraction(OffsetSubtraction):
    def __init__(self, signal, offset):
        super(PreciseOffsetSubtraction, self).__init__(signal, offset)

    def find_average_offset(self):
        pass

    def subtract_offset(self):
        pass

    def run(self):
        pass
