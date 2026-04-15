import error_handling
import convert

"""INPUT AND CONVERT"""


def input_and_convert_sas():
    side1, side2, angle3 = input_ssa()
    return convert.ssa_to_sss(side1=side1, side2=side2, angle3=angle3)


def input_and_convert_saa():
    side, angle1_opp, angle2 = input_saa()
    return convert.saa_to_sss(side=side, angle1_opp=angle1_opp, angle2=angle2)


def input_and_convert_coords():
    p1, p2, p3 = input_coordinates()
    return convert.coordinates_to_sss(p1, p2, p3)


"""INPUT AND VALIDATE INPUT"""


def input_sss():
    s1 = float(input("Enter side 1: "))
    s2 = float(input("Enter side 2: "))
    s3 = float(input("Enter side 3: "))
    # if input isn't parsable, it will automatically raise ValueError

    error_handling.validate_input("side", s1, s2, s3)
    # will raise InvalidValueError & InvalidAngleError

    # catch exception in main.py only ! :D

    sort = sorted([s1, s2, s3])
    return (
        sort[0],
        sort[1],
        sort[2],
    )  # returns SORTED tuple instead of returning the above list :D


def input_ssa():
    side1 = float(input("Enter side 1: "))
    side2 = float(input("Enter side 2: "))

    angle3 = float(
        input("Enter the angle (in degrees) enclosed by the sides 1 and 2: ")
    )

    error_handling.validate_input("side", side1, side2)
    error_handling.validate_input("angle", angle3)

    return (side1, side2, angle3)  # returning ssa as tuple


def input_saa():
    side = float(input("Enter the side (opp. to known angle): "))
    angle1_opp = float(input("Enter the angle (degrees) opposite to the given side: "))
    angle2 = float(input("Enter the other angle(degrees): "))

    error_handling.validate_input("side", side)
    error_handling.validate_input("angle", angle1_opp, angle2)

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

    # point1 2 3 will be lists containing [x1, y1]
    # x1 and y1 will be Strings, hence converting to flot

    x1, y1 = float(point1[0]), float(point1[1])
    x2, y2 = float(point2[0]), float(point2[1])
    x3, y3 = float(point3[0]), float(point3[1])
    # will raise error if not parsable to float :D

    return ((x1, y1), (x2, y2), (x3, y3))  # lists containing ["x", "y"]
