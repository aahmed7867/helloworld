import math


# For your reference
def fahrenheit_to_celsius(temp_f):
    temp_c = (temp_f - 32) * 5 / 9
    return temp_c


# For your reference
def circle_circumference(radius):
    return 2 * math.pi * radius


def celsius_to_fahrenheit(temp_c):
    temp_f = temp_c * 9 / 5 + 32
    return temp_f


def circle_area(radius):
    return math.pi * radius**2


def cylinder_volume_surface(radius, height):
    volume = circle_area(radius) * height
    surface = (2 * circle_area(radius)) + (circle_circumference(radius) * height)
    return volume, surface


if __name__ == '__main__':
    # If you want to use input, use it here, inside the above if statement
    # temp_f = float(input())
    temp_f = 1.0

    # Testing Q1
    print(celsius_to_fahrenheit(temp_f))

    # Testing Q2
    print(circle_area(1.0))

    # Testing Q3
    print(cylinder_volume_surface(2.0, 2.0))
