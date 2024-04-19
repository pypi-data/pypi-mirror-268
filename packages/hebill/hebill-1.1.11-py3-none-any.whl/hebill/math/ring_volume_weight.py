import math


def ring_volume_weight(diameter: float, height: float, inner_diameter: float = 0, margin: float = 0,
                       density: float = 1):
    diameter += 2 * margin
    height += 2 * margin
    if inner_diameter < 2 * margin:
        inner_diameter = 0
    else:
        inner_diameter -= 2 * margin
    vol = math.pi * (pow(diameter / 2, 2) - pow(inner_diameter / 2, 2)) * height
    return vol * density
