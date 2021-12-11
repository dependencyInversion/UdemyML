students = {
    "Ben": 1,
    "Jan": 2,
    "Peter": 1,
    "Melissa": 4
}

print(students)

# Read element
student1 = students["Ben"]
print(student1)

# Write element
students["Ben"] = 6
print(students)

# Add element
students["Julia"] = 1
print(students)

# Remove element
students.pop("Julia")
print(students)

# Keys
for key in students:
    print(key)

# Values
for value in students.values():
    print(value)

# Key value pair
for key, value in students.items():
    print(key, value)
