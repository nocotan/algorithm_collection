import math


def arc_length(diameter, angle):
    if angle >= 360:
        return 0
    else:
        arc = (math.pi * diameter) * (angle / 360.0)
        return arc
