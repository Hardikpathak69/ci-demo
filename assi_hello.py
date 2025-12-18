# Simple Student Grade Calculator
# Made by a student, for students 😄

def calculate_percentage(marks):
    total = sum(marks)
    percentage = total / len(marks)
    return percentage

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"

print("----- Student Result System -----")

name = input("Enter student name: ")

marks = []
for i in range(1, 6):
    m = int(input(f"Enter marks of subject {i}: "))
    marks.append(m)

percentage = calculate_percentage(marks)
grade = calculate_grade(percentage)

print("\n----- Result -----")
print("Name:", name)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
