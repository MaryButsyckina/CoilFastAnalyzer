from numpy import pi
from Spline import CubicScipySpline


class Slope:
    def __init__(self, angle, signal):
        self.angle = angle
        self.signal = signal
        self.slope = 0

    def find_slope(self):
        point1 = CubicScipySpline(self.angle, self.signal, -1, 1, 2).spline()[1]
        point2 = CubicScipySpline(self.angle, self.signal, 359, 361, 2).spline()[1]
        self.slope = (point2 - point1) / pi / 2
        return self.slope

    def reduce_slope(self):
        for i, el in enumerate(self.signal):
            self.signal[i] -= self.angle[i] * self.slope * pi / 180
        return self.signal

    def run(self):
        self.find_slope()
        self.reduce_slope()
        return self.signal
