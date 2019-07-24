#!/usr/bin/python3

print("What score did you get?")
prompt_grade = float(input())

if prompt_grade >= 90:
    print("You scored an A")
elif prompt_grade >= 80:
    print("You scored an B")
elif prompt_grade >= 70:
    print("You scored an C")
elif prompt_grade >= 60:
    print("You scored an D")
else:
    print("You scored an F")

