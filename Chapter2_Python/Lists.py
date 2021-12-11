import os

grade_ben = 1
grade_jan = 2
grade_peter = 1

grades = [1, 2, 1]

grade_melissa = 4

grades.append(grade_melissa)

print(grades)

grades.pop()

print("Ben's grade: ", grades[0])
print("Jan's grade: ", grades[1])
print("Peter's grade: ", grades[2])

grades[0] = 3

grades.pop(1)

print(grades)
