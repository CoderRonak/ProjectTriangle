# 'triangle' is an object of class 'Triangle'

# using class methods, just grouping the methods together, nothing else


class Output:
    triangle = None  # will do "Output.triangle = triangle" in main.py after creating triangle object triangle = Triangle()

    @classmethod
    def triangle_type(cls):
        print(
            "The given triangle is:",
            cls.triangle.triangle_angle_type(),
            "&",
            cls.triangle.triangle_side_type(),
        )

    @classmethod
    def perimeter(cls):
        print("Perimeter:", cls.triangle.perimeter(), "units")

    @classmethod
    def area(cls):
        print("Area:", cls.triangle.area(), "sq. units")

    @classmethod
    def angles(cls):
        print("Angles(in degrees): ", " , ".join(cls.triangle.angles()))

    @classmethod
    def inradius(cls):
        print("Inradius:", cls.triangle.inradius(), "units")

    @classmethod
    def circumradius(cls):
        print("Circumradius:", cls.triangle.circumradius(), "units")

    @classmethod
    def medians(cls):
        print(
            "Length of medians (ascending order):",
            " , ".join(cls.triangle.medians()),
            "units",
        )

    @classmethod
    def altitudes(cls):
        print(
            "Length of altitudes (ascending order):",
            " , ".join(cls.triangle.altitudes()),
            "units",
        )
