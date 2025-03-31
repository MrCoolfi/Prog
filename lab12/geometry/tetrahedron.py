import math

def calculate_volume(a):
    return (a ** 3) * math.sqrt(2) / 12

def calculate_surface_area(a):
    return math.sqrt(3) * (a ** 2)

def calculate_mass(volume, material_density):
    return volume * material_density