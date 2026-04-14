import math


# EXCEPTIONS
class InvalidValueError(Exception):
    pass


class InvalidAngleError(Exception):
    pass


class InvalidTriangleError(Exception):
    pass


# just grouping two functions into a class, nothing else
class ErrorHandling:

    @staticmethod
    def validate_input(mode="side", *args):
        # mode can be 'side' or 'angle
        for i in args:
            if not isinstance(i, (int, float)) or math.isnan(i) or math.isinf(i):
                # i is not an INT or i is not a FLOAT
                # or i is NaN or i is INFINITE
                raise ValueError("Invalid number !")
            elif not i > 0:
                raise InvalidValueError("Invalid Value ! Should be positive !")
            elif mode == "angle" and not i < 180:
                raise InvalidAngleError("Invalid Angle ! Should be < 180° !")

        if mode == "angle" and len(args) == 2:
            # 2 angles have been entered, their sum should be < 180°
            if not args[0] + args[1] < 180:
                raise InvalidAngleError(
                    "Invalid Angles ! Sum of both angle should be < 180° !"
                )

    @staticmethod
    def validate_triangle(s1, s2, s3):
        if not (s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2):
            raise InvalidTriangleError("Invalid Triangle !")
