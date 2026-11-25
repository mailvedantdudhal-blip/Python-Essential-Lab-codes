import math


def calculate_area(shape, *args):
    shape = shape.lower()
    if shape == "circle" and len(args) == 1:
        radius = args[0]
        return math.pi * (radius ** 2)
    elif shape == "rectangle" and len(args) == 2:
        width, height = args
        return width * height
    elif shape == "triangle" and len(args) == 2:
        base, height = args
        return 0.5 * base * height
    else:
        return "Invalid parameters for shape"


print("Circle Area (r=5):", round(calculate_area("circle", 5), 2))
print("Rectangle Area (w=4, h=6):", calculate_area("rectangle", 4, 6))
print("Triangle Area (b=3, h=8):", calculate_area("triangle", 3, 8))
