# Create a tuple
coordinates = (34.0522, -118.2437)

print(coordinates[0])
print(coordinates[1])
print()

# Create a dctionary
student = {
    'name': 'Alice',
    'age': 24,
    'courses': ['Math', 'Science', 'English',]
}

student['graduated'] = False

student['age'] = 25

print('Student dictionary:', student)
print()

# Create a set
unique_numbers = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}

unique_numbers.add(6)

unique_numbers.remove(2)

is_3_in_set = 3 in unique_numbers
print('Is the number 3 in the set?', is_3_in_set)

print('Unique numbers in set:', unique_numbers)