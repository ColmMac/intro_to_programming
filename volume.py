#Ask user what shape they are finding volume of cube, cuboid (rectangular prism), cylinder, sphere, cone, and pyramid
#Ask for measurements
#Calculate volume
import math

shapes = ["cube", "cuboid", "cylinder", "sphere", "cone", "pyramid"]

def start():
    shape = 0
    print("\n Welcome to the volume calculator! Please enter what shape you will be finding the volume of.")
    print("1. Cube")
    print("2. Cuboid")
    print("3. Cylinder")
    print("4. Sphere")
    print("5. Cone")
    print("6. Pyramid")
    try:
        shape = int(input("Enter shape, from 1-6: "))
    except ValueError:
        print("Please enter an integer from 1-6.")
    return shape

def cube(length):
    return length ** 3

def cuboid(length, height, width):
    return length * height * width

def cylinder(height, radius):
    return math.pi * (radius*radius) * height

def sphere(radius):
    return 1.33 * (radius ** 3) * math.pi

def cone(radius, height):
    return 1.33 * math.pi * height * (radius*radius)

def pyramid(base_area, height):
    return 0.33 * base_area * height

result = 0
operation = start()
if operation == 1:
    length = float(input("Please enter the length of the cube's side: "))
    result = cube(length)

elif operation == 2:
    length = float(input("Please enter the length of the cuboid: "))
    height = float(input("Please enter the height of the cuboid: "))
    width = float(input("Please enter the width of the cuboid: "))
    result = cuboid(length, height, width)

elif operation == 3:
    radius = float(input("Please enter the radius of the cylinder: "))
    height = float(input("Please enter the height of the cylinder: "))
    result = cylinder(height, radius)

elif operation == 4:
    radius = float(input("Please enter the radius of the sphere: "))
    result = sphere(radius)

elif operation == 5:
    radius = float(input("Please enter the radius of the cone: "))
    height = float(input("Please enter the height of the cone: "))
    result = cone(radius, height)

elif operation == 6:
    base_area = float(input("Please enter the base area of the pyramid: "))
    height = float(input("Please enter the height of the pyramid: "))
    result = pyramid(base_area, height)


print(f"The volume of the {shapes[operation-1]} is equal to {round(result, 2)}cm³")