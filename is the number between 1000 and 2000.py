print(    'Is the number between a 1000 and 2000?'    )

running = True
while True:

    num = int(input('Enter a number: '))

    if num < 1000:
        print('This number is lower than 1000')

    elif 1000 <= num <= 2000:
        print('This number is between a 1000 and 2000')

    else:
        print('This number is higher than 2000')