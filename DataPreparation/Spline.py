import scipy as sp
from numpy import arange
from abc import ABC, abstractmethod
from scipy.interpolate import interp1d


class AbstractSpline(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def spline(self):
        pass


class CubicScipySpline(AbstractSpline):
    def __init__(self, x, y, start_angle, stop_angle=None, num_of_points=128):
        super(CubicScipySpline).__init__()
        self.start_angle = start_angle
        self.x, self.y = x, y
        self.num_of_points = num_of_points
        if not stop_angle:
            self.stop_angle = start_angle + 360
        else:
            self.stop_angle = stop_angle

    def spline(self):
        angle = arange(self.start_angle, self.stop_angle, (self.stop_angle - self.start_angle) / self.num_of_points)
        return sp.interpolate.CubicSpline(self.x, self.y)(angle)
