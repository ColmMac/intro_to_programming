#Ask user what shape they are finding volume of cube, cuboid (rectangular prism), cylinder, sphere, cone, and pyramid
#Ask for measurements
#Calculate volume

def start():
    print("\n Welcome to the volume calculator! Please enter what shape you will be finding the volume of.")
    print("1. Cube")
    print("2. Cuboid")
    print("3. Cylinder")
    print("4. Sphere")
    print("5. Cone")
    print("6. Pyramid")
    try:
        shape = int(input("Enter shape, from 1-6: "))#
    except ValueError:
        print("Please enter an integer from 1-6.")
    return shape

def cube():
    pass

def cuboid():
    pass

def cylinder():
    pass

def sphere():
    pass

def cone():
    pass

def pyramid():
    pass