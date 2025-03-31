def calculate_volume(a, b, c):
    return a * b * c

def calculate_surface_area(a, b, c):
    return 2 * (a*b + a*c + b*c)

def calculate_mass(volume, material_density):
    return volume * material_density