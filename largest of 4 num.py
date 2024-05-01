print("   Which of the 4 numbers is the largest"   )

running = True
while True:

    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    num_3 = int(input("Enter third number: "))
    num_4 = int(input("Enter fourth number: "))

    largest_number = num_1

    if num_2 > largest_number:
        largest_number = num_2

    if num_3 > largest_number:
        largest_number = num_3

    if num_4 > largest_number:
        largest_number = num_4

    print(f"The largets number is {largest_number}")
