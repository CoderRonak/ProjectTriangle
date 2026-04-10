# convert all to SSS
import math


def ascending_order(s1, s2, s3):
    sort = sorted([s1, s2, s3])
    return (
        sort[0],
        sort[1],
        sort[2],
    )  # returns tuple instead of returning the above list :D


def ssa_to_sss(side1, side2, angle3):
    # angle3 (in radians) -> angle between the sides
    side3 = math.sqrt(side1**2 + side2**2 - 2 * side1 * side2 * math.cos(angle3))
    return ascending_order(
        side1,
        side2,
        side3,
    )  # returns tuple


def saa_to_sss(side, angle1_opp, angle2):
    # angle1_opp -> angle opposite to side

    # Third angle
    angle3 = math.pi - angle1_opp - angle2  # sum of angles = 180°

    # Using Law of Sines to find the other sides
    # input 'side' is opposite angle 'angle1_opp'
    side1 = side
    side2 = side1 * math.sin(angle2) / math.sin(angle1_opp)
    side3 = side1 * math.sin(angle3) / math.sin(angle1_opp)

    return ascending_order(
        side1,
        side2,
        side3,
    )


def coordinates_to_sss(point1, point2, point3):
    # point1 2 3 will be lists containing [x1, y1]
    # x1 and y1 will be Strings, hence converting to int

    x1, y1 = int(point1[0]), int(point1[1])
    x2, y2 = int(point2[0]), int(point2[1])
    x3, y3 = int(point3[0]), int(point3[1])

    # Getting the sides
    a = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
    b = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    c = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    return ascending_order(a, b, c)
