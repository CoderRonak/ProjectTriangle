import math


def input_sss():
    s1 = int(input("Enter side 1: "))
    s2 = int(input("Enter side 2: "))
    s3 = int(input("Enter side 3: "))

    sort = sorted([s1, s2, s3])
    return (
        sort[0],
        sort[1],
        sort[2],
    )  # returns SORTED tuple instead of returning the above list :D


def input_ssa():
    side1 = int(input("Enter side 1: "))
    side2 = int(input("Enter side 2: "))
    angle3 = math.radians(
        int(input("Enter the angle (in degrees) enclosed by the sides 1 and 2: "))
    )

    return (side1, side2, angle3)  # returning ssa as tuple


def input_saa():
    side = int(input("Enter the side (opp. to known angle): "))
    angle1_opp = math.radians(
        int(input("Enter the angle (degrees) opposite to the given side: "))
    )
    angle2 = math.radians(int(input("Enter the other angle(degrees): ")))

    return (
        side,
        angle1_opp,
        angle2,
    )  # returning saa as tuple, where 2nd a is the opposite angle


def input_coordinates():
    print("Enter co-ordinates x,y (comma separated) of 3 points: ")
    point1 = (
        input("Enter point 1 -> x1, y1: ").replace(" ", "").split(",")
    )  # list of strings [x1, y1]
    point2 = input("Enter point 2 -> x2, y2: ").replace(" ", "").split(",")
    point3 = input("Enter point 3 -> x3, y3: ").replace(" ", "").split(",")

    # replacing any blank space because user can enter:
    #'x,y' or 'x, y' or 'x , y' ..

    return (point1, point2, point3)  # lists containing ["x", "y"]
