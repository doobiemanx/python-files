# Create a string
text = "Python programming is powerful and versatile"

substring = text[7:18]
print(substring)
print()

words_list = text.split()
print(words_list)
print()

joined_string = '-'.join(words_list)
print(joined_string)
print()

# Create a list
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

squares = [x**2 for x in numbers] #for loops
print(squares)