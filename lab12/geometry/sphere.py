import math

def calculate_volume(r):
    return (4/3) * math.pi * (r ** 3)

def calculate_surface_area(r):
    return 4 * math.pi * (r ** 2)

def calculate_mass(volume, material_density):
    return volume * material_density