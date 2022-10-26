#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Oct 2022
# This program decides whether students can attend the exam


def main():
    # this program calculates attendance

    # input
    print("Attendance will decide whether students can sit in the exam.")
    classes_held = int(input("Enter the number of classes held: "))
    classes_attended = int(input("Enter the number of classes attended: "))

    # process

    attendance_percent = classes_attended / classes_held * 100

    try:
        classes_held = int(classes_held)
        classes_attended = int(classes_attended)
        print("You entered everything correctly.")

    except ValueError:
        print("That was not a valid number.")

    if attendance_percent > 75:
        print(
            "The student has {0}% attendance. They may sit in for the exam.".format(
                attendance_percent
            )
        )
    elif attendance_percent < 75:
        print(
            "The student has {0}% attendance. They may not sit in for the exam.".format(
                attendance_percent
            )
        )
    else:
        print("Input is invalid.".format(attendance_percent))

    # output
    print("\nDone.")


if __name__ == "__main__":
    main()