# A school has many students studying in different standards. Each student has a roll number, name, marks in 4 subjects and standard.
# The school wants a system that can calculate his grade and promote him/her if his grade is greater than 'F'.
# The criteria for grade calculation is:
# i. If percentage >=80,  grade  is  'A'
# ii. if  60<=percentage<80, grade  is 'B'
# iii. if 40<=percentage<60, grade is 'C'
# iv. percentage<40, grade is 'F'
import re


def grade():
    name = input("NAME:\n")
    roll = input("ROLL NO:\n")

    def cls():
        loop = True
        global std
        while loop:
            std = int(input("STANDARD:\n"))
            if 1 < std <= 12:
                loop = False

            else:
                print("Wrong Standard")

    cls()

    mark1 = float(input("MARKS OF SUBJECT 1:\n"))
    mark2 = float(input("MARKS OF SUBJECT 2:\n"))
    mark3 = float(input("MARKS OF SUBJECT 3:\n"))
    mark4 = float(input("MARKS OF SUBJECT 4:\n"))
    mark5 = float(input("MARKS OF SUBJECT 5:\n"))

    obt = mark1 + mark2 + mark3 + mark4 + mark5
    total = int(input("TOTAL MARKS OF ALL SUBJECTS:"))

    per = obt / total * 100

    cgpa = per/9.5

    if per >= 80:
        print("Your Grade is A. YOU HAVE PASSED!!")
    elif 60 <= per < 80:
        print("Your Grade is B. YOU HAVE PASSED!!")
    elif 40 <= per < 60:
        print("Your Grade is C. YOU HAVE PASSED!!")
    elif per < 40:
        print("Your Grade is F. YOU HAVE FAILED!!")

    per = "{:.2f}".format(per)
    cgpa = "{:.1f}".format(cgpa)

    print(f"YOUR NAME:{name}")
    print(f"YOUR ROLL:{roll}")
    print(f"YOUR STANDARD:{std}")
    print(f"YOUR PERCENTAGE:{per}%")
    print(f"YOUR CGPA is:{cgpa}")
    print("==========XXXXXXXXXX==========")
    print("")


while True:
    grade()
