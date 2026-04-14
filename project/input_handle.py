import math
from error_handling import ErrorHandling


# just grouping into class nothing else
class InputHandle:

    @staticmethod
    def input_sss():

        s1 = float(input("Enter side 1: "))
        s2 = float(input("Enter side 2: "))
        s3 = float(input("Enter side 3: "))
        # if input isn't parsable, it will automatically raise ValueError

        ErrorHandling.validate_input("side", s1, s2, s3)
        # will raise InvalidValueError & InvalidAngleError

        # catch exception in main.py only ! :D

        sort = sorted([s1, s2, s3])
        return (
            sort[0],
            sort[1],
            sort[2],
        )  # returns SORTED tuple instead of returning the above list :D

    @staticmethod
    def input_ssa():
        side1 = float(input("Enter side 1: "))
        side2 = float(input("Enter side 2: "))

        angle3 = float(
            input("Enter the angle (in degrees) enclosed by the sides 1 and 2: ")
        )

        ErrorHandling.validate_input("side", side1, side2)
        ErrorHandling.validate_input("angle", angle3)

        return (side1, side2, math.radians(angle3))  # returning ssa as tuple

    @staticmethod
    def input_saa():
        side = float(input("Enter the side (opp. to known angle): "))
        angle1_opp = float(
            input("Enter the angle (degrees) opposite to the given side: ")
        )
        angle2 = float(input("Enter the other angle(degrees): "))

        ErrorHandling.validate_input("side", side)
        ErrorHandling.validate_input("angle", angle1_opp, angle2)

        return (
            side,
            math.radians(angle1_opp),
            math.radians(angle2),
        )  # returning saa as tuple, where 2nd a is the opposite angle

    @staticmethod
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
