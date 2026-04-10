# GIVING OUTPUT CHOICE
import compute
import convert
import input_handle
import sys

print("Welcome to this Program!")

print("We can calulate everything of a triangle!")

s1 = s2 = s3 = 0

while True:
    print("Please choose your input type---\n")
    print("Press 1 to enter 3 sides")
    print("Press 2 to enter 2 sides & angle enclosed")
    print("Press 3 to enter 1 sides & two angles")
    print("Press 4 to enter co-ordinates x,y of vertices")
    print("Press 5 to exit")
    choice = int(input("Your choice:--- "))

    if choice == 1:
        s1, s2, s3 = input_handle.input_sss()

        break
    elif choice == 2:
        side1, side2, angle3 = input_handle.input_ssa()

        s1, s2, s3 = convert.ssa_to_sss(
            side1=side1,
            side2=side2,
            angle3=angle3,
        )

        break
    elif choice == 3:
        side, angle1_opp, angle2 = input_handle.input_saa()

        s1, s2, s3 = convert.saa_to_sss(
            side=side,
            angle1_opp=angle1_opp,
            angle2=angle2,
        )

        break
    elif choice == 4:
        point1, point2, point3 = input_handle.input_coordinates()

        s1, s2, s3 = convert.coordinates_to_sss(
            point1=point1, point2=point2, point3=point3
        )

        break
    elif choice == 5:
        print("Thanks!")
        sys.exit("Exiting Succesfully")  # EXIT

    else:
        print("Wrong input! Please try again!\n")
        continue

triangle = compute.Triangle(a=s1, b=s2, c=s3)

while True:
    print("\n-------------\nPlease choose your desired output----\n")
    print("Press 1 to know Triangle Type")
    print("Press 2 to compute Perimeter")
    print("Press 3 to compute Area")
    print("Press 4 to compute All Angles")
    print("Press 5 to compute Inradius")
    print("Press 6 to compute Circumradius")
    print("Press 7 to compute length of Medians")
    print("Press 8 to compute length of Altitudes")

    print("Press 9 to exit\n")
    choice = int(input("Your choice:--- "))

    if choice == 1:
        print(
            "The given triangle is:",
            triangle.triangle_angle_type(),
            "&",
            triangle.triangle_side_type(),
        )

        break
    elif choice == 2:
        print("Perimeter:", triangle.perimeter(), "units")

        break
    elif choice == 3:
        print("Area:", triangle.area(), "sq. units")

        break
    elif choice == 4:
        print("Angles(in degrees): ", " , ".join(triangle.angles()))

        break
    elif choice == 5:
        print("Inradius:", triangle.inradius(), "units")

        break
    elif choice == 6:
        print("Circumradius:", triangle.circumradius(), "units")

        break
    elif choice == 7:
        print(
            "Length of medians (ascending order):",
            " , ".join(triangle.medians()),
            "units",
        )

        break
    elif choice == 8:
        print(
            "Length of altitudes (ascending order):",
            " , ".join(triangle.altitudes()),
            "units",
        )

        break
    elif choice == 9:
        print("Thanks!")
        sys.exit("Exiting Succesfully")  # EXIT

    else:
        print("Wrong input! Please try again!\n")
        continue
