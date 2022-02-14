# Florido Task 13/02/2022

print("Hello teacher!")
while True:
    hours = input("How many hours did you work this week? (Type end to exit) ")
    if hours.isnumeric() is True:
        students = input("How many children are in your class? (Type end to exit) ")
        if students.isnumeric() is True:
            students = int(students)
            hours = int(hours)
            salary = hours * students
            formatSalary = "{:.2f}".format(salary)
            print("You earned $", formatSalary, "this week")
        elif students == "end":
            print("Goodbye teacher!")
            break
        else:
            print("Wrong input, try again!")
    elif hours == "end":
        print("Goodbye teacher!")
        break
    else:
        print("Wrong input, try again!")









