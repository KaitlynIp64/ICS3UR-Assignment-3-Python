#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Oct 2022
# This program decides whether students can attend the exam based on attendance


def main():
    # this program calculates attendance

    # input
    print("Attendance will decide whether students can sit in the exam or not.")
    classes_held = int(input("Enter the number of classes held: "))
    classes_attended = int(input("Enter the number of classes attended: "))

    # process

    attendance_percent = classes_attended / classes_held * 100

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

    # output
    print("\nDone.")


if __name__ == "__main__":
    main()
