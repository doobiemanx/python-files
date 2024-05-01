print("We are going to give you the sum of 3 numbers you've entered.")

running = True
while True:

    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))

    sum_of_nums = num1 + num2 + num3

    if num1 == num2 == num3:
        print(f"These numbers are the same, the sum of these numbers is {sum_of_nums} multiplied by 4 this becomes {sum_of_nums * 4}")

    else:
        print(f"The sum of thes numbers is {sum_of_nums}")


