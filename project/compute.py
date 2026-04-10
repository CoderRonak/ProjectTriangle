# triangle class for computing area perimeter etc etc from SSS

import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def semi_perimeter(self):
        return round((self.a + self.b + self.c) / 2, 2)  # semi perimeter 's'

    def perimeter(self):
        return round(self.a + self.b + self.c, 2)

    def area(self):
        s = self.semi_perimeter()
        area = 0

        # Check for equilateral, Right Angle, if not , use Heron's

        if self.triangle_side_type() == "equilateral":
            # equilateral triangle
            area = self.a * self.a * (math.sqrt(3)) / 4
        elif self.triangle_angle_type() == "right":
            # right angle triangle
            area = 0.5 * self.a * self.b
        else:
            # heron's formula
            area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

        return round(area, 2)

    def angles(self):
        A = B = C = 0

        # calculating cos of angles
        cosA = (self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c)
        cosB = (self.a**2 + self.c**2 - self.b**2) / (2 * self.a * self.c)
        cosC = (self.a**2 + self.b**2 - self.c**2) / (2 * self.a * self.b)

        # return angles A, B, C in degrees
        A = math.degrees(math.acos(cosA))  # cos inverse
        B = math.degrees(math.acos(cosB))
        C = math.degrees(math.acos(cosC))

        return (str(round(A, 2)), str(round(B, 2)), str(round(C, 2)))
        # the input sides will already be sorted hence no need to sort the angles
        # "".join requires string tuple

    def triangle_angle_type(self):
        if math.isclose(self.c**2, (self.a**2 + self.b**2)):
            return "right"
        elif self.c**2 < self.a**2 + self.b**2:
            return "acute"
        elif self.c**2 > self.a**2 + self.b**2:
            return "obtuse"  # returns string

    def triangle_side_type(self):
        if math.isclose(self.a, self.b) and math.isclose(self.b, self.c):
            return "equilateral"

        elif (
            math.isclose(self.a, self.b)
            or math.isclose(self.b, self.c)
            or math.isclose(self.c, self.a)
        ):
            return "isosceles"

        else:
            return "scalene"

    def inradius(self):
        return round(self.area() / self.semi_perimeter(), 2)

    def circumradius(self):
        return round(self.a * self.b * self.c / (4 * self.area()), 2)

    def altitudes(self):
        area = self.area()

        alt1 = 2 * area / self.a  # length of altitude from vertex 1 (angle1) to side 1
        alt2 = 2 * area / self.b
        alt3 = 2 * area / self.c

        return sorted(
            [str(round(alt1, 2)), str(round(alt2, 2)), str(round(alt3, 2))]
        )  # tuple of strings

    def medians(self):
        m1 = 0.5 * math.sqrt(
            2 * self.b**2 + 2 * self.c**2 - self.a**2
        )  # median to mid of side1
        m2 = 0.5 * math.sqrt(2 * self.a**2 + 2 * self.c**2 - self.b**2)
        m3 = 0.5 * math.sqrt(2 * self.a**2 + 2 * self.b**2 - self.c**2)

        return sorted(
            [str(round(m1, 2)), str(round(m2, 2)), str(round(m3, 2))]
        )  # tuple
