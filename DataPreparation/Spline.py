import scipy as sp
from abc import ABC, abstractmethod


class AbstractSpline(ABC):
    def __init__(self, x, y, start_angle=0):
        self.x = x
        self.y = y
        self.start_angle = start_angle

    @abstractmethod
    def spline(self):
        pass


class CubicScipySpline(AbstractSpline):
    def __init__(self, x, y, start_angle):
        super(CubicScipySpline).__init__(x, y, start_angle)

    def spline(self):
        pass
