# GIVING OUTPUT CHOICE
from compute import Triangle
from output import Output
from convert import Convert
from input_handle import InputHandle
import sys

while True:  # the whole program will repeat until exit is chosen
    print("Welcome to this Program!")

    print("We can calulate everything of a triangle!")

    s1 = s2 = s3 = 0

    while (
        True
    ):  # for choosing input, will break if valid input, will run again for invalid input
        print("Please choose your input type---\n")
        print("Press 1 to enter 3 sides")
        print("Press 2 to enter 2 sides & angle enclosed")
        print("Press 3 to enter 1 sides & two angles")
        print("Press 4 to enter co-ordinates x,y of vertices")
        print("Press 5 to exit")
        choice = int(input("Your choice:--- "))

        if choice == 1:
            # SSS
            try:
                s1, s2, s3 = InputHandle.input_sss()
                break
            except Exception as e:
                print(e)
                continue

        elif choice == 2:
            # SAS
            try:
                side1, side2, angle3 = InputHandle.input_ssa()

                s1, s2, s3 = Convert.ssa_to_sss(
                    side1=side1,
                    side2=side2,
                    angle3=angle3,
                )
                break

            except Exception as e:
                print(e)
                continue

        elif choice == 3:
            # SAA
            try:
                side, angle1_opp, angle2 = InputHandle.input_saa()

                s1, s2, s3 = Convert.saa_to_sss(
                    side=side,
                    angle1_opp=angle1_opp,
                    angle2=angle2,
                )
                break

            except Exception as e:
                print(e)
                continue

        elif choice == 4:
            # COORDINATES
            try:
                point1, point2, point3 = (
                    InputHandle.input_coordinates()
                )  # won't raise any error

                s1, s2, s3 = Convert.coordinates_to_sss(
                    point1=point1, point2=point2, point3=point3
                )
                break

            except Exception as e:
                print(e)
                continue
        elif choice == 5:
            # EXIT
            print("Thanks!")
            sys.exit("Exiting Succesfully")

        else:
            print("Invalid choice! Please try again!\n")
            continue

    triangle = Triangle(a=s1, b=s2, c=s3)
    Output.triangle = triangle

    while True:  # for choosing output; will run again for invalid choice
        print("\n-------------\nPlease choose your desired output----\n")
        print("Press 1 to know Triangle Type")
        print("Press 2 to compute Perimeter")
        print("Press 3 to compute Area")
        print("Press 4 to compute All Angles")
        print("Press 5 to compute Inradius")
        print("Press 6 to compute Circumradius")
        print("Press 7 to compute length of Medians")
        print("Press 8 to compute length of Altitudes\n")
        print("Press 9 to compute everything\n")
        print("Press 10 to exit\n")

        choice = int(input("Your choice:--- "))

        if choice == 1:
            Output.triangle_type()
            break
        elif choice == 2:
            Output.perimeter()
            break
        elif choice == 3:
            Output.area()
            break
        elif choice == 4:
            Output.angles()
            break
        elif choice == 5:
            Output.inradius()
            break
        elif choice == 6:
            Output.circumradius()
            break
        elif choice == 7:
            Output.medians()
            break
        elif choice == 8:
            Output.altitudes()
            break
        elif choice == 9:
            # DISPLAY ALL
            Output.triangle_type()
            Output.perimeter()
            Output.area()
            Output.angles()
            Output.inradius()
            Output.circumradius()
            Output.medians()
            Output.altitudes()
            break
        elif choice == 10:
            print("Thanks!")
            sys.exit("Exiting Succesfully")  # EXIT

        else:
            print("Invalid choice! Please try again!\n")
            continue

# END OF PROGRAM :D
