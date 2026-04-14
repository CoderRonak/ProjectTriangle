# convert all to SSS
import math
from error_handling import ErrorHandling

# just grouping into class nothing else
# using classmethod because we have to access ascending order in other methods :D


class Convert:
    @classmethod
    def ascending_order(cls, s1, s2, s3):
        sort = sorted([s1, s2, s3])
        return (
            sort[0],
            sort[1],
            sort[2],
        )  # returns tuple instead of returning the above list :D

    @classmethod
    def ssa_to_sss(cls, side1, side2, angle3):
        # angle3 (in radians) -> angle between the sides
        side3 = math.sqrt(side1**2 + side2**2 - 2 * side1 * side2 * math.cos(angle3))

        ErrorHandling.validate_triangle(side1, side2, side3)

        return cls.ascending_order(
            side1,
            side2,
            side3,
        )  # returns tuple

    @classmethod
    def saa_to_sss(cls, side, angle1_opp, angle2):
        # angle1_opp -> angle opposite to side

        # Third angle
        angle3 = math.pi - angle1_opp - angle2  # sum of angles = 180°

        # Using Law of Sines to find the other sides
        # input 'side' is opposite angle 'angle1_opp'
        side1 = side
        side2 = side1 * math.sin(angle2) / math.sin(angle1_opp)
        side3 = side1 * math.sin(angle3) / math.sin(angle1_opp)

        ErrorHandling.validate_triangle(side1, side2, side3)

        return cls.ascending_order(
            side1,
            side2,
            side3,
        )

    @classmethod
    def coordinates_to_sss(cls, point1, point2, point3):
        # point1 2 3 will be lists containing [x1, y1]
        # x1 and y1 will be Strings, hence converting to int

        x1, y1 = float(point1[0]), float(point1[1])
        x2, y2 = float(point2[0]), float(point2[1])
        x3, y3 = float(point3[0]), float(point3[1])
        # will raise error if not parsable to float :D

        # Getting the sides
        a = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
        b = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
        c = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        # If the side lengths are 0 or negative, then automatically validate_triangle will handle it by triangle inequality

        ErrorHandling.validate_triangle(a, b, c)

        return cls.ascending_order(a, b, c)
