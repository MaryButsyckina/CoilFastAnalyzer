from numpy import pi


def radians_to_degree(angle):
    try:
        return [x * 180 / pi for x in angle]
    except TypeError:
        return angle * 180 / pi
